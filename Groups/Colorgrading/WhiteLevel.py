import bpy
from bpy.types import NodeTree


def create_whitelevel_group() -> NodeTree:

    # Create the group
    sac_whitelevel_group: NodeTree = bpy.data.node_groups.new(name=".SAC WhiteLevel", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_whitelevel_group.nodes.new("NodeGroupInput")
    output_node = sac_whitelevel_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_whitelevel_group.inputs.new("NodeSocketColor", "Image")
    sac_whitelevel_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # rgb curves node
    rgb_curves_node = sac_whitelevel_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node.name = "SAC Colorgrade_Color_WhiteLevel"

    # Create the links
    # link the input node to the rgb curves node
    sac_whitelevel_group.links.new(input_node.outputs[0], rgb_curves_node.inputs[1])
    # link the rgb curves node to the output node
    sac_whitelevel_group.links.new(rgb_curves_node.outputs[0], output_node.inputs[0])

    # return
    return sac_whitelevel_group
