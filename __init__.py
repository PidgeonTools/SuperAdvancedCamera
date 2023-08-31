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
    SAC_PT_EFFECTS_Panel
)

from .SAC_Settings import (
    SAC_Settings
)

bl_info = {
    "name": "Super Advanced Camera",
    "author": "Kevin Lorengel, Slinc",
    "version": (0, 0, 2),
    "blender": (3, 6, 0),
    "location": "TODO",
    "description": "TODO",
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
