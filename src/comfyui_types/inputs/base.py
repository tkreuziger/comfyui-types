"""Base types."""

from abc import abstractmethod
from enum import Enum


class InputType(str, Enum):
    """Input types."""

    REQUIRED = 'required'
    OPTIONAL = 'optional'
    HIDDEN = 'hidden'


class InputBase:
    """ComfyUI input."""

    input_type: InputType = InputType.REQUIRED
    type_name: str = ''
    display_name: str | None = None

    def __init__(
        self,
        *,
        required: bool = True,
        hidden: bool | None = None,
        display_name: str | None = None,
    ) -> None:
        """Initialize InputBase."""
        if required and not hidden:
            self.input_type = InputType.REQUIRED
        elif hidden:
            self.input_type = InputType.HIDDEN
        else:
            self.input_type = InputType.OPTIONAL

        self.display_name = display_name

    @abstractmethod
    def get_input_type(self) -> tuple:
        """Return input type."""
        return (self.type_name,)


class NumberDisplayMode(str, Enum):
    """Number display mode."""

    NUMBER = 'number'
    SLIDER = 'slider'
