"""Tests for input types."""

import pytest

from comfyui_types.inputs import (
    BooleanInput,
    ChoiceInput,
    CLIPInput,
    ConditioningInput,
    FloatInput,
    ImageInput,
    InputBase,
    InputType,
    IntegerInput,
    LatentInput,
    MaskInput,
    ModelInput,
    NumberDisplayMode,
    StringInput,
    VAEInput,
)


class TestInputBase:
    """Tests for InputBase."""

    def test_default_values(self) -> None:
        inp = InputBase()
        assert inp.input_type == InputType.REQUIRED
        assert inp.type_name == ''
        assert inp.display_name is None
        assert inp.lazy is False

    def test_required(self) -> None:
        inp = InputBase(required=True)
        assert inp.input_type == InputType.REQUIRED

    def test_optional(self) -> None:
        inp = InputBase(required=False)
        assert inp.input_type == InputType.OPTIONAL

    def test_hidden(self) -> None:
        inp = InputBase(hidden=True)
        assert inp.input_type == InputType.HIDDEN

    def test_hidden_overrides_required(self) -> None:
        inp = InputBase(required=True, hidden=True)
        assert inp.input_type == InputType.HIDDEN

    def test_display_name(self) -> None:
        inp = InputBase(display_name='Custom Name')
        assert inp.display_name == 'Custom Name'

    def test_lazy(self) -> None:
        inp = InputBase(lazy=True)
        assert inp.lazy is True

    def test_get_input_type(self) -> None:
        inp = InputBase()
        assert inp.get_input_type() == ('',)


class TestStringInput:
    """Tests for StringInput."""

    def test_default_values(self) -> None:
        inp = StringInput()
        assert inp.default == ''
        assert inp.multiline is False

    def test_custom_values(self) -> None:
        inp = StringInput(default='hello', multiline=True)
        assert inp.default == 'hello'
        assert inp.multiline is True

    def test_get_input_type(self) -> None:
        inp = StringInput(default='test', multiline=True, lazy=True)
        result = inp.get_input_type()
        assert result == (
            'STRING',
            {'default': 'test', 'multiline': True, 'lazy': True},
        )


class TestIntegerInput:
    """Tests for IntegerInput."""

    def test_default_values(self) -> None:
        inp = IntegerInput()
        assert inp.default == 0
        assert inp.min == 0
        assert inp.max == 1
        assert inp.step == 1
        assert inp.display == NumberDisplayMode.NUMBER

    def test_custom_values(self) -> None:
        inp = IntegerInput(
            default=5,
            min=1,
            max=10,
            step=2,
            display=NumberDisplayMode.SLIDER,
        )
        assert inp.default == 5
        assert inp.min == 1
        assert inp.max == 10
        assert inp.step == 2
        assert inp.display == NumberDisplayMode.SLIDER

    def test_get_input_type(self) -> None:
        inp = IntegerInput(default=5, min=0, max=100, step=5)
        result = inp.get_input_type()
        assert result == (
            'INT',
            {
                'default': 5,
                'min': 0,
                'max': 100,
                'step': 5,
                'display': 'number',
                'lazy': False,
            },
        )


class TestFloatInput:
    """Tests for FloatInput."""

    def test_default_values(self) -> None:
        inp = FloatInput()
        assert inp.default == 0.0
        assert inp.min == 0.0
        assert inp.max == 1.0
        assert inp.step == 1.0
        assert inp.round is False
        assert inp.display == NumberDisplayMode.NUMBER

    def test_custom_values(self) -> None:
        inp = FloatInput(
            default=0.5,
            min=0.0,
            max=2.0,
            step=0.1,
            round=0.01,
            display=NumberDisplayMode.SLIDER,
        )
        assert inp.default == 0.5
        assert inp.min == 0.0
        assert inp.max == 2.0
        assert inp.step == 0.1
        assert inp.round == 0.01
        assert inp.display == NumberDisplayMode.SLIDER

    def test_round_none_uses_step(self) -> None:
        inp = FloatInput(step=0.25, round=None)
        assert inp.round == 0.25

    def test_get_input_type(self) -> None:
        inp = FloatInput(default=0.5, min=0.0, max=1.0, step=0.1)
        result = inp.get_input_type()
        assert result == (
            'FLOAT',
            {
                'default': 0.5,
                'min': 0.0,
                'max': 1.0,
                'step': 0.1,
                'round': False,
                'display': 'number',
                'lazy': False,
            },
        )


class TestBooleanInput:
    """Tests for BooleanInput."""

    def test_default_values(self) -> None:
        inp = BooleanInput()
        assert inp.default is False
        assert inp.label_on == 'true'
        assert inp.label_off == 'false'

    def test_custom_values(self) -> None:
        inp = BooleanInput(default=True, label_on='yes', label_off='no')
        assert inp.default is True
        assert inp.label_on == 'yes'
        assert inp.label_off == 'no'

    def test_get_input_type(self) -> None:
        inp = BooleanInput(
            default=True, label_on='enabled', label_off='disabled'
        )
        result = inp.get_input_type()
        assert result == (
            'BOOLEAN',
            {
                'default': True,
                'lazy': False,
                'label_on': 'enabled',
                'label_off': 'disabled',
            },
        )


class TestChoiceInput:
    """Tests for ChoiceInput."""

    def test_default_uses_first_choice(self) -> None:
        inp = ChoiceInput(choices=['a', 'b', 'c'])
        assert inp.default == 'a'
        assert inp.choices == ['a', 'b', 'c']

    def test_explicit_default(self) -> None:
        inp = ChoiceInput(choices=['a', 'b', 'c'], default='b')
        assert inp.default == 'b'

    def test_invalid_default_falls_back_to_first(self) -> None:
        inp = ChoiceInput(choices=['a', 'b'], default='invalid')
        assert inp.default == 'a'

    def test_empty_choices_raises(self) -> None:
        with pytest.raises(ValueError, match='at least one choice'):
            ChoiceInput(choices=[])

    def test_get_input_type(self) -> None:
        inp = ChoiceInput(choices=['x', 'y', 'z'], default='y')
        result = inp.get_input_type()
        assert result == (['x', 'y', 'z'], {'default': 'y', 'lazy': False})


class TestBuiltinInputs:
    """Tests for builtin input types."""

    def test_model_input(self) -> None:
        inp = ModelInput()
        assert inp.type_name == 'Model'
        assert inp.get_input_type() == ('Model',)

    def test_vae_input(self) -> None:
        inp = VAEInput()
        assert inp.type_name == 'VAE'
        assert inp.get_input_type() == ('VAE',)

    def test_clip_input(self) -> None:
        inp = CLIPInput()
        assert inp.type_name == 'CLIP'
        assert inp.get_input_type() == ('CLIP',)

    def test_conditioning_input(self) -> None:
        inp = ConditioningInput()
        assert inp.type_name == 'CONDITIONING'
        assert inp.get_input_type() == ('CONDITIONING',)

    def test_latent_input(self) -> None:
        inp = LatentInput()
        assert inp.type_name == 'LATENT'
        assert inp.get_input_type() == ('LATENT',)

    def test_image_input(self) -> None:
        inp = ImageInput()
        assert inp.type_name == 'IMAGE'
        assert inp.get_input_type() == ('IMAGE',)

    def test_mask_input(self) -> None:
        inp = MaskInput()
        assert inp.type_name == 'Mask'
        assert inp.get_input_type() == ('Mask',)


class TestInputType:
    """Tests for InputType enum."""

    def test_values(self) -> None:
        assert InputType.REQUIRED.value == 'required'
        assert InputType.OPTIONAL.value == 'optional'
        assert InputType.HIDDEN.value == 'hidden'


class TestNumberDisplayMode:
    """Tests for NumberDisplayMode enum."""

    def test_values(self) -> None:
        assert NumberDisplayMode.NUMBER.value == 'number'
        assert NumberDisplayMode.SLIDER.value == 'slider'
