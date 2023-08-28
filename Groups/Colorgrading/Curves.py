import bpy
from bpy.types import NodeTree

def create_curves_group() -> NodeTree:

    # Create the group
    sac_curves_group: NodeTree = bpy.data.node_groups.new(name=".SAC Curves",type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_curves_group.nodes.new("NodeGroupInput")
    output_node = sac_curves_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_curves_group.inputs.new("NodeSocketColor","Image")
    sac_curves_group.outputs.new("NodeSocketColor","Image")

    # Create the nodes
    # RGB Curves node
    rgb_curves_node = sac_curves_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node.name = "SAC Colorgrade_Curves_RGB"

    # HSV Curves node
    hsv_curves_node = sac_curves_group.nodes.new("CompositorNodeHueCorrect")
    hsv_curves_node.name = "SAC Colorgrade_Curves_HSV"

    # Create the links
    # link the input node to the rgb curves node
    sac_curves_group.links.new(input_node.outputs[0],rgb_curves_node.inputs[1])
    # link the rgb curves node to the hsv curves node
    sac_curves_group.links.new(rgb_curves_node.outputs[0],hsv_curves_node.inputs[1])
    # link the hsv curves node to the output node
    sac_curves_group.links.new(hsv_curves_node.outputs[0],output_node.inputs[0])

    # return
    return(sac_curves_group)