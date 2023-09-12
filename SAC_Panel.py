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

from bpy.types import (
    Context,
    Panel,
)

from .SAC_Settings import SAC_Settings
from .SAC_Operators import SAC_OT_Initialize
from .SAC_List import SAC_EffectList, SAC_UL_List


def active_effect_update(self, context):
    settings = context.scene.sac_settings
    # using the index, we can get the item from the list
    item = context.scene.sac_effect_list[self.sac_effect_list_index]
    node_name = f"{item.EffectGroup}_{item.ID}"
    node_group_name = f".{node_name}"
    # Bokeh
    if item.EffectGroup == "SAC_BOKEH":
        settings.Effects_Bokeh_MaxSize = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Blur"].blur_max
        settings.Effects_Bokeh_Range = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Range"].inputs[1].default_value
        settings.Effects_Bokeh_Offset = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Offset"].inputs[1].default_value
        settings.Effects_Bokeh_Rotation = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Rotation"].inputs[1].default_value
    # Chromatic Aberration
    elif item.EffectGroup == "SAC_CHROMATICABERRATION":
        settings.Effects_ChromaticAberration_Amount = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ChromaticAberration"].inputs[2].default_value
    # Duotone
    elif item.EffectGroup == "SAC_DUOTONE":
        # Color 1
        settings.Effects_Duotone_Color1[0] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[0]
        settings.Effects_Duotone_Color1[1] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[1]
        settings.Effects_Duotone_Color1[2] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[2]
        # Color 2
        settings.Effects_Duotone_Color2[0] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[0]
        settings.Effects_Duotone_Color2[1] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[1]
        settings.Effects_Duotone_Color2[2] = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[2]
        # Blend
        settings.Effects_Duotone_Blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Blend"].inputs[0].default_value
    # Emboss
    elif item.EffectGroup == "SAC_EMBOSS":
        settings.Effects_Emboss_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Emboss"].inputs[0].default_value
    # Film Grain
    elif item.EffectGroup == "SAC_FILMGRAIN":
        settings.Filmgrain_strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Strength"].inputs[0].default_value
        settings.Filmgrain_dustproportion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].sigma_color
        settings.Filmgrain_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].iterations
    # Fish Eye
    elif item.EffectGroup == "SAC_FISHEYE":
        settings.Effects_Fisheye = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Fisheye"].inputs[1].default_value
    # Fog Glow
    elif item.EffectGroup == "SAC_FOGGLOW":
        settings.Effects_FogGlow_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlowStrength"].inputs[0].default_value
        settings.Effects_FogGlow_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].threshold
        settings.Effects_FogGlow_Size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].size
    # Ghost
    elif item.EffectGroup == "SAC_GHOST":
        settings.Effects_Ghosts_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GhostsStrength"].inputs[0].default_value
        settings.Effects_Ghosts_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].threshold
        settings.Effects_Ghosts_Count = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].iterations
        settings.Effects_Ghosts_Distortion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].color_modulation
    # Gradient Map
    elif item.EffectGroup == "SAC_GRADIENTMAP":
        settings.Effects_GradientMap_blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap_Mix"].inputs[0].default_value
    # Halftone
    elif item.EffectGroup == "SAC_HALFTONE":
        settings.Effects_Halftone_value = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Value"].outputs[0].default_value
        settings.Effects_Halftone_delta = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Delta"].outputs[0].default_value
        settings.Effects_Halftone_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_SizeSave"].outputs[0].default_value
    # Infrared
    elif item.EffectGroup == "SAC_INFRARED":
        settings.Effects_Infrared_Blend = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Mix"].inputs[0].default_value
        settings.Effects_Infrared_Offset = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Add"].inputs[1].default_value
    # ISO Noise
    elif item.EffectGroup == "SAC_ISONOISE":
        settings.ISO_strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Add"].inputs[0].default_value
        settings.ISO_size = bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Despeckle"].inputs[0].default_value
    # Mosaic
    elif item.EffectGroup == "SAC_MOSAIC":
        settings.Effects_Pixelate_PixelSize = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Pixelate_Size"].inputs[0].default_value
    # Negative
    elif item.EffectGroup == "SAC_NEGATIVE":
        settings.Effects_Negative = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Negative"].inputs[0].default_value
    # Overlay
    elif item.EffectGroup == "SAC_OVERLAY":
        settings.Effects_Overlay_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay"].inputs[0].default_value
    # Perspective Shift
    elif item.EffectGroup == "SAC_PERSPECTIVESHIFT":
        if bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] > 0:
            settings.Effects_PerspectiveShift_Horizontal = bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] * 2
        else:
            settings.Effects_PerspectiveShift_Horizontal = -bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[0] * 2

        if bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] > 0:
            settings.Effects_PerspectiveShift_Vertical = bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] * 2
        else:
            settings.Effects_PerspectiveShift_Vertical = -bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[1] * 2
    # Posterize
    elif item.EffectGroup == "SAC_POSTERIZE":
        settings.Effects_Posterize_Steps = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Posterize"].inputs[1].default_value
    # Streaks
    elif item.EffectGroup == "SAC_STREAKS":
        settings.Effects_Streaks_Strength = bpy.data.node_groups[node_group_name].nodes["SAC Effects_StreaksStrength"].inputs[0].default_value
        settings.Effects_Streaks_Threshold = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].threshold
        settings.Effects_Streaks_Count = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].streaks
        settings.Effects_Streaks_Length = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].iterations
        settings.Effects_Streaks_Fade = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].fade
        settings.Effects_Streaks_Angle = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].angle_offset
        settings.Effects_Streaks_Distortion = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].color_modulation
    # Vignette
    elif item.EffectGroup == "SAC_VIGNETTE":
        settings.Effects_Vignette_Intensity = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Intensity"].inputs[0].default_value
        settings.Effects_Vignette_Roundness = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Roundness"].inputs[0].default_value
        settings.Effects_Vignette_Feather = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Directional_Blur"].zoom
        settings.Effects_Vignette_Midpoint = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Midpoint"].inputs[0].default_value
    # Warp
    elif item.EffectGroup == "SAC_WARP":
        settings.Effects_Warp = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Warp"].zoom


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

