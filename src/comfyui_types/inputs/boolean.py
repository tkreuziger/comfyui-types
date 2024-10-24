"""ComfyUI boolean input."""

from .base import InputBase, InputTypeReturnType


class BooleanInput(InputBase):
    """ComfyUI boolean input."""

    default: bool = False
    lazy: bool = True
    label_on: str = 'On'
    label_off: str = 'Off'

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: bool = False,
        label_on: str = 'On',
        label_off: str = 'Off',
        display_name: str | None = None,
    ) -> None:
        """Initialize BooleanInput."""
        super().__init__(
            required=required, hidden=hidden, display_name=display_name
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
