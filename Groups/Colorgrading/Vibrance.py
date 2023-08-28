import bpy
from bpy.types import NodeTree

def create_vibrance_group() -> NodeTree:

    # Create the group
    sac_vibrance_group: NodeTree = bpy.data.node_groups.new(name=".SAC Vibrance",type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_vibrance_group.nodes.new("NodeGroupInput")
    output_node = sac_vibrance_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_vibrance_group.inputs.new("NodeSocketColor","Image")
    sac_vibrance_group.outputs.new("NodeSocketColor","Image")

    # Create the nodes
    # Separate RGB
    separate_rgb_node = sac_vibrance_group.nodes.new("CompositorNodeSeparateColor")
    # Two Maximum nodes
    maximum_node_1 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    maximum_node_1.operation = "MAXIMUM"
    maximum_node_2 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    maximum_node_2.operation = "MAXIMUM"
    # Two Minimum nodes
    minimum_node_1 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    minimum_node_1.operation = "MINIMUM"
    minimum_node_2 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    minimum_node_2.operation = "MINIMUM"
    # Two Subtract nodes
    subtract_node_1 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_2 = sac_vibrance_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.inputs[0].default_value = 1
    # Divide node
    divide_node = sac_vibrance_group.nodes.new("CompositorNodeMath")
    divide_node.operation = "DIVIDE"
    # Hue Saturation Value node
    hsv_node = sac_vibrance_group.nodes.new("CompositorNodeHueSat")
    hsv_node.name = "SAC Colorgrade_Presets_Vibrance"

    # Create the links
    # link the input node to the separate RGB node
    sac_vibrance_group.links.new(input_node.outputs[0], separate_rgb_node.inputs[0])
    # link the separate RGB node to the maximum nodes
    sac_vibrance_group.links.new(separate_rgb_node.outputs[0], maximum_node_1.inputs[0])
    sac_vibrance_group.links.new(separate_rgb_node.outputs[1], maximum_node_1.inputs[1])
    sac_vibrance_group.links.new(maximum_node_1.outputs[0], maximum_node_2.inputs[0])
    sac_vibrance_group.links.new(separate_rgb_node.outputs[2], maximum_node_2.inputs[1])
    # link the separate RGB node to the minimum nodes
    sac_vibrance_group.links.new(separate_rgb_node.outputs[0], minimum_node_1.inputs[0])
    sac_vibrance_group.links.new(separate_rgb_node.outputs[1], minimum_node_1.inputs[1])
    sac_vibrance_group.links.new(minimum_node_1.outputs[0], minimum_node_2.inputs[0])
    sac_vibrance_group.links.new(separate_rgb_node.outputs[2], minimum_node_2.inputs[1])
    # link the maximum nodes to the subtract nodes
    sac_vibrance_group.links.new(maximum_node_2.outputs[0], subtract_node_1.inputs[0])
    # link the minimum nodes to the subtract nodes
    sac_vibrance_group.links.new(minimum_node_2.outputs[0], subtract_node_1.inputs[1])
    # link the maximum nodes to the divide node
    sac_vibrance_group.links.new(maximum_node_2.outputs[0], divide_node.inputs[1])
    # link the subtract nodes to the divide node
    sac_vibrance_group.links.new(subtract_node_1.outputs[0], divide_node.inputs[0])
    # link the divide node to the subtract nodes
    sac_vibrance_group.links.new(divide_node.outputs[0], subtract_node_2.inputs[1])
    # link the subtract nodes to the HSV node
    sac_vibrance_group.links.new(subtract_node_2.outputs[0], hsv_node.inputs[4])
    # link the input node to the HSV node
    sac_vibrance_group.links.new(input_node.outputs[0], hsv_node.inputs[0])
    # link the HSV node to the output node
    sac_vibrance_group.links.new(hsv_node.outputs[0], output_node.inputs[0])

    # return
    return(sac_vibrance_group)