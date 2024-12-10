"""ComfyUI boolean input."""

from .base import InputBase, InputTypeReturnType


class BooleanInput(InputBase):
    """ComfyUI boolean input."""

    default: bool = False
    label_on: str = 'true'
    label_off: str = 'false'

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: bool = False,
        label_on: str = 'true',
        label_off: str = 'false',
        display_name: str | None = None,
        lazy: bool = False,
    ) -> None:
        """Initialize BooleanInput."""
        super().__init__(
            required=required,
            hidden=hidden,
            display_name=display_name,
            lazy=lazy,
        )

        self.default = default
        self.label_on = label_on
        self.label_off = label_off

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return (
            'BOOLEAN',
            {
                'default': self.default,
                'lazy': self.lazy,
                'label_on': self.label_on,
                'label_off': self.label_off,
            },
        )
