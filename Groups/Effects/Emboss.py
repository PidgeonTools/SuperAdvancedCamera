import bpy
from bpy.types import NodeTree


def create_emboss_group() -> NodeTree:

    # Create the group
    sac_emboss_group: NodeTree = bpy.data.node_groups.new(name=".SAC Emboss", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_emboss_group.nodes.new("NodeGroupInput")
    output_node = sac_emboss_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_emboss_group.inputs.new("NodeSocketColor", "Image")
    sac_emboss_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # filter node set to shadow
    emboss_node = sac_emboss_group.nodes.new("CompositorNodeFilter")
    emboss_node.filter_type = "SHADOW"
    emboss_node.name = "SAC Effects_Emboss"

    # Create the links
    # Link the input node to the filter node
    sac_emboss_group.links.new(input_node.outputs[0], emboss_node.inputs[1])
    # Link the filter node to the output node
    sac_emboss_group.links.new(emboss_node.outputs[0], output_node.inputs[0])

    # return
    return sac_emboss_group
