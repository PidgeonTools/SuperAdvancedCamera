import bpy
from bpy.types import NodeTree


def create_warp_group() -> NodeTree:

    # Create the group
    sac_warp_group: NodeTree = bpy.data.node_groups.new(name=".SAC Warp", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_warp_group.nodes.new("NodeGroupInput")
    output_node = sac_warp_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_warp_group.inputs.new("NodeSocketColor", "Image")
    sac_warp_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Directional blur node
    directional_blur_node = sac_warp_group.nodes.new("CompositorNodeDBlur")
    directional_blur_node.name = "SAC Effects_Warp"

    # Create the links
    # Link the input node to the directional blur node
    sac_warp_group.links.new(input_node.outputs[0], directional_blur_node.inputs[0])
    # Link the directional blur node to the output node
    sac_warp_group.links.new(directional_blur_node.outputs[0], output_node.inputs[0])

    # return
    return sac_warp_group
