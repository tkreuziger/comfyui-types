"""Tests for export_nodes."""

from comfyui_types.export import export_nodes
from comfyui_types.inputs import StringInput
from comfyui_types.node import ComfyUINode
from comfyui_types.outputs import StringOutput


class NodeA(ComfyUINode):
    """First test node."""

    display_name = 'Node A'
    inp = StringInput()
    out = StringOutput()


class NodeB(ComfyUINode):
    """Second test node."""

    display_name = 'Node B'
    inp = StringInput()
    out = StringOutput()


class TestExportNodes:
    """Tests for export_nodes."""

    def test_returns_two_dicts(self) -> None:
        result = export_nodes([NodeA, NodeB])
        assert len(result) == 2
        assert isinstance(result[0], dict)
        assert isinstance(result[1], dict)

    def test_node_class_mappings(self) -> None:
        class_mappings, _ = export_nodes([NodeA, NodeB])

        assert 'NodeA' in class_mappings
        assert 'NodeB' in class_mappings
        assert class_mappings['NodeA'] is NodeA
        assert class_mappings['NodeB'] is NodeB

    def test_node_display_name_mappings(self) -> None:
        _, display_mappings = export_nodes([NodeA, NodeB])

        assert 'NodeA' in display_mappings
        assert 'NodeB' in display_mappings
        assert display_mappings['NodeA'] == 'Node A'
        assert display_mappings['NodeB'] == 'Node B'

    def test_empty_list(self) -> None:
        class_mappings, display_mappings = export_nodes([])
        assert class_mappings == {}
        assert display_mappings == {}

    def test_single_node(self) -> None:
        class_mappings, display_mappings = export_nodes([NodeA])
        assert len(class_mappings) == 1
        assert len(display_mappings) == 1
