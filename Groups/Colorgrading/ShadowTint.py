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


def create_shadowtint_group() -> NodeTree:

    # Create the group
    sac_shadowtint_group: NodeTree = bpy.data.node_groups.new(name=".SAC ShadowTint", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_shadowtint_group.nodes.new("NodeGroupInput")
    output_node = sac_shadowtint_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_shadowtint_group.inputs.new("NodeSocketColor", "Image")
    sac_shadowtint_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Subtract node
    subtract_node = sac_shadowtint_group.nodes.new("CompositorNodeMath")
    subtract_node.operation = "SUBTRACT"
    subtract_node.inputs[0].default_value = 1
    subtract_node.use_clamp = True

    # MixRGB Color node
    mixrgb_node = sac_shadowtint_group.nodes.new("CompositorNodeMixRGB")
    mixrgb_node.blend_type = "COLOR"
    mixrgb_node.name = "SAC Colorgrade_Presets_ShadowTint"

    # Create the links
    # link the input node to the subtract node
    sac_shadowtint_group.links.new(input_node.outputs[0], subtract_node.inputs[1])
    # link the input node to the mixrgb node
    sac_shadowtint_group.links.new(input_node.outputs[0], mixrgb_node.inputs[1])
    # link the subtract node to the mixrgb node
    sac_shadowtint_group.links.new(subtract_node.outputs[0], mixrgb_node.inputs[0])
    # link the mixrgb node to the output node
    sac_shadowtint_group.links.new(mixrgb_node.outputs[0], output_node.inputs[0])

    # return
    return sac_shadowtint_group
