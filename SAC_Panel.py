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

from bpy.types import (
    Context,
    Panel,
)

from .SAC_Settings import SAC_Settings
from .SAC_Operators import SAC_OT_Initialize


# Main
class SAC_PT_Panel:
    bl_label = "Super Advanced Camera"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {"DEFAULT_CLOSED"}


class SAC_PT_SAC_Panel(SAC_PT_Panel, Panel):
    bl_label = "Super Advanced Camera"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="SHADERFX")

    def draw(self, context: Context):
        layout = self.layout
        layout.operator("object.superadvancedcamerainit", icon="SHADERFX")


# Colorgrade
class SAC_PT_COLORGRADE_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color Grading"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout


# Colorgrade - Color
class SAC_PT_COLORGRADE_Color_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="COLOR")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        layout.prop(settings, "Colorgrade_Color_WhiteLevel")
        layout.prop(settings, "Colorgrade_Color_Temperature")
        layout.prop(settings, "Colorgrade_Color_Tint")
        layout.prop(settings, "Colorgrade_Color_Saturation")
        layout.prop(settings, "Colorgrade_Color_Hue")


# Colorgrade - Light
class SAC_PT_COLORGRADE_Light_Panel(SAC_PT_Panel, Panel):
    bl_label = "Light"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_OB_LIGHT")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        layout.prop(settings, "Colorgrade_Light_Exposure")
        layout.prop(settings, "Colorgrade_Light_Contrast")
        layout.prop(settings, "Colorgrade_Light_Highlights")
        layout.prop(settings, "Colorgrade_Light_Shadows")
        layout.prop(settings, "Colorgrade_Light_Whites")
        layout.prop(settings, "Colorgrade_Light_Darks")


# Colorgrade - Presets
class SAC_PT_COLORGRADE_Presets_Panel(SAC_PT_Panel, Panel):
    bl_label = "Presets"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="PRESET")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        layout.prop(settings, "Colorgrade_Presets_Presets")
        layout.prop(settings, "Colorgrade_Presets_Sharpen")
        layout.prop(settings, "Colorgrade_Presets_Vibrance")
        layout.prop(settings, "Colorgrade_Presets_Saturation")
        layout.prop(settings, "Colorgrade_Presets_HighlightTint")
        layout.prop(settings, "Colorgrade_Presets_ShadowTint")


# Colorgrade - Curves
class SAC_PT_COLORGRADE_Curves_Panel(SAC_PT_Panel, Panel):
    bl_label = "Curves"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="FCURVE")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        rgb_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_RGB"]
        hsv_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_HSV"]

        layout = self.layout
        layout.template_curve_mapping(rgb_curves_node, "mapping", type='COLOR')
        layout.prop(settings, "Colorgrade_Curves_RGB_Intensity")
        layout.template_curve_mapping(hsv_curves_node, "mapping", type='HUE')
        layout.prop(settings, "Colorgrade_Curves_HSV_Intensity")


# Colorgrade - Colorwheels
class SAC_PT_COLORGRADE_Colorwheels_Panel(SAC_PT_Panel, Panel):
    bl_label = "Colorwheels"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MESH_CIRCLE")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        color_wheel_node_lift = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Shadows"]
        color_wheel_node_gamma = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Midtones"]
        color_wheel_node_gain = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Highlights"]

        layout = self.layout
        layout.alignment = "CENTER"
        layout.label(text="Shadows")
        layout.template_color_picker(color_wheel_node_lift, "lift")
        layout.prop(settings, "Colorgrade_Colorwheel_Shadows_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Shadows_Intensity")
        layout.label(text="Midtones")
        layout.template_color_picker(color_wheel_node_gamma, "gamma")
        layout.prop(settings, "Colorgrade_Colorwheel_Midtones_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Midtones_Intensity")
        layout.label(text="Highlights")
        layout.template_color_picker(color_wheel_node_gain, "gain")
        layout.prop(settings, "Colorgrade_Colorwheel_Highlights_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Highlights_Intensity")


# Effects
class SAC_PT_EFFECTS_Panel(SAC_PT_Panel, Panel):
    bl_label = "Effects"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="IMAGE")

    def draw(self, context: Context):
        layout = self.layout
        layout.operator("wm.url_open", text="Submit your requests", icon="URL").url = "https://go.pidgeontools.com/2023-08-29-sac-survey"


# Effects - Color
class SAC_PT_EFFECTS_Color_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="COLOR")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Duotone
class SAC_PT_EFFECTS_Duotone_Panel(SAC_PT_Panel, Panel):
    bl_label = "Duotone"
    bl_parent_id = "SAC_PT_EFFECTS_Color_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_TINT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Duotone_Color1")
        layout.prop(settings, "Effects_Duotone_Color2")
        layout.prop(settings, "Effects_Duotone_Blend")


