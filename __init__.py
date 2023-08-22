bl_info = {
    "name": "Super Advanced Compositor",
    "author": "Kevin Lorengel, Slinc",
    "version": (0, 0, 1),
    "blender": (3, 6, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Compositor",
}


import bpy
from bpy.types import (
    Context,
    Panel,
)
from bpy.types import Operator


# # # S E T T I N G S # # #

from bpy.types import (
    PropertyGroup,
)
from bpy.props import (
    EnumProperty,
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    StringProperty,
    BoolProperty
)

class SAC_Settings(PropertyGroup):

    # COLOR
    Colorgrade_Color_WhiteBalance: FloatVectorProperty(
        name="White Balance",
        min=0.0,
        max=1.0,
        default=(1.0,1.0,1.0),
        subtype="COLOR",
    )

    Colorgrade_Color_Temperature: FloatProperty(
        name="Temperature",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Color_Tint: FloatProperty(
        name="Tint",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Color_Saturation: FloatProperty(
        name="Saturation",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    # LIGHT

    Colorgrade_Light_Exposure: FloatProperty(
        name="Exposure",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Light_Contrast: FloatProperty(
        name="Contrast",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Light_Highlights: FloatProperty(
        name="Highlights",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Light_Shadows: FloatProperty(
        name="Shadows",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Light_Whites: FloatProperty(
        name="Whites",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    Colorgrade_Light_Blacks: FloatProperty(
        name="Blacks",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR"
    )

    # Presets

    Colorgrade_Presets_Presets: EnumProperty(
        name="Presets",
        items=(
            (
                'DEFAULT',
                'Default',
                'Unchanged Image'
            ),
            (
                'SEPIA',
                'Sepia',
                'Sepia Preset applied'
            ),
        ),
        default='DEFAULT'
        )

    Colorgrade_Presets_Intensity: FloatProperty(
        name="Intensity",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )

    Colorgrade_Presets_FadedFilm: FloatProperty(
        name="Faded Film",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )

    Colorgrade_Presets_Sharpen: FloatProperty(
        name="Sharpen",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )

    Colorgrade_Presets_Vibrance: FloatProperty(
        name="Vibrance",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )

    Colorgrade_Presets_Saturation: FloatProperty(
        name="Saturation",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )

    Colorgrade_Presets_HighlightTint: FloatVectorProperty(
        name="Highlight Tint",
        min=0.0,
        max=1.0,
        default=(1.0,1.0,1.0),
        subtype="COLOR",
    )

    Colorgrade_Presets_ShadowTint: FloatVectorProperty(
        name="Shadow Tint",
        min=0.0,
        max=1.0,
        default=(1.0,1.0,1.0),
        subtype="COLOR",
    )

    Colorgrade_Presets_Intensity: FloatProperty(
        name="Tint Balance",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR"
    )


# # # P A N E L # # #

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
        layout.separator

# Colorgrade
class SAC_PT_COLORGRADE_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color Grading"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

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
        layout.separator
        layout.prop(settings, "Colorgrade_Presets_Presets")
        layout.prop(settings, "Colorgrade_Presets_FadedFilm")
        layout.prop(settings, "Colorgrade_Presets_Sharpen")
        layout.prop(settings, "Colorgrade_Presets_Vibrance")
        layout.prop(settings, "Colorgrade_Presets_Saturation")
        layout.prop(settings, "Colorgrade_Presets_HighlightTint")
        layout.prop(settings, "Colorgrade_Presets_ShadowTint")
        layout.prop(settings, "Colorgrade_Presets_TintBalance")

# Colorgrade - Curves
class SAC_PT_COLORGRADE_Curves_Panel(SAC_PT_Panel, Panel):
    bl_label = "Curves"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Colorgrade - Colorwheels
class SAC_PT_COLORGRADE_Colorwheels_Panel(SAC_PT_Panel, Panel):
    bl_label = "Colorwheels"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Colorgrade - HSL Secondary
class SAC_PT_COLORGRADE_HSLSecondary_Panel(SAC_PT_Panel, Panel):
    bl_label = "HSL Secondary"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Colorgrade - HSL Secondary - Key
class SAC_PT_COLORGRADE_HSLSecondary_Key_Panel(SAC_PT_Panel, Panel):
    bl_label = "Key"
    bl_parent_id = "SAC_PT_COLORGRADE_HSLSecondary_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Colorgrade - HSL Secondary - Refine
class SAC_PT_COLORGRADE_HSLSecondary_Refine_Panel(SAC_PT_Panel, Panel):
    bl_label = "Refine"
    bl_parent_id = "SAC_PT_COLORGRADE_HSLSecondary_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Colorgrade - HSL Secondary - Correction
class SAC_PT_COLORGRADE_HSLSecondary_Correction_Panel(SAC_PT_Panel, Panel):
    bl_label = "Key"
    bl_parent_id = "SAC_PT_COLORGRADE_HSLSecondary_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator

# Effects
class SAC_PT_EFFECTS_Panel(SAC_PT_Panel, Panel):
    bl_label = "Effects"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout
        layout.separator


# Registration

classes = (
    SAC_PT_SAC_Panel,
    SAC_PT_COLORGRADE_Panel,
    SAC_PT_COLORGRADE_Color_Panel,
    SAC_PT_COLORGRADE_Light_Panel,
    SAC_PT_COLORGRADE_Presets_Panel,
    SAC_PT_COLORGRADE_Curves_Panel,
    SAC_PT_COLORGRADE_Colorwheels_Panel,
    SAC_PT_COLORGRADE_HSLSecondary_Panel,
    SAC_PT_COLORGRADE_HSLSecondary_Key_Panel,
    SAC_PT_COLORGRADE_HSLSecondary_Refine_Panel,
    SAC_PT_COLORGRADE_HSLSecondary_Correction_Panel,
    SAC_PT_EFFECTS_Panel,

    SAC_Settings
    )

def register():
    # register the example panel, to show updater buttons
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.sac_settings = bpy.props.PointerProperty(type=SAC_Settings)

def unregister():
    # register the example panel, to show updater buttons
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.sac_settings


if __name__ == "__main__":
    register()
