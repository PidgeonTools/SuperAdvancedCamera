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
from ...filters.filter import get_filter


def create_max_group() -> NodeTree:

    # Create the group
    sac_max_group: NodeTree = bpy.data.node_groups.new(name=".SAC Three Max", type="CompositorNodeTree")

    input_node = sac_max_group.nodes.new("NodeGroupInput")
    output_node = sac_max_group.nodes.new("NodeGroupOutput")

    sac_max_group.inputs.new("NodeSocketFloat", "A")
    sac_max_group.inputs.new("NodeSocketFloat", "B")
    sac_max_group.inputs.new("NodeSocketFloat", "C")
    sac_max_group.outputs.new("NodeSocketFloat", "Value")

    # Create the nodes
    math_max_1 = sac_max_group.nodes.new("CompositorNodeMath")
    math_max_1.operation = "MAXIMUM"

    math_max_2 = sac_max_group.nodes.new("CompositorNodeMath")
    math_max_2.operation = "MAXIMUM"

    # Create the links
    link_nodes(sac_max_group, input_node, 0, math_max_1, 0)
    link_nodes(sac_max_group, input_node, 1, math_max_1, 1)
    link_nodes(sac_max_group, math_max_1, 0, math_max_2, 0)
    link_nodes(sac_max_group, input_node, 2, math_max_2, 1)
    link_nodes(sac_max_group, math_max_2, 0, output_node, 0)

    return sac_max_group


def create_combine_group() -> NodeTree:

    if ".SAC Three Max" not in bpy.data.node_groups:
        sac_max = create_max_group()
    else:
        sac_max = bpy.data.node_groups[".SAC Three Max"]

    # Create the group
    sac_combine_group: NodeTree = bpy.data.node_groups.new(name=".SAC Combine", type="CompositorNodeTree")

    input_node = sac_combine_group.nodes.new("NodeGroupInput")
    output_node = sac_combine_group.nodes.new("NodeGroupOutput")

    sac_combine_group.inputs.new("NodeSocketColor", "R")
    sac_combine_group.inputs.new("NodeSocketColor", "G")
    sac_combine_group.inputs.new("NodeSocketColor", "B")
    sac_combine_group.inputs.new("NodeSocketFloat", "A")
    sac_combine_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    separate_rgb_1 = sac_combine_group.nodes.new("CompositorNodeSeparateColor")
    separate_rgb_2 = sac_combine_group.nodes.new("CompositorNodeSeparateColor")
    separate_rgb_3 = sac_combine_group.nodes.new("CompositorNodeSeparateColor")

    max_group_1 = sac_combine_group.nodes.new("CompositorNodeGroup")
    max_group_1.node_tree = sac_max
    max_group_2 = sac_combine_group.nodes.new("CompositorNodeGroup")
    max_group_2.node_tree = sac_max
    max_group_3 = sac_combine_group.nodes.new("CompositorNodeGroup")
    max_group_3.node_tree = sac_max

    combine_rgb = sac_combine_group.nodes.new("CompositorNodeCombineColor")

    # Create the links
    link_nodes(sac_combine_group, input_node, 0, separate_rgb_1, 0)
    link_nodes(sac_combine_group, input_node, 1, separate_rgb_2, 0)
    link_nodes(sac_combine_group, input_node, 2, separate_rgb_3, 0)
    link_nodes(sac_combine_group, separate_rgb_1, 0, max_group_1, "A")
    link_nodes(sac_combine_group, separate_rgb_2, 0, max_group_1, "B")
    link_nodes(sac_combine_group, separate_rgb_3, 0, max_group_1, "C")
    link_nodes(sac_combine_group, separate_rgb_1, 1, max_group_2, "A")
    link_nodes(sac_combine_group, separate_rgb_2, 1, max_group_2, "B")
    link_nodes(sac_combine_group, separate_rgb_3, 1, max_group_2, "C")
    link_nodes(sac_combine_group, separate_rgb_1, 2, max_group_3, "A")
    link_nodes(sac_combine_group, separate_rgb_2, 2, max_group_3, "B")
    link_nodes(sac_combine_group, separate_rgb_3, 2, max_group_3, "C")
    link_nodes(sac_combine_group, max_group_1, 0, combine_rgb, 0)
    link_nodes(sac_combine_group, max_group_2, 0, combine_rgb, 1)
    link_nodes(sac_combine_group, max_group_3, 0, combine_rgb, 2)
    link_nodes(sac_combine_group, input_node, 3, combine_rgb, 3)
    link_nodes(sac_combine_group, combine_rgb, 0, output_node, 0)

    return sac_combine_group


def create_filter_group() -> NodeTree:

    # Create the groups once
    if ".SAC Combine" not in bpy.data.node_groups:
        sac_combine = create_combine_group()
    else:
        sac_combine = bpy.data.node_groups[".SAC Combine"]

    # Create the group
    sac_filter_group: NodeTree = bpy.data.node_groups.new(name=".SAC Filter", type="CompositorNodeTree")

    input_node = sac_filter_group.nodes.new("NodeGroupInput")
    output_node = sac_filter_group.nodes.new("NodeGroupOutput")

    sac_filter_group.inputs.new("NodeSocketColor", "Image")
    sac_filter_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    separate_rgb = sac_filter_group.nodes.new("CompositorNodeSeparateColor")

    red_channel = sac_filter_group.nodes.new("CompositorNodeCurveRGB")
    red_channel.name = "SAC Colorgrade_Filter_Red"
    green_channel = sac_filter_group.nodes.new("CompositorNodeCurveRGB")
    green_channel.name = "SAC Colorgrade_Filter_Green"
    blue_channel = sac_filter_group.nodes.new("CompositorNodeCurveRGB")
    blue_channel.name = "SAC Colorgrade_Filter_Blue"

    filter_channels = get_filter("Default")
    channels = [red_channel, green_channel, blue_channel]

    for channel, filter_channel in enumerate(filter_channels):
        channel_node = channels[channel]
        for curve, filter_curve in enumerate(filter_channel):
            channel_mapping = channel_node.mapping.curves[curve]
            for point, filter_point in enumerate(reversed(filter_curve)):
                if (point == len(filter_curve)-1) or (point == 0):
                    continue
                channel_mapping.points.new(point/(len(filter_curve)-1), filter_point)
        channel_node.mapping.update()

    combine_group = sac_filter_group.nodes.new("CompositorNodeGroup")
    combine_group.node_tree = sac_combine

    mix_node = sac_filter_group.nodes.new("CompositorNodeMixRGB")
    mix_node.blend_type = "MIX"
    mix_node.inputs[0].default_value = 0.5
    mix_node.name = "SAC Colorgrade_Filter_Mix"

    # Create the links
    link_nodes(sac_filter_group, input_node, 0, separate_rgb, 0)
    link_nodes(sac_filter_group, separate_rgb, 0, red_channel, 1)
    link_nodes(sac_filter_group, separate_rgb, 1, green_channel, 1)
    link_nodes(sac_filter_group, separate_rgb, 2, blue_channel, 1)
    link_nodes(sac_filter_group, red_channel, 0, combine_group, "R")
    link_nodes(sac_filter_group, green_channel, 0, combine_group, "G")
    link_nodes(sac_filter_group, blue_channel, 0, combine_group, "B")
    link_nodes(sac_filter_group, separate_rgb, 3, combine_group, "A")
    link_nodes(sac_filter_group, combine_group, 0, mix_node, 2)
    link_nodes(sac_filter_group, input_node, 0, mix_node, 1)
    link_nodes(sac_filter_group, mix_node, 0, output_node, 0)

    return sac_filter_group
