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

from .SAC_Functions import mute_update

from bpy.types import (
    PropertyGroup,
    UIList,
)


class SAC_EffectList(PropertyGroup):
    name: bpy.props.StringProperty(name="Name", default="Untitled")
    icon: bpy.props.StringProperty(name="Icon", default="NONE")
    warn: bpy.props.BoolProperty(name="Warn", default=False, description="This effect is not viewport compatible.\nIt will work in the final render.\n\nThis is a limitation of Blender.\nDisable this effect to see the viewport.")
    mute: bpy.props.BoolProperty(name="Mute", default=False, update=mute_update, description="Disable this effect for viewport and final render.")
    EffectGroup: bpy.props.StringProperty(name="Effect Group", default="")
    ID: bpy.props.StringProperty(name="ID", default="")


class SAC_UL_List(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            main_row = layout.row(align=True)

            # Create the first part of the layout
            split = main_row.split(factor=0.66, align=False)
            # split.prop(item, "name", text="", emboss=False, icon=item.icon)
            split.label(text=f"{item.ID} - {item.name}", icon=item.icon)

            row = split.row(align=True)
            row.emboss = 'NONE_OR_STATUS'

            # Create a new row for the warning icon
            warning_row = main_row.row(align=True)
            warning_row.prop(item, "warn", text="", emboss=False, icon='ERROR' if item.warn else 'NONE')

            # Create a new row for the mute button on the far right
            mute_row = main_row.row(align=True)
            mute_row.prop(item, "mute", text="", emboss=False, icon='HIDE_OFF' if not item.mute else 'HIDE_ON')
            if item.mute:
                split.active = False


classes = (
    SAC_EffectList,
    SAC_UL_List,
)


def register_function():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_function():
    for cls in reversed(classes):
        if hasattr(bpy.types, cls.__name__):
            try:
                bpy.utils.unregister_class(cls)
            except (RuntimeError, Exception) as e:
                print(f"Failed to unregister {cls}: {e}")
