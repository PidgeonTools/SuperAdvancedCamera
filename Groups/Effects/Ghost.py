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


def create_ghost_group() -> NodeTree:

    # Create the group
    sac_ghost_group: NodeTree = bpy.data.node_groups.new(name=".SAC Ghost", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_ghost_group.nodes.new("NodeGroupInput")
    output_node = sac_ghost_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_ghost_group.inputs.new("NodeSocketColor", "Image")
    sac_ghost_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Glare node set to ghosts
    ghost_node_3 = sac_ghost_group.nodes.new("CompositorNodeGlare")
    ghost_node_3.name = "SAC Effects_Ghosts"
    ghost_node_3.glare_type = "GHOSTS"
    ghost_node_3.quality = "HIGH"
    ghost_node_3.mix = 1
    # Color Mix node named GhostsStrength
    color_mix_node_3 = sac_ghost_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_3.name = "SAC Effects_GhostsStrength"
    color_mix_node_3.blend_type = "ADD"
    color_mix_node_3.inputs[0].default_value = 0

    # Create the links
    # link the input node to the ghost node 3
    sac_ghost_group.links.new(input_node.outputs[0], ghost_node_3.inputs[0])
    # link the input node to the color mix node 3
    sac_ghost_group.links.new(input_node.outputs[0], color_mix_node_3.inputs[1])
    # link the ghost node 3 to the color mix node 3
    sac_ghost_group.links.new(ghost_node_3.outputs[0], color_mix_node_3.inputs[2])
    # link the color mix node 3 to the output node
    sac_ghost_group.links.new(color_mix_node_3.outputs[0], output_node.inputs[0])

    # return
    return sac_ghost_group
