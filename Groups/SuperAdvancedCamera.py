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

from .Colorgrading.WhiteLevel import create_whitelevel_group
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
from .Effects.Duotone import create_duotone_group
from .Effects.FogGlow import create_fogglow_group
from .Effects.Streaks import create_streaks_group
from .Effects.Ghost import create_ghost_group
from .Effects.Emboss import create_emboss_group
from .Effects.Posterize import create_posterize_group
from .Effects.Overlay import create_overlay_group
from .Effects.Pixelate import create_pixelate_group
from .Effects.ChromaticAberration import create_chromatic_group
from .Effects.Viginette import create_viginette_group
from .Effects.Infrared import create_infrared_group
from .Effects.Negative import create_negative_group
from .Effects.Warp import create_warp_group
from .Effects.Fisheye import create_fisheye_group
from .Effects.PerspectiveShift import create_perspectiveshift_group
from .Effects.ISO import create_iso_group
from .Effects.FilmGrain import create_filmgrain_group
from .Effects.Halftone import create_halftone_group
from .Effects.GradientMap import create_gradientmap_group


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

    # White Level
    sac_whitelevel_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC WhiteLevel"]:
            sac_whitelevel_group.node_tree = bpy.data.node_groups[".SAC WhiteLevel"]
    except:
        sac_whitelevel_group.node_tree = create_whitelevel_group()
    sac_whitelevel_group.name = "SAC WhiteLevel"
    sac_whitelevel_group.mute = True

    # Temperature
    sac_temperature_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Temperature"]:
            sac_temperature_group.node_tree = bpy.data.node_groups[".SAC Temperature"]
    except:
        sac_temperature_group.node_tree = create_temperature_group()
    sac_temperature_group.name = "SAC Temperature"
    sac_temperature_group.mute = True

    # Tint
    sac_tint_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Tint"]:
            sac_tint_group.node_tree = bpy.data.node_groups[".SAC Tint"]
    except:
        sac_tint_group.node_tree = create_tint_group()
    sac_tint_group.name = "SAC Tint"
    sac_tint_group.mute = True

    # Saturation
    sac_saturation_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Saturation"]:
            sac_saturation_group.node_tree = bpy.data.node_groups[".SAC Saturation"]
    except:
        sac_saturation_group.node_tree = create_saturation_group("SAC Colorgrade_Color_Saturation", ".SAC Saturation")
    sac_saturation_group.name = "SAC Saturation"
    sac_saturation_group.mute = True

    # Exposure
    sac_exposure_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Exposure"]:
            sac_exposure_group.node_tree = bpy.data.node_groups[".SAC Exposure"]
    except:
        sac_exposure_group.node_tree = create_exposure_group()
    sac_exposure_group.name = "SAC Exposure"
    sac_exposure_group.mute = True

    # Contrast
    sac_contrast_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Contrast"]:
            sac_contrast_group.node_tree = bpy.data.node_groups[".SAC Contrast"]
    except:
        sac_contrast_group.node_tree = create_contrast_group()
    sac_contrast_group.name = "SAC Contrast"
    sac_contrast_group.mute = True

    # Highlights
    sac_highlights_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Highlights"]:
            sac_highlights_group.node_tree = bpy.data.node_groups[".SAC Highlights"]
    except:
        sac_highlights_group.node_tree = create_highlights_group()
    sac_highlights_group.name = "SAC Highlights"
    sac_highlights_group.mute = True

    # Shadows
    sac_shadows_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Shadows"]:
            sac_shadows_group.node_tree = bpy.data.node_groups[".SAC Shadows"]
    except:
        sac_shadows_group.node_tree = create_shadows_group()
    sac_shadows_group.name = "SAC Shadows"
    sac_shadows_group.mute = True

    # Whites
    sac_whites_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Whites"]:
            sac_whites_group.node_tree = bpy.data.node_groups[".SAC Whites"]
    except:
        sac_whites_group.node_tree = create_whites_group()
    sac_whites_group.name = "SAC Whites"
    sac_whites_group.mute = True

    # Darks
    sac_darks_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Darks"]:
            sac_darks_group.node_tree = bpy.data.node_groups[".SAC Darks"]
    except:
        sac_darks_group.node_tree = create_darks_group()
    sac_darks_group.name = "SAC Darks"
    sac_darks_group.mute = True

    # Sharpen
    sac_sharpen_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Sharpen"]:
            sac_sharpen_group.node_tree = bpy.data.node_groups[".SAC Sharpen"]
    except:
        sac_sharpen_group.node_tree = create_sharpen_group()
    sac_sharpen_group.name = "SAC Sharpen"
    sac_sharpen_group.mute = True

    # Vibrance
    sac_vibrance_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Vibrance"]:
            sac_vibrance_group.node_tree = bpy.data.node_groups[".SAC Vibrance"]
    except:
        sac_vibrance_group.node_tree = create_vibrance_group()
    sac_vibrance_group.name = "SAC Vibrance"
    sac_vibrance_group.mute = True

    # Saturation 2
    sac_saturation_group_2 = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Saturation2"]:
            sac_saturation_group_2.node_tree = bpy.data.node_groups[".SAC Saturation2"]
    except:
        sac_saturation_group_2.node_tree = create_saturation_group("SAC Colorgrade_Presets_Saturation", ".SAC Saturation2")
    sac_saturation_group_2.name = "SAC Saturation2"
    sac_saturation_group_2.mute = True

    # Highlight Tint
    sac_highlighttint_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC HighlightTint"]:
            sac_highlighttint_group.node_tree = bpy.data.node_groups[".SAC HighlightTint"]
    except:
        sac_highlighttint_group.node_tree = create_highlighttint_group()
    sac_highlighttint_group.name = "SAC HighlightTint"
    sac_highlighttint_group.mute = True

    # Shadow Tint
    sac_shadowtint_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC ShadowTint"]:
            sac_shadowtint_group.node_tree = bpy.data.node_groups[".SAC ShadowTint"]
    except:
        sac_shadowtint_group.node_tree = create_shadowtint_group()
    sac_shadowtint_group.name = "SAC ShadowTint"
    sac_shadowtint_group.mute = True

    # Curves
    sac_curves_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Curves"]:
            sac_curves_group.node_tree = bpy.data.node_groups[".SAC Curves"]
    except:
        sac_curves_group.node_tree = create_curves_group()
    sac_curves_group.name = "SAC Curves"

    # Colorwheels
    sac_colorwheels_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Colorwheel"]:
            sac_colorwheels_group.node_tree = bpy.data.node_groups[".SAC Colorwheel"]
    except:
        sac_colorwheels_group.node_tree = create_colorwheel_group()
    sac_colorwheels_group.name = "SAC Colorwheels"

    # Duotone
    sac_duotone_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Duotone"]:
            sac_duotone_group.node_tree = bpy.data.node_groups[".SAC Duotone"]
    except:
        sac_duotone_group.node_tree = create_duotone_group()
    sac_duotone_group.name = "SAC Duotone"
    sac_duotone_group.mute = True

    # Fog Glow
    sac_fogglow_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC FogGlow"]:
            sac_fogglow_group.node_tree = bpy.data.node_groups[".SAC FogGlow"]
    except:
        sac_fogglow_group.node_tree = create_fogglow_group()
    sac_fogglow_group.name = "SAC FogGlow"
    sac_fogglow_group.mute = True

    # Streaks
    sac_streaks_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Streaks"]:
            sac_streaks_group.node_tree = bpy.data.node_groups[".SAC Streaks"]
    except:
        sac_streaks_group.node_tree = create_streaks_group()
    sac_streaks_group.name = "SAC Streaks"
    sac_streaks_group.mute = True

    # Ghost
    sac_ghost_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Ghost"]:
            sac_ghost_group.node_tree = bpy.data.node_groups[".SAC Ghost"]
    except:
        sac_ghost_group.node_tree = create_ghost_group()
    sac_ghost_group.name = "SAC Ghost"
    sac_ghost_group.mute = True

    # Emboss
    sac_emboss_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Emboss"]:
            sac_emboss_group.node_tree = bpy.data.node_groups[".SAC Emboss"]
    except:
        sac_emboss_group.node_tree = create_emboss_group()
    sac_emboss_group.name = "SAC Emboss"
    sac_emboss_group.mute = True

    # Posterize
    sac_posterize_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Posterize"]:
            sac_posterize_group.node_tree = bpy.data.node_groups[".SAC Posterize"]
    except:
        sac_posterize_group.node_tree = create_posterize_group()
    sac_posterize_group.name = "SAC Posterize"
    sac_posterize_group.mute = True

    # Overlay
    sac_overlay_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Overlay"]:
            sac_overlay_group.node_tree = bpy.data.node_groups[".SAC Overlay"]
    except:
        sac_overlay_group.node_tree = create_overlay_group()
    sac_overlay_group.name = "SAC Overlay"
    sac_overlay_group.mute = True

    # Pixelate
    sac_pixelate_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Pixelate"]:
            sac_pixelate_group.node_tree = bpy.data.node_groups[".SAC Pixelate"]
    except:
        sac_pixelate_group.node_tree = create_pixelate_group()
    sac_pixelate_group.name = "SAC Pixelate"
    sac_pixelate_group.mute = True

    # Chromatic Aberration
    sac_chromatic_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC ChromaticAberration"]:
            sac_chromatic_group.node_tree = bpy.data.node_groups[".SAC ChromaticAberration"]
    except:
        sac_chromatic_group.node_tree = create_chromatic_group()
    sac_chromatic_group.name = "SAC ChromaticAberration"
    sac_chromatic_group.mute = True

    # Viginette
    sac_viginette_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Viginette"]:
            sac_viginette_group.node_tree = bpy.data.node_groups[".SAC Viginette"]
    except:
        sac_viginette_group.node_tree = create_viginette_group()
    sac_viginette_group.name = "SAC Viginette"
    sac_viginette_group.mute = True

    # Infrared
    sac_infrared_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Infrared"]:
            sac_infrared_group.node_tree = bpy.data.node_groups[".SAC Infrared"]
    except:
        sac_infrared_group.node_tree = create_infrared_group()
    sac_infrared_group.name = "SAC Infrared"
    sac_infrared_group.mute = True

    # Negative
    sac_negative_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Negative"]:
            sac_negative_group.node_tree = bpy.data.node_groups[".SAC Negative"]
    except:
        sac_negative_group.node_tree = create_negative_group()
    sac_negative_group.name = "SAC Negative"
    sac_negative_group.mute = True

    # Warp
    sac_warp_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Warp"]:
            sac_warp_group.node_tree = bpy.data.node_groups[".SAC Warp"]
    except:
        sac_warp_group.node_tree = create_warp_group()
    sac_warp_group.name = "SAC Warp"
    sac_warp_group.mute = True

    # Fisheye
    sac_fisheye_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Fisheye"]:
            sac_fisheye_group.node_tree = bpy.data.node_groups[".SAC Fisheye"]
    except:
        sac_fisheye_group.node_tree = create_fisheye_group()
    sac_fisheye_group.name = "SAC Fisheye"
    sac_fisheye_group.mute = True

    # Perspective Shift
    sac_perspectiveshift_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC PerspectiveShift"]:
            sac_perspectiveshift_group.node_tree = bpy.data.node_groups[".SAC PerspectiveShift"]
    except:
        sac_perspectiveshift_group.node_tree = create_perspectiveshift_group()
    sac_perspectiveshift_group.name = "SAC PerspectiveShift"
    sac_perspectiveshift_group.mute = True

    # ISO
    sac_iso_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC ISO"]:
            sac_iso_group.node_tree = bpy.data.node_groups[".SAC ISO"]
    except:
        sac_iso_group.node_tree = create_iso_group()
    sac_iso_group.name = "SAC ISO"
    sac_iso_group.mute = True

    # Film Grain
    sac_filmgrain_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC FilmGrain"]:
            sac_filmgrain_group.node_tree = bpy.data.node_groups[".SAC FilmGrain"]
    except:
        sac_filmgrain_group.node_tree = create_filmgrain_group()
    sac_filmgrain_group.name = "SAC FilmGrain"
    sac_filmgrain_group.mute = True

    # Halftone
    sac_halftone_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC Halftone"]:
            sac_halftone_group.node_tree = bpy.data.node_groups[".SAC Halftone"]
    except:
        sac_halftone_group.node_tree = create_halftone_group()
    sac_halftone_group.name = "SAC Halftone"
    sac_halftone_group.mute = True

    # Gradient Map
    sac_gradientmap_group = sac_group.nodes.new("CompositorNodeGroup")
    try:
        if bpy.data.node_groups[".SAC GradientMap"]:
            sac_gradientmap_group.node_tree = bpy.data.node_groups[".SAC GradientMap"]
    except:
        sac_gradientmap_group.node_tree = create_gradientmap_group()
    sac_gradientmap_group.name = "SAC GradientMap"
    sac_gradientmap_group.mute = True

    # Create the links
    # link the input node to the white level node
    sac_group.links.new(input_node.outputs[0], sac_whitelevel_group.inputs[0])
    # link the white level node to the temperature node
    sac_group.links.new(sac_whitelevel_group.outputs[0], sac_temperature_group.inputs[0])
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
    # link the colorwheels node to the duotone node
    sac_group.links.new(sac_colorwheels_group.outputs[0], sac_duotone_group.inputs[0])
    # link the duotone node to the fogglow node
    sac_group.links.new(sac_duotone_group.outputs[0], sac_fogglow_group.inputs[0])
    # link the fogglow node to the streaks node
    sac_group.links.new(sac_fogglow_group.outputs[0], sac_streaks_group.inputs[0])
    # link the streaks node to the ghost node
    sac_group.links.new(sac_streaks_group.outputs[0], sac_ghost_group.inputs[0])
    # link the ghost node to the emboss node
    sac_group.links.new(sac_ghost_group.outputs[0], sac_emboss_group.inputs[0])
    # link the emboss node to the posterize node
    sac_group.links.new(sac_emboss_group.outputs[0], sac_posterize_group.inputs[0])
    # link the posterize node to the overlay node
    sac_group.links.new(sac_posterize_group.outputs[0], sac_overlay_group.inputs[0])
    # link the overlay node to the pixelate node
    sac_group.links.new(sac_overlay_group.outputs[0], sac_pixelate_group.inputs[0])
    # link the pixelate node to the chromatic node
    sac_group.links.new(sac_pixelate_group.outputs[0], sac_chromatic_group.inputs[0])
    # link the chromatic node to the viginette node
    sac_group.links.new(sac_chromatic_group.outputs[0], sac_viginette_group.inputs[0])
    # link the viginette node to the infrared node
    sac_group.links.new(sac_viginette_group.outputs[0], sac_infrared_group.inputs[0])
    # link the infrared node to the negative node
    sac_group.links.new(sac_infrared_group.outputs[0], sac_negative_group.inputs[0])
    # link the negative node to the warp node
    sac_group.links.new(sac_negative_group.outputs[0], sac_warp_group.inputs[0])
    # link the warp node to the fisheye node
    sac_group.links.new(sac_warp_group.outputs[0], sac_fisheye_group.inputs[0])
    # link the fisheye node to the perspectiveshift node
    sac_group.links.new(sac_fisheye_group.outputs[0], sac_perspectiveshift_group.inputs[0])
    # link the perspectiveshift node to the iso node
    sac_group.links.new(sac_perspectiveshift_group.outputs[0], sac_iso_group.inputs[0])
    # link the iso node to the filmgrain node
    sac_group.links.new(sac_iso_group.outputs[0], sac_filmgrain_group.inputs[0])
    # link the filmgrain node to the halftone node
    sac_group.links.new(sac_filmgrain_group.outputs[0], sac_halftone_group.inputs[0])
    # link the halftone node to the gradientmap node
    sac_group.links.new(sac_halftone_group.outputs[0], sac_gradientmap_group.inputs[0])
    # link the gradientmap node to the output node
    sac_group.links.new(sac_gradientmap_group.outputs[0], output_node.inputs[0])

    # return
    return (sac_group)


