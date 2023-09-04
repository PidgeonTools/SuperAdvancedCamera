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


def create_pixelate_group() -> NodeTree:

    # Create the group
    sac_pixelate_group: NodeTree = bpy.data.node_groups.new(name=".SAC Pixelate", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_pixelate_group.nodes.new("NodeGroupInput")
    output_node = sac_pixelate_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_pixelate_group.inputs.new("NodeSocketColor", "Image")
    sac_pixelate_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # math add node
    math_add_node = sac_pixelate_group.nodes.new("CompositorNodeMath")
    math_add_node.operation = "ADD"
    math_add_node.name = "SAC Effects_Pixelate_Size"
    math_add_node.inputs[1].default_value = 1
    # math divide node
    math_divide_node = sac_pixelate_group.nodes.new("CompositorNodeMath")
    math_divide_node.operation = "DIVIDE"
    math_divide_node.inputs[0].default_value = 1
    # two scale node set to relative
    scale_node_1 = sac_pixelate_group.nodes.new("CompositorNodeScale")
    scale_node_1.space = "RELATIVE"
    scale_node_2 = sac_pixelate_group.nodes.new("CompositorNodeScale")
    scale_node_2.space = "RELATIVE"
    # pixelate node
    pixelate_node = sac_pixelate_group.nodes.new("CompositorNodePixelate")

    # Create the links
    # link the input to the scale node
    sac_pixelate_group.links.new(input_node.outputs[0], scale_node_1.inputs[0])
    # link the divide node to both scale node inputs
    sac_pixelate_group.links.new(math_divide_node.outputs[0], scale_node_1.inputs[1])
    sac_pixelate_group.links.new(math_divide_node.outputs[0], scale_node_1.inputs[2])
    # link the add node to the divide node
    sac_pixelate_group.links.new(math_add_node.outputs[0], math_divide_node.inputs[1])
    # link the scale node to the pixelate node
    sac_pixelate_group.links.new(scale_node_1.outputs[0], pixelate_node.inputs[0])
    # link the pixelate node to the scale node
    sac_pixelate_group.links.new(pixelate_node.outputs[0], scale_node_2.inputs[0])
    # link the add node to the scale node
    sac_pixelate_group.links.new(math_add_node.outputs[0], scale_node_2.inputs[1])
    sac_pixelate_group.links.new(math_add_node.outputs[0], scale_node_2.inputs[2])
    # link the scale node to the output
    sac_pixelate_group.links.new(scale_node_2.outputs[0], output_node.inputs[0])

    # return
    return sac_pixelate_group