# region ColorGrade
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
# endregion ColorGrade

# region Effects
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


# Effects - List
class SAC_PT_List(SAC_PT_Panel, Panel):
    bl_label = "Effect List"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="LONGDISPLAY")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout = self.layout
        layout.template_icon_view(context.scene, "new_item_type", show_labels=True, scale=8.0, scale_popup=8.0)

        row = layout.row()
        row.template_list("SAC_UL_List", "", scene, "sac_effect_list", scene, "sac_effect_list_index")

        col = row.column(align=True)
        col.scale_x = 1  # Set a fixed width
        col.operator("sac_effect_list.add_effect", text="", icon='ADD')
        col.operator("sac_effect_list.remove_effect", text="", icon='REMOVE')
        col.separator()
        col.operator("sac_effect_list.move_effect_up", text="", icon='TRIA_UP')
        col.operator("sac_effect_list.move_effect_down", text="", icon='TRIA_DOWN')


# Effects - Color
class SAC_PT_EFFECTS_Color_Panel(SAC_PT_Panel, Panel):
    bl_label = "Effect Properties"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="PROPERTIES")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        if item is None:
            return
        node_group_name = f".{item.EffectGroup}_{item.ID}"

        if item is not None:
            layout.label(text=f"These are settings for {item.name}.")
            # Bokah
            if item.EffectGroup == "SAC_BOKEH":
                # warning that this effect is not viewport compatible
                layout.label(text="This effect is not viewport compatible.", icon="ERROR")
                layout.prop(settings, "Effects_Bokeh_MaxSize")
                layout.prop(settings, "Effects_Bokeh_Offset")
                layout.prop(settings, "Effects_Bokeh_Range")
                layout.prop(settings, "Effects_Bokeh_Rotation")
                layout.label(text="Custom Bokeh")
                bokeh_image = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Image"]
                layout.template_ID(bokeh_image, "image", open="image.open")
            # Chromatic Aberration
            elif item.EffectGroup == "SAC_CHROMATICABERRATION":
                layout.prop(settings, "Effects_ChromaticAberration_Amount")
            # Duotone
            elif item.EffectGroup == "SAC_DUOTONE":
                layout.prop(settings, "Effects_Duotone_Color1")
                layout.prop(settings, "Effects_Duotone_Color2")
                layout.prop(settings, "Effects_Duotone_Blend")
            # Emboss
            elif item.EffectGroup == "SAC_EMBOSS":
                layout.prop(settings, "Effects_Emboss_Strength")
            # Film Grain
            elif item.EffectGroup == "SAC_FILMGRAIN":
                layout.prop(settings, "Filmgrain_strength")
                layout.prop(settings, "Filmgrain_dustproportion")
                layout.prop(settings, "Filmgrain_size")
            # Fish Eye
            elif item.EffectGroup == "SAC_FISHEYE":
                layout.prop(settings, "Effects_Fisheye")
            # Fog Glow
            elif item.EffectGroup == "SAC_FOGGLOW":
                layout.prop(settings, "Effects_FogGlow_Strength")
                layout.prop(settings, "Effects_FogGlow_Threshold")
                layout.prop(settings, "Effects_FogGlow_Size")
            # Ghost
            elif item.EffectGroup == "SAC_GHOST":
                layout.prop(settings, "Effects_Ghosts_Strength")
                layout.prop(settings, "Effects_Ghosts_Threshold")
                layout.prop(settings, "Effects_Ghosts_Count")
                layout.prop(settings, "Effects_Ghosts_Distortion")
            # Gradient Map
            elif item.EffectGroup == "SAC_GRADIENTMAP":
                gradient_map_node = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap"]
                layout.template_color_ramp(gradient_map_node, "color_ramp")
                layout.prop(settings, "Effects_GradientMap_blend")
            # Halftone
            elif item.EffectGroup == "SAC_HALFTONE":
                layout.prop(settings, "Effects_Halftone_value")
                layout.prop(settings, "Effects_Halftone_delta")
                layout.prop(settings, "Effects_Halftone_size")
            # Infrared
            elif item.EffectGroup == "SAC_INFRARED":
                layout.prop(settings, "Effects_Infrared_Blend")
                layout.prop(settings, "Effects_Infrared_Offset")
            # ISO Noise
            elif item.EffectGroup == "SAC_ISONOISE":
                layout.prop(settings, "ISO_strength")
                layout.prop(settings, "ISO_size")
            # Mosaic
            elif item.EffectGroup == "SAC_MOSAIC":
                layout.prop(settings, "Effects_Pixelate_PixelSize")
            # Negative
            elif item.EffectGroup == "SAC_NEGATIVE":
                layout.prop(settings, "Effects_Negative")
            # Overlay
            elif item.EffectGroup == "SAC_OVERLAY":
                overlay_texture = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay_Texture"]
                layout.template_ID(overlay_texture, "image", open="image.open")
                layout.prop(settings, "Effects_Overlay_Strength")
            # Perspective Shift
            elif item.EffectGroup == "SAC_PERSPECTIVESHIFT":
                layout.prop(settings, "Effects_PerspectiveShift_Horizontal")
                layout.prop(settings, "Effects_PerspectiveShift_Vertical")
            # Posterize
            elif item.EffectGroup == "SAC_POSTERIZE":
                layout.prop(settings, "Effects_Posterize_Steps")
            # Streaks
            elif item.EffectGroup == "SAC_STREAKS":
                layout.prop(settings, "Effects_Streaks_Strength")
                layout.prop(settings, "Effects_Streaks_Threshold")
                layout.prop(settings, "Effects_Streaks_Count")
                layout.prop(settings, "Effects_Streaks_Length")
                layout.prop(settings, "Effects_Streaks_Fade")
                layout.prop(settings, "Effects_Streaks_Angle")
                layout.prop(settings, "Effects_Streaks_Distortion")
            # Vignette
            elif item.EffectGroup == "SAC_VIGNETTE":
                layout.prop(settings, "Effects_Vignette_Intensity")
                layout.prop(settings, "Effects_Vignette_Roundness")
                layout.prop(settings, "Effects_Vignette_Feather")
                layout.prop(settings, "Effects_Vignette_Midpoint")
            # Warp
            elif item.EffectGroup == "SAC_WARP":
                layout.prop(settings, "Effects_Warp")
            # Error
            else:
                layout.label(text="Oops, that's not supposed to happen.")
                layout.label(text=f"Effect: {item.EffectGroup} was selected.")
                layout.label(text="Please report this to us.")
                layout.operator("wm.url_open", text="Our Discord", icon="URL").url = "https://discord.gg/cnFdGQP"
        else:
            layout.label(text="No item selected.")


# endregion Effects

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

        layout.prop(settings, "Camera_TiltShift_AmountX")
        layout.prop(settings, "Camera_TiltShift_AmountY")
        layout.label(text="(it's buggy and I don't know how to do it properly)")

# Bokeh


class SAC_PT_CAMERA_Bokeh_Panel(SAC_PT_Panel, Panel):
    bl_label = "Bokeh (coming soon)"
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="ANTIALIASED")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        layout.label(text="This effect is very resource demanding, it might not get viewport support")