# Effects - Lighting
class SAC_PT_EFFECTS_Lighting_Panel(SAC_PT_Panel, Panel):
    bl_label = "Lighting Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_OB_LIGHT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Glare
class SAC_PT_EFFECTS_Glare_Panel(SAC_PT_Panel, Panel):
    bl_label = "Glare"
    bl_parent_id = "SAC_PT_EFFECTS_Lighting_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="CON_CAMERASOLVER")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Glare FogGlow
class SAC_PT_EFFECTS_GLARE_FogGlow_Panel(SAC_PT_Panel, Panel):
    bl_label = "Fog Glow"
    bl_parent_id = "SAC_PT_EFFECTS_Glare_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ALIGN_FLUSH")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Glare_FogGlow_Strength")
        layout.prop(settings, "Effects_Glare_FogGlow_Threshold")
        layout.prop(settings, "Effects_Glare_FogGlow_Size")


# Glare Streaks
class SAC_PT_EFFECTS_GLARE_Streaks_Panel(SAC_PT_Panel, Panel):
    bl_label = "Streaks"
    bl_parent_id = "SAC_PT_EFFECTS_Glare_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="LIGHT_SUN")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Glare_Streaks_Strength")
        layout.prop(settings, "Effects_Glare_Streaks_Threshold")
        layout.prop(settings, "Effects_Glare_Streaks_Count")
        layout.prop(settings, "Effects_Glare_Streaks_Length")
        layout.prop(settings, "Effects_Glare_Streaks_Fade")
        layout.prop(settings, "Effects_Glare_Streaks_Angle")
        layout.prop(settings, "Effects_Glare_Streaks_Distortion")


# Glare Ghost
class SAC_PT_EFFECTS_GLARE_Ghost_Panel(SAC_PT_Panel, Panel):
    bl_label = "Lense Ghosts"
    bl_parent_id = "SAC_PT_EFFECTS_Glare_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="GHOST_DISABLED")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Glare_Ghosts_Strength")
        layout.prop(settings, "Effects_Glare_Ghosts_Threshold")
        layout.prop(settings, "Effects_Glare_Ghosts_Count")
        layout.prop(settings, "Effects_Glare_Ghosts_Distortion")


# Effects - Texture
class SAC_PT_EFFECTS_Texture_Panel(SAC_PT_Panel, Panel):
    bl_label = "Texture Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="NODE_TEXTURE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Emboss
class SAC_PT_EFFECTS_Emboss_Panel(SAC_PT_Panel, Panel):
    bl_label = "Emboss"
    bl_parent_id = "SAC_PT_EFFECTS_Texture_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="AXIS_TOP")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Emboss_Strength")


# Posterize
class SAC_PT_EFFECTS_Posterize_Panel(SAC_PT_Panel, Panel):
    bl_label = "Posterize"
    bl_parent_id = "SAC_PT_EFFECTS_Texture_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="IMAGE_ZDEPTH")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Posterize_Toggle")
        layout.prop(settings, "Effects_Posterize_Steps")


# Halftone
class SAC_PT_EFFECTS_Halftone_Panel(SAC_PT_Panel, Panel):
    bl_label = "Halftone (maybe coming)"
    bl_parent_id = "SAC_PT_EFFECTS_Texture_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="LIGHTPROBE_GRID")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect is extremely complex, we might not implement it")


# Overlay
class SAC_PT_EFFECTS_Overlay_Panel(SAC_PT_Panel, Panel):
    bl_label = "Overlay"
    bl_parent_id = "SAC_PT_EFFECTS_Texture_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="XRAY")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        overlay_texture = bpy.data.node_groups[".SAC Overlay"].nodes["SAC Effects_Overlay_Texture"]

        layout.template_ID(overlay_texture, "image", open="image.open")
        layout.prop(settings, "Effects_Overlay_Strength")


# Effects - Special
class SAC_PT_EFFECTS_Special_Panel(SAC_PT_Panel, Panel):
    bl_label = "Special Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="FREEZE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Bokeh
class SAC_PT_EFFECTS_Bokeh_Panel(SAC_PT_Panel, Panel):
    bl_label = "Bokeh (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ANTIALIASED")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect is very resource demanding, it might not get viewport support")


# Vignette
class SAC_PT_EFFECTS_Vignette_Panel(SAC_PT_Panel, Panel):
    bl_label = "Vignette"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="CLIPUV_DEHLT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Vignette_Intensity")
        layout.prop(settings, "Effects_Vignette_Roundness")
        layout.prop(settings, "Effects_Vignette_Feather")
        layout.prop(settings, "Effects_Vignette_Midpoint")


