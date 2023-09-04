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


def create_viginette_group() -> NodeTree:

    # Create the group
    sac_viginette_group: NodeTree = bpy.data.node_groups.new(name=".SAC Viginette", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_viginette_group.nodes.new("NodeGroupInput")
    output_node = sac_viginette_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_viginette_group.inputs.new("NodeSocketColor", "Image")
    sac_viginette_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Map Range node for roundness
    roundness_map_range_node = sac_viginette_group.nodes.new("CompositorNodeMapRange")
    roundness_map_range_node.name = "SAC Effects_Viginette_Roundness"
    roundness_map_range_node.inputs[0].default_value = 0
    roundness_map_range_node.inputs[1].default_value = -1
    roundness_map_range_node.inputs[2].default_value = 1
    roundness_map_range_node.inputs[3].default_value = 0
    roundness_map_range_node.inputs[4].default_value = 1
    # Map Range node for intensity
    intensity_map_range_node = sac_viginette_group.nodes.new("CompositorNodeMapRange")
    intensity_map_range_node.name = "SAC Effects_Viginette_Intensity"
    intensity_map_range_node.inputs[0].default_value = 0
    intensity_map_range_node.inputs[1].default_value = -1
    intensity_map_range_node.inputs[2].default_value = 1
    intensity_map_range_node.inputs[3].default_value = 0
    intensity_map_range_node.inputs[4].default_value = 1
    # Map Range node for Midpoint
    midpoint_map_range_node = sac_viginette_group.nodes.new("CompositorNodeMapRange")
    midpoint_map_range_node.name = "SAC Effects_Viginette_Midpoint"
    midpoint_map_range_node.inputs[0].default_value = 0
    midpoint_map_range_node.inputs[1].default_value = -0.999
    midpoint_map_range_node.inputs[2].default_value = 1
    midpoint_map_range_node.inputs[3].default_value = 0
    midpoint_map_range_node.inputs[4].default_value = 2
    # Math node set to add to balance out midpoint
    midpoint_add_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    midpoint_add_node.operation = "ADD"
    midpoint_add_node.inputs[1].default_value = (0.25/4)
    midpoint_add_node.name = "SAC Effects_Viginette_Midpoint_Add"
    # Math node set to add to whiten the image
    whiten_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    whiten_node.operation = "ADD"
    whiten_node.inputs[1].default_value = 1
    whiten_node.use_clamp = True
    # Lense Distortion node to warp the white image
    lense_distortion_node = sac_viginette_group.nodes.new("CompositorNodeLensdist")
    # scale node to scale the image relative
    scale_node = sac_viginette_group.nodes.new("CompositorNodeScale")
    scale_node.space = "RELATIVE"
    # Math node set to multiply
    multiply_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    multiply_node.operation = "MULTIPLY"
    # Math node set to pingpong
    pingpong_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    pingpong_node.operation = "PINGPONG"
    pingpong_node.inputs[1].default_value = 0.5
    # Math node set to multiply
    multiply_node2 = sac_viginette_group.nodes.new("CompositorNodeMath")
    multiply_node2.operation = "MULTIPLY"
    multiply_node2.inputs[1].default_value = 2
    multiply_node2.use_clamp = True
    # Math node set to greater than
    greater_than_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    greater_than_node.operation = "GREATER_THAN"
    greater_than_node.inputs[1].default_value = 0.5
    greater_than_node.use_clamp = True
    # Math node set to add
    add_node = sac_viginette_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.use_clamp = True
    # Directional blur node
    directional_blur_node = sac_viginette_group.nodes.new("CompositorNodeDBlur")
    directional_blur_node.iterations = 6
    directional_blur_node.zoom = 0.25
    directional_blur_node.name = "SAC Effects_Viginette_Directional_Blur"
    # Color Mix node to mix the greater than and the image
    color_mix_node = sac_viginette_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node.blend_type = "MIX"

    # Create the links
    # link the input node to the whiten node
    sac_viginette_group.links.new(input_node.outputs[0], whiten_node.inputs[0])
    # link the whiten node to the lense distortion node
    sac_viginette_group.links.new(whiten_node.outputs[0], lense_distortion_node.inputs[0])
    # link the roundness map range node to the lense distortion node
    sac_viginette_group.links.new(roundness_map_range_node.outputs[0], lense_distortion_node.inputs[1])
    # link the lense distortion node to the scale node
    sac_viginette_group.links.new(lense_distortion_node.outputs[0], scale_node.inputs[0])
    # link the midpoint map range node to the midpoint add node
    sac_viginette_group.links.new(midpoint_map_range_node.outputs[0], midpoint_add_node.inputs[0])
    # link the midpoint add node to the scale node
    sac_viginette_group.links.new(midpoint_add_node.outputs[0], scale_node.inputs[1])
    sac_viginette_group.links.new(midpoint_add_node.outputs[0], scale_node.inputs[2])
    # link the scale node to the multiply node
    sac_viginette_group.links.new(scale_node.outputs[0], multiply_node.inputs[1])
    # link the whiten node to the multiply node
    sac_viginette_group.links.new(whiten_node.outputs[0], multiply_node.inputs[0])
    # link the multiply node to the directional blur node
    sac_viginette_group.links.new(multiply_node.outputs[0], directional_blur_node.inputs[0])
    # link the intensity map range node to the pingpong node
    sac_viginette_group.links.new(intensity_map_range_node.outputs[0], pingpong_node.inputs[0])
    # link the pingpong node to the multiply node
    sac_viginette_group.links.new(pingpong_node.outputs[0], multiply_node2.inputs[0])
    # link the multiply node to the add node
    sac_viginette_group.links.new(multiply_node2.outputs[0], add_node.inputs[0])
    # link the directional blur node to the add node
    sac_viginette_group.links.new(directional_blur_node.outputs[0], add_node.inputs[1])
    # link the add node to the color mix node
    sac_viginette_group.links.new(add_node.outputs[0], color_mix_node.inputs[0])
    # link the intensity map range node to the greater than node
    sac_viginette_group.links.new(intensity_map_range_node.outputs[0], greater_than_node.inputs[0])
    # link the greater than node to the color mix node
    sac_viginette_group.links.new(greater_than_node.outputs[0], color_mix_node.inputs[1])
    # link the import node to the color mix node
    sac_viginette_group.links.new(input_node.outputs[0], color_mix_node.inputs[2])
    # link the color mix node to the output node
    sac_viginette_group.links.new(color_mix_node.outputs[0], output_node.inputs[0])

    # return
    return sac_viginette_group
