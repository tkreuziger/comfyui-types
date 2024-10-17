"""ComfyUI builtin inputs."""

from .base import InputBase


class ModelInput(InputBase):
    """ComfyUI Model input."""

    type_name = 'Model'


class VAEInput(InputBase):
    """ComfyUI VAE input."""

    type_name = 'VAE'


class CLIPInput(InputBase):
    """ComfyUI CLIP input."""

    type_name = 'CLIP'


class ConditioningInput(InputBase):
    """ComfyUI Conditioning input."""

    type_name = 'CONDITIONING'


class LatentInput(InputBase):
    """ComfyUI Latent input."""

    type_name = 'LATENT'


class ImageInput(InputBase):
    """ComfyUI Image input."""

    type_name = 'IMAGE'


class MaskInput(InputBase):
    """ComfyUI Mask input."""

    type_name = 'Mask'
