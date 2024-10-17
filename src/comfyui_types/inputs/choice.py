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
        default: str | None = None,
        choices: list,
    ) -> None:
        """Initialize ChoiceInput."""
        super().__init__(required=required, hidden=hidden)

        if not choices or len(choices) == 0:
            error_msg = 'ChoiceInput must have at least one choice.'
            raise ValueError(error_msg)

        if default and default in choices:
            self.default = default
        else:
            self.default = choices[0]

        self.choices = choices

    def get_input_type(self) -> tuple:
        """Return input type."""
        return (self.choices, {'default': self.default})
