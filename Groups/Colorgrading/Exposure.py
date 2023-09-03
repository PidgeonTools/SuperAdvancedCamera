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


def create_exposure_group() -> NodeTree:

    # Create the group
    sac_exposure_group: NodeTree = bpy.data.node_groups.new(name=".SAC Exposure", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_exposure_group.nodes.new("NodeGroupInput")
    output_node = sac_exposure_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_exposure_group.inputs.new("NodeSocketColor", "Image")
    sac_exposure_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Exposure
    exposure_node = sac_exposure_group.nodes.new("CompositorNodeExposure")
    exposure_node.name = "SAC Colorgrade_Light_Exposure"

    # Create the links
    # link the input node to the exposure node
    sac_exposure_group.links.new(input_node.outputs[0], exposure_node.inputs[0])
    # link the exposure node to the output node
    sac_exposure_group.links.new(exposure_node.outputs[0], output_node.inputs[0])

    # return
    return sac_exposure_group
