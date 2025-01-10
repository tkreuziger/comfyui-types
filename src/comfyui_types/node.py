"""ComfyUI node."""

import json
from typing import Any

from .inputs import InputBase
from .outputs import OutputBase

INPUT_TYPES_TYPE = dict[str, dict[str, tuple[str | int | float]]]


class ComfyUINode:
    """Abstract base class for all typed ComfyUI nodes."""

    function: str = 'execute'
    category: str = 'default'
    display_name: str = 'Unnamed Node'
    output_node: bool = False
    deprecated: bool = False
    experimental: bool = False

    def __init_subclass__(cls, **kwargs: Any) -> None:  # noqa: ANN401
        """Initialize subclass attributes."""
        super().__init_subclass__(**kwargs)

        cls.FUNCTION = cls.function  # type: ignore[attr-defined]
        cls.CATEGORY = cls.category  # type: ignore[attr-defined]
        cls.DISPLAY_NAME = cls.display_name  # type: ignore[attr-defined]
        cls.OUTPUT_NODE = cls.output_node  # type: ignore[attr-defined]
        cls.DEPRECATED = cls.deprecated  # type: ignore[attr-defined]
        cls.EXPERIMENTAL = cls.experimental  # type: ignore[attr-defined]

    @classmethod
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

    @classmethod
    @property
    def RETURN_TYPES(cls) -> tuple[str, ...]:  # noqa: N802
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

    @classmethod
    def _get_display_name(cls) -> str:
        """Return display name."""
        return cls.display_name if cls.display_name != '' else cls.__name__

    def describe(self) -> str:
        """Describe node."""
        name = self.__class__.__name__
        description = f'Node "{name}" in category "{self.category}"'
        description += f'\nEntry: {self.function}'
        inputs = f'Inputs:\n{json.dumps(self.INPUT_TYPES(), indent=2)}'
        outputs = f'Outputs: {self.RETURN_TYPES}'
        return_names = f'Return names: {self.RETURN_NAMES}'

        return f'{description}\n{inputs}\n{outputs}\n{return_names}'
