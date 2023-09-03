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


def create_highlighttint_group() -> NodeTree:

    # Create the group
    sac_highlighttint_group: NodeTree = bpy.data.node_groups.new(name=".SAC HighlightTint", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_highlighttint_group.nodes.new("NodeGroupInput")
    output_node = sac_highlighttint_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_highlighttint_group.inputs.new("NodeSocketColor", "Image")
    sac_highlighttint_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Math Add node
    add_node = sac_highlighttint_group.nodes.new("CompositorNodeMath")
    add_node.inputs[1].default_value = 0
    add_node.use_clamp = True

    # MixRGB Color node
    mixrgb_node = sac_highlighttint_group.nodes.new("CompositorNodeMixRGB")
    mixrgb_node.blend_type = "COLOR"
    mixrgb_node.name = "SAC Colorgrade_Presets_HighlightTint"

    # Create the links
    # link the input node to the add node
    sac_highlighttint_group.links.new(input_node.outputs[0], add_node.inputs[0])
    # link the input node to the mixrgb node
    sac_highlighttint_group.links.new(input_node.outputs[0], mixrgb_node.inputs[1])
    # link the add node to the mixrgb node
    sac_highlighttint_group.links.new(add_node.outputs[0], mixrgb_node.inputs[0])
    # link the mixrgb node to the output node
    sac_highlighttint_group.links.new(mixrgb_node.outputs[0], output_node.inputs[0])

    # return
    return sac_highlighttint_group
