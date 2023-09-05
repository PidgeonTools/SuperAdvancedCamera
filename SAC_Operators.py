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
