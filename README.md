# ComfyUI Types

This is a small helper project to make it easier to write custom nodes for
ComfyUI. Usually, ComfyUI types use string values for parameter and return
types, which can cause errors during development. With string values, an IDE
like VS Code or neovim cannot recognize the types and offer suggestions. This
project provides a small set of shallow Python classes that provide typing, so
an IDE can pick up correct types and show errors before the node is imported,
making development much faster and reducing debugging.

## Installation

PyPI and conda packages are coming soon, in the meantime, please install the
package locally:

```bash
git clone git@github.com:tkreuziger/comfyui-types.git ./comfyui_types
pip install ./comfyui_types
```

## Defining a custom node

### Base node

Your custom node must derive from `ComfyUINode`:

```python
from comfyui_types import ComfyUINode

class MyCustomNode(ComfyUINode):
    """Your custom node."""
```

This does most of the heavy lifting and ensures that ComfyUI can import your
node correctly.

### Meta parameters

Next you can define some meta parameters:

```python
from comfyui_types import ComfyUINode

class MyCustomNode(ComfyUINode):
    category = 'mycategory/mynodes'
    display_name = 'My Custom Node'
    function = 'execute'
```

- The `category` member is equivalent to the `CATEGORY` member, it is simply
written in lower case letters for consistency. Feel free to continue using
`CATEGORY`, if you prefer so, it will work as usual.
- `display_name` defines the name that will be exported and used for showing
your name in the ComfyUI frontend. If you do not define this member, it will
simply use the name of the class, i.e. `MyCustomNode` in this example,
automatically. This is only relevant, if you use the [exporter
function](#exporting-custom-nodes), described below, otherwise it be safely
ignored.
- `function` works the same as the traditional `FUNCTION` member, but has a
default value of `execute`. This means that you can save yourself writing one
line of code, if you simply name the method of your node that you want to be
executed `execute`. Same as with `category`, you can simply stick to the
current way of defining a `FUNCTION` field and it will work as intended.

### Defining input parameters

Now it is time to define your inputs. The following types are included in the
type library, [but more can easily be added](#extending-with-new-types):

- `StringInput`
- `IntegerInput`
- `FloatInput`
- ...

Simply add members to your node. The name of the field will be used as the name
that is shown in the UI. Any other options are defined as parameters of the
input field:

```python
from comfyui_types import ComfyUINode, StringInput, FloatInput

class MyCustomNode(ComfyUINode):
    pos_prompt_text = StringInput(default='masterpiece', multiline=True)
    neg_prompt_text = StringInput(required=False, default='b&w', multiline=True)
    custom_weight = FloatInput(default=1.0, min=0.0, max=1.0, step=0.1)
    secret_parameter = FloatInput(hidden=True)
```

Input parameters can be `required`, `optional`, or `hidden`. Usually, most
parameters are required, so the default value for `required` is `True`. If
you need an optional parameter, pass in `required=False`. If you want a hidden
parameter, pass in `hidden=True`. Due to the assumption of required being the
default state, `hidden=True` will overwrite the required state.

You can find descriptions and explanations for all possible parameters in the
[documentation](/docs).

### Defining output parameters

Finally, add your output parameters. For each input parameter type there is a
corresponding output parameter type:

- `StringOutput`
- `IntegerOutput`
- ...

Define your output parameters
```python
from comfyui_types import ComfyUINode, StringOutput, FloatOutput

class MyCustomNode(ComfyUINode):
    # all the other things so far

    combined_prompt = StringOutput()
    calculated_score = FloatOutput()
```

Outputs are very straightforward to define, as they do not need any
configuration. The name for the `RETURN_NAMES` list is taken from the variable
name that you are assigning, i.e., `combined_prompt` in this example. The
example above would result in the following outputs:

```python
RETURN_TYPES = ('STRING', 'FLOAT')
RETURN_NAMES = ('combined_prompt', 'calculated_score')
```

## Examples

We are providing some examples [here](/examples) to help you better understand,
how to write your own custom nodes.

## Exporting custom nodes

Custom nodes can be manually exported as always like this:

```python
NODE_CLASS_MAPPING = {
    'MyCustomNode': MyCustomNode,
}
NODE_DISPLAY_NAME_MAPPING = {
    'MyCustomNode': 'My Cool Custom Node',
}
```

However, there is a convenience function to help with this:

```python
NODE_CLASS_MAPPING, NODE_DISPLAY_NAME_MAPPING = export_nodes([
    MyCustomNode,
])
```

This will automatically create the mapping tables according to the class name
and optionally the `display_name` property. If no `display_name` is set, the
class name is used.

## Under the hood

Internally, the `ComfyUINode` simply exports the parameters that you have
defined with proper classes and types in such a way that ComfyUI can load them.
That means for example that all your input parameters are collected and used to
automatically create the `INPUT_TYPES` dictionary that ComfyUI will try to find
in your node. For example, the input parameter

```python
pos_prompt_text = StringInput(default='masterpiece', multiline=True)
```

will automatically create the following entry in `INPUT_TYPES`:

```python
('STRING', {'default': 'masterpiece', 'multiline': True})
```

## Backwards compatibility

The way the `ComfyUINode` is defined is 100% backwards compatible with existing
nodes and practices. It simply creates the fields that are expected from a class
that ComfyUI imports as a custom node, like `INPUT_TYPES`. If at any point, you
do not like the conventions or they do not work with your use case, you can fall
back to the regular way of defining custom nodes in ComfyUI, i.e.:

- use `CATEGORY` instead of `category`
- use `FUNCTION` instead of `function`
- define your `INPUT_TYPES` or `RETURN_TYPES` as always

Only the parts that you choose to use will actually be active, you can mix and
match to suit your preferences.

## Extending with new types

Adding new types is very simple and straightforward. In most cases, a few lines
(less than 10) should be enough to bring in any custom type that you may need.
For example, IP-Adapter input and output types would look like this:

```python
import comfyui_types as ct

class IPAdapterInput(ct.InputBase):
    type_name = 'IPADAPTER'

class IPAdapterOutput(ct.OutputBase):
    type_name = 'IPADAPTER'
```

Those can then be imported and used throughout your project.

A more complex type with custom values is not much more complicated. Output
types remain exactly the same, as there are no options to define. For input
types, we have to define how they will be exported into `INPUT_TYPES`. Let's say
we want to define a (fictional) vector type for example:

```python
import comfyui_types as ct

class VectorInput(ct.InputBase):
    default: tuple[float, float] = (0.0, 0.0)

    def __init__(
            self,
            *,
            required: bool = True,
            hidden: bool | None = None,
            default: tuple[float, float] | None = None,
    ) -> None:
        super().__init__(required=required, hidden=hidden)

        if default:
            self.default = default

    def get_input_type(self) -> tuple:
        return ('VECTOR', {'default': self.default})

class VectorOutput(ct.OutputBase):
    type_name = 'VECTOR'
```

## Development

For development, there is no special setup, simply install the project in edit
mode (`pip install -e ./comfyui_types`) and go at it.

## License

This code is provided under the terms of the GPL-3.0 license.

## Contributions

Contributions of any kind (bug fixes, extensions, documentation etc.) are always
welcome, simply open a PR!