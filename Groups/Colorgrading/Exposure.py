import bpy
from bpy.types import NodeTree


def create_exposure_group() -> NodeTree:

    # Create the group
    sac_exposure_group: NodeTree = bpy.data.node_groups.new(name=".SAC Exposure", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_exposure_group.nodes.new("NodeGroupInput")
    output_node = sac_exposure_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_exposure_group.inputs.new("NodeSocketColor", "Image")
    sac_exposure_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Exposure
    exposure_node = sac_exposure_group.nodes.new("CompositorNodeExposure")
    exposure_node.name = "SAC Colorgrade_Light_Exposure"

    # Create the links
    # link the input node to the exposure node
    sac_exposure_group.links.new(input_node.outputs[0], exposure_node.inputs[0])
    # link the exposure node to the output node
    sac_exposure_group.links.new(exposure_node.outputs[0], output_node.inputs[0])

    # return
    return sac_exposure_group
