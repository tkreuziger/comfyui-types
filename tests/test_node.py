"""Tests for ComfyUINode."""

from comfyui_types.inputs import FloatInput, IntegerInput, StringInput
from comfyui_types.node import ComfyUINode
from comfyui_types.outputs import IntegerOutput, StringOutput


class TestNode(ComfyUINode):
    """Test node for testing."""

    function = 'run'
    category = 'test'
    display_name = 'Test Node'
    output_node = True
    deprecated = False
    experimental = True

    name = StringInput(default='hello', display_name='Name')
    count = IntegerInput(default=5, min=1, max=10)
    optional_input = FloatInput(required=False, display_name='Optional')

    text_output = StringOutput(display_name='Text')
    number_output = IntegerOutput()


class TestComfyUINode:
    """Tests for ComfyUINode."""

    def test_class_attributes_set(self) -> None:
        assert TestNode.FUNCTION == 'run'
        assert TestNode.CATEGORY == 'test'
        assert TestNode.DISPLAY_NAME == 'Test Node'
        assert TestNode.OUTPUT_NODE is True
        assert TestNode.DEPRECATED is False
        assert TestNode.EXPERIMENTAL is True

    def test_input_types(self) -> None:
        input_types = TestNode.INPUT_TYPES()

        assert 'required' in input_types
        assert 'optional' in input_types
        assert 'hidden' in input_types

        assert 'Name' in input_types['required']
        assert 'count' in input_types['required']
        assert 'Optional' in input_types['optional']

    def test_input_types_uses_display_name(self) -> None:
        input_types = TestNode.INPUT_TYPES()
        assert 'Name' in input_types['required']
        assert 'name' not in input_types['required']

    def test_input_types_uses_field_name_when_no_display_name(self) -> None:
        input_types = TestNode.INPUT_TYPES()
        assert 'count' in input_types['required']

    def test_return_types(self) -> None:
        assert TestNode.RETURN_TYPES == ('STRING', 'INT')

    def test_return_names(self) -> None:
        assert TestNode.RETURN_NAMES == ('Text', 'number_output')

    def test_return_names_uses_display_name(self) -> None:
        assert 'Text' in TestNode.RETURN_NAMES

    def test_return_names_uses_field_name_when_no_display_name(self) -> None:
        assert 'number_output' in TestNode.RETURN_NAMES

    def test_get_display_name_with_custom_name(self) -> None:
        assert TestNode._get_display_name() == 'Test Node'

    def test_describe(self) -> None:
        node = TestNode()
        description = node.describe()

        assert 'TestNode' in description
        assert 'test' in description
        assert 'run' in description
        assert 'STRING' in description
        assert 'INT' in description


class TestComfyUINodeDefaults:
    """Tests for ComfyUINode default values."""

    def test_default_function(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.FUNCTION == 'execute'

    def test_default_category(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.CATEGORY == 'default'

    def test_default_display_name(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.DISPLAY_NAME == 'Unnamed Node'

    def test_default_output_node(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.OUTPUT_NODE is False

    def test_default_deprecated(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.DEPRECATED is False

    def test_default_experimental(self) -> None:
        class DefaultNode(ComfyUINode):
            pass

        assert DefaultNode.EXPERIMENTAL is False

    def test_get_display_name_uses_class_name_when_empty(self) -> None:
        class MyCustomNode(ComfyUINode):
            display_name = ''

        assert MyCustomNode._get_display_name() == 'MyCustomNode'

    def test_empty_return_types(self) -> None:
        class NoOutputNode(ComfyUINode):
            pass

        assert NoOutputNode.RETURN_TYPES == ()

    def test_empty_return_names(self) -> None:
        class NoOutputNode(ComfyUINode):
            pass

        assert NoOutputNode.RETURN_NAMES == ()
