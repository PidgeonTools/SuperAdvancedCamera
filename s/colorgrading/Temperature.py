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


def create_temperature_group() -> NodeTree:

    # Create the group
    sac_temperature_group: NodeTree = bpy.data.node_groups.new(name=".SAC Temperature", type="CompositorNodeTree")

    input_node = sac_temperature_group.nodes.new("NodeGroupInput")
    output_node = sac_temperature_group.nodes.new("NodeGroupOutput")

    sac_temperature_group.inputs.new("NodeSocketColor", "Image")
    sac_temperature_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    map_range_node = sac_temperature_group.nodes.new("CompositorNodeMapRange")
    map_range_node.name = "SAC Colorgrade_Color_Temperature"
    map_range_node.inputs[0].default_value = 0
    map_range_node.inputs[1].default_value = -1
    map_range_node.inputs[2].default_value = 1
    map_range_node.inputs[3].default_value = 0
    map_range_node.inputs[4].default_value = 1

    multiply_node_1 = sac_temperature_group.nodes.new("CompositorNodeMath")
    multiply_node_1.operation = "MULTIPLY"
    multiply_node_1.inputs[1].default_value = 2

    multiply_node_2 = sac_temperature_group.nodes.new("CompositorNodeMath")
    multiply_node_2.operation = "MULTIPLY"
    multiply_node_2.inputs[1].default_value = 2

    subtract_node_1 = sac_temperature_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_1.use_clamp = True
    subtract_node_1.inputs[0].default_value = 1
    subtract_node_2 = sac_temperature_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.use_clamp = True
    subtract_node_2.inputs[1].default_value = 1

    rgb_curves_node_1 = sac_temperature_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_1.mapping.curves[0].points[1].location = (1.0, 0.5)
    rgb_curves_node_1.mapping.curves[2].points[1].location = (0.5, 1.0)
    rgb_curves_node_2 = sac_temperature_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_2.mapping.curves[0].points[1].location = (0.5, 1.0)
    rgb_curves_node_2.mapping.curves[2].points[1].location = (1.0, 0.5)

    # Create the links
    link_nodes(sac_temperature_group, map_range_node, 0, multiply_node_1, 0)
    link_nodes(sac_temperature_group, map_range_node, 0, multiply_node_2, 0)
    link_nodes(sac_temperature_group, multiply_node_1, 0, subtract_node_1, 1)
    link_nodes(sac_temperature_group, multiply_node_2, 0, subtract_node_2, 0)
    link_nodes(sac_temperature_group, subtract_node_1, 0, rgb_curves_node_1, 0)
    link_nodes(sac_temperature_group, subtract_node_2, 0, rgb_curves_node_2, 0)
    link_nodes(sac_temperature_group, input_node, 0, rgb_curves_node_1, 1)
    link_nodes(sac_temperature_group, rgb_curves_node_1, 0, rgb_curves_node_2, 1)
    link_nodes(sac_temperature_group, rgb_curves_node_2, 0, output_node, 0)

    return sac_temperature_group
