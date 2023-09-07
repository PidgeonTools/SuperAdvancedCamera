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
)


class SAC_Settings(PropertyGroup):

    # EffectTypes
    effect_types = [
        # Chromatic Aberration
        ('SAC_CHROMATICABERRATION', 'Chromatic Aberation', 'MOD_EDGESPLIT'),
        # Duotone
        ('SAC_DUOTONE', 'Duotone', 'MOD_TINT'),
        # Emboss
        ('SAC_EMBOSS', 'Emboss', 'AXIS_TOP'),
        # Filmgrain
        ('SAC_FILMGRAIN', 'Film Grain', 'ALIGN_FLUSH'),
        # Fish Eye
        ('SAC_FISHEYE', 'Fish Eye', 'MESH_UVSPHERE'),
        # Fog Glow
        ('SAC_FOGGLOW', 'Fog Glow', 'ALIGN_FLUSH'),
        # Ghost
        ('SAC_GHOST', 'Ghost', 'GHOST_DISABLED'),
        # Gradient Map
        ('SAC_GRADIENTMAP', 'Gradient Map', 'SNAP_INCREMENT'),
        # Halftone
        ('SAC_HALFTONE', 'Halftone', 'LIGHTPROBE_GRID'),
        # Infrared
        ('SAC_INFRARED', 'Infrared', 'OUTLINER_DATA_LIGHT'),
        # ISO Noise
        ('SAC_ISONOISE', 'ISO Noise', 'ALIGN_FLUSH'),
        # Mosaic
        ('SAC_MOSAIC', 'Mosaic', 'MOD_UVPROJECT'),
        # Negative
        ('SAC_NEGATIVE', 'Negative', 'SELECT_DIFFERENCE'),
        # Overlay
        ('SAC_OVERLAY', 'Overlay', 'XRAY'),
        # Perspective Shift
        ('SAC_PERSPECTIVESHIFT', 'Perspective Shift', 'VIEW_PERSPECTIVE'),
        # Posterize
        ('SAC_POSTERIZE', 'Posterize', 'IMAGE_ZDEPTH'),
        # Streaks
        ('SAC_STREAKS', 'Streaks', 'LIGHT_SUN'),
        # Vignette
        ('SAC_VIGNETTE', 'Vignette', 'CLIPUV_DEHLT'),
        # Warp
        ('SAC_WARP', 'Warp', 'MOD_WARP'),
    ]

    # region Colorgrade

    # White Level
    def update_Colorgrade_Color_WhiteLevel(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC WhiteLevel"].nodes["SAC Colorgrade_Color_WhiteLevel"].inputs[3].default_value[0] = settings.Colorgrade_Color_WhiteLevel[0]
        bpy.data.node_groups[".SAC WhiteLevel"].nodes["SAC Colorgrade_Color_WhiteLevel"].inputs[3].default_value[1] = settings.Colorgrade_Color_WhiteLevel[1]
        bpy.data.node_groups[".SAC WhiteLevel"].nodes["SAC Colorgrade_Color_WhiteLevel"].inputs[3].default_value[2] = settings.Colorgrade_Color_WhiteLevel[2]

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC WhiteLevel"].mute = False
        if (
            settings.Colorgrade_Color_WhiteLevel[0] == 1 and
            settings.Colorgrade_Color_WhiteLevel[1] == 1 and
            settings.Colorgrade_Color_WhiteLevel[2] == 1
        ):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC WhiteLevel"].mute = True

    Colorgrade_Color_WhiteLevel: FloatVectorProperty(
        name="White Balance",
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype="COLOR",
        update=update_Colorgrade_Color_WhiteLevel
    )

    # Temperature

    def update_Colorgrade_Color_Temperature(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        bpy.data.node_groups[".SAC Temperature"].nodes["SAC Colorgrade_Color_Temperature"].inputs[0].default_value = settings.Colorgrade_Color_Temperature

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Temperature"].mute = False
        if settings.Colorgrade_Color_Temperature == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Temperature"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Tint"].mute = False
        if settings.Colorgrade_Color_Tint == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Tint"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = False
        if (settings.Colorgrade_Color_Saturation == 1) and (settings.Colorgrade_Color_Hue == 0.5):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = False
        if (settings.Colorgrade_Color_Hue == 0.5) and (settings.Colorgrade_Color_Saturation == 1):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Exposure"].mute = False
        if settings.Colorgrade_Light_Exposure == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Exposure"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Contrast"].mute = False
        if settings.Colorgrade_Light_Contrast == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Contrast"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Highlights"].mute = False
        if settings.Colorgrade_Light_Highlights == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Highlights"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Shadows"].mute = False
        if settings.Colorgrade_Light_Shadows == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Shadows"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Whites"].mute = False
        if settings.Colorgrade_Light_Whites == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Whites"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Darks"].mute = False
        if settings.Colorgrade_Light_Darks == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Darks"].mute = True

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
        name="Presets (coming soon)",
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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Sharpen"].mute = False
        if settings.Colorgrade_Presets_Sharpen == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Sharpen"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Vibrance"].mute = False
        if settings.Colorgrade_Presets_Vibrance == 0:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Vibrance"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation2"].mute = False
        if settings.Colorgrade_Presets_Saturation == 1:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Saturation2"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC HighlightTint"].mute = False
        if (
            settings.Colorgrade_Presets_HighlightTint[0] == 1 and
            settings.Colorgrade_Presets_HighlightTint[1] == 1 and
            settings.Colorgrade_Presets_HighlightTint[2] == 1
        ):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC HighlightTint"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ShadowTint"].mute = False
        if (
            settings.Colorgrade_Presets_ShadowTint[0] == 1 and
            settings.Colorgrade_Presets_ShadowTint[1] == 1 and
            settings.Colorgrade_Presets_ShadowTint[2] == 1
        ):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC ShadowTint"].mute = True

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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Curves"].mute = False
        if (settings.Colorgrade_Curves_RGB_Intensity == 0) and (settings.Colorgrade_Curves_HSV_Intensity == 0):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Curves"].mute = True

    Colorgrade_Curves_RGB_Intensity: FloatProperty(
        name="RGB Curves Intensity",
        default=0,
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

        bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Curves"].mute = False
        if (settings.Colorgrade_Curves_RGB_Intensity == 0) and (settings.Colorgrade_Curves_HSV_Intensity == 0):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Curves"].mute = True

    Colorgrade_Curves_HSV_Intensity: FloatProperty(
        name="HSV Curves Intensity",
        default=0,
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

        if (settings.Colorgrade_Colorwheel_Highlights_Intensity == 0) and (settings.Colorgrade_Colorwheel_Midtones_Intensity == 0) and (settings.Colorgrade_Colorwheel_Shadows_Intensity == 0):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = False

    Colorgrade_Colorwheel_Shadows_Intensity: FloatProperty(
        name="Shadows Colorwheel Intensity",
        default=0,
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

        if (settings.Colorgrade_Colorwheel_Highlights_Intensity == 0) and (settings.Colorgrade_Colorwheel_Midtones_Intensity == 0) and (settings.Colorgrade_Colorwheel_Shadows_Intensity == 0):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = False

    Colorgrade_Colorwheel_Midtones_Intensity: FloatProperty(
        name="Midtones Colorwheel Intensity",
        default=0,
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

        if (settings.Colorgrade_Colorwheel_Highlights_Intensity == 0) and (settings.Colorgrade_Colorwheel_Midtones_Intensity == 0) and (settings.Colorgrade_Colorwheel_Shadows_Intensity == 0):
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = True
        else:
            bpy.data.node_groups["Super Advanced Camera"].nodes["SAC Colorwheel"].mute = False

    Colorgrade_Colorwheel_Highlights_Intensity: FloatProperty(
        name="Highlights Colorwheel Intensity",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Colorgrade_Colorwheel_Highlights_Intensity
    )

    # endregion Colorgrade

    # region Effects

    # Duotone
    def update_Effects_DuotoneColor1(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[0] = settings.Effects_Duotone_Color1[0]
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[1] = settings.Effects_Duotone_Color1[1]
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[1].default_value[2] = settings.Effects_Duotone_Color1[2]

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[0] = settings.Effects_Duotone_Color2[0]
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[1] = settings.Effects_Duotone_Color2[1]
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Colors"].inputs[2].default_value[2] = settings.Effects_Duotone_Color2[2]

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Duotone_Blend"].inputs[0].default_value = settings.Effects_Duotone_Blend

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Duotone_Blend == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Duotone_Blend: FloatProperty(
        name="Blend",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_DuotoneBlend
    )

    # Fog Glow
    def update_Effects_FogGlow_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].threshold = settings.Effects_FogGlow_Threshold

    Effects_FogGlow_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_FogGlow_Threshold
    )

    def update_Effects_FogGlow_Size(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlow"].size = settings.Effects_FogGlow_Size + 5

    Effects_FogGlow_Size: IntProperty(
        name="Size",
        default=2,
        max=4,
        min=1,
        subtype="FACTOR",
        update=update_Effects_FogGlow_Size
    )

    def update_Effects_FogGlow_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FogGlowStrength"].inputs[0].default_value = settings.Effects_FogGlow_Strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_FogGlow_Strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_FogGlow_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_FogGlow_Strength
    )
    # Streaks

    def update_Effects_Streaks_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].threshold = settings.Effects_Streaks_Threshold

    Effects_Streaks_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_Streaks_Threshold
    )

    def update_Effects_Streaks_Count(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].streaks = settings.Effects_Streaks_Count

    Effects_Streaks_Count: IntProperty(
        name="Count",
        default=6,
        max=16,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Streaks_Count
    )

    def update_Effects_Streaks_Angle(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].angle_offset = settings.Effects_Streaks_Angle

    Effects_Streaks_Angle: FloatProperty(
        name="Angle",
        default=0.1963495,  # 11.25 degrees
        max=3.1415,  # 180 degrees
        min=0,
        subtype="ANGLE",
        update=update_Effects_Streaks_Angle
    )

    def update_Effects_Streaks_Distortion(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].color_modulation = settings.Effects_Streaks_Distortion

    Effects_Streaks_Distortion: FloatProperty(
        name="Distortion",
        default=0.25,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Streaks_Distortion
    )

    def update_Effects_Streaks_Fade(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].fade = settings.Effects_Streaks_Fade

    Effects_Streaks_Fade: FloatProperty(
        name="Fade",
        default=0.85,
        max=1,
        min=0.75,
        subtype="FACTOR",
        update=update_Effects_Streaks_Fade
    )

    def update_Effects_Streaks_Length(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Streaks"].iterations = settings.Effects_Streaks_Length + 1

    Effects_Streaks_Length: IntProperty(
        name="Length",
        default=2,
        max=4,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Streaks_Length
    )

    def update_Effects_Streaks_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_StreaksStrength"].inputs[0].default_value = settings.Effects_Streaks_Strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Streaks_Strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Streaks_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Streaks_Strength
    )

    # Ghosts

    def update_Effects_Ghosts_Threshold(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].threshold = settings.Effects_Ghosts_Threshold

    Effects_Ghosts_Threshold: FloatProperty(
        name="Threshold",
        default=1,
        max=1000,
        min=0,
        subtype="NONE",
        update=update_Effects_Ghosts_Threshold
    )

    def update_Effects_Ghosts_Distortion(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].color_modulation = settings.Effects_Ghosts_Distortion

    Effects_Ghosts_Distortion: FloatProperty(
        name="Distortion",
        default=0.1,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Ghosts_Distortion
    )

    def update_Effects_Ghosts_Count(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Ghosts"].iterations = settings.Effects_Ghosts_Count

    Effects_Ghosts_Count: IntProperty(
        name="Count",
        default=3,
        max=5,
        min=2,
        subtype="FACTOR",
        update=update_Effects_Ghosts_Count
    )

    def update_Effects_Ghosts_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_GhostsStrength"].inputs[0].default_value = settings.Effects_Ghosts_Strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Ghosts_Strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Ghosts_Strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Ghosts_Strength
    )

    # Emboss

    def update_Effects_Emboss_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Emboss"].inputs[0].default_value = settings.Effects_Emboss_Strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Emboss_Strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Posterize"].inputs[1].default_value = settings.Effects_Posterize_Steps
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

    # Overlay

    def update_Effects_Overlay_Strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay"].inputs[0].default_value = settings.Effects_Overlay_Strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Overlay_Strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Pixelate_Size"].inputs[0].default_value = settings.Effects_Pixelate_PixelSize

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Pixelate_PixelSize == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_ChromaticAberration"].inputs[2].default_value = settings.Effects_ChromaticAberration_Amount
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_ChromaticAberration"].inputs[1].default_value = -settings.Effects_ChromaticAberration_Amount/3.5

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_ChromaticAberration_Amount == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Intensity"].inputs[0].default_value = settings.Effects_Vignette_Intensity

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Vignette_Intensity == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Roundness"].inputs[0].default_value = settings.Effects_Vignette_Roundness

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Directional_Blur"].zoom = settings.Effects_Vignette_Feather
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Midpoint"].inputs[3].default_value = -settings.Effects_Vignette_Feather/4
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Midpoint"].inputs[1].default_value = -0.999-settings.Effects_Vignette_Feather/4

        feather_value = settings.Effects_Vignette_Feather
        node_to_update = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Directional_Blur"]

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
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Viginette_Midpoint"].inputs[0].default_value = settings.Effects_Vignette_Midpoint

    Effects_Vignette_Midpoint: FloatProperty(
        name="Midpoint",
        default=0,
        max=1,
        min=-0.998,
        subtype="FACTOR",
        update=update_Effects_Vignette_Midpoint
    )

    # Infrared
    # Infrared Blend
    def update_Effects_Infrared_Blend(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Mix"].inputs[0].default_value = settings.Effects_Infrared_Blend

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Infrared_Blend == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Infrared_Blend: FloatProperty(
        name="Blend",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Infrared_Blend
    )

    # Infrared Offset
    def update_Effects_Infrared_Offset(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Infrared_Add"].inputs[1].default_value = settings.Effects_Infrared_Offset

    Effects_Infrared_Offset: FloatProperty(
        name="Offset",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Infrared_Offset
    )

    # Negative

    def update_Effects_Negative(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Negative"].inputs[0].default_value = settings.Effects_Negative

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Negative == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Negative: FloatProperty(
        name="Negative",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Negative
    )

    # Warp

    def update_Effects_Warp(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        warp_node = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Warp"]
        warp_node.zoom = settings.Effects_Warp

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Warp == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

        warp_value = settings.Effects_Warp

        if warp_value <= 0.05:
            warp_node.iterations = 4
        elif warp_value <= 0.2:
            warp_node.iterations = 5
        elif warp_value <= 0.4:
            warp_node.iterations = 6
        else:  # warp_value > 0.4
            warp_node.iterations = 7

    Effects_Warp: FloatProperty(
        name="Warp",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Warp
    )

    # Fisheye

    def update_Effects_Fisheye(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Fisheye"].inputs[1].default_value = settings.Effects_Fisheye

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_Fisheye == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_Fisheye: FloatProperty(
        name="Fisheye",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Fisheye
    )

    # Perspective Shift
    # Horizontal
    def update_Effects_PerspectiveShift_Horizontal(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        horizontal_shift = settings.Effects_PerspectiveShift_Horizontal / 2
        if settings.Effects_PerspectiveShift_Horizontal > 0:
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] = horizontal_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[2].default_value[0] = 1 - horizontal_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[1].default_value = 1/(1-horizontal_shift*2)
        elif settings.Effects_PerspectiveShift_Horizontal < 0:
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[0] = -horizontal_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[0] = 1 - (-horizontal_shift)
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[1].default_value = 1/(1-horizontal_shift*-2)

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if (settings.Effects_PerspectiveShift_Horizontal == 0):
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[0] = 0
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[2].default_value[0] = 1
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[0] = 0
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[0] = 1
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[1].default_value = 1
            if (settings.Effects_PerspectiveShift_Vertical == 0):
                bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_PerspectiveShift_Horizontal: FloatProperty(
        name="Horizontal",
        default=0,
        max=0.999,
        min=-0.999,
        subtype="FACTOR",
        update=update_Effects_PerspectiveShift_Horizontal
    )
    # Vertical

    def update_Effects_PerspectiveShift_Vertical(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        vertical_shift = settings.Effects_PerspectiveShift_Vertical / 2
        if settings.Effects_PerspectiveShift_Vertical > 0:
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[1] = 1 - vertical_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] = vertical_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[2].default_value = 1/(1-vertical_shift*2)
        elif settings.Effects_PerspectiveShift_Vertical < 0:
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[2].default_value[1] = 1 - (-vertical_shift)
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[1] = -vertical_shift
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[2].default_value = 1/(1-vertical_shift*-2)

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_PerspectiveShift_Vertical == 0:
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[1].default_value[1] = 1
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[2].default_value[1] = 1
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[3].default_value[1] = 0
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_CornerPin"].inputs[4].default_value[1] = 0
            bpy.data.node_groups[node_group_name].nodes["SAC Effects_PerspectiveShift_Scale"].inputs[2].default_value = 1
            if settings.Effects_PerspectiveShift_Horizontal == 0:
                bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_PerspectiveShift_Vertical: FloatProperty(
        name="Vertical",
        default=0,
        max=0.999,
        min=-0.999,
        subtype="FACTOR",
        update=update_Effects_PerspectiveShift_Vertical
    )

    # ISO
    # Strength
    def update_ISO_strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Add"].inputs[0].default_value = settings.ISO_strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.ISO_strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    ISO_strength: FloatProperty(
        name="Strength",
        default=0,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_ISO_strength
    )
    # Size

    def update_ISO_size(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_ISO_Despeckle"].inputs[0].default_value = settings.ISO_size

    ISO_size: FloatProperty(
        name="Size",
        default=1,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_ISO_size
    )

    # Filmgrain
    # Strength

    def update_Filmgrain_strength(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Strength"].inputs[0].default_value = settings.Filmgrain_strength

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Filmgrain_strength == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Filmgrain_strength: FloatProperty(
        name="Strength",
        default=0,
        max=10,
        min=0,
        subtype="FACTOR",
        update=update_Filmgrain_strength
    )

    # Dust Proportion

    def update_Filmgrain_dustproportion(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].sigma_color = settings.Filmgrain_dustproportion

    Filmgrain_dustproportion: FloatProperty(
        name="Dust Proportion",
        default=0.35,
        max=0.5,
        min=0.01,
        subtype="FACTOR",
        update=update_Filmgrain_dustproportion
    )

    # Size

    def update_Filmgrain_size(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_FilmGrain_Blur"].iterations = settings.Filmgrain_size

    Filmgrain_size: IntProperty(
        name="Size",
        default=3,
        max=12,
        min=1,
        subtype="FACTOR",
        update=update_Filmgrain_size
    )

    # Halftone
    # Value

    def update_Effects_Halftone_value(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Value"].outputs[0].default_value = settings.Effects_Halftone_value

    Effects_Halftone_value: FloatProperty(
        name="Value",
        default=-0.2,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_Halftone_value
    )

    # Delta

    def update_Effects_Halftone_delta(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Delta"].outputs[0].default_value = settings.Effects_Halftone_delta

    Effects_Halftone_delta: FloatProperty(
        name="Delta",
        default=0.2,
        max=1,
        min=0,
        subtype="FACTOR",
        update=update_Effects_Halftone_delta
    )

    # Size

    def update_Effects_Halftone_size(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Texture"].inputs[1].default_value[0] = context.scene.render.resolution_x / (settings.Effects_Halftone_size*10)
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_Texture"].inputs[1].default_value[1] = context.scene.render.resolution_y / (settings.Effects_Halftone_size*10)
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Halftone_SizeSave"].outputs[0].default_value = settings.Effects_Halftone_size

    Effects_Halftone_size: FloatProperty(
        name="Size",
        default=2,
        max=10,
        min=1,
        subtype="FACTOR",
        update=update_Effects_Halftone_size
    )

    # Gradient Map
    # Blend

    def update_Effects_GradientMap_blend(self, context):
        scene = bpy.context.scene
        settings: SAC_Settings = scene.sac_settings
        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        node_name = f"{item.EffectGroup}_{item.ID}"
        node_group_name = f".{node_name}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap_Mix"].inputs[0].default_value = settings.Effects_GradientMap_blend

        bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = False
        if settings.Effects_GradientMap_blend == 0:
            bpy.data.node_groups[".SAC Effects"].nodes[node_name].mute = True

    Effects_GradientMap_blend: FloatProperty(
        name="Blend",
        default=0,
        max=1,
        min=-1,
        subtype="FACTOR",
        update=update_Effects_GradientMap_blend
    )
# endregion Effects
