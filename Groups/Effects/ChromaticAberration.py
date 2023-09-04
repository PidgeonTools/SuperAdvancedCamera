import bpy
from bpy.types import NodeTree


def create_chromatic_group() -> NodeTree:

    # Create the group
    sac_chromatic_group: NodeTree = bpy.data.node_groups.new(name=".SAC ChromaticAberration", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_chromatic_group.nodes.new("NodeGroupInput")
    output_node = sac_chromatic_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_chromatic_group.inputs.new("NodeSocketColor", "Image")
    sac_chromatic_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Lens Distortion node
    chromatic_node = sac_chromatic_group.nodes.new("CompositorNodeLensdist")
    chromatic_node.use_fit = True
    chromatic_node.name = "SAC Effects_ChromaticAberration"

    # Create the links
    # Link the input node to the chromatic node
    sac_chromatic_group.links.new(input_node.outputs[0], chromatic_node.inputs[0])
    # Link the chromatic node to the output node
    sac_chromatic_group.links.new(chromatic_node.outputs[0], output_node.inputs[0])

    # return
    return sac_chromatic_group
