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


def create_infrared_group() -> NodeTree:

    # Create the group
    sac_infrared_group: NodeTree = bpy.data.node_groups.new(name=".SAC Infrared", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_infrared_group.nodes.new("NodeGroupInput")
    output_node = sac_infrared_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_infrared_group.inputs.new("NodeSocketColor", "Image")
    sac_infrared_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Math add node with second value 0
    add_node = sac_infrared_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.inputs[1].default_value = 0
    add_node.name = "SAC Effects_Infrared_Add"
    # Color ramp node with 5 colors and 5 positions
    color_ramp_node = sac_infrared_group.nodes.new("CompositorNodeValToRGB")
    color_ramp_node.color_ramp.elements[0].color = (1, 0.122138, 0.715693, 1)
    color_ramp_node.color_ramp.elements[0].position = 0.05
    color_ramp_node.color_ramp.elements[1].color = (0.048172, 0.05286, 0.434154, 1)
    color_ramp_node.color_ramp.elements[1].position = 0.25
    color_ramp_node.color_ramp.elements.new(0.4)
    color_ramp_node.color_ramp.elements[2].color = (0, 1, 0.921582, 1)
    color_ramp_node.color_ramp.elements.new(0.55)
    color_ramp_node.color_ramp.elements[3].color = (0, 0.62396, 0.052861, 1)
    color_ramp_node.color_ramp.elements.new(0.75)
    color_ramp_node.color_ramp.elements[4].color = (1, 0.973445, 0, 1)
    color_ramp_node.color_ramp.elements.new(0.85)
    color_ramp_node.color_ramp.elements[5].color = (1, 0, 0, 1)
    color_ramp_node.color_ramp.elements.new(1)
    color_ramp_node.color_ramp.elements[6].color = (1, 1, 1, 1)
    # Color mix node
    color_mix_node = sac_infrared_group.nodes.new("CompositorNodeMixRGB")
    color_mix_node.blend_type = "MIX"
    color_mix_node.inputs[0].default_value = 0
    color_mix_node.name = "SAC Effects_Infrared_Mix"

    # Create the links
    # connect input node to add node
    sac_infrared_group.links.new(input_node.outputs[0], add_node.inputs[0])
    # connect add node to color ramp node
    sac_infrared_group.links.new(add_node.outputs[0], color_ramp_node.inputs[0])
    # connect color ramp node to color mix node
    sac_infrared_group.links.new(color_ramp_node.outputs[0], color_mix_node.inputs[2])
    # connect input node to color mix node
    sac_infrared_group.links.new(input_node.outputs[0], color_mix_node.inputs[1])
    # connect color mix node to output node
    sac_infrared_group.links.new(color_mix_node.outputs[0], output_node.inputs[0])

    # return
    return sac_infrared_group
