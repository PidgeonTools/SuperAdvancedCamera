import bpy
from bpy.types import NodeTree


def create_shadowtint_group() -> NodeTree:

    # Create the group
    sac_shadowtint_group: NodeTree = bpy.data.node_groups.new(name=".SAC ShadowTint", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_shadowtint_group.nodes.new("NodeGroupInput")
    output_node = sac_shadowtint_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_shadowtint_group.inputs.new("NodeSocketColor", "Image")
    sac_shadowtint_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Subtract node
    subtract_node = sac_shadowtint_group.nodes.new("CompositorNodeMath")
    subtract_node.operation = "SUBTRACT"
    subtract_node.inputs[0].default_value = 1
    subtract_node.use_clamp = True

    # MixRGB Color node
    mixrgb_node = sac_shadowtint_group.nodes.new("CompositorNodeMixRGB")
    mixrgb_node.blend_type = "COLOR"
    mixrgb_node.name = "SAC Colorgrade_Presets_ShadowTint"

    # Create the links
    # link the input node to the subtract node
    sac_shadowtint_group.links.new(input_node.outputs[0], subtract_node.inputs[1])
    # link the input node to the mixrgb node
    sac_shadowtint_group.links.new(input_node.outputs[0], mixrgb_node.inputs[1])
    # link the subtract node to the mixrgb node
    sac_shadowtint_group.links.new(subtract_node.outputs[0], mixrgb_node.inputs[0])
    # link the mixrgb node to the output node
    sac_shadowtint_group.links.new(mixrgb_node.outputs[0], output_node.inputs[0])

    # return
    return sac_shadowtint_group
