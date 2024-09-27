"""ComfyUI output."""


class OutputBase:
    """ComfyUI output."""

    output_type = ''

    @classmethod
    def get_output_type(cls) -> str:
        """Return output type."""
        return cls.output_type
