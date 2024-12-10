"""ComfyUI integer input."""

from .base import InputBase, InputTypeReturnType, NumberDisplayMode


class IntegerInput(InputBase):
    """ComfyUI integer input."""

    default: int = 0
    min: int = 0
    max: int = 0
    step: int = 1
    display: NumberDisplayMode = NumberDisplayMode.NUMBER

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: int = 0,
        min: int = 0,  # noqa: A002
        max: int = 1,  # noqa: A002
        step: int = 1,
        display: NumberDisplayMode = NumberDisplayMode.NUMBER,
        display_name: str | None = None,
        lazy: bool = False,
    ) -> None:
        """Initialize IntegerInput."""
        super().__init__(
            required=required,
            hidden=hidden,
            display_name=display_name,
            lazy=lazy,
        )

        self.default = default
        self.min = min
        self.max = max
        self.step = step
        self.display = display

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return (
            'INT',
            {
                'default': self.default,
                'min': self.min,
                'max': self.max,
                'step': self.step,
                'display': self.display.value,
                'lazy': self.lazy,
            },
        )
