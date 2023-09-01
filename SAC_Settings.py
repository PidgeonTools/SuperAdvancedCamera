import bpy

from bpy.types import (
    PropertyGroup,
)

from bpy.props import (
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
)


class SAC_Settings(PropertyGroup):

    # COLOR
    Colorgrade_Color_WhiteBalance: FloatVectorProperty(
        name="White Balance",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
    )

    # Temperature
    def update_Colorgrade_Color_Temperature(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Temperature"].nodes["SAC Colorgrade_Color_Temperature"].inputs[0].default_value = settings.Colorgrade_Color_Temperature

    Colorgrade_Color_Temperature: FloatProperty(
        name="Temperature",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Color_Temperature
    )

    # Tint
    def update_Colorgrade_Color_Tint(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Tint"].nodes["SAC Colorgrade_Color_Tint"].inputs[0].default_value = settings.Colorgrade_Color_Tint

    Colorgrade_Color_Tint: FloatProperty(
        name="Tint",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Color_Tint
    )

    # Saturation
    def update_Colorgrade_Color_Saturation(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Saturation"].nodes["SAC Colorgrade_Color_Saturation"].inputs[2].default_value = settings.Colorgrade_Color_Saturation

    Colorgrade_Color_Saturation: FloatProperty(
        name="Saturation",
        default=1,
        max=2,
        min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Color_Saturation
    )

    # Hue1
    def update_Colorgrade_Color_Hue(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Saturation"].nodes["SAC Colorgrade_Color_Saturation"].inputs[1].default_value = settings.Colorgrade_Color_Hue

    Colorgrade_Color_Hue: FloatProperty(
        name="Hue",
        default=0.5,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Color_Hue
    )

    # LIGHT

    # Exposure
    def update_Colorgrade_Light_Exposure(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Exposure"].nodes["SAC Colorgrade_Light_Exposure"].inputs[1].default_value = settings.Colorgrade_Light_Exposure

    Colorgrade_Light_Exposure: FloatProperty(
        name="Exposure",
        default=0,
        max=10,
        soft_max=5,
        min=-10,
        soft_min=-5,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Exposure
    )

    # Contrast
    def update_Colorgrade_Light_Contrast(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Contrast"].nodes["SAC Colorgrade_Light_Contrast"].inputs[2].default_value = settings.Colorgrade_Light_Contrast

    Colorgrade_Light_Contrast: FloatProperty(
        name="Contrast",
        default=0,
        max=100,
        soft_max=25,
        min=-100,
        soft_min=-25,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Contrast
    )

    # Highlights
    def update_Colorgrade_Light_Highlights(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Highlights"].nodes["SAC Colorgrade_Light_Highlights"].inputs[0].default_value = settings.Colorgrade_Light_Highlights

    Colorgrade_Light_Highlights: FloatProperty(
        name="Highlights",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Highlights
    )

    # Shadows
    def update_Colorgrade_Light_Shadows(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Shadows"].nodes["SAC Colorgrade_Light_Shadows"].inputs[0].default_value = settings.Colorgrade_Light_Shadows

    Colorgrade_Light_Shadows: FloatProperty(
        name="Shadows",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Shadows
    )

    # Whites
    def update_Colorgrade_Light_Whites(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Whites"].nodes["SAC Colorgrade_Light_Whites"].inputs[0].default_value = settings.Colorgrade_Light_Whites

    Colorgrade_Light_Whites: FloatProperty(
        name="Whites",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Whites
    )

    # Darks
    def update_Colorgrade_Light_Darks(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Darks"].nodes["SAC Colorgrade_Light_Darks"].inputs[0].default_value = settings.Colorgrade_Light_Darks

    Colorgrade_Light_Darks: FloatProperty(
        name="Darks",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Light_Darks
    )

    # Presets

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

    # Sharpen
    def update_Colorgrade_Presets_Sharpen(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Sharpen"].nodes["SAC Colorgrade_Presets_Sharpen"].outputs[0].default_value = settings.Colorgrade_Presets_Sharpen

    Colorgrade_Presets_Sharpen: FloatProperty(
        name="Sharpen",
        default=0,
        max=5,
        soft_max=2,
        min=-5,
        soft_min=-2,
        subtype="FACTOR",
        update=update_Colorgrade_Presets_Sharpen
    )

    # Vibrance
    def update_Colorgrade_Presets_Vibrance(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Vibrance"].nodes["SAC Colorgrade_Presets_Vibrance"].inputs[2].default_value = settings.Colorgrade_Presets_Vibrance + 1

    Colorgrade_Presets_Vibrance: FloatProperty(
        name="Vibrance",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Presets_Vibrance
    )

    # Saturation
    def update_Colorgrade_Presets_Saturation(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups["..SAC Saturation2"].nodes["SAC Colorgrade_Presets_Saturation"].inputs[2].default_value = settings.Colorgrade_Presets_Saturation

    Colorgrade_Presets_Saturation: FloatProperty(
        name="Saturation",
        default=1,
        max=2,
        min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Presets_Saturation
    )

    # Highlight Tint
    def update_Colorgrade_Presets_HighlightTint(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Highlight Tint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[0] = settings.Colorgrade_Presets_HighlightTint[0]
        bpy.data.node_groups[".SAC Highlight Tint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[1] = settings.Colorgrade_Presets_HighlightTint[1]
        bpy.data.node_groups[".SAC Highlight Tint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[2] = settings.Colorgrade_Presets_HighlightTint[2]

    Colorgrade_Presets_HighlightTint: FloatVectorProperty(
        name="Highlight Tint",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
        update=update_Colorgrade_Presets_HighlightTint
    )

    # Shadow Tint
    def update_Colorgrade_Presets_ShadowTint(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Shadow Tint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[0] = settings.Colorgrade_Presets_ShadowTint[0]
        bpy.data.node_groups[".SAC Shadow Tint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[1] = settings.Colorgrade_Presets_ShadowTint[1]
        bpy.data.node_groups[".SAC Shadow Tint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[2] = settings.Colorgrade_Presets_ShadowTint[2]

    Colorgrade_Presets_ShadowTint: FloatVectorProperty(
        name="Shadow Tint",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
        update=update_Colorgrade_Presets_ShadowTint
    )

    # RGB Curves
    def update_Colorgrade_Curves_RGB_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_RGB"].inputs[0].default_value = settings.Colorgrade_Curves_RGB_Intensity

    Colorgrade_Curves_RGB_Intensity: FloatProperty(
        name="RGB Curves Intensity",
        default=1,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Curves_RGB_Intensity
    )

    # HSV Curves
    def update_Colorgrade_Curves_HSV_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_HSV"].inputs[0].default_value = settings.Colorgrade_Curves_HSV_Intensity

    Colorgrade_Curves_HSV_Intensity: FloatProperty(
        name="HSV Curves Intensity",
        default=1,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Curves_HSV_Intensity
    )

    # Colorwheel

    # Lift Brightness
    def update_Colorgrade_Colorwheel_Shadows_Brightness(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Shadows_Brightness"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Shadows_Brightness

    Colorgrade_Colorwheel_Shadows_Brightness: FloatProperty(
        name="Shadows Brightness",
        default=1,
        max=2,
        min=-2,
        soft_min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Shadows_Brightness
    )

    # Lift Intensity
    def update_Colorgrade_Colorwheel_Shadows_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Shadows"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Shadows_Intensity

    Colorgrade_Colorwheel_Shadows_Intensity: FloatProperty(
        name="Shadows Colorwheel Intensity",
        default=1,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Shadows_Intensity
    )

    # Gamma Brightness
    def update_Colorgrade_Colorwheel_Midtones_Brightness(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Midtones_Brightness"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Midtones_Brightness

    Colorgrade_Colorwheel_Midtones_Brightness: FloatProperty(
        name="Midtones Brightness",
        default=1,
        max=2,
        min=-2,
        soft_min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Midtones_Brightness
    )

    # Gamma Intensity
    def update_Colorgrade_Colorwheel_Midtones_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Midtones"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Midtones_Intensity

    Colorgrade_Colorwheel_Midtones_Intensity: FloatProperty(
        name="Midtones Colorwheel Intensity",
        default=1,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Midtones_Intensity
    )

    # Lift Brightness
    def update_Colorgrade_Colorwheel_Highlights_Brightness(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Highlights_Brightness"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Highlights_Brightness

    Colorgrade_Colorwheel_Highlights_Brightness: FloatProperty(
        name="Highlights Brightness",
        default=1,
        max=2,
        min=-2,
        soft_min=0,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Highlights_Brightness
    )

    # Lift Intensity
    def update_Colorgrade_Colorwheel_Highlights_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Highlights"].inputs[0].default_value = settings.Colorgrade_Colorwheel_Highlights_Intensity

    Colorgrade_Colorwheel_Highlights_Intensity: FloatProperty(
        name="Highlights Colorwheel Intensity",
        default=1,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Highlights_Intensity
    )

    # Duotone
    def update_Effects_Duotone(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Blend"].inputs[0].default_value = settings.Effects_Duotone_Blend
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[0] = settings.Effects_Duotone_Color1[0]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[1] = settings.Effects_Duotone_Color1[1]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[2] = settings.Effects_Duotone_Color1[2]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[0] = settings.Effects_Duotone_Color2[0]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[1] = settings.Effects_Duotone_Color2[1]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[2] = settings.Effects_Duotone_Color2[2]

    Effects_Duotone_Color1: FloatVectorProperty(
        name="Color 1",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
        update=update_Effects_Duotone
    )

    Effects_Duotone_Color2: FloatVectorProperty(
        name="Color 2",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
        update=update_Effects_Duotone
    )

    Effects_Duotone_Blend: FloatProperty(
        name="Blend",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Duotone
    )
