import bpy
from bpy.types import NodeTree


def create_negative_group() -> NodeTree:

    # Create the group
    sac_negative_group: NodeTree = bpy.data.node_groups.new(name=".SAC Negative", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_negative_group.nodes.new("NodeGroupInput")
    output_node = sac_negative_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_negative_group.inputs.new("NodeSocketColor", "Image")
    sac_negative_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # invert node
    negative_node = sac_negative_group.nodes.new("CompositorNodeInvert")
    negative_node.inputs[0].default_value = 0
    negative_node.name = "SAC Effects_Negative"

    # Create the links
    # Link the input node to the filter node
    sac_negative_group.links.new(input_node.outputs[0], negative_node.inputs[1])
    # Link the filter node to the output node
    sac_negative_group.links.new(negative_node.outputs[0], output_node.inputs[0])

    # return
    return sac_negative_group
