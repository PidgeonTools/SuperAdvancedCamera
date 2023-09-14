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


def create_bokeh_group() -> NodeTree:

    # Create the group
    sac_bokeh_group: NodeTree = bpy.data.node_groups.new(name=".SAC Bokeh", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_bokeh_group.nodes.new("NodeGroupInput")
    output_node = sac_bokeh_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_bokeh_group.inputs.new("NodeSocketColor", "Image")
    sac_bokeh_group.inputs.new("NodeSocketFloat", "Depth")
    sac_bokeh_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # vector normalize node
    normalize_node = sac_bokeh_group.nodes.new("CompositorNodeNormalize")
    # math add node
    add_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    add_node.operation = "ADD"
    add_node.inputs[1].default_value = 0
    add_node.name = "SAC Effects_Bokeh_Offset"
    # math multiply node
    multiply_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    multiply_node.operation = "MULTIPLY"
    multiply_node.inputs[1].default_value = 1
    multiply_node.name = "SAC Effects_Bokeh_Range"
    # math absolute node
    absolute_node = sac_bokeh_group.nodes.new("CompositorNodeMath")
    absolute_node.operation = "ABSOLUTE"
    # image node
    image_node = sac_bokeh_group.nodes.new("CompositorNodeImage")
    image_node.name = "SAC Effects_Bokeh_Image"
    # image node
    custom_node = sac_bokeh_group.nodes.new("CompositorNodeImage")
    custom_node.name = "SAC Effects_Bokeh_Custom_Image"
    # bokeh image node
    bokeh_image_node = sac_bokeh_group.nodes.new("CompositorNodeBokehImage")
    bokeh_image_node.name = "SAC Effects_Bokeh_Procedural"
    # switch node
    switch_node = sac_bokeh_group.nodes.new("CompositorNodeSwitch")
    switch_node.name = "SAC Effects_Bokeh_Switch"
    # switch node
    switch_image_node = sac_bokeh_group.nodes.new("CompositorNodeSwitch")
    switch_image_node.name = "SAC Effects_Bokeh_ImageSwitch"
    # rotate node
    rotate_node = sac_bokeh_group.nodes.new("CompositorNodeRotate")
    rotate_node.name = "SAC Effects_Bokeh_Rotation"
    # bokeh blur node
    bokeh_blur_node = sac_bokeh_group.nodes.new("CompositorNodeBokehBlur")
    bokeh_blur_node.name = "SAC Effects_Bokeh_Blur"
    bokeh_blur_node.use_variable_size = True

    # Create the links
    # Link the input node to the normalize node
    sac_bokeh_group.links.new(input_node.outputs[1], normalize_node.inputs[0])
    # Link the normalize node to the add node
    sac_bokeh_group.links.new(normalize_node.outputs[0], add_node.inputs[0])
    # Link the add node to the multiply node
    sac_bokeh_group.links.new(add_node.outputs[0], multiply_node.inputs[0])
    # Link the multiply node to the absolute node
    sac_bokeh_group.links.new(multiply_node.outputs[0], absolute_node.inputs[0])
    # Link the absolute node to the bokeh blur node
    sac_bokeh_group.links.new(absolute_node.outputs[0], bokeh_blur_node.inputs[2])
    # link the input node to the bokeh blur node
    sac_bokeh_group.links.new(input_node.outputs[0], bokeh_blur_node.inputs[0])
    # link the image node to the switch image node
    sac_bokeh_group.links.new(image_node.outputs[0], switch_image_node.inputs[0])
    # link the custom node to the switch image node
    sac_bokeh_group.links.new(custom_node.outputs[0], switch_image_node.inputs[1])
    # link the switch image node to the rotate node
    sac_bokeh_group.links.new(switch_image_node.outputs[0], rotate_node.inputs[0])
    # link the rotate node to the switch node
    sac_bokeh_group.links.new(rotate_node.outputs[0], switch_node.inputs[0])
    # link the bokeh image node to the switch node
    sac_bokeh_group.links.new(bokeh_image_node.outputs[0], switch_node.inputs[1])
    # link the switch node to the bokeh blur node
    sac_bokeh_group.links.new(switch_node.outputs[0], bokeh_blur_node.inputs[1])
    # link the bokeh blur node to the output node
    sac_bokeh_group.links.new(bokeh_blur_node.outputs[0], output_node.inputs[0])

    # return
    return sac_bokeh_group
