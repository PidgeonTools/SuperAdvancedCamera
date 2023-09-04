import bpy
from bpy.types import NodeTree


def create_overlay_group() -> NodeTree:

    # Create the group
    sac_overlay_group: NodeTree = bpy.data.node_groups.new(name=".SAC Overlay", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_overlay_group.nodes.new("NodeGroupInput")
    output_node = sac_overlay_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_overlay_group.inputs.new("NodeSocketColor", "Image")
    sac_overlay_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # mix node set to overlay
    mix_node = sac_overlay_group.nodes.new("CompositorNodeMixRGB")
    mix_node.blend_type = "OVERLAY"
    mix_node.name = "SAC Effects_Overlay"
    # Texture node
    texture_node = sac_overlay_group.nodes.new("CompositorNodeImage")
    texture_node.name = "SAC Effects_Overlay_Texture"

    # Create the links
    # Link the input to the mix node
    sac_overlay_group.links.new(input_node.outputs[0], mix_node.inputs[1])
    # Link the texture to the mix node
    sac_overlay_group.links.new(texture_node.outputs[0], mix_node.inputs[2])
    # Link the mix node to the output
    sac_overlay_group.links.new(mix_node.outputs[0], output_node.inputs[0])

    # return
    return sac_overlay_group
