import bpy
from bpy.types import NodeTree


def create_contrast_group() -> NodeTree:

    # Create the group
    sac_contrast_group: NodeTree = bpy.data.node_groups.new(name=".SAC Contrast", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_contrast_group.nodes.new("NodeGroupInput")
    output_node = sac_contrast_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_contrast_group.inputs.new("NodeSocketColor", "Image")
    sac_contrast_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Exposure
    contrast_node = sac_contrast_group.nodes.new("CompositorNodeBrightContrast")
    contrast_node.name = "SAC Colorgrade_Light_Contrast"

    # Create the links
    # link the input node to the contrast node
    sac_contrast_group.links.new(input_node.outputs[0], contrast_node.inputs[0])
    # link the contrast node to the output node
    sac_contrast_group.links.new(contrast_node.outputs[0], output_node.inputs[0])

    # return
    return sac_contrast_group
