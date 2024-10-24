"""ComfyUI node."""

import json

from .inputs import InputBase
from .outputs import OutputBase

INPUT_TYPES_TYPE = dict[str, dict[str, tuple[str | int | float]]]


class ComfyUINodeMetaClass(type):
    """Meta class for ComfyUINode."""

    function: str = 'execute'
    category: str = ''
    display_name: str = ''
    output_node: bool = False
    deprecated: bool = False
    experimental: bool = False

    def _get_display_name(cls) -> str:
        """Return display name."""
        return cls.display_name if cls.display_name != '' else cls.__name__

    @property
    def FUNCTION(cls) -> str:  # noqa: N802
        """Return entry function."""
        return cls.function

    def INPUT_TYPES(cls) -> INPUT_TYPES_TYPE:  # noqa: N802
        """Return list of input types."""
        input_types: INPUT_TYPES_TYPE = {
            'required': {},
            'optional': {},
            'hidden': {},
        }

        for field in cls.__dict__:
            if isinstance(getattr(cls, field), InputBase):
                field_obj = getattr(cls, field)
                input_type = field_obj.get_input_type()

                if field_obj.display_name not in [None, '']:
                    field_name = field_obj.display_name
                else:
                    field_name = field
                input_types[field_obj.input_type.value][field_name] = input_type

        return input_types

    @property
    def OUTPUT_NODE(cls) -> bool:  # noqa: N802
        """Whether this is an output node or not."""
        return cls.output_node

    @property
    def RETURN_TYPES(cls) -> tuple[str, ...]:  # noqa: N802
        """Return list of return types."""
        output_types = []
        for field in cls.__dict__:
            if isinstance(getattr(cls, field), OutputBase):
                field_obj = getattr(cls, field)
                output_types.append(str(field_obj.get_output_type()))

        return tuple(output_types)

    @property
    def RETURN_NAMES(cls) -> tuple[str]:  # noqa: N802
        """Return list of return names."""
        output_names = []
        for field in cls.__dict__:
            if isinstance(getattr(cls, field), OutputBase):
                field_obj = getattr(cls, field)

                if field_obj.display_name not in [None, '']:
                    field_name = field_obj.display_name
                else:
                    field_name = field
                output_names.append(field_name)

        return tuple(output_names)  # type: ignore  # noqa: PGH003

    @property
    def DEPRECATED(cls) -> bool:  # noqa: N802
        """Indicated whether the node is deprecated."""
        return cls.deprecated

    @property
    def EXPERIMENTAL(cls) -> bool:  # noqa: N802
        """Indicated whether the node is experimental."""
        return cls.experimental

    def describe(cls) -> str:
        """Describe node."""
        description = f'"{cls.__name__}" in "{cls.category}"'
        description += f'\nEntry: {cls.FUNCTION}'
        intputs = f'Inputs:\n{json.dumps(cls.INPUT_TYPES(), indent=2)}'
        outputs = f'Outputs: {cls.RETURN_TYPES}'
        return_names = f'Return names: {cls.RETURN_NAMES}'

        return f'{description}\n{intputs}\n{outputs}\n{return_names}'


class ComfyUINode(metaclass=ComfyUINodeMetaClass):
    """Abstract base class for all typed ComfyUI nodes."""
