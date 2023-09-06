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

from .SAC_Operators import (
    SAC_OT_Initialize,
    SAC_OT_AddEffect,
    SAC_OT_RemoveEffect,
    SAC_OT_MoveEffectUp,
    SAC_OT_MoveEffectDown,
    SAC_OT_PrintEffectGroups
)

from .SAC_List import (
    SAC_EffectList,
    SAC_UL_List
)

from .SAC_Panel import (
    SAC_PT_SAC_Panel,

    SAC_PT_List,

    SAC_PT_COLORGRADE_Panel,
    SAC_PT_COLORGRADE_Color_Panel,
    SAC_PT_COLORGRADE_Light_Panel,
    SAC_PT_COLORGRADE_Presets_Panel,
    SAC_PT_COLORGRADE_Curves_Panel,
    SAC_PT_COLORGRADE_Colorwheels_Panel,

    SAC_PT_EFFECTS_Panel,

    SAC_PT_EFFECTS_Color_Panel,
    SAC_PT_EFFECTS_Duotone_Panel,
    SAC_PT_EFFECTS_GradientMap_Panel,

    SAC_PT_EFFECTS_Lighting_Panel,
    SAC_PT_EFFECTS_FogGlow_Panel,
    SAC_PT_EFFECTS_Streaks_Panel,
    SAC_PT_EFFECTS_Ghost_Panel,

    SAC_PT_EFFECTS_Texture_Panel,
    SAC_PT_EFFECTS_Emboss_Panel,
    SAC_PT_EFFECTS_Posterize_Panel,
    SAC_PT_EFFECTS_Halftone_Panel,
    SAC_PT_EFFECTS_Overlay_Panel,

    SAC_PT_EFFECTS_Special_Panel,
    SAC_PT_CAMERA_Bokeh_Panel,
    SAC_PT_EFFECTS_Vignette_Panel,
    SAC_PT_EFFECTS_Mosaic_Panel,
    SAC_PT_EFFECTS_ChromaticAberration_Panel,
    SAC_PT_EFFECTS_Infrared_Panel,
    SAC_PT_EFFECTS_Negative_Panel,
    SAC_PT_EFFECTS_ISONoise_Panel,
    SAC_PT_EFFECTS_FilmGrain_Panel,

    SAC_PT_EFFECTS_Geometric_Panel,
    SAC_PT_EFFECTS_Warp_Panel,
    SAC_PT_EFFECTS_FishEye_Panel,
    SAC_PT_EFFECTS_PerspectiveShift_Panel,

    SAC_PT_EFFECTS_Artistic_Panel,
    SAC_PT_EFFECTS_OilPaint_Panel,
    SAC_PT_EFFECTS_Sketch_Panel,
    SAC_PT_EFFECTS_Watercolor_Panel,
    SAC_PT_EFFECTS_Pointillism_Panel,

    SAC_PT_CAMERA_Panel,
    SAC_PT_CAMERA_TiltShift_Panel,
)
from .SAC_Settings import (
    SAC_Settings
)

bl_info = {
    "name": "Super Advanced Camera (SAC)",
    "author": "Kevin Lorengel, Slinc",
    "version": (0, 0, 7),
    "blender": (3, 6, 0),
    "description": "Adds plenty of new features to the camera and compositor",
    "warning": "",
    "doc_url": "",
    "category": "Compositor",
}


classes = (
    SAC_PT_SAC_Panel,

    SAC_PT_COLORGRADE_Panel,
    SAC_PT_COLORGRADE_Color_Panel,
    SAC_PT_COLORGRADE_Light_Panel,
    SAC_PT_COLORGRADE_Presets_Panel,
    SAC_PT_COLORGRADE_Curves_Panel,
    SAC_PT_COLORGRADE_Colorwheels_Panel,

    SAC_PT_EFFECTS_Panel,

    SAC_PT_List,
    SAC_EffectList,
    SAC_UL_List,

    SAC_PT_EFFECTS_Color_Panel,
    SAC_PT_EFFECTS_Duotone_Panel,
    SAC_PT_EFFECTS_GradientMap_Panel,

    SAC_PT_EFFECTS_Lighting_Panel,
    SAC_PT_EFFECTS_FogGlow_Panel,
    SAC_PT_EFFECTS_Streaks_Panel,
    SAC_PT_EFFECTS_Ghost_Panel,

    SAC_PT_EFFECTS_Texture_Panel,
    SAC_PT_EFFECTS_Emboss_Panel,
    SAC_PT_EFFECTS_Posterize_Panel,
    SAC_PT_EFFECTS_Halftone_Panel,
    SAC_PT_EFFECTS_Overlay_Panel,

    SAC_PT_EFFECTS_Special_Panel,
    SAC_PT_EFFECTS_Vignette_Panel,
    SAC_PT_EFFECTS_Mosaic_Panel,
    SAC_PT_EFFECTS_ChromaticAberration_Panel,
    SAC_PT_EFFECTS_Infrared_Panel,
    SAC_PT_EFFECTS_Negative_Panel,

    SAC_PT_EFFECTS_Geometric_Panel,
    SAC_PT_EFFECTS_Warp_Panel,
    SAC_PT_EFFECTS_FishEye_Panel,
    SAC_PT_EFFECTS_PerspectiveShift_Panel,

    SAC_PT_EFFECTS_Artistic_Panel,
    SAC_PT_EFFECTS_OilPaint_Panel,
    SAC_PT_EFFECTS_Sketch_Panel,
    SAC_PT_EFFECTS_Watercolor_Panel,
    SAC_PT_EFFECTS_Pointillism_Panel,
    SAC_PT_EFFECTS_ISONoise_Panel,
    SAC_PT_EFFECTS_FilmGrain_Panel,

    SAC_PT_CAMERA_Panel,
    SAC_PT_CAMERA_TiltShift_Panel,
    SAC_PT_CAMERA_Bokeh_Panel,

    SAC_OT_Initialize,
    SAC_OT_AddEffect,
    SAC_OT_RemoveEffect,
    SAC_OT_MoveEffectUp,
    SAC_OT_MoveEffectDown,
    SAC_OT_PrintEffectGroups,

    SAC_Settings
)


def register():
    # register the example panel, to show updater buttons
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.sac_settings = bpy.props.PointerProperty(type=SAC_Settings)
    bpy.types.Scene.last_used_id = bpy.props.IntProperty(name="Last Used ID", default=0)
    bpy.types.Scene.sac_effect_list = bpy.props.CollectionProperty(type=SAC_EffectList)
    bpy.types.Scene.sac_effect_list_index = bpy.props.IntProperty(name="Index for sac_effect_list", default=0)


def unregister():
    # register the example panel, to show updater buttons
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.sac_settings
    del bpy.types.Scene.sac_effect_list
    del bpy.types.Scene.sac_effect_list_index
    del bpy.types.Scene.last_used_id


if __name__ == "__main__":
    register()
