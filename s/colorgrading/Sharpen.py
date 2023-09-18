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
from ...SAC_Functions import link_nodes


def create_sharpen_group() -> NodeTree:

    # Create the group
    sac_sharpen_group: NodeTree = bpy.data.node_groups.new(name=".SAC Sharpen", type="CompositorNodeTree")

    input_node = sac_sharpen_group.nodes.new("NodeGroupInput")
    output_node = sac_sharpen_group.nodes.new("NodeGroupOutput")

    sac_sharpen_group.inputs.new("NodeSocketColor", "Image")
    sac_sharpen_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    value_node = sac_sharpen_group.nodes.new("CompositorNodeValue")
    value_node.name = "SAC Colorgrade_Presets_Sharpen"
    value_node.outputs[0].default_value = 0

    map_range_node = sac_sharpen_group.nodes.new("CompositorNodeMapRange")
    map_range_node.inputs[0].default_value = 0
    map_range_node.inputs[1].default_value = -1
    map_range_node.inputs[2].default_value = 1
    map_range_node.inputs[3].default_value = 0
    map_range_node.inputs[4].default_value = 1

    greater_than_node = sac_sharpen_group.nodes.new("CompositorNodeMath")
    greater_than_node.operation = "GREATER_THAN"
    greater_than_node.inputs[1].default_value = 0

    multiply_node_1 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    multiply_node_1.operation = "MULTIPLY"
    multiply_node_1.inputs[1].default_value = 2

    multiply_node_2 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    multiply_node_2.operation = "MULTIPLY"
    multiply_node_2.inputs[1].default_value = 2

    subtract_node_1 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_1.inputs[0].default_value = 1

    subtract_node_2 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.inputs[1].default_value = 1

    soften_node = sac_sharpen_group.nodes.new("CompositorNodeFilter")
    soften_node.filter_type = "SOFTEN"

    sharpen_node = sac_sharpen_group.nodes.new("CompositorNodeFilter")
    sharpen_node.filter_type = "SHARPEN_DIAMOND"

    mix_node = sac_sharpen_group.nodes.new("CompositorNodeMixRGB")

    # Create the links
    link_nodes(sac_sharpen_group, value_node, 0, map_range_node, 0)
    link_nodes(sac_sharpen_group, value_node, 0, greater_than_node, 0)
    link_nodes(sac_sharpen_group, map_range_node, 0, multiply_node_1, 0)
    link_nodes(sac_sharpen_group, map_range_node, 0, multiply_node_2, 0)
    link_nodes(sac_sharpen_group, multiply_node_1, 0, subtract_node_1, 1)
    link_nodes(sac_sharpen_group, multiply_node_2, 0, subtract_node_2, 0)
    link_nodes(sac_sharpen_group, subtract_node_1, 0, soften_node, 0)
    link_nodes(sac_sharpen_group, subtract_node_2, 0, sharpen_node, 0)
    link_nodes(sac_sharpen_group, input_node, 0, soften_node, 1)
    link_nodes(sac_sharpen_group, input_node, 0, sharpen_node, 1)
    link_nodes(sac_sharpen_group, greater_than_node, 0, mix_node, 0)
    link_nodes(sac_sharpen_group, soften_node, 0, mix_node, 1)
    link_nodes(sac_sharpen_group, sharpen_node, 0, mix_node, 2)
    link_nodes(sac_sharpen_group, mix_node, 0, output_node, 0)

    return sac_sharpen_group
