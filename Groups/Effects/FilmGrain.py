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


def create_filmgrain_group() -> NodeTree:

    # Create the group
    sac_filmgrain_group: NodeTree = bpy.data.node_groups.new(name=".SAC FilmGrain", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_filmgrain_group.nodes.new("NodeGroupInput")
    output_node = sac_filmgrain_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_filmgrain_group.inputs.new("NodeSocketColor", "Image")
    sac_filmgrain_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # math add node, second value 1, clamped
    add_node = sac_filmgrain_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.use_clamp = True
    add_node.inputs[1].default_value = 1
    # Lens Distortion node, jitter enabled, distortion 0.0001
    lens_distortion_node = sac_filmgrain_group.nodes.new("CompositorNodeLensdist")
    lens_distortion_node.use_jitter = True
    lens_distortion_node.inputs[1].default_value = 0.00001
    # RGB to BW
    rgb_to_bw_node = sac_filmgrain_group.nodes.new("CompositorNodeRGBToBW")
    # math subtract node, first value 1, clamped
    math_subtract_node = sac_filmgrain_group.nodes.new("CompositorNodeMath")
    math_subtract_node.operation = "SUBTRACT"
    math_subtract_node.use_clamp = True
    math_subtract_node.inputs[0].default_value = 1
    # Bilateral Blur node, iterations 5, color sigma 0.4, space sigma 1
    bilateral_blur_node = sac_filmgrain_group.nodes.new("CompositorNodeBilateralblur")
    bilateral_blur_node.iterations = 5
    bilateral_blur_node.sigma_color = 0.4
    bilateral_blur_node.sigma_space = 1
    bilateral_blur_node.name = "SAC Effects_FilmGrain_Blur"
    # color screen node
    color_screen_node = sac_filmgrain_group.nodes.new("CompositorNodeMixRGB")
    color_screen_node.blend_type = "SCREEN"
    color_screen_node.name = "SAC Effects_FilmGrain_Strength"
    color_screen_node.inputs[0].default_value = 0

    # Create the links
    # input node to add node
    sac_filmgrain_group.links.new(input_node.outputs[0], add_node.inputs[0])
    # add node to lens distortion node
    sac_filmgrain_group.links.new(add_node.outputs[0], lens_distortion_node.inputs[0])
    # lens distortion node to rgb to bw node
    sac_filmgrain_group.links.new(lens_distortion_node.outputs[0], rgb_to_bw_node.inputs[0])
    # rgb to bw node to math subtract node
    sac_filmgrain_group.links.new(rgb_to_bw_node.outputs[0], math_subtract_node.inputs[1])
    # math subtract node to bilateral blur node
    sac_filmgrain_group.links.new(math_subtract_node.outputs[0], bilateral_blur_node.inputs[0])
    sac_filmgrain_group.links.new(math_subtract_node.outputs[0], bilateral_blur_node.inputs[1])
    # bilateral blur node to color screen node
    sac_filmgrain_group.links.new(bilateral_blur_node.outputs[0], color_screen_node.inputs[2])
    # input node to color screen node
    sac_filmgrain_group.links.new(input_node.outputs[0], color_screen_node.inputs[1])
    # color screen node to output node
    sac_filmgrain_group.links.new(color_screen_node.outputs[0], output_node.inputs[0])

    # return
    return sac_filmgrain_group
