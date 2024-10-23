"""ComfyUI output."""


class OutputBase:
    """ComfyUI output."""

    output_type = ''
    display_name: str | None = None

    def __init__(self, *, display_name: str | None = None) -> None:
        """Initialize an output."""
        self.display_name = display_name

    @classmethod
    def get_output_type(cls) -> str:
        """Return output type."""
        return cls.output_type