# Mosaic
class SAC_PT_EFFECTS_Mosaic_Panel(SAC_PT_Panel, Panel):
    bl_label = "Mosaic"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_UVPROJECT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Pixelate_PixelSize")


# Chromatic Aberration
class SAC_PT_EFFECTS_ChromaticAberration_Panel(SAC_PT_Panel, Panel):
    bl_label = "Chromatic Aberration"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_EDGESPLIT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_ChromaticAberration_Amount")


# Infrared
class SAC_PT_EFFECTS_Infrared_Panel(SAC_PT_Panel, Panel):
    bl_label = "Infrared"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_DATA_LIGHT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Infrared_Blend")
        layout.prop(settings, "Effects_Infrared_Offset")


# Lomo
class SAC_PT_EFFECTS_Lomo_Panel(SAC_PT_Panel, Panel):
    bl_label = "Lomo (maybe coming)"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="LIGHT_POINT")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect is complex, we might not implement it")


# Negative
class SAC_PT_EFFECTS_Negative_Panel(SAC_PT_Panel, Panel):
    bl_label = "Negative"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="SELECT_DIFFERENCE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Negative")


# ISO Noise
class SAC_PT_EFFECTS_ISONoise_Panel(SAC_PT_Panel, Panel):
    bl_label = "ISO Noise"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ALIGN_FLUSH")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "ISO_strength")
        layout.prop(settings, "ISO_size")


# Film Grain
class SAC_PT_EFFECTS_FilmGrain_Panel(SAC_PT_Panel, Panel):
    bl_label = "Film Grain (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Special_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ALIGN_FLUSH")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="Coming soon")


# Effects - Geometric
class SAC_PT_EFFECTS_Geometric_Panel(SAC_PT_Panel, Panel):
    bl_label = "Geometric Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MESH_ICOSPHERE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Warp
class SAC_PT_EFFECTS_Warp_Panel(SAC_PT_Panel, Panel):
    bl_label = "Warp"
    bl_parent_id = "SAC_PT_EFFECTS_Geometric_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_WARP")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Warp")


# Fish Eye
class SAC_PT_EFFECTS_FishEye_Panel(SAC_PT_Panel, Panel):
    bl_label = "Fish Eye"
    bl_parent_id = "SAC_PT_EFFECTS_Geometric_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MESH_UVSPHERE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_Fisheye")


# Perspective Shift
class SAC_PT_EFFECTS_PerspectiveShift_Panel(SAC_PT_Panel, Panel):
    bl_label = "Perspective Shift"
    bl_parent_id = "SAC_PT_EFFECTS_Geometric_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="VIEW_PERSPECTIVE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.prop(settings, "Effects_PerspectiveShift_Horizontal")
        layout.prop(settings, "Effects_PerspectiveShift_Vertical")


# Effects - Artistic
class SAC_PT_EFFECTS_Artistic_Panel(SAC_PT_Panel, Panel):
    bl_label = "Artistic Effects"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ARMATURE_DATA")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings


# Oil Paint
class SAC_PT_EFFECTS_OilPaint_Panel(SAC_PT_Panel, Panel):
    bl_label = "Oil Paint (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Artistic_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_FLUIDSIM")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="Coming soon")


# Sketch
class SAC_PT_EFFECTS_Sketch_Panel(SAC_PT_Panel, Panel):
    bl_label = "Sketch (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Artistic_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="GREASEPENCIL")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="Coming soon")


# Watercolor
class SAC_PT_EFFECTS_Watercolor_Panel(SAC_PT_Panel, Panel):
    bl_label = "Watercolor (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Artistic_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="BRUSHES_ALL")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="Coming soon")


# Pointillism
class SAC_PT_EFFECTS_Pointillism_Panel(SAC_PT_Panel, Panel):
    bl_label = "Pointillism (coming soon)"
    bl_parent_id = "SAC_PT_EFFECTS_Artistic_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_OB_LIGHTPROBE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect is very resource demanding, it might not get viewport support")


# Camera
class SAC_PT_CAMERA_Panel(SAC_PT_Panel, Panel):
    bl_label = "Camera"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_DATA_CAMERA")

    def draw(self, context: Context):
        layout = self.layout


# Tilt Shift
class SAC_PT_CAMERA_TiltShift_Panel(SAC_PT_Panel, Panel):
    bl_label = "Tilt Shift (coming soon)"
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_LATTICE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect will most likely be done through camera settings")
