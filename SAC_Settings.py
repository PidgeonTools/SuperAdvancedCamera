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
    PropertyGroup,
)

from bpy.props import (
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
    IntProperty,
    BoolProperty,
    PointerProperty,
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

        if settings.Colorgrade_Color_Temperature == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Temperature"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Temperature"].mute = False

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

        if settings.Colorgrade_Color_Tint == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Tint"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Tint"].mute = False

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

        if (settings.Colorgrade_Color_Saturation == 1) and (settings.Colorgrade_Color_Hue == 0.5):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = False

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

        if (settings.Colorgrade_Color_Hue == 0.5) and (settings.Colorgrade_Color_Saturation == 1):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = False

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

        if settings.Colorgrade_Light_Exposure == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Exposure"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Exposure"].mute = False

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

        if settings.Colorgrade_Light_Contrast == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Contrast"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Contrast"].mute = False

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

        if settings.Colorgrade_Light_Highlights == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Highlights"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Highlights"].mute = False

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

        if settings.Colorgrade_Light_Shadows == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Shadows"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Shadows"].mute = False

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

        if settings.Colorgrade_Light_Whites == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Whites"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Whites"].mute = False

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

        if settings.Colorgrade_Light_Darks == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Darks"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Darks"].mute = False

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

        if settings.Colorgrade_Presets_Sharpen == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Sharpen"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Sharpen"].mute = False

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

        if settings.Colorgrade_Presets_Vibrance == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Vibrance"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Vibrance"].mute = False

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
        bpy.data.node_groups[".SAC Saturation2"].nodes["SAC Colorgrade_Presets_Saturation"].inputs[2].default_value = settings.Colorgrade_Presets_Saturation

        if settings.Colorgrade_Presets_Saturation == 1:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation2"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation2"].mute = False

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
        bpy.data.node_groups[".SAC HighlightTint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[0] = settings.Colorgrade_Presets_HighlightTint[0]
        bpy.data.node_groups[".SAC HighlightTint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[1] = settings.Colorgrade_Presets_HighlightTint[1]
        bpy.data.node_groups[".SAC HighlightTint"].nodes["SAC Colorgrade_Presets_HighlightTint"].inputs[2].default_value[2] = settings.Colorgrade_Presets_HighlightTint[2]

        if (
            settings.Colorgrade_Presets_HighlightTint[0] == 1 and
            settings.Colorgrade_Presets_HighlightTint[1] == 1 and
            settings.Colorgrade_Presets_HighlightTint[2] == 1
        ):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC HighlightTint"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC HighlightTint"].mute = False

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
        bpy.data.node_groups[".SAC ShadowTint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[0] = settings.Colorgrade_Presets_ShadowTint[0]
        bpy.data.node_groups[".SAC ShadowTint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[1] = settings.Colorgrade_Presets_ShadowTint[1]
        bpy.data.node_groups[".SAC ShadowTint"].nodes["SAC Colorgrade_Presets_ShadowTint"].inputs[2].default_value[2] = settings.Colorgrade_Presets_ShadowTint[2]

        if (
            settings.Colorgrade_Presets_ShadowTint[0] == 1 and
            settings.Colorgrade_Presets_ShadowTint[1] == 1 and
            settings.Colorgrade_Presets_ShadowTint[2] == 1
        ):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ShadowTint"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ShadowTint"].mute = False

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
    def update_Effects_DuotoneColor1(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[0] = settings.Effects_Duotone_Color1[0]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[1] = settings.Effects_Duotone_Color1[1]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[2] = settings.Effects_Duotone_Color1[2]

    Effects_Duotone_Color1: FloatVectorProperty(
        name="Color 1",
        min=0.0,
        max=1.0,
        default=(0.01, 0.01, 0.17),
        subtype="COLOR",
        update=update_Effects_DuotoneColor1
    )

    def update_Effects_DuotoneColor2(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[0] = settings.Effects_Duotone_Color2[0]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[1] = settings.Effects_Duotone_Color2[1]
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[2] = settings.Effects_Duotone_Color2[2]

    Effects_Duotone_Color2: FloatVectorProperty(
        name="Color 2",
        min=0.0,
        max=1.0,
        default=(1.0, 0.56, 0.06),
        subtype="COLOR",
        update=update_Effects_DuotoneColor2
    )

    def update_Effects_DuotoneBlend(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Duotone"].nodes["SAC Effects_Duotone_Blend"].inputs[0].default_value = settings.Effects_Duotone_Blend

        if settings.Effects_Duotone_Blend == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Duotone"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Duotone"].mute = False

    Effects_Duotone_Blend: FloatProperty(
        name="Blend",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_DuotoneBlend
    )

    # Glare

    # Fog Glow
    def update_Effects_Glare_FogGlow_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_FogGlow"].threshold = settings.Effects_Glare_FogGlow_Threshold

    Effects_Glare_FogGlow_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_Glare_FogGlow_Threshold
    )

    def update_Effects_Glare_FogGlow_Size(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_FogGlow"].size = settings.Effects_Glare_FogGlow_Size + 5

    Effects_Glare_FogGlow_Size: IntProperty(
        name="Size",
        default=2,
        max=4,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Glare_FogGlow_Size
    )

    def update_Effects_Glare_FogGlow_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_FogGlowStrength"].inputs[0].default_value = settings.Effects_Glare_FogGlow_Strength

        if settings.Effects_Glare_FogGlow_Strength == 0:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_FogGlowStrength"].mute = True
        else:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_FogGlowStrength"].mute = False

    Effects_Glare_FogGlow_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Glare_FogGlow_Strength
    )
    # Streaks

    def update_Effects_Glare_Streaks_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].threshold = settings.Effects_Glare_Streaks_Threshold

    Effects_Glare_Streaks_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_Glare_Streaks_Threshold
    )

    def update_Effects_Glare_Streaks_Count(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].streaks = settings.Effects_Glare_Streaks_Count

    Effects_Glare_Streaks_Count: IntProperty(
        name="Count",
        default=6,
        max=16,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Glare_Streaks_Count
    )

    def update_Effects_Glare_Streaks_Angle(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].angle_offset = settings.Effects_Glare_Streaks_Angle

    Effects_Glare_Streaks_Angle: FloatProperty(
        name="Angle",
        default=0.1963495,  # 11.25 degrees
        max=3.1415,  # 180 degrees
        min=0,
        subtype="ANGLE",
        update=update_Effects_Glare_Streaks_Angle
    )

    def update_Effects_Glare_Streaks_Distortion(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].color_modulation = settings.Effects_Glare_Streaks_Distortion

    Effects_Glare_Streaks_Distortion: FloatProperty(
        name="Distortion",
        default=0.25,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Glare_Streaks_Distortion
    )

    def update_Effects_Glare_Streaks_Fade(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].fade = settings.Effects_Glare_Streaks_Fade

    Effects_Glare_Streaks_Fade: FloatProperty(
        name="Fade",
        default=0.85,
        max=1,
        min=0.75,
        subtype="FACTOR",
        update=update_Effects_Glare_Streaks_Fade
    )

    def update_Effects_Glare_Streaks_Length(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Streaks"].iterations = settings.Effects_Glare_Streaks_Length + 1

    Effects_Glare_Streaks_Length: IntProperty(
        name="Length",
        default=2,
        max=4,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Glare_Streaks_Length
    )

    def update_Effects_Glare_Streaks_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_StreaksStrength"].inputs[0].default_value = settings.Effects_Glare_Streaks_Strength

        if settings.Effects_Glare_Streaks_Strength == 0:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_StreaksStrength"].mute = True
        else:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_StreaksStrength"].mute = False

    Effects_Glare_Streaks_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Glare_Streaks_Strength
    )

    # Ghosts

    def update_Effects_Glare_Ghosts_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Ghosts"].threshold = settings.Effects_Glare_Ghosts_Threshold

    Effects_Glare_Ghosts_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_Glare_Ghosts_Threshold
    )

    def update_Effects_Glare_Ghosts_Distortion(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Ghosts"].color_modulation = settings.Effects_Glare_Ghosts_Distortion

    Effects_Glare_Ghosts_Distortion: FloatProperty(
        name="Distortion",
        default=0.1,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Glare_Ghosts_Distortion
    )

    def update_Effects_Glare_Ghosts_Count(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_Ghosts"].iterations = settings.Effects_Glare_Ghosts_Count

    Effects_Glare_Ghosts_Count: IntProperty(
        name="Count",
        default=3,
        max=5,
        min=2,
        subtype="FACTOR",
        update=update_Effects_Glare_Ghosts_Count
    )

    def update_Effects_Glare_Ghosts_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_GhostsStrength"].inputs[0].default_value = settings.Effects_Glare_Ghosts_Strength

        if settings.Effects_Glare_Ghosts_Strength == 0:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_GhostsStrength"].mute = True
        else:
            bpy.data.node_groups[".SAC Glare"].nodes["SAC Effects_GhostsStrength"].mute = False

    Effects_Glare_Ghosts_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Glare_Ghosts_Strength
    )

    # Emboss

    def update_Effects_Emboss_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Emboss"].nodes["SAC Effects_Emboss"].inputs[0].default_value = settings.Effects_Emboss_Strength

        if settings.Effects_Emboss_Strength == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Emboss"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Emboss"].mute = False

    Effects_Emboss_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Emboss_Strength
    )

    # Posterize

    def update_Effects_Posterize_Steps(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Posterize"].nodes["SAC Effects_Posterize"].inputs[1].default_value = settings.Effects_Posterize_Steps
        settings.Effects_Posterize_Toggle = True

    Effects_Posterize_Steps: FloatProperty(
        name="Steps",
        default=128,
        max=1024,
        soft_max=256,
        min=2,
        subtype="FACTOR",
        update=update_Effects_Posterize_Steps
    )

    def update_Effects_Posterize_Toggle(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings

        if settings.Effects_Posterize_Toggle == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Posterize"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Posterize"].mute = False

    Effects_Posterize_Toggle: BoolProperty(
        name="Enabled",
        default=False,
        update=update_Effects_Posterize_Toggle
    )

    # Overlay

    def update_Effects_Overlay_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Overlay"].nodes["SAC Effects_Overlay"].inputs[0].default_value = settings.Effects_Overlay_Strength

        if settings.Effects_Overlay_Strength == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Overlay"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Overlay"].mute = False

    Effects_Overlay_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Overlay_Strength
    )

    # Pixelate

    def update_Effects_Pixelate_PixelSize(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Pixelate"].nodes["SAC Effects_Pixelate_Size"].inputs[0].default_value = settings.Effects_Pixelate_PixelSize

        if settings.Effects_Pixelate_PixelSize == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Pixelate"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Pixelate"].mute = False

    Effects_Pixelate_PixelSize: FloatProperty(
        name="Pixel Size",
        default=0,
        max=100,
        soft_max=25,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Pixelate_PixelSize
    )

    # Chromatic Aberration

    def update_Effects_ChromaticAberration_Amount(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC ChromaticAberration"].nodes["SAC Effects_ChromaticAberration"].inputs[2].default_value = settings.Effects_ChromaticAberration_Amount
        bpy.data.node_groups[".SAC ChromaticAberration"].nodes["SAC Effects_ChromaticAberration"].inputs[1].default_value = -settings.Effects_ChromaticAberration_Amount/3.5

        if settings.Effects_ChromaticAberration_Amount == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ChromaticAberration"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ChromaticAberration"].mute = False

    Effects_ChromaticAberration_Amount: FloatProperty(
        name="Amount",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_ChromaticAberration_Amount
    )

    # Vignette
    # Intensity
    def update_Effects_Vignette_Intensity(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Intensity"].inputs[0].default_value = settings.Effects_Vignette_Intensity

        if settings.Effects_Vignette_Intensity == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Viginette"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Viginette"].mute = False

    Effects_Vignette_Intensity: FloatProperty(
        name="Intensity",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Vignette_Intensity
    )

    # Roundness
    def update_Effects_Vignette_Roundness(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Roundness"].inputs[0].default_value = settings.Effects_Vignette_Roundness

    Effects_Vignette_Roundness: FloatProperty(
        name="Roundness",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Vignette_Roundness
    )

    # Feather
    def update_Effects_Vignette_Feather(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Directional_Blur"].zoom = settings.Effects_Vignette_Feather
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Midpoint"].inputs[3].default_value = -settings.Effects_Vignette_Feather/4
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Midpoint"].inputs[1].default_value = -0.999-settings.Effects_Vignette_Feather/4

        feather_value = settings.Effects_Vignette_Feather
        node_to_update = bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Directional_Blur"]

        if feather_value <= 0.05:
            node_to_update.iterations = 4
        elif feather_value <= 0.2:
            node_to_update.iterations = 5
        elif feather_value <= 0.4:
            node_to_update.iterations = 6
        else:  # feather_value > 0.4
            node_to_update.iterations = 7

    Effects_Vignette_Feather: FloatProperty(
        name="Feather",
        default=0.25,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Vignette_Feather
    )

    # Midpoint
    def update_Effects_Vignette_Midpoint(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Viginette"].nodes["SAC Effects_Viginette_Midpoint"].inputs[0].default_value = settings.Effects_Vignette_Midpoint

    Effects_Vignette_Midpoint: FloatProperty(
        name="Midpoint",
        default=0,
        max=1,
        min=-0.998,
        subtype="FACTOR",
        update=update_Effects_Vignette_Midpoint
    )
