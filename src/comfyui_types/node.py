"""ComfyUI node."""

import json

from .inputs import InputBase
from .outputs import OutputBase


class ComfyUINode:
    """Abstract base class for all typed ComfyUI nodes."""

    function = 'execute'
    category = ''
    display_name = ''
    output_node = False

    @classmethod
    def _get_display_name(cls) -> str:
        """Return display name."""
        return cls.display_name if cls.display_name != '' else cls.__name__

    @classmethod
    def INPUT_TYPES(cls) -> dict[str, dict[str, tuple]]:  # noqa: N802
        """Return list of input types."""
        input_types = {'required': {}, 'optional': {}, 'hidden': {}}

        for field in cls.__dict__:
            if isinstance(getattr(cls, field), InputBase):
                field_obj = getattr(cls, field)
                input_type = field_obj.get_input_type()
                input_types[field_obj.input_type.value][field] = input_type

        return input_types

    @classmethod
    @property
    def FUNCTION(cls) -> str:  # noqa: N802
        """Return entry function."""
        return cls.function

    @classmethod
    @property
    def OUTPUT_NODE(cls) -> bool:  # noqa: N802
        """Whether this is an output node or not."""
        return cls.output_node

    @classmethod
    @property
    def RETURN_TYPES(cls) -> tuple[str]:  # noqa: N802
        """Return list of return types."""
        output_types = []
        for field in cls.__dict__:
            if isinstance(getattr(cls, field), OutputBase):
                field_obj = getattr(cls, field)
                output_types.append(str(field_obj.get_output_type()))

        return tuple(output_types)

    @classmethod
    @property
    def RETURN_NAMES(cls) -> tuple[str]:  # noqa: N802
        """Return list of return names."""
        output_names = [
            field
            for field in cls.__dict__
            if isinstance(getattr(cls, field), OutputBase)
        ]

        return tuple(output_names)  # type: ignore  # noqa: PGH003

    @classmethod
    def describe(cls) -> str:
        """Describe node."""
        description = f'"{cls.__name__}" in "{cls.category}"'
        description += f'\nEntry: {cls.FUNCTION}'
        intputs = f'Inputs:\n{json.dumps(cls.INPUT_TYPES(), indent=2)}'
        outputs = f'Outputs: {cls.RETURN_TYPES}'
        return_names = f'Return names: {cls.RETURN_NAMES}'

        return f'{description}\n{intputs}\n{outputs}\n{return_names}'
