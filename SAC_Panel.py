import bpy

from bpy.types import (
    Context,
    Panel,
)

from . import (
    SAC_Settings
)

# Main
class SAC_PT_Panel:
    bl_label = "Super Advanced Compositor"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {"DEFAULT_CLOSED"}

class SAC_PT_SAC_Panel(SAC_PT_Panel, Panel):
    bl_label = "Super Advanced Compositor"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="SHADERFX")

    def draw(self, context: Context):
        layout = self.layout

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
        layout.prop(settings, "Colorgrade_Light_Blacks")

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

        rgb_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC RGB Curves"]
        hsv_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC HSV Curves"]

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
        layout.alignment="CENTER"
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
    bl_label = "Effects (comming soon)"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
