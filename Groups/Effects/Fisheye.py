import bpy
from bpy.types import NodeTree


def create_fisheye_group() -> NodeTree:

    # Create the group
    sac_fisheye_group: NodeTree = bpy.data.node_groups.new(name=".SAC Fisheye", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_fisheye_group.nodes.new("NodeGroupInput")
    output_node = sac_fisheye_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_fisheye_group.inputs.new("NodeSocketColor", "Image")
    sac_fisheye_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Lens distortion node
    lens_distortion_node = sac_fisheye_group.nodes.new("CompositorNodeLensdist")
    lens_distortion_node.name = "SAC Effects_Fisheye"
    lens_distortion_node.use_fit = True

    # Create the links
    # Link the input node to the lens distortion node
    sac_fisheye_group.links.new(input_node.outputs[0], lens_distortion_node.inputs[0])
    # Link the lens distortion node to the output node
    sac_fisheye_group.links.new(lens_distortion_node.outputs[0], output_node.inputs[0])

    # return
    return sac_fisheye_group
