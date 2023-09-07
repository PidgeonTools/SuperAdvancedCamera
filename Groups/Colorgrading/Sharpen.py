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


def create_sharpen_group() -> NodeTree:

    # Create the group
    sac_sharpen_group: NodeTree = bpy.data.node_groups.new(name=".SAC Sharpen", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_sharpen_group.nodes.new("NodeGroupInput")
    output_node = sac_sharpen_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_sharpen_group.inputs.new("NodeSocketColor", "Image")
    sac_sharpen_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Value
    value_node = sac_sharpen_group.nodes.new("CompositorNodeValue")
    value_node.name = "SAC Colorgrade_Presets_Sharpen"
    value_node.outputs[0].default_value = 0

    # Map Range
    map_range_node = sac_sharpen_group.nodes.new("CompositorNodeMapRange")
    map_range_node.inputs[0].default_value = 0
    map_range_node.inputs[1].default_value = -1
    map_range_node.inputs[2].default_value = 1
    map_range_node.inputs[3].default_value = 0
    map_range_node.inputs[4].default_value = 1

    # Greater Than
    greater_than_node = sac_sharpen_group.nodes.new("CompositorNodeMath")
    greater_than_node.operation = "GREATER_THAN"
    greater_than_node.inputs[1].default_value = 0

    # Two Multiply nodes
    multiply_node_1 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    multiply_node_1.operation = "MULTIPLY"
    multiply_node_1.inputs[1].default_value = 2

    multiply_node_2 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    multiply_node_2.operation = "MULTIPLY"
    multiply_node_2.inputs[1].default_value = 2

    # Two Subtract nodes
    subtract_node_1 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    subtract_node_1.operation = "SUBTRACT"
    subtract_node_1.inputs[0].default_value = 1

    subtract_node_2 = sac_sharpen_group.nodes.new("CompositorNodeMath")
    subtract_node_2.operation = "SUBTRACT"
    subtract_node_2.inputs[1].default_value = 1

    # sharpen node set to soften
    soften_node = sac_sharpen_group.nodes.new("CompositorNodeFilter")
    soften_node.filter_type = "SOFTEN"
    # sharpen node set to diamond sharpen
    sharpen_node = sac_sharpen_group.nodes.new("CompositorNodeFilter")
    sharpen_node.filter_type = "SHARPEN_DIAMOND"

    # Mix node
    mix_node = sac_sharpen_group.nodes.new("CompositorNodeMixRGB")

    # Create the links
    # link the value node to the map range node
    sac_sharpen_group.links.new(value_node.outputs[0], map_range_node.inputs[0])
    # link the value node to the greater than node
    sac_sharpen_group.links.new(value_node.outputs[0], greater_than_node.inputs[0])
    # link the map range node to the multiply node 1
    sac_sharpen_group.links.new(map_range_node.outputs[0], multiply_node_1.inputs[0])
    # link the map range node to the multiply node 2
    sac_sharpen_group.links.new(map_range_node.outputs[0], multiply_node_2.inputs[0])
    # link the multiply node 1 to the subtract node 1
    sac_sharpen_group.links.new(multiply_node_1.outputs[0], subtract_node_1.inputs[1])
    # link the multiply node 2 to the subtract node 2
    sac_sharpen_group.links.new(multiply_node_2.outputs[0], subtract_node_2.inputs[0])
    # link the subtract node 1 to the soften node
    sac_sharpen_group.links.new(subtract_node_1.outputs[0], soften_node.inputs[0])
    # link the subtract node 2 to the sharpen node
    sac_sharpen_group.links.new(subtract_node_2.outputs[0], sharpen_node.inputs[0])
    # link the input node to the soften node
    sac_sharpen_group.links.new(input_node.outputs[0], soften_node.inputs[1])
    # link the input node to the sharpen node
    sac_sharpen_group.links.new(input_node.outputs[0], sharpen_node.inputs[1])
    # link the greater than node to the mix node
    sac_sharpen_group.links.new(greater_than_node.outputs[0], mix_node.inputs[0])
    # link the soften node to the mix node
    sac_sharpen_group.links.new(soften_node.outputs[0], mix_node.inputs[1])
    # link the sharpen node to the mix node
    sac_sharpen_group.links.new(sharpen_node.outputs[0], mix_node.inputs[2])
    # link the mix node to the output node
    sac_sharpen_group.links.new(mix_node.outputs[0], output_node.inputs[0])

    # return
    return sac_sharpen_group
