import bpy
from bpy.types import NodeTree


def create_whites_group() -> NodeTree:

    # Create the group
    sac_whites_group: NodeTree = bpy.data.node_groups.new(name=".SAC Whites", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_whites_group.nodes.new("NodeGroupInput")
    output_node = sac_whites_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_whites_group.inputs.new("NodeSocketColor", "Image")
    sac_whites_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Map Range
    map_range_node = sac_whites_group.nodes.new("CompositorNodeMapRange")
    map_range_node.name = "SAC Colorgrade_Light_Whites"
    map_range_node.inputs[0].default_value = 0
    map_range_node.inputs[1].default_value = -1
    map_range_node.inputs[2].default_value = 1
    map_range_node.inputs[3].default_value = 0
    map_range_node.inputs[4].default_value = 1

    # Two math nodes set to multiply by 2
    multiply_node_1 = sac_whites_group.nodes.new("CompositorNodeMath")
    multiply_node_1.operation = "MULTIPLY"
    multiply_node_1.inputs[1].default_value = 2

    multiply_node_2 = sac_whites_group.nodes.new("CompositorNodeMath")
    multiply_node_2.operation = "MULTIPLY"
    multiply_node_2.inputs[1].default_value = 2

    # Two math nodes set to subtract 1 and clamp enabled
    subtract_node_1 = sac_whites_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_1.use_clamp = True
    subtract_node_1.inputs[0].default_value = 1
    subtract_node_2 = sac_whites_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.use_clamp = True
    subtract_node_2.inputs[1].default_value = 1

    # Two RGB Curves nodes
    rgb_curves_node_1 = sac_whites_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_1.mapping.curves[3].points[1].location = (1.0, 0.25)
    rgb_curves_node_2 = sac_whites_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_2.mapping.curves[3].points[1].location = (0.25, 1.0)

    # Create the links
    # link the maprange node to the multiply nodes
    sac_whites_group.links.new(map_range_node.outputs[0], multiply_node_1.inputs[0])
    sac_whites_group.links.new(map_range_node.outputs[0], multiply_node_2.inputs[0])
    # link the multiply nodes to the subtract nodes
    sac_whites_group.links.new(multiply_node_1.outputs[0], subtract_node_1.inputs[1])
    sac_whites_group.links.new(multiply_node_2.outputs[0], subtract_node_2.inputs[0])
    # link the subtract nodes to the rgb curves nodes
    sac_whites_group.links.new(subtract_node_1.outputs[0], rgb_curves_node_1.inputs[0])
    sac_whites_group.links.new(subtract_node_2.outputs[0], rgb_curves_node_2.inputs[0])
    # link the input node to the first rgb curves node
    sac_whites_group.links.new(input_node.outputs[0], rgb_curves_node_1.inputs[1])
    # link the first rgb curves node to the second rgb curves node
    sac_whites_group.links.new(rgb_curves_node_1.outputs[0], rgb_curves_node_2.inputs[1])
    # link the second rgb curves node to the output node
    sac_whites_group.links.new(rgb_curves_node_2.outputs[0], output_node.inputs[0])

    # return
    return sac_whites_group