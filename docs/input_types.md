# Input types

## Included types

The most common types are included in the type library and should enable you to
write your own nodes. If you need to add a new type, please refer to the
[section on extending](/docs/README.md#extending-with-new-types).

### InputBase

`comfyui_types.base.InputBase`

The base class for all input types. Usually, you will only need this class to
create your own custom input types.

The one shared parameter across all inputs is the `display_name` parameter that
defines the name used in the UI of the node.

### NumberDisplayMode

`comfyui_types.base.NumberDisplayMode`

Integer and float inputs can either be rendered as simple number inputs or as
sliders by ComfyUI.

Values:
- `NumberDisplayMode.NUMBER`: A simple number input.
- `NumberDisplayMode.SLIDER`: A slider input.

### InputType

`comfyui_types.base.InputType`

This type determines, whether an input is required, optional, or hidden. You do
not need to use this type directly, use the provided parameters `required: bool
= True` and `hidden: bool | None = None` of the `InputBase` constructor instead.

By default, all inputs are required. Setting `hidden=True` will overwrite the
required state.

Example:

```python
# An optional input is achieved by setting required=False.
some_optional_input = IntegerInput(required=False)

# A hidden input is achieved by setting hidden=True.
some_hidden_input = FloatInput(hidden=True)

# Will also be hidden, as the required state is overriden.
yet_more_hidden_input = FloatInput(hidden=True, required=True)
```

### StringInput

`comfyui_types.inputs.StringInput`

A simple string input with two optional parameters:

- `default: str = ''`: The default value of the input, an empty string if not
set.
- `multiline: bool = False`: Whether the input should be multiline. `False` by
default.

Example:

```python
my_string_input = StringInput(
    default='hello world',
    multiline=True,
)
```

### BooleanInput

`comfyui_types.inputs.BooleanInput`

A simple boolean input with three optional `default` parameters (which itself
defaults to `False`):
- `default: bool = False`: The default value for this input.
- `label_on: str = 'true'`: The label shown in the UI, when the input is true.
- `label_off: str = 'false'`: The label shown in the UI, when the input is false.

Example:

```python
my_bool_input = BooleanInput(default=True, label_on='Yes', label_off='No')
```

### IntegerInput

`comfyui_types.inputs.IntegerInput`

A simple integer input with the following optional parameters:

- `default: int = 0`: The default value of the input, `0` if not set.
- `min: int = 0`: The minimum value of the input, `0` by default.
- `max: int = 1`: The maximum value of the input, `1` by default.
- `step: int = 1`: The step value of the input, `1` by default.
- `display: NumberDisplayMode = NumberDisplayMode.NUMBER`: The display mode of
the input, either as [a number or a slider](#NumberDisplayMode), `NUMBER` by default.

Example:

```python
my_int_input = IntegerInput(
    default=4,
    min=0,
    max=10,
    step=2,
    display=NumberDisplayMode.SLIDER,
)
```

### FloatInput

`comfyui_types.inputs.FloatInput`

A simple integer input with the following optional parameters:

- `default: float = 0.0`: The default value of the input, `0.0` if not set.
- `min: float = 0.0`: The minimum value of the input, `0.0` by default.
- `max: float = 1.0`: The maximum value of the input, `1.0` by default.
- `step: float = 0.1`: The step value of the input, `0.1` by default.
- `round: float | bool = False`: The rounding precision of the input, `False` if
no rounding should be performed. If not specified, the value of `step` will be
used.
- `display: NumberDisplayMode = NumberDisplayMode.NUMBER`: The display mode of
the input, either as [a number or a slider](#NumberDisplayMode), `NUMBER` by
default.

Example:

```python
my_float_input = FloatInput(
    default=4.0,
    min=0.0,
    max=10.0,
    step=0.5,
    round=0.5,
    display=NumberDisplayMode.SLIDER,
)
```

### ChoiceInput

`comfyui_types.inputs.ChoiceInput`

A simple choice input that allows selection from a list of options with the
following parameters:

- `default: str | None = None`: The default choice from the list. If `None`, the
first option from the options list will be selected.
- `options: list[str]`: The list of options to choose from.

Example:

```python
my_choice_input = ChoiceInput(
    default='foo',
    choices=['foo', 'bar', 'baz'],
)
```

Should the default value not be in the list, the first value from the list will
be used. If no default value is provided, the first option from the list will be
used.

### Builtin ComfyUI types

The following types represent the core ComfyUI types. They do not need any
parameters, except the [input type](#InputType).

#### ModelInput

`comfyui_types.inputs.builtin.ModelInput`

A parameter that accepts a model (`MODEL` ComfyUI type).

Example:

```python
my_model_input = ModelInput()
```

#### VAEInput

`comfyui_types.inputs.builtin.VAEInput`

A parameter that accepts a VAE (`VAE` ComfyUI type).

Example:

```python
my_vae_input = VAEInput()
```

#### CLIPInput

`comfyui_types.inputs.builtin.CLIPInput`

A parameter that accepts a CLIP (`CLIP` ComfyUI type).

Example:

```python
my_clip_input = CLIPInput()
```

#### ConditioningInput

`comfyui_types.inputs.builtin.ConditioningInput`

A parameter that accepts a conditioning (`CONDITIONING` ComfyUI type).

Example:

```python
my_cond_input = ConditioningInput()
```

#### ImageInput

`comfyui_types.inputs.builtin.ImageInput`

A parameter that accepts an image (`IMAGE` ComfyUI type).

Example:

```python
my_image_input = ImageInput()
```

#### LatentInput

`comfyui_types.inputs.builtin.LatentInput`

A parameter that accepts a latent image (`LATENT` ComfyUI type).

Example:

```python
my_latent_input = LatentInput()
```

#### MaskInput

`comfyui_types.inputs.builtin.MaskInput`

A parameter that accepts a mask (`MASK` ComfyUI type).

Example:

```python
my_mask_input = MaskInput()
```
