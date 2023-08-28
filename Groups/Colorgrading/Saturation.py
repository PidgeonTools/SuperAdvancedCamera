import bpy
from bpy.types import NodeTree

def create_saturation_group(NodeName, GroupName) -> NodeTree:

    # Create the group
    sac_saturation_group: NodeTree = bpy.data.node_groups.new(name=GroupName,type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_saturation_group.nodes.new("NodeGroupInput")
    output_node = sac_saturation_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_saturation_group.inputs.new("NodeSocketColor","Image")
    sac_saturation_group.outputs.new("NodeSocketColor","Image")

    # Create the nodes
    # Hue/Saturation/Value
    hsv_node = sac_saturation_group.nodes.new("CompositorNodeHueSat")
    hsv_node.name = NodeName

    # Create the links
    # link the input node to the hsv node
    sac_saturation_group.links.new(input_node.outputs[0],hsv_node.inputs[0])
    # link the hsv node to the output node
    sac_saturation_group.links.new(hsv_node.outputs[0],output_node.inputs[0])

    # return
    return(sac_saturation_group)