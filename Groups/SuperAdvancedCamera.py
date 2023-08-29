import bpy
from bpy.types import NodeTree

from .Colorgrading.Temperature import create_temperature_group
from .Colorgrading.Tint import create_tint_group
from .Colorgrading.Saturation import create_saturation_group
from .Colorgrading.Exposure import create_exposure_group
from .Colorgrading.Contrast import create_contrast_group
from .Colorgrading.Highlights import create_highlights_group
from .Colorgrading.Shadows import create_shadows_group
from .Colorgrading.Whites import create_whites_group
from .Colorgrading.Darks import create_darks_group
from .Colorgrading.Sharpen import create_sharpen_group
from .Colorgrading.Vibrance import create_vibrance_group
from .Colorgrading.HighlightTint import create_highlighttint_group
from .Colorgrading.ShadowTint import create_shadowtint_group
from .Colorgrading.Curves import create_curves_group
from .Colorgrading.Colorwheels import create_colorwheel_group


def create_main_group() -> NodeTree:

    # Create the group
    sac_group: NodeTree = bpy.data.node_groups.new(name="Super Advanced Camera", type="CompositorNodeTree")

    # Create the input and output nodes
    input_node = sac_group.nodes.new("NodeGroupInput")
    output_node = sac_group.nodes.new("NodeGroupOutput")

    # Add the input and output sockets
    sac_group.inputs.new("NodeSocketColor", "Image")
    sac_group.outputs.new("NodeSocketColor", "Image")

    # Create the nodes
    # Temperature
    sac_temperature_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_temperature_group.node_tree = create_temperature_group()
    # Tint
    sac_tint_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_tint_group.node_tree = create_tint_group()
    # Saturation
    sac_saturation_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_saturation_group.node_tree = create_saturation_group("SAC Colorgrade_Color_Saturation", ".SAC Saturation")
    # Exposure
    sac_exposure_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_exposure_group.node_tree = create_exposure_group()
    # Contrast
    sac_contrast_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_contrast_group.node_tree = create_contrast_group()
    # Highlights
    sac_highlights_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_highlights_group.node_tree = create_highlights_group()
    # Shadows
    sac_shadows_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_shadows_group.node_tree = create_shadows_group()
    # Whites
    sac_whites_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_whites_group.node_tree = create_whites_group()
    # Darks
    sac_darks_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_darks_group.node_tree = create_darks_group()
    # Sharpen
    sac_sharpen_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_sharpen_group.node_tree = create_sharpen_group()
    # Vibrance
    sac_vibrance_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_vibrance_group.node_tree = create_vibrance_group()
    # Saturation 2
    sac_saturation_group_2 = sac_group.nodes.new("CompositorNodeGroup")
    sac_saturation_group_2.node_tree = create_saturation_group("SAC Colorgrade_Presets_Saturation", "..SAC Saturation2")
    # Highlight Tint
    sac_highlighttint_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_highlighttint_group.node_tree = create_highlighttint_group()
    # Shadow Tint
    sac_shadowtint_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_shadowtint_group.node_tree = create_shadowtint_group()
    # Curves
    sac_curves_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_curves_group.node_tree = create_curves_group()
    # Colorwheels
    sac_colorwheels_group = sac_group.nodes.new("CompositorNodeGroup")
    sac_colorwheels_group.node_tree = create_colorwheel_group()

    # Create the links
    # link the input node to the temperature node
    sac_group.links.new(input_node.outputs[0], sac_temperature_group.inputs[0])
    # link the temperature node to the tint node
    sac_group.links.new(sac_temperature_group.outputs[0], sac_tint_group.inputs[0])
    # link the tint node to the saturation node
    sac_group.links.new(sac_tint_group.outputs[0], sac_saturation_group.inputs[0])
    # link the saturation node to the exposure node
    sac_group.links.new(sac_saturation_group.outputs[0], sac_exposure_group.inputs[0])
    # link the exposure node to the contrast node
    sac_group.links.new(sac_exposure_group.outputs[0], sac_contrast_group.inputs[0])
    # link the contrast node to the highlights node
    sac_group.links.new(sac_contrast_group.outputs[0], sac_highlights_group.inputs[0])
    # link the highlights node to the shadows node
    sac_group.links.new(sac_highlights_group.outputs[0], sac_shadows_group.inputs[0])
    # link the shadows node to the whites node
    sac_group.links.new(sac_shadows_group.outputs[0], sac_whites_group.inputs[0])
    # link the whites node to the darks node
    sac_group.links.new(sac_whites_group.outputs[0], sac_darks_group.inputs[0])
    # link the darks node to the sharpen node
    sac_group.links.new(sac_darks_group.outputs[0], sac_sharpen_group.inputs[0])
    # link the sharpen node to the vibrance node
    sac_group.links.new(sac_sharpen_group.outputs[0], sac_vibrance_group.inputs[0])
    # link the vibrance node to the saturation2 node
    sac_group.links.new(sac_vibrance_group.outputs[0], sac_saturation_group_2.inputs[0])
    # link the saturation2 node to the highlighttint node
    sac_group.links.new(sac_saturation_group_2.outputs[0], sac_highlighttint_group.inputs[0])
    # link the highlighttint node to the shadowtint node
    sac_group.links.new(sac_highlighttint_group.outputs[0], sac_shadowtint_group.inputs[0])
    # link the shadowtint node to the curves node
    sac_group.links.new(sac_shadowtint_group.outputs[0], sac_curves_group.inputs[0])
    # link the curves node to the colorwheels node
    sac_group.links.new(sac_curves_group.outputs[0], sac_colorwheels_group.inputs[0])
    # link the colorwheels node to the output node
    sac_group.links.new(sac_colorwheels_group.outputs[0], output_node.inputs[0])

    # return
    return sac_group
