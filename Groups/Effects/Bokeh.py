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
import os
from bpy.types import NodeTree
from ...SAC_Functions import link_nodes, load_image_once


def create_bokeh_group() -> NodeTree:

    # Create the group
    sac_bokeh_group: NodeTree = bpy.data.node_groups.new(name=".SAC Bokeh", type="CompositorNodeTree")

    input_node = sac_bokeh_group.nodes.new("NodeGroupInput")
    output_node = sac_bokeh_group.nodes.new("NodeGroupOutput")

    sac_bokeh_group.inputs.new("NodeSocketColor", "Image")
    sac_bokeh_group.inputs.new("NodeSocketFloat", "Depth")
    sac_bokeh_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    normalize_node = sac_bokeh_group.nodes.new("CompositorNodeNormalize")

    add_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.inputs[1].default_value = 0
    add_node.name = "SAC Effects_Bokeh_Offset"

    multiply_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    multiply_node.operation = "MULTIPLY"
    multiply_node.inputs[1].default_value = 1
    multiply_node.name = "SAC Effects_Bokeh_Range"

    absolute_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    absolute_node.operation = "ABSOLUTE"

    image_node = sac_bokeh_group.nodes.new("CompositorNodeImage")
    image_node.name = "SAC Effects_Bokeh_Image"

    custom_node = sac_bokeh_group.nodes.new("CompositorNodeImage")
    custom_node.name = "SAC Effects_Bokeh_Custom_Image"

    bokeh_image_node = sac_bokeh_group.nodes.new("CompositorNodeBokehImage")
    bokeh_image_node.name = "SAC Effects_Bokeh_Procedural"

    switch_node = sac_bokeh_group.nodes.new("CompositorNodeSwitch")
    switch_node.name = "SAC Effects_Bokeh_Switch"

    switch_image_node = sac_bokeh_group.nodes.new("CompositorNodeSwitch")
    switch_image_node.name = "SAC Effects_Bokeh_ImageSwitch"

    rotate_node = sac_bokeh_group.nodes.new("CompositorNodeRotate")
    rotate_node.name = "SAC Effects_Bokeh_Rotation"

    bokeh_blur_node = sac_bokeh_group.nodes.new("CompositorNodeBokehBlur")
    bokeh_blur_node.name = "SAC Effects_Bokeh_Blur"
    bokeh_blur_node.use_variable_size = True

    # Create the links
    link_nodes(sac_bokeh_group, input_node, 1, normalize_node, 0)
    link_nodes(sac_bokeh_group, normalize_node, 0, add_node, 0)
    link_nodes(sac_bokeh_group, add_node, 0, multiply_node, 0)
    link_nodes(sac_bokeh_group, multiply_node, 0, absolute_node, 0)
    link_nodes(sac_bokeh_group, absolute_node, 0, bokeh_blur_node, 2)
    link_nodes(sac_bokeh_group, input_node, 0, bokeh_blur_node, 0)
    link_nodes(sac_bokeh_group, image_node, 0, switch_image_node, 0)
    link_nodes(sac_bokeh_group, custom_node, 0, switch_image_node, 1)
    link_nodes(sac_bokeh_group, switch_image_node, 0, rotate_node, 0)
    link_nodes(sac_bokeh_group, rotate_node, 0, switch_node, 0)
    link_nodes(sac_bokeh_group, bokeh_image_node, 0, switch_node, 1)
    link_nodes(sac_bokeh_group, switch_node, 0, bokeh_blur_node, 1)
    link_nodes(sac_bokeh_group, bokeh_blur_node, 0, output_node, 0)

    return sac_bokeh_group
