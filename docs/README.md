# Documentation

This is the documentation for the `comfyui_types` package.

## [Input types](/docs/input_types.md)

The following types are included:

- `InputBase`
- `NumberDisplayMode`
- `InputType`
- `StringInput`
- `BooleanInput`
- `IntegerInput`
- `FloatInput`
- `ChoiceInput`
- `ModelInput`
- `VAEInput`
- `CLIPInput`
- `ConditioningInput`
- `ImageInput`
- `LatentInput`
- `MaskInput`

## Output types

The following output types are included:

- `OutputBase`
- `StringOutput`
- `IntegerOutput`
- `FloatOutput`
- `CLIPOutput`
- `ConditioningOutput`
- `ImageOutput`
- `LatentOutput`
- `MaskOutput`
- `ModelOutput`
- `VAEOutput`

Output types do not require any additional configuration. They are simply
defined as fields like this:

```python
from comfyui_types import ComfyUINode, StringOutput, FloatOutput, ModelOutput

class MyCustomNode(ComfyUINode):
    # Your other fields.
    # ...
    combined_prompt = StringOutput()
    calculated_score = FloatOutput()
    improved_model = ModelOutput()
```

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

## Python support

`comfyui-types` currently relies on Python 3.10 for type annotations, but could
probably made to work with earlier versions like 3.8.
