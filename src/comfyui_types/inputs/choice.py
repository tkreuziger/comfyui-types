"""ComfyUI choice input."""

from .base import InputBase, InputTypeReturnType


class ChoiceInput(InputBase):
    """ComfyUI choice input."""

    default: str
    choices: list[str]

    def __init__(
        self,
        choices: list[str],
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: str | None = None,
        display_name: str | None = None,
        lazy: bool = False,
    ) -> None:
        """Initialize ChoiceInput."""
        super().__init__(
            required=required,
            hidden=hidden,
            display_name=display_name,
            lazy=lazy,
        )

        if not choices or len(choices) == 0:
            error_msg = 'ChoiceInput must have at least one choice.'
            raise ValueError(error_msg)

        if default and default in choices:
            self.default = default
        else:
            self.default = choices[0]

        self.choices = choices

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return (self.choices, {'default': self.default, 'lazy': self.lazy})
