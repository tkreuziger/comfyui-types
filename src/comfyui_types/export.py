"""Conveniently export nodes."""

from .node import ComfyUINode


def export_nodes(nodes: list[type]) -> tuple[dict[str, type], dict[str, str]]:
    """Export nodes for ComfyUI to import properly.

    Use like this:
    `NODE_CLASS_MAPPING, NODE_DISPLAY_NAME_MAPPING = export_nodes([
        MyFirstExampleNode,
        MySecondExampleNode,
    ])`
    """
    node_class_mappings = {cls.__name__: cls for cls in nodes}

    node_display_name_mappings = {
        cls.__name__: cls._get_display_name()
        for cls in nodes
        if issubclass(cls, ComfyUINode)
    }

    return node_class_mappings, node_display_name_mappings
