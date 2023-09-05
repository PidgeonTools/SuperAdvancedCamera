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
    SAC_OT_Initialize
)

from .SAC_Panel import (
    SAC_PT_SAC_Panel,

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
    SAC_PT_EFFECTS_GLARE_FogGlow_Panel,
    SAC_PT_EFFECTS_GLARE_Streaks_Panel,
    SAC_PT_EFFECTS_GLARE_Ghost_Panel,

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

    SAC_PT_EFFECTS_Color_Panel,
    SAC_PT_EFFECTS_Duotone_Panel,
    SAC_PT_EFFECTS_GradientMap_Panel,

    SAC_PT_EFFECTS_Lighting_Panel,
    SAC_PT_EFFECTS_GLARE_FogGlow_Panel,
    SAC_PT_EFFECTS_GLARE_Streaks_Panel,
    SAC_PT_EFFECTS_GLARE_Ghost_Panel,

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
