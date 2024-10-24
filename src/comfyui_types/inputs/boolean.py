"""ComfyUI boolean input."""

from .base import InputBase, InputTypeReturnType


class BooleanInput(InputBase):
    """ComfyUI boolean input."""

    default: bool = False
    lazy: bool = True

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: bool = False,
        display_name: str | None = None,
    ) -> None:
        """Initialize BooleanInput."""
        super().__init__(
            required=required, hidden=hidden, display_name=display_name
        )

        self.default = default

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return ('BOOL', {'default': self.default, 'lazy': self.lazy})
