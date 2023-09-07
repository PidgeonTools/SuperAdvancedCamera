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
    Context,
    Operator
)

from .Groups.SuperAdvancedCamera import (
    connect_renderLayer_node
)
from .SAC_Settings import SAC_Settings


class SAC_OT_Initialize(Operator):
    bl_idname = "object.superadvancedcamerainit"
    bl_label = "Initialize Super Advanced Camera"
    bl_description = ""

    def execute(self, context: Context):
        connect_renderLayer_node()
        create_dot_texture()

        return {'FINISHED'}


def create_dot_texture():
    texture = bpy.data.textures.get(".SAC Dot Screen")
    if texture is None:
        texture = bpy.data.textures.new(name=".SAC Dot Screen", type='MAGIC')
    texture.noise_depth = 1  # Depth
    texture.turbulence = 6.0  # Turbulence
    texture.use_color_ramp = True
    texture.color_ramp.interpolation = 'CONSTANT'
    texture.color_ramp.elements[1].position = 0.65


class SAC_OT_AddEffect(Operator):
    bl_idname = "sac_effect_list.add_effect"
    bl_label = "Add a new effect to the list"

    def execute(self, context):
        item = context.scene.sac_effect_list.add()
        new_item_type = context.scene.new_item_type
        settings: SAC_Settings = context.scene.sac_settings

        # Create the item_type_info dictionary from item_types
        item_type_info = {internal: (name, icon, internal) for internal, name, icon in settings.effect_types}

        item.name, item.icon, item.EffectGroup = item_type_info.get(new_item_type, ('Untitled', 'NONE', ''))
        # Set the ID using the Scene property and increment it
        item.ID = str(context.scene.last_used_id).zfill(2)
        context.scene.last_used_id += 1

        context.scene.sac_effect_list_index = len(context.scene.sac_effect_list) - 1
        connect_renderLayer_node()
        return {'FINISHED'}


class SAC_OT_RemoveEffect(Operator):
    bl_idname = "sac_effect_list.remove_effect"
    bl_label = "Remove the selected effect from the list"

    @classmethod
    def poll(cls, context):
        return context.scene.sac_effect_list

    def execute(self, context):
        list = context.scene.sac_effect_list
        index = context.scene.sac_effect_list_index

        list.remove(index)
        context.scene.sac_effect_list_index = min(max(0, index - 1), len(list) - 1)
        connect_renderLayer_node()
        return {'FINISHED'}


class SAC_OT_MoveEffectUp(Operator):
    bl_idname = "sac_effect_list.move_effect_up"
    bl_label = "Move the selected effect up in the list"

    @classmethod
    def poll(cls, context):
        return context.scene.sac_effect_list_index > 0

    def execute(self, context):
        list = context.scene.sac_effect_list
        index = context.scene.sac_effect_list_index

        list.move(index, index-1)
        context.scene.sac_effect_list_index = index - 1
        connect_renderLayer_node()
        return {'FINISHED'}


class SAC_OT_MoveEffectDown(Operator):
    bl_idname = "sac_effect_list.move_effect_down"
    bl_label = "Move the selected effect down in the list"

    @classmethod
    def poll(cls, context):
        return context.scene.sac_effect_list_index < len(context.scene.sac_effect_list) - 1

    def execute(self, context):
        list = context.scene.sac_effect_list
        index = context.scene.sac_effect_list_index

        list.move(index, index+1)
        context.scene.sac_effect_list_index = index + 1
        connect_renderLayer_node()
        return {'FINISHED'}


class SAC_OT_PrintEffectGroups(Operator):
    bl_idname = "sac_effect_list.print_effect_groups"
    bl_label = "Print Effect Groups"

    def execute(self, context):
        for item in context.scene.sac_effect_list:
            print(f"{item.EffectGroup}_{item.ID}")
        return {'FINISHED'}
