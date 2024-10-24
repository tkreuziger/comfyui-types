"""ComfyUI string input."""

from .base import InputBase, InputTypeReturnType


class StringInput(InputBase):
    """ComfyUI string input."""

    default: str = ''
    multiline: bool = False
    lazy: bool = True

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: str = '',
        multiline: bool = False,
        display_name: str | None = None,
    ) -> None:
        """Initialize StringInput."""
        super().__init__(
            required=required, hidden=hidden, display_name=display_name
        )

        self.default = default
        self.multiline = multiline

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return (
            'STRING',
            {
                'default': self.default,
                'multiline': self.multiline,
                'lazy': self.lazy,
            },
        )
