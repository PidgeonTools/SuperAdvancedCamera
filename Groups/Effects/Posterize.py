import bpy
from bpy.types import NodeTree


def create_posterize_group() -> NodeTree:

    # Create the group
    sac_posterize_group: NodeTree = bpy.data.node_groups.new(name=".SAC Posterize", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_posterize_group.nodes.new("NodeGroupInput")
    output_node = sac_posterize_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_posterize_group.inputs.new("NodeSocketColor", "Image")
    sac_posterize_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # posterize node
    posterize_node = sac_posterize_group.nodes.new("CompositorNodePosterize")
    posterize_node.name = "SAC Effects_Posterize"
    posterize_node.inputs[1].default_value = 128

    # Create the links
    # Link the input node to the posterize node
    sac_posterize_group.links.new(input_node.outputs[0], posterize_node.inputs[0])
    # Link the posterize node to the output node
    sac_posterize_group.links.new(posterize_node.outputs[0], output_node.inputs[0])

    # return
    return sac_posterize_group
