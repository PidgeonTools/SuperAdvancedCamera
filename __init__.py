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
import bpy.utils.previews

import os


from . import (
    SAC_Settings,
    SAC_Operators,
    SAC_Panel,
    SAC_List,
    SAC_Functions,
)

bl_info = {
    "name": "Super Advanced Camera (SAC)",
    "author": "Kevin Lorengel, Slinc",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "description": "Adds plenty of new features to the camera and compositor",
    "warning": "",
    "doc_url": "",
    "category": "Compositor",
}

bpy.types.Scene.new_effect_type = bpy.props.EnumProperty(
    items=SAC_Functions.enum_previews_from_directory_effects)

bpy.types.Scene.new_bokeh_type = bpy.props.EnumProperty(
    items=SAC_Functions.enum_previews_from_directory_bokeh)

bpy.types.Scene.new_camera_bokeh_type = bpy.props.EnumProperty(
    items=SAC_Functions.enum_previews_from_directory_bokeh)

bpy.types.Scene.new_filter_type = bpy.props.EnumProperty(
    items=SAC_Functions.enum_previews_from_directory_filter)

bpy.types.Scene.new_gradient_type = bpy.props.EnumProperty(
    items=SAC_Functions.enum_previews_from_directory_gradient)


def register():

    SAC_Settings.register_function()
    SAC_List.register_function()
    SAC_Operators.register_function()
    SAC_Panel.register_function()

    bpy.types.Scene.last_used_id = bpy.props.IntProperty(name="Last Used ID", default=0)
    bpy.types.Scene.sac_effect_list = bpy.props.CollectionProperty(type=SAC_List.SAC_EffectList)
    bpy.types.Scene.sac_effect_list_index = bpy.props.IntProperty(name="Index for sac_effect_list", default=0, update=SAC_Functions.active_effect_update)

    bpy.types.Scene.effect_previews = SAC_Functions.load_effect_previews()
    bpy.types.Scene.bokeh_previews = SAC_Functions.load_bokeh_previews()
    bpy.types.Scene.filter_previews = SAC_Functions.load_filter_previews()
    bpy.types.Scene.gradient_previews = SAC_Functions.load_gradient_previews()


def unregister():

    SAC_Panel.unregister_function()
    SAC_Operators.unregister_function()
    SAC_List.unregister_function()
    SAC_Settings.unregister_function()

    del bpy.types.Scene.last_used_id
    del bpy.types.Scene.sac_effect_list
    del bpy.types.Scene.sac_effect_list_index

    bpy.utils.previews.remove(bpy.types.Scene.effect_previews)
    bpy.utils.previews.remove(bpy.types.Scene.bokeh_previews)
    bpy.utils.previews.remove(bpy.types.Scene.filter_previews)
    bpy.utils.previews.remove(bpy.types.Scene.gradient_previews)


if __name__ == "__main__":
    register()