def connect_renderLayer_node():
    # Make sure the compositor is enabled for the active scene
    bpy.context.scene.use_nodes = True
    # bpy.context.space_data.shading.use_compositor = 'ALWAYS'
    tree = bpy.context.scene.node_tree

    # Loop through all nodes to find Render Layer nodes
    render_layer_nodes = [node for node in tree.nodes if node.type == 'R_LAYERS']
    super_denoiser_nodes = [node for node in tree.nodes if node.name == 'sid_node']

    # Exit if no Render Layer nodes are found
    if not render_layer_nodes:
        print("No Render Layer nodes found.")
        return

    # Process each Render Layer node
    for render_layer_node in render_layer_nodes:
        # Check if SuperImageDenoiser is connected to this Render Layer node
        connect_to_node = render_layer_node
        for link in tree.links:
            if link.from_node == render_layer_node and link.to_node in super_denoiser_nodes:
                connect_to_node = link.to_node
                break

        # Create a new mix node
        sac_node = tree.nodes.new(type='CompositorNodeGroup')
        try:
            if bpy.data.node_groups["Super Advanced Camera"]:
                sac_node.node_tree = bpy.data.node_groups["Super Advanced Camera"]
        except:
            sac_node.node_tree = create_main_group()
        sac_node.location = (render_layer_node.location.x + 300, render_layer_node.location.y)

        # Collect links to be rerouted
        to_disconnect = []
        to_connect = []
        for link in tree.links:
            if link.from_node == connect_to_node:
                # Save the links to be disconnected
                to_disconnect.append(link)

                # Save the information needed to make new connections
                to_connect.append((sac_node.outputs[0], link.to_socket, connect_to_node.outputs[link.from_socket.name]))

        # Disconnect the original links
        for link in to_disconnect:
            tree.links.remove(link)

        # Make new connections
        for mix_output, to_socket, from_socket in to_connect:
            # Connect the mix node to where the connect_to_node was connected
            tree.links.new(mix_output, to_socket)

            # Connect the connect_to_node to the mix node
            tree.links.new(from_socket, sac_node.inputs[0])
