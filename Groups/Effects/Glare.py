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


def create_glare_group() -> NodeTree:

    # Create the group
    sac_glare_group: NodeTree = bpy.data.node_groups.new(name=".SAC Glare", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_glare_group.nodes.new("NodeGroupInput")
    output_node = sac_glare_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_glare_group.inputs.new("NodeSocketColor", "Image")
    sac_glare_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Glare node set to fog glow
    glare_node_1 = sac_glare_group.nodes.new("CompositorNodeGlare")
    glare_node_1.name = "SAC Effects_FogGlow"
    glare_node_1.glare_type = "FOG_GLOW"
    glare_node_1.quality = "HIGH"
    glare_node_1.mix = 1
    glare_node_1.size = 7
    # Glare node set to streaks
    glare_node_2 = sac_glare_group.nodes.new("CompositorNodeGlare")
    glare_node_2.name = "SAC Effects_Streaks"
    glare_node_2.glare_type = "STREAKS"
    glare_node_2.quality = "HIGH"
    glare_node_2.mix = 1
    glare_node_2.streaks = 6
    glare_node_2.angle_offset = 0.1963495  # 11.25 degrees
    glare_node_2.fade = 0.85
    # Glare node set to ghosts
    glare_node_3 = sac_glare_group.nodes.new("CompositorNodeGlare")
    glare_node_3.name = "SAC Effects_Ghosts"
    glare_node_3.glare_type = "GHOSTS"
    glare_node_3.quality = "HIGH"
    glare_node_3.mix = 1
    # Color Mix node named FogGlowStrength
    color_mix_node_1 = sac_glare_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_1.name = "SAC Effects_FogGlowStrength"
    color_mix_node_1.blend_type = "ADD"
    color_mix_node_1.inputs[0].default_value = 0
    color_mix_node_1.mute = True
    # Color Mix node named StreaksStrength
    color_mix_node_2 = sac_glare_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_2.name = "SAC Effects_StreaksStrength"
    color_mix_node_2.blend_type = "ADD"
    color_mix_node_2.inputs[0].default_value = 0
    color_mix_node_2.mute = True
    # Color Mix node named GhostsStrength
    color_mix_node_3 = sac_glare_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node_3.name = "SAC Effects_GhostsStrength"
    color_mix_node_3.blend_type = "ADD"
    color_mix_node_3.inputs[0].default_value = 0
    color_mix_node_3.mute = True

    # Create the links
    # link the input node to the glare node 1
    sac_glare_group.links.new(input_node.outputs[0], glare_node_1.inputs[0])
    # link the input node to the glare node 2
    sac_glare_group.links.new(input_node.outputs[0], glare_node_2.inputs[0])
    # link the input node to the glare node 3
    sac_glare_group.links.new(input_node.outputs[0], glare_node_3.inputs[0])
    # link the input node to the color mix node 1
    sac_glare_group.links.new(input_node.outputs[0], color_mix_node_1.inputs[1])
    # link the glare node 1 to the color mix node 1
    sac_glare_group.links.new(glare_node_1.outputs[0], color_mix_node_1.inputs[2])
    # link the color mix node 1 to the color mix node 2
    sac_glare_group.links.new(color_mix_node_1.outputs[0], color_mix_node_2.inputs[1])
    # link the glare node 2 to the color mix node 2
    sac_glare_group.links.new(glare_node_2.outputs[0], color_mix_node_2.inputs[2])
    # link the color mix node 2 to the color mix node 3
    sac_glare_group.links.new(color_mix_node_2.outputs[0], color_mix_node_3.inputs[1])
    # link the glare node 3 to the color mix node 3
    sac_glare_group.links.new(glare_node_3.outputs[0], color_mix_node_3.inputs[2])
    # link the color mix node 3 to the output node
    sac_glare_group.links.new(color_mix_node_3.outputs[0], output_node.inputs[0])

    # return
    return sac_glare_group
