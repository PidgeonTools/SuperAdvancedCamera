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


def create_highlights_group() -> NodeTree:

    # Create the group
    sac_highlights_group: NodeTree = bpy.data.node_groups.new(name=".SAC Highlights", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_highlights_group.nodes.new("NodeGroupInput")
    output_node = sac_highlights_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_highlights_group.inputs.new("NodeSocketColor", "Image")
    sac_highlights_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Map Range
    map_range_node = sac_highlights_group.nodes.new("CompositorNodeMapRange")
    map_range_node.name = "SAC Colorgrade_Light_Highlights"
    map_range_node.inputs[0].default_value = 0
    map_range_node.inputs[1].default_value = -1
    map_range_node.inputs[2].default_value = 1
    map_range_node.inputs[3].default_value = 0
    map_range_node.inputs[4].default_value = 1

    # Two math nodes set to multiply by 2
    multiply_node_1 = sac_highlights_group.nodes.new("CompositorNodeMath")
    multiply_node_1.operation = "MULTIPLY"
    multiply_node_1.inputs[1].default_value = 2

    multiply_node_2 = sac_highlights_group.nodes.new("CompositorNodeMath")
    multiply_node_2.operation = "MULTIPLY"
    multiply_node_2.inputs[1].default_value = 2

    # Two math nodes set to subtract 1 and clamp enabled
    subtract_node_1 = sac_highlights_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_1.use_clamp = True
    subtract_node_1.inputs[0].default_value = 1
    subtract_node_2 = sac_highlights_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.use_clamp = True
    subtract_node_2.inputs[1].default_value = 1

    # Two math nodes set to multiply
    multiply_node_3 = sac_highlights_group.nodes.new("CompositorNodeMath")
    multiply_node_3.operation = "MULTIPLY"

    multiply_node_4 = sac_highlights_group.nodes.new("CompositorNodeMath")
    multiply_node_4.operation = "MULTIPLY"

    # Two RGB Curves nodes
    rgb_curves_node_1 = sac_highlights_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_1.mapping.curves[3].points[1].location = (1.0, 0.5)
    rgb_curves_node_2 = sac_highlights_group.nodes.new("CompositorNodeCurveRGB")
    rgb_curves_node_2.mapping.curves[3].points[1].location = (0.5, 1.0)

    # Create the links
    # link the maprange node to the multiply nodes
    sac_highlights_group.links.new(map_range_node.outputs[0], multiply_node_1.inputs[0])
    sac_highlights_group.links.new(map_range_node.outputs[0], multiply_node_2.inputs[0])
    # link the multiply nodes to the subtract nodes
    sac_highlights_group.links.new(multiply_node_1.outputs[0], subtract_node_1.inputs[1])
    sac_highlights_group.links.new(multiply_node_2.outputs[0], subtract_node_2.inputs[0])
    # link the subtract nodes to the multiply nodes
    sac_highlights_group.links.new(subtract_node_1.outputs[0], multiply_node_3.inputs[0])
    sac_highlights_group.links.new(subtract_node_2.outputs[0], multiply_node_4.inputs[0])
    # link the input node to the multiply nodes
    sac_highlights_group.links.new(input_node.outputs[0], multiply_node_3.inputs[1])
    sac_highlights_group.links.new(input_node.outputs[0], multiply_node_4.inputs[1])
    # link the multiply nodes to the rgb curves nodes
    sac_highlights_group.links.new(multiply_node_3.outputs[0], rgb_curves_node_1.inputs[0])
    sac_highlights_group.links.new(multiply_node_4.outputs[0], rgb_curves_node_2.inputs[0])
    # link the input node to the first rgb curves node
    sac_highlights_group.links.new(input_node.outputs[0], rgb_curves_node_1.inputs[1])
    # link the first rgb curves node to the second rgb curves node
    sac_highlights_group.links.new(rgb_curves_node_1.outputs[0], rgb_curves_node_2.inputs[1])
    # link the second rgb curves node to the output node
    sac_highlights_group.links.new(rgb_curves_node_2.outputs[0], output_node.inputs[0])

    # return
    return sac_highlights_group
