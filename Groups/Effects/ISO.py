# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <Adds plenty of new features to Blenders camera and compositor>
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


def create_iso_group() -> NodeTree:

    # Create the group
    sac_iso_group: NodeTree = bpy.data.node_groups.new(name=".SAC ISO", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_iso_group.nodes.new("NodeGroupInput")
    output_node = sac_iso_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_iso_group.inputs.new("NodeSocketColor", "Image")
    sac_iso_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # math add node clamped, second value 1
    add_node = sac_iso_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.use_clamp = True
    add_node.inputs[1].default_value = 1
    # Lens Distortion node, jitter enabled, distortion 0.0001
    lens_distortion_node = sac_iso_group.nodes.new("CompositorNodeLensdist")
    lens_distortion_node.use_jitter = True
    lens_distortion_node.inputs[1].default_value = 0.000001
    # color subtract node, clamped
    color_subtract_node = sac_iso_group.nodes.new("CompositorNodeMixRGB")
    color_subtract_node.blend_type = "SUBTRACT"
    color_subtract_node.use_clamp = True
    # math less than node, threshold 0.03
    math_less_than_node = sac_iso_group.nodes.new("CompositorNodeMath")
    math_less_than_node.operation = "LESS_THAN"
    math_less_than_node.inputs[1].default_value = 0.03
    # color mix node, second color #007C00
    color_mix_node = sac_iso_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node.blend_type = "MIX"
    color_mix_node.inputs[2].default_value = (0, 0.2, 0, 1)
    # Despecle node, threshold 0, neighbor 0
    despeckle_node = sac_iso_group.nodes.new("CompositorNodeDespeckle")
    despeckle_node.threshold = 0
    despeckle_node.threshold_neighbor = 0
    despeckle_node.name = "SAC Effects_ISO_Despeckle"
    # color add node
    color_add_node = sac_iso_group.nodes.new("CompositorNodeMixRGB")
    color_add_node.blend_type = "ADD"
    color_add_node.name = "SAC Effects_ISO_Add"
    color_add_node.inputs[0].default_value = 0

    # Create the links
    # input node to add node
    sac_iso_group.links.new(input_node.outputs[0], add_node.inputs[0])
    # add node to lens distortion node
    sac_iso_group.links.new(add_node.outputs[0], lens_distortion_node.inputs[0])
    # lens distortion node to color subtract node
    sac_iso_group.links.new(lens_distortion_node.outputs[0], color_subtract_node.inputs[1])
    # color subtract node to math less than node
    sac_iso_group.links.new(color_subtract_node.outputs[0], math_less_than_node.inputs[0])
    # math less than node to color mix node
    sac_iso_group.links.new(math_less_than_node.outputs[0], color_mix_node.inputs[0])
    # subtract to mix node
    sac_iso_group.links.new(color_subtract_node.outputs[0], color_mix_node.inputs[1])
    # mix node to despeckle node
    sac_iso_group.links.new(color_mix_node.outputs[0], despeckle_node.inputs[1])
    # despeckle node to color add node
    sac_iso_group.links.new(despeckle_node.outputs[0], color_add_node.inputs[2])
    # input node to add node
    sac_iso_group.links.new(input_node.outputs[0], color_add_node.inputs[1])
    # color add node to output node
    sac_iso_group.links.new(color_add_node.outputs[0], output_node.inputs[0])

    # return
    return sac_iso_group
