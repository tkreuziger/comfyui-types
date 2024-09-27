"""ComfyUI boolean input."""

from .base import InputBase


class BooleanInput(InputBase):
    """ComfyUI boolean input."""

    default: bool = False

    def __init__(
            self,
            *,
            required: bool = True,
            hidden: bool | None = None,
            default: bool = False
    ) -> None:
        """Initialize BooleanInput."""
        super().__init__(required=required, hidden=hidden)

        self.default = default

    def get_input_type(self) -> tuple:
        """Return input type."""
        return ('BOOL', {'default': self.default})
