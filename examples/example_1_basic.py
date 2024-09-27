"""Examples of typed ComfyUI nodes."""

import comfyui_types as ct


class ExampleNode(ct.ComfyUINode):
    """An example node."""

    category = 'My category'
    display_name = 'My example node'

    # Inputs
    my_text = ct.StringInput(default='stuff', multiline=True)
    my_other_text = ct.StringInput(required=False, default='morestuff')
    my_number = ct.IntegerInput(default=42, min=0, max=100)

    # Outputs
    my_output = ct.StringOutput()

    def execute(self, my_text: str, my_other_text: str, my_number: int) -> str:
        """The function that will be executed, when this node is run."""
        return f'{my_text} {my_other_text} {my_number}'


# Export custom nodes.
NODE_CLASS_MAPPING, NODE_DISPLAY_NAME_MAPPING = ct.export_nodes([
    ExampleNode,
])

