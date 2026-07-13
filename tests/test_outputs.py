"""Tests for output types."""

from comfyui_types.outputs import (
    CLIPOutput,
    ConditioningOutput,
    FloatOutput,
    ImageOutput,
    IntegerOutput,
    LatentOutput,
    MaskOutput,
    ModelOutput,
    OutputBase,
    StringOutput,
    VAEOutput,
)


class TestOutputBase:
    """Tests for OutputBase."""

    def test_default_values(self) -> None:
        out = OutputBase()
        assert out.output_type == ''
        assert out.display_name is None

    def test_display_name(self) -> None:
        out = OutputBase(display_name='Custom Output')
        assert out.display_name == 'Custom Output'

    def test_get_output_type(self) -> None:
        out = OutputBase()
        assert out.get_output_type() == ''


class TestBasicOutputs:
    """Tests for basic output types."""

    def test_string_output(self) -> None:
        out = StringOutput()
        assert out.output_type == 'STRING'
        assert out.get_output_type() == 'STRING'

    def test_integer_output(self) -> None:
        out = IntegerOutput()
        assert out.output_type == 'INT'
        assert out.get_output_type() == 'INT'

    def test_float_output(self) -> None:
        out = FloatOutput()
        assert out.output_type == 'FLOAT'
        assert out.get_output_type() == 'FLOAT'


class TestBuiltinOutputs:
    """Tests for builtin output types."""

    def test_model_output(self) -> None:
        out = ModelOutput()
        assert out.output_type == 'Model'
        assert out.get_output_type() == 'Model'

    def test_vae_output(self) -> None:
        out = VAEOutput()
        assert out.output_type == 'VAE'
        assert out.get_output_type() == 'VAE'

    def test_clip_output(self) -> None:
        out = CLIPOutput()
        assert out.output_type == 'CLIP'
        assert out.get_output_type() == 'CLIP'

    def test_conditioning_output(self) -> None:
        out = ConditioningOutput()
        assert out.output_type == 'CONDITIONING'
        assert out.get_output_type() == 'CONDITIONING'

    def test_latent_output(self) -> None:
        out = LatentOutput()
        assert out.output_type == 'LATENT'
        assert out.get_output_type() == 'LATENT'

    def test_image_output(self) -> None:
        out = ImageOutput()
        assert out.output_type == 'IMAGE'
        assert out.get_output_type() == 'IMAGE'

    def test_mask_output(self) -> None:
        out = MaskOutput()
        assert out.output_type == 'Mask'
        assert out.get_output_type() == 'Mask'
