"""ComfyUI builtin outputs."""

from .base import OutputBase


class ModelOutput(OutputBase):
    """ComfyUI Model output."""

    output_type = 'Model'


class VAEOutput(OutputBase):
    """ComfyUI VAE output."""

    output_type = 'VAE'


class CLIPOutput(OutputBase):
    """ComfyUI CLIP output."""

    output_type = 'CLIP'


class ConditioningOutput(OutputBase):
    """ComfyUI Conditioning output."""

    output_type = 'CONDITIONING'


class LatentOutput(OutputBase):
    """ComfyUI Latent output."""

    output_type = 'LATENT'


class ImageOutput(OutputBase):
    """ComfyUI Image output."""

    output_type = 'IMAGE'


class MaskOutput(OutputBase):
    """ComfyUI Mask output."""

    output_type = 'Mask'
