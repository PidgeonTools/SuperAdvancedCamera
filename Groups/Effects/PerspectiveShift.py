import bpy
from bpy.types import NodeTree


def create_perspectiveshift_group() -> NodeTree:

    # Create the group
    sac_perspectiveshift_group: NodeTree = bpy.data.node_groups.new(name=".SAC PerspectiveShift", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_perspectiveshift_group.nodes.new("NodeGroupInput")
    output_node = sac_perspectiveshift_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_perspectiveshift_group.inputs.new("NodeSocketColor", "Image")
    sac_perspectiveshift_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Corner Pin node
    corner_pin_node = sac_perspectiveshift_group.nodes.new("CompositorNodeCornerPin")
    corner_pin_node.name = "SAC Effects_PerspectiveShift_CornerPin"
    # Scale node
    scale_node = sac_perspectiveshift_group.nodes.new("CompositorNodeScale")
    scale_node.name = "SAC Effects_PerspectiveShift_Scale"
    scale_node.space = "RELATIVE"

    # Create the links
    # Link the input node to the corner pin node
    sac_perspectiveshift_group.links.new(input_node.outputs[0], corner_pin_node.inputs[0])
    # Link the corner pin node to the scale node
    sac_perspectiveshift_group.links.new(corner_pin_node.outputs[0], scale_node.inputs[0])
    # Link the scale node to the output node
    sac_perspectiveshift_group.links.new(scale_node.outputs[0], output_node.inputs[0])

    # return
    return sac_perspectiveshift_group
