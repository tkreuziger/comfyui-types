"""ComfyUI string input."""

from .base import InputBase


class StringInput(InputBase):
    """ComfyUI string input."""

    default: str = ''
    multiline: bool = False

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: str = '',
        multiline: bool = False,
    ) -> None:
        """Initialize StringInput."""
        super().__init__(required=required, hidden=hidden)

        self.default = default
        self.multiline = multiline

    def get_input_type(self) -> tuple:
        """Return input type."""
        return (
            'STRING',
            {
                'default': self.default,
                'multiline': self.multiline,
            },
        )
