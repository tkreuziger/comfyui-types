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
