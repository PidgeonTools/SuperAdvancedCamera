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


def create_overlay_group() -> NodeTree:

    # Create the group
    sac_overlay_group: NodeTree = bpy.data.node_groups.new(name=".SAC Overlay", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_overlay_group.nodes.new("NodeGroupInput")
    output_node = sac_overlay_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_overlay_group.inputs.new("NodeSocketColor", "Image")
    sac_overlay_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # mix node set to overlay
    mix_node = sac_overlay_group.nodes.new("CompositorNodeMixRGB")
    mix_node.blend_type = "OVERLAY"
    mix_node.name = "SAC Effects_Overlay"
    mix_node.inputs[0].default_value = 0
    # Texture node
    texture_node = sac_overlay_group.nodes.new("CompositorNodeImage")
    texture_node.name = "SAC Effects_Overlay_Texture"

    # Create the links
    # Link the input to the mix node
    sac_overlay_group.links.new(input_node.outputs[0], mix_node.inputs[1])
    # Link the texture to the mix node
    sac_overlay_group.links.new(texture_node.outputs[0], mix_node.inputs[2])
    # Link the mix node to the output
    sac_overlay_group.links.new(mix_node.outputs[0], output_node.inputs[0])

    # return
    return sac_overlay_group
