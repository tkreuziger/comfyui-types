"""Basic output types."""

from .base import OutputBase


class StringOutput(OutputBase):
    """ComfyUI string output."""

    output_type = 'STRING'


class IntegerOutput(OutputBase):
    """ComfyUI integer output."""

    output_type = 'INT'


class FloatOutput(OutputBase):
    """ComfyUI float output."""

    output_type = 'FLOAT'
