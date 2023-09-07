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


def create_negative_group() -> NodeTree:

    # Create the group
    sac_negative_group: NodeTree = bpy.data.node_groups.new(name=".SAC Negative", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_negative_group.nodes.new("NodeGroupInput")
    output_node = sac_negative_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_negative_group.inputs.new("NodeSocketColor", "Image")
    sac_negative_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # invert node
    negative_node = sac_negative_group.nodes.new("CompositorNodeInvert")
    negative_node.inputs[0].default_value = 0
    negative_node.name = "SAC Effects_Negative"

    # Create the links
    # Link the input node to the filter node
    sac_negative_group.links.new(input_node.outputs[0], negative_node.inputs[1])
    # Link the filter node to the output node
    sac_negative_group.links.new(negative_node.outputs[0], output_node.inputs[0])

    # return
    return sac_negative_group
