"""ComfyUI choice input."""

from .base import InputBase


class ChoiceInput(InputBase):
    """ComfyUI choice input."""

    default: str
    choices: list

    def __init__(
            self,
            *,
            required: bool = True,
            hidden: bool | None = None,
            default: str,
            choices: list,
    ) -> None:
        """Initialize ChoiceInput."""
        super().__init__(required=required, hidden=hidden)

        self.default = default
        self.choices = choices

    def get_input_type(self) -> tuple:
        """Return input type."""
        return (self.choices, {'default': self.default})



