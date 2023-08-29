import bpy
from bpy.types import NodeTree


def create_colorwheel_group() -> NodeTree:

    # Create the group
    sac_colorwheel_group: NodeTree = bpy.data.node_groups.new(name=".SAC Colorwheel", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_colorwheel_group.nodes.new("NodeGroupInput")
    output_node = sac_colorwheel_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_colorwheel_group.inputs.new("NodeSocketColor", "Image")
    sac_colorwheel_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Color Balance node 1
    color_balance_node_1 = sac_colorwheel_group.nodes.new("CompositorNodeColorBalance")
    color_balance_node_1.name = "SAC Colorgrade_Colorwheel_Shadows"
    # gamma node 1
    gamma_node_1 = sac_colorwheel_group.nodes.new("CompositorNodeGamma")
    # map range node 1
    map_range_node_1 = sac_colorwheel_group.nodes.new("CompositorNodeMapRange")
    map_range_node_1.inputs[0].default_value = 1
    map_range_node_1.inputs[1].default_value = -2
    map_range_node_1.inputs[2].default_value = 2
    map_range_node_1.inputs[3].default_value = 4
    map_range_node_1.inputs[4].default_value = 0.001
    map_range_node_1.name = "SAC Colorgrade_Colorwheel_Shadows_Brightness"

    # Color Balance node 2
    color_balance_node_2 = sac_colorwheel_group.nodes.new("CompositorNodeColorBalance")
    color_balance_node_2.name = "SAC Colorgrade_Colorwheel_Midtones"
    # gamma node 2
    gamma_node_2 = sac_colorwheel_group.nodes.new("CompositorNodeGamma")
    # map range node 2
    map_range_node_2 = sac_colorwheel_group.nodes.new("CompositorNodeMapRange")
    map_range_node_2.inputs[0].default_value = 1
    map_range_node_2.inputs[1].default_value = -2
    map_range_node_2.inputs[2].default_value = 2
    map_range_node_2.inputs[3].default_value = 4
    map_range_node_2.inputs[4].default_value = 0.001
    map_range_node_2.name = "SAC Colorgrade_Colorwheel_Midtones_Brightness"

    # Color Balance node 3
    color_balance_node_3 = sac_colorwheel_group.nodes.new("CompositorNodeColorBalance")
    color_balance_node_3.name = "SAC Colorgrade_Colorwheel_Highlights"
    # exposure node
    exposure_node = sac_colorwheel_group.nodes.new("CompositorNodeExposure")
    # map range node 3
    map_range_node_3 = sac_colorwheel_group.nodes.new("CompositorNodeMapRange")
    map_range_node_3.inputs[0].default_value = 1
    map_range_node_3.inputs[1].default_value = 0
    map_range_node_3.inputs[2].default_value = 2
    map_range_node_3.inputs[3].default_value = -10
    map_range_node_3.inputs[4].default_value = 10
    map_range_node_3.name = "SAC Colorgrade_Colorwheel_Highlights_Brightness"

    # Create the links
    # link the input node to the color balance node 1
    sac_colorwheel_group.links.new(input_node.outputs[0], color_balance_node_1.inputs[1])
    # link the color balance node 1 to the gamma node 1
    sac_colorwheel_group.links.new(color_balance_node_1.outputs[0], gamma_node_1.inputs[0])
    # link the map range node 1 to the gamma node 1
    sac_colorwheel_group.links.new(map_range_node_1.outputs[0], gamma_node_1.inputs[1])
    # link the gamma node 1 to the color balance node 2
    sac_colorwheel_group.links.new(gamma_node_1.outputs[0], color_balance_node_2.inputs[1])
    # link the color balance node 2 to the gamma node 2
    sac_colorwheel_group.links.new(color_balance_node_2.outputs[0], gamma_node_2.inputs[0])
    # link the map range node 2 to the gamma node 2
    sac_colorwheel_group.links.new(map_range_node_2.outputs[0], gamma_node_2.inputs[1])
    # link the gamma node 2 to the color balance node 3
    sac_colorwheel_group.links.new(gamma_node_2.outputs[0], color_balance_node_3.inputs[1])
    # link the color balance node 3 to the exposure node
    sac_colorwheel_group.links.new(color_balance_node_3.outputs[0], exposure_node.inputs[0])
    # link the map range node 3 to the exposure node
    sac_colorwheel_group.links.new(map_range_node_3.outputs[0], exposure_node.inputs[1])
    # link the exposure node to the output node
    sac_colorwheel_group.links.new(exposure_node.outputs[0], output_node.inputs[0])

    # return
    return sac_colorwheel_group
