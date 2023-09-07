# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <one line to give the program's name and a brief idea of what it does.>
#    Copyright (C) <2023>  <Kevin Lorengel>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#  Alternatively, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import NodeTree


def create_halftone_group() -> NodeTree:

    # Create the group
    sac_halftone_group: NodeTree = bpy.data.node_groups.new(name=".SAC Halftone", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_halftone_group.nodes.new("NodeGroupInput")
    output_node = sac_halftone_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_halftone_group.inputs.new("NodeSocketColor", "Image")
    sac_halftone_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # value node
    value_node = sac_halftone_group.nodes.new("CompositorNodeValue")
    value_node.name = "SAC Effects_Halftone_SizeSave"
    # separate rgb node
    separate_rgb_node = sac_halftone_group.nodes.new("CompositorNodeSeparateColor")
    # rgb to bw node
    rgb_to_bw_node = sac_halftone_group.nodes.new("CompositorNodeRGBToBW")
    # switch node
    switch_node = sac_halftone_group.nodes.new("CompositorNodeSwitch")
    switch_node.name = "SAC Effects_Halftone_Switch"
    # texture node with the ".SAC Dot Screen" texture
    texture_node = sac_halftone_group.nodes.new("CompositorNodeTexture")
    texture = bpy.data.textures.get(".SAC Dot Screen")
    texture_node.texture = texture
    texture_node.inputs[1].default_value[0] = 96.0
    texture_node.inputs[1].default_value[1] = 54.0
    texture_node.name = "SAC Effects_Halftone_Texture"
    # halftone part
    halftone_part = halftonepart_group()
    # halftone part group node named C
    halftone_part_group_node_c = sac_halftone_group.nodes.new("CompositorNodeGroup")
    halftone_part_group_node_c.node_tree = halftone_part
    # halftone part group node named R
    halftone_part_group_node_r = sac_halftone_group.nodes.new("CompositorNodeGroup")
    halftone_part_group_node_r.node_tree = halftone_part
    # halftone part group node named G
    halftone_part_group_node_g = sac_halftone_group.nodes.new("CompositorNodeGroup")
    halftone_part_group_node_g.node_tree = halftone_part
    # halftone part group node named B
    halftone_part_group_node_b = sac_halftone_group.nodes.new("CompositorNodeGroup")
    halftone_part_group_node_b.node_tree = halftone_part
    # combine rgb node
    combine_rgb_node = sac_halftone_group.nodes.new("CompositorNodeCombineColor")
    # value node
    value_node = sac_halftone_group.nodes.new("CompositorNodeValue")
    value_node.name = "SAC Effects_Halftone_Value"
    value_node.outputs[0].default_value = -0.2
    # value node
    delta_node = sac_halftone_group.nodes.new("CompositorNodeValue")
    delta_node.name = "SAC Effects_Halftone_Delta"
    delta_node.outputs[0].default_value = 0.2

    # Create the links
    # link input node to separate rgb node
    sac_halftone_group.links.new(input_node.outputs[0], separate_rgb_node.inputs[0])
    # link input node to rgb to bw node
    sac_halftone_group.links.new(input_node.outputs[0], rgb_to_bw_node.inputs[0])
    # link the rgb to bw node to the half tone part group node named C
    sac_halftone_group.links.new(rgb_to_bw_node.outputs[0], halftone_part_group_node_c.inputs["Image Input"])
    # link the separate rgb node to the half tone part group node named R
    sac_halftone_group.links.new(separate_rgb_node.outputs[0], halftone_part_group_node_r.inputs["Image Input"])
    # link the separate rgb node to the half tone part group node named G
    sac_halftone_group.links.new(separate_rgb_node.outputs[1], halftone_part_group_node_g.inputs["Image Input"])
    # link the separate rgb node to the half tone part group node named B
    sac_halftone_group.links.new(separate_rgb_node.outputs[2], halftone_part_group_node_b.inputs["Image Input"])
    # link the texture node to every halftone part nodes "Dots" input
    sac_halftone_group.links.new(texture_node.outputs[0], halftone_part_group_node_c.inputs["Dots"])
    sac_halftone_group.links.new(texture_node.outputs[0], halftone_part_group_node_r.inputs["Dots"])
    sac_halftone_group.links.new(texture_node.outputs[0], halftone_part_group_node_g.inputs["Dots"])
    sac_halftone_group.links.new(texture_node.outputs[0], halftone_part_group_node_b.inputs["Dots"])
    # link the value node to every halftone part nodes "Value" input
    sac_halftone_group.links.new(value_node.outputs[0], halftone_part_group_node_c.inputs["Value"])
    sac_halftone_group.links.new(value_node.outputs[0], halftone_part_group_node_r.inputs["Value"])
    sac_halftone_group.links.new(value_node.outputs[0], halftone_part_group_node_g.inputs["Value"])
    sac_halftone_group.links.new(value_node.outputs[0], halftone_part_group_node_b.inputs["Value"])
    # link the delta node to every halftone part nodes "Delta" input
    sac_halftone_group.links.new(delta_node.outputs[0], halftone_part_group_node_c.inputs["Delta"])
    sac_halftone_group.links.new(delta_node.outputs[0], halftone_part_group_node_r.inputs["Delta"])
    sac_halftone_group.links.new(delta_node.outputs[0], halftone_part_group_node_g.inputs["Delta"])
    sac_halftone_group.links.new(delta_node.outputs[0], halftone_part_group_node_b.inputs["Delta"])
    # link the halftone part group node named R, G and B to the combine rgb node
    sac_halftone_group.links.new(halftone_part_group_node_r.outputs["Image"], combine_rgb_node.inputs[0])
    sac_halftone_group.links.new(halftone_part_group_node_g.outputs["Image"], combine_rgb_node.inputs[1])
    sac_halftone_group.links.new(halftone_part_group_node_b.outputs["Image"], combine_rgb_node.inputs[2])
    # link the separate rgb node alpha to the combine rgb node alpha
    sac_halftone_group.links.new(separate_rgb_node.outputs[3], combine_rgb_node.inputs[3])
    # link the halftone part group node named C to the switch node
    sac_halftone_group.links.new(halftone_part_group_node_c.outputs["Image"], switch_node.inputs[0])
    # link the combine rgb node to the switch node
    sac_halftone_group.links.new(combine_rgb_node.outputs[0], switch_node.inputs[1])
    # link the switch node to the output node
    sac_halftone_group.links.new(switch_node.outputs[0], output_node.inputs[0])

    # return
    return sac_halftone_group


def halftonepart_group() -> NodeTree:

    # Create the group
    halftone_part_group: NodeTree = bpy.data.node_groups.new(name=".SAC Halftone part", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = halftone_part_group.nodes.new("NodeGroupInput")
    output_node = halftone_part_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    halftone_part_group.inputs.new("NodeSocketFloat", "Image Input")
    halftone_part_group.inputs.new("NodeSocketFloat", "Dots")
    halftone_part_group.inputs.new("NodeSocketFloat", "Value")
    halftone_part_group.inputs.new("NodeSocketFloat", "Delta")
    halftone_part_group.outputs.new("NodeSocketFloat", "Image")

    # Create the nodes
    # color ramp node, first dial position 0.085
    color_ramp_node_1 = halftone_part_group.nodes.new("CompositorNodeValToRGB")
    color_ramp_node_1.color_ramp.elements[0].position = 0.085
    # math multiply node
    math_multiply_node = halftone_part_group.nodes.new("CompositorNodeMath")
    math_multiply_node.operation = "MULTIPLY"
    # math add node 1 of 4
    math_add_node_1 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_add_node_1.operation = "ADD"
    # math add node 2 of 4
    math_add_node_2 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_add_node_2.operation = "ADD"
    # math add node 3 of 4
    math_add_node_3 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_add_node_3.operation = "ADD"
    # math add node 4 of 4
    math_add_node_4 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_add_node_4.operation = "ADD"
    # math greater than node 1 of 5, threshold 0
    math_greater_than_node_1 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_greater_than_node_1.operation = "GREATER_THAN"
    math_greater_than_node_1.inputs[1].default_value = 0
    # math greater than node 2 of 5
    math_greater_than_node_2 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_greater_than_node_2.operation = "GREATER_THAN"
    # math greater than node 3 of 5
    math_greater_than_node_3 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_greater_than_node_3.operation = "GREATER_THAN"
    # math greater than node 4 of 5
    math_greater_than_node_4 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_greater_than_node_4.operation = "GREATER_THAN"
    # math greater than node 5 of 5
    math_greater_than_node_5 = halftone_part_group.nodes.new("CompositorNodeMath")
    math_greater_than_node_5.operation = "GREATER_THAN"
    # color mix node 1 of 5, first value black
    color_mix_node_1 = halftone_part_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_1.blend_type = "MIX"
    color_mix_node_1.inputs[1].default_value = (0, 0, 0, 1)
    # color mix node 2 of 5
    color_mix_node_2 = halftone_part_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_2.blend_type = "MIX"
    # color mix node 3 of 5
    color_mix_node_3 = halftone_part_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_3.blend_type = "MIX"
    # color mix node 4 of 5
    color_mix_node_4 = halftone_part_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_4.blend_type = "MIX"
    # color mix node 5 of 5, second value white
    color_mix_node_5 = halftone_part_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_5.blend_type = "MIX"
    color_mix_node_5.inputs[2].default_value = (1, 1, 1, 1)
    # Dialate Erode node 1 of 4
    dialate_erode_node_1 = halftone_part_group.nodes.new("CompositorNodeDilateErode")
    dialate_erode_node_1.mode = "DISTANCE"
    dialate_erode_node_1.distance = -2
    # Dialate Erode node 2 of 4
    dialate_erode_node_2 = halftone_part_group.nodes.new("CompositorNodeDilateErode")
    dialate_erode_node_2.mode = "DISTANCE"
    dialate_erode_node_2.distance = -1
    # Dialate Erode node 4 of 4
    dialate_erode_node_4 = halftone_part_group.nodes.new("CompositorNodeDilateErode")
    dialate_erode_node_4.mode = "DISTANCE"
    dialate_erode_node_4.distance = 1
    # Filter soften node
    filter_soften_node = halftone_part_group.nodes.new("CompositorNodeFilter")
    filter_soften_node.filter_type = "SOFTEN"
    # greater than node
    greater_than_node = halftone_part_group.nodes.new("CompositorNodeMath")
    greater_than_node.operation = "GREATER_THAN"
    greater_than_node.inputs[1].default_value = 0.018

    # Create the links
    # link input node "Image Input" into color ramp
    halftone_part_group.links.new(input_node.outputs["Image Input"], color_ramp_node_1.inputs[0])
    # link color ramp into math multiply
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_multiply_node.inputs[0])
    # link input node "Dots" to math multiply
    halftone_part_group.links.new(input_node.outputs["Dots"], math_multiply_node.inputs[1])
    # link input "Value" to first math add node
    halftone_part_group.links.new(input_node.outputs["Value"], math_add_node_1.inputs[0])
    # link input "Delta" to every math add nodes second value
    halftone_part_group.links.new(input_node.outputs["Delta"], math_add_node_1.inputs[1])
    halftone_part_group.links.new(input_node.outputs["Delta"], math_add_node_2.inputs[1])
    halftone_part_group.links.new(input_node.outputs["Delta"], math_add_node_3.inputs[1])
    halftone_part_group.links.new(input_node.outputs["Delta"], math_add_node_4.inputs[1])
    # link math add node 1 to 2
    halftone_part_group.links.new(math_add_node_1.outputs[0], math_add_node_2.inputs[0])
    # link math add node 2 to 3
    halftone_part_group.links.new(math_add_node_2.outputs[0], math_add_node_3.inputs[0])
    # link math add node 3 to 4
    halftone_part_group.links.new(math_add_node_3.outputs[0], math_add_node_4.inputs[0])
    # link math add node 1 to greater than node 2 threshold
    halftone_part_group.links.new(math_add_node_1.outputs[0], math_greater_than_node_2.inputs[1])
    # link math add node 2 to greater than node 3 threshold
    halftone_part_group.links.new(math_add_node_3.outputs[0], math_greater_than_node_3.inputs[1])
    # link math add node 3 to greater than node 4 threshold
    halftone_part_group.links.new(math_add_node_4.outputs[0], math_greater_than_node_4.inputs[1])
    # link math add node 4 to greater than node 5 threshold
    halftone_part_group.links.new(math_add_node_4.outputs[0], math_greater_than_node_5.inputs[1])
    # link color ramp to every greater than node
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_greater_than_node_1.inputs[0])
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_greater_than_node_2.inputs[0])
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_greater_than_node_3.inputs[0])
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_greater_than_node_4.inputs[0])
    halftone_part_group.links.new(color_ramp_node_1.outputs[0], math_greater_than_node_5.inputs[0])
    # link greater than node 1 to color mix node 1
    halftone_part_group.links.new(math_greater_than_node_1.outputs[0], color_mix_node_1.inputs[0])
    # link greater than node 2 to color mix node 2
    halftone_part_group.links.new(math_greater_than_node_2.outputs[0], color_mix_node_2.inputs[0])
    # link greater than node 3 to color mix node 3
    halftone_part_group.links.new(math_greater_than_node_3.outputs[0], color_mix_node_3.inputs[0])
    # link greater than node 4 to color mix node 4
    halftone_part_group.links.new(math_greater_than_node_4.outputs[0], color_mix_node_4.inputs[0])
    # link greater than node 5 to color mix node 5
    halftone_part_group.links.new(math_greater_than_node_5.outputs[0], color_mix_node_5.inputs[0])
    # link math multiply node to every dialate erode node
    halftone_part_group.links.new(math_multiply_node.outputs[0], dialate_erode_node_1.inputs[0])
    halftone_part_group.links.new(math_multiply_node.outputs[0], dialate_erode_node_2.inputs[0])
    halftone_part_group.links.new(math_multiply_node.outputs[0], dialate_erode_node_4.inputs[0])
    # link dialate erode node 1 to color mix node 1
    halftone_part_group.links.new(dialate_erode_node_1.outputs[0], color_mix_node_1.inputs[2])
    # link dialate erode node 2 to color mix node 2
    halftone_part_group.links.new(dialate_erode_node_2.outputs[0], color_mix_node_2.inputs[2])
    # link dialate erode node 3 to color mix node 3
    halftone_part_group.links.new(math_multiply_node.outputs[0], color_mix_node_3.inputs[2])
    # link dialate erode node 4 to color mix node 4
    halftone_part_group.links.new(dialate_erode_node_4.outputs[0], color_mix_node_4.inputs[2])
    # link color mix 1 to color mix 2
    halftone_part_group.links.new(color_mix_node_1.outputs[0], color_mix_node_2.inputs[1])
    # link color mix 2 to color mix 3
    halftone_part_group.links.new(color_mix_node_2.outputs[0], color_mix_node_3.inputs[1])
    # link color mix 3 to color mix 4
    halftone_part_group.links.new(color_mix_node_3.outputs[0], color_mix_node_4.inputs[1])
    # link color mix 4 to color mix 5
    halftone_part_group.links.new(color_mix_node_4.outputs[0], color_mix_node_5.inputs[1])
    # link color mix 5 to filter soften
    halftone_part_group.links.new(color_mix_node_5.outputs[0], filter_soften_node.inputs[1])
    # link filter soften to greater than
    halftone_part_group.links.new(filter_soften_node.outputs[0], greater_than_node.inputs[0])
    # link greater than to output node
    halftone_part_group.links.new(greater_than_node.outputs[0], output_node.inputs[0])

    # return
    return halftone_part_group
