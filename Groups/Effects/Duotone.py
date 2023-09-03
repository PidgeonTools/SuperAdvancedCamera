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


def create_duotone_group() -> NodeTree:

    # Create the group
    sac_duotone_group: NodeTree = bpy.data.node_groups.new(name=".SAC Duotone", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_duotone_group.nodes.new("NodeGroupInput")
    output_node = sac_duotone_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_duotone_group.inputs.new("NodeSocketColor", "Image")
    sac_duotone_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Mix node 1
    mix_node_1 = sac_duotone_group.nodes.new("CompositorNodeMixRGB")
    mix_node_1.name = "SAC Effects_Duotone_Colors"
    mix_node_1.inputs[1].default_value = (0.01, 0.01, 0.17, 1)
    mix_node_1.inputs[2].default_value = (1, 0.56, 0.06, 1)

    # Mix node 2
    mix_node_2 = sac_duotone_group.nodes.new("CompositorNodeMixRGB")
    mix_node_2.name = "SAC Effects_Duotone_Blend"
    mix_node_2.inputs[0].default_value = 0

    # Create the links
    # link the input node to the mix node 1
    sac_duotone_group.links.new(input_node.outputs[0], mix_node_1.inputs[0])
    # link the mix node 1 to the mix node 2
    sac_duotone_group.links.new(mix_node_1.outputs[0], mix_node_2.inputs[2])
    # link the input node to the mix node 2
    sac_duotone_group.links.new(input_node.outputs[0], mix_node_2.inputs[1])
    # link the mix node 2 to the output node
    sac_duotone_group.links.new(mix_node_2.outputs[0], output_node.inputs[0])

    # return
    return sac_duotone_group
