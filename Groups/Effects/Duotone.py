import bpy
from bpy.types import NodeTree


def create_duotone_group() -> NodeTree:

    # Create the group
    sac_duotone_group: NodeTree = bpy.data.node_groups.new(name=".SAC Duotone", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_duotone_group.nodes.new("NodeGroupInput")
    output_node = sac_duotone_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_duotone_group.inputs.new("NodeSocketColor", "Image")
    sac_duotone_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Mix node 1
    mix_node_1 = sac_duotone_group.nodes.new("CompositorNodeMixRGB")
    mix_node_1.name = "SAC Effects_Duotone_Colors"
    # Mix node 2
    mix_node_2 = sac_duotone_group.nodes.new("CompositorNodeMixRGB")
    mix_node_2.name = "SAC Effects_Duotone_Blend"
    mix_node_2.inputs[0].default_value = 0

    # Create the links
    # link the input node to the mix node 1
    sac_duotone_group.links.new(input_node.outputs[0], mix_node_1.inputs[0])
    # link the mix node 1 to the mix node 2
    sac_duotone_group.links.new(mix_node_1.outputs[0], mix_node_2.inputs[2])
    # link the input node to the mix node 2
    sac_duotone_group.links.new(input_node.outputs[0], mix_node_2.inputs[1])
    # link the mix node 2 to the output node
    sac_duotone_group.links.new(mix_node_2.outputs[0], output_node.inputs[0])

    # return
    return sac_duotone_group
