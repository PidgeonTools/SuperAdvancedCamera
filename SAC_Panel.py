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
        layout.prop(settings, "Colorgrade_Color_WhiteBalance")
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
    bl_label = "Effects (coming soon)"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.operator("wm.url_open", text="Submit your requests", icon="URL").url = "https://go.pidgeontools.com/2023-08-29-sac-survey"


class SAC_PT_EFFECTS_Duotone_Panel(SAC_PT_Panel, Panel):
    bl_label = "Duotone"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="COLOR")

    def draw(self, context: Context):
        layout = self.layout
        SAC_Settings = context.scene.sac_settings

        layout.prop(SAC_Settings, "Effects_Duotone_Color1")
        layout.prop(SAC_Settings, "Effects_Duotone_Color2")
        layout.prop(SAC_Settings, "Effects_Duotone_Blend")
