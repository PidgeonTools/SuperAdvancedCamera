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
from ...SAC_Functions import link_nodes


def create_contrast_group() -> NodeTree:

    # Create the group
    sac_contrast_group: NodeTree = bpy.data.node_groups.new(name=".SAC Contrast", type="CompositorNodeTree")

    input_node = sac_contrast_group.nodes.new("NodeGroupInput")
    output_node = sac_contrast_group.nodes.new("NodeGroupOutput")

    sac_contrast_group.inputs.new("NodeSocketColor", "Image")
    sac_contrast_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    contrast_node = sac_contrast_group.nodes.new("CompositorNodeBrightContrast")
    contrast_node.name = "SAC Colorgrade_Light_Contrast"

    # Create the links
    link_nodes(sac_contrast_group, input_node, 0, contrast_node, 0)
    link_nodes(sac_contrast_group, contrast_node, 0, output_node, 0)

    return sac_contrast_group
