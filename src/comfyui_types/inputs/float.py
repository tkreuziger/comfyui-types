"""ComfyUI float input."""

from .base import InputBase, InputTypeReturnType, NumberDisplayMode


class FloatInput(InputBase):
    """ComfyUI float input."""

    default: float = 0.0
    min: float = 0.0
    max: float = 1.0
    step: float = 0.1
    round: float | bool = False
    display: NumberDisplayMode = NumberDisplayMode.NUMBER
    lazy: bool = True

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        default: float = 0.0,
        min: float = 0.0,  # noqa: A002
        max: float = 1.0,  # noqa: A002
        step: float = 1.0,
        round: float | bool | None = False,  # noqa: A002
        display: NumberDisplayMode = NumberDisplayMode.NUMBER,
        display_name: str | None = None,
    ) -> None:
        """Initialize FloatInput."""
        super().__init__(
            required=required, hidden=hidden, display_name=display_name
        )

        self.default = default
        self.min = min
        self.max = max
        self.step = step

        if round is None:
            self.round = step
        else:
            self.round = round

        self.display = display

    def get_input_type(self) -> InputTypeReturnType:
        """Return input type."""
        return (
            'FLOAT',
            {
                'default': self.default,
                'min': self.min,
                'max': self.max,
                'step': self.step,
                'round': self.round,
                'display': self.display.value,
                'lazy': self.lazy,
            },
        )
