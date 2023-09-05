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


def create_perspectiveshift_group() -> NodeTree:

    # Create the group
    sac_perspectiveshift_group: NodeTree = bpy.data.node_groups.new(name=".SAC PerspectiveShift", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_perspectiveshift_group.nodes.new("NodeGroupInput")
    output_node = sac_perspectiveshift_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_perspectiveshift_group.inputs.new("NodeSocketColor", "Image")
    sac_perspectiveshift_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Corner Pin node
    corner_pin_node = sac_perspectiveshift_group.nodes.new("CompositorNodeCornerPin")
    corner_pin_node.name = "SAC Effects_PerspectiveShift_CornerPin"
    # Scale node
    scale_node = sac_perspectiveshift_group.nodes.new("CompositorNodeScale")
    scale_node.name = "SAC Effects_PerspectiveShift_Scale"
    scale_node.space = "RELATIVE"

    # Create the links
    # Link the input node to the corner pin node
    sac_perspectiveshift_group.links.new(input_node.outputs[0], corner_pin_node.inputs[0])
    # Link the corner pin node to the scale node
    sac_perspectiveshift_group.links.new(corner_pin_node.outputs[0], scale_node.inputs[0])
    # Link the scale node to the output node
    sac_perspectiveshift_group.links.new(scale_node.outputs[0], output_node.inputs[0])

    # return
    return sac_perspectiveshift_group
