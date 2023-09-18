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
import os
import mathutils
from bpy.types import (
    Context,
    Operator
)
from .Groups.SuperAdvancedCamera import connect_renderLayer_node
from .SAC_Settings import SAC_Settings
from .SAC_Functions import link_nodes, load_image_once, create_dot_texture


class SAC_OT_Initialize(Operator):
    bl_idname = "object.superadvancedcamerainit"
    bl_label = "Initialize Super Advanced Camera"
    bl_description = ""

    def execute(self, context: Context):
        connect_renderLayer_node()
        create_dot_texture()

        return {'FINISHED'}


class SAC_OT_AddEffect(Operator):
    bl_idname = "sac_effect_list.add_effect"
    bl_label = "Add a new effect to the list"

    def execute(self, context):
        item = context.scene.sac_effect_list.add()
        new_effect_type = context.scene.new_effect_type
        settings: SAC_Settings = context.scene.sac_settings

        # for each view layer, enable the Z pass
        for view_layer in context.scene.view_layers:
            view_layer.use_pass_z = True

        # Create the item_type_info dictionary from item_types
        item_type_info = {internal: (name, icon, internal) for internal, name, icon in settings.effect_types}

        item.name, item.icon, item.EffectGroup = item_type_info.get(new_effect_type, ('Untitled', 'NONE', ''))
        # Set the ID using the Scene property and increment it
        item.ID = str(context.scene.last_used_id).zfill(2)
        context.scene.last_used_id += 1

        # If the item is in array "slow", set the warning to True
        item.warn = new_effect_type in settings.slow_effects

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


class SAC_OT_ApplyBokeh(Operator):
    bl_idname = "sac_effect_list.apply_bokeh"
    bl_label = "Apply selected Bokeh to the effect"
    bl_description = ""

    def execute(self, context: Context):

        bokeh_dir = os.path.join(os.path.dirname(__file__), "bokeh")
        image_name = f"{bpy.context.scene.new_bokeh_type}.jpg"
        image_path = os.path.join(bokeh_dir, image_name)

        image = load_image_once(image_path, image_name)

        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None

        node_group_name = f".{item.EffectGroup}_{item.ID}"
        bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Image"].image = image

        return {'FINISHED'}


class SAC_OT_ApplyCameraBokeh(Operator):
    bl_idname = "sac_camera_bokeh.apply_bokeh"
    bl_label = "Apply selected Bokeh to the camera"
    bl_description = ""

    def execute(self, context: Context):

        bokeh_dir = os.path.join(os.path.dirname(__file__), "bokeh")
        image_name = f"{bpy.context.scene.new_camera_bokeh_type}.jpg"
        image_path = os.path.join(bokeh_dir, image_name)

        image = load_image_once(image_path, image_name)

        # get the currently selected camera
        active_obj = bpy.context.view_layer.objects.active
        # if nothing is selected, give an error message
        if active_obj is None:
            self.report({'ERROR'}, "No camera selected")
            return {'CANCELLED'}
        if active_obj and active_obj.type == 'CAMERA':
            camera_object = bpy.data.objects[active_obj.name]
            camera_data = bpy.data.cameras[camera_object.data.name]

        plane_name = f"{active_obj.name}_Bokeh_Plane"

        camera_location = camera_object.location
        camera_rotation = camera_object.rotation_euler
        matrix_rotation = camera_rotation.to_matrix()
        camera_data.clip_start = 0.0025

        forward_vector = mathutils.Vector((0, 0, -1))
        rotated_forward_vector = matrix_rotation @ forward_vector
        scaled_forward_vector = rotated_forward_vector * 0.003
        plane_location = camera_location + scaled_forward_vector

        try:
            bpy.data.objects[plane_name]

        except KeyError:
            bpy.ops.mesh.primitive_plane_add(size=0.04, enter_editmode=False, align='WORLD', location=plane_location, rotation=camera_rotation)
            bpy.context.view_layer.objects.active.name = plane_name
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[plane_name].select_set(True)
            bpy.data.objects[active_obj.name].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[active_obj.name]
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            bpy.data.objects[plane_name].hide_select = True

        # create the material named f".{active_obj.name}_Bokeh_Plane_Material" and assign it to the plane
        material_name = f".{plane_name}_Material"
        try:
            material = bpy.data.materials[material_name]
            material_node_tree = material.node_tree
            material_node_tree.nodes["SAC Camera_Bokeh_Image"].image = image

            for material_slot in bpy.data.objects[plane_name].material_slots:
                bpy.data.objects[plane_name].data.materials.clear()
            bpy.data.objects[plane_name].data.materials.append(material)

        except KeyError:
            material = bpy.data.materials.new(name=material_name)
            bpy.data.objects[plane_name].data.materials.append(material)
            material.use_nodes = True
            material_node_tree = material.node_tree

            for node in material_node_tree.nodes:
                material_node_tree.nodes.remove(node)

            texture_coordinate_node = material_node_tree.nodes.new(type='ShaderNodeTexCoord')

            vector_subtract_node = material_node_tree.nodes.new(type='ShaderNodeVectorMath')
            vector_subtract_node.operation = 'SUBTRACT'
            vector_subtract_node.inputs[1].default_value = (0.5, 0.5, 0.0)

            vector_rotate_node = material_node_tree.nodes.new(type='ShaderNodeVectorRotate')
            vector_rotate_node.rotation_type = 'Z_AXIS'
            vector_rotate_node.name = "SAC Camera_Bokeh_Rotate"

            vector_scale_node = material_node_tree.nodes.new(type='ShaderNodeVectorMath')
            vector_scale_node.operation = 'SCALE'
            vector_scale_node.inputs["Scale"].default_value = 2
            vector_scale_node.name = "SAC Camera_Bokeh_Scale"

            vector_add_node = material_node_tree.nodes.new(type='ShaderNodeVectorMath')
            vector_add_node.operation = 'ADD'
            vector_add_node.inputs[1].default_value = (0.5, 0.5, 0.0)

            image_texture_node = material_node_tree.nodes.new(type='ShaderNodeTexImage')
            image_texture_node.extension = 'CLIP'
            image_texture_node.image = image
            image_texture_node.name = "SAC Camera_Bokeh_Image"

            switch_node = material_node_tree.nodes.new(type='ShaderNodeMix')
            switch_node.data_type = "RGBA"
            switch_node.inputs["Factor"].default_value = 1
            switch_node.mute = True
            switch_node.name = "SAC Camera_Bokeh_Switch"

            custom_texture_node = material_node_tree.nodes.new(type='ShaderNodeTexImage')
            custom_texture_node.extension = 'CLIP'
            custom_texture_node.image = load_image_once(os.path.join(os.path.join(os.path.dirname(__file__), "bokeh"), "PidgeonTools.png"), "PidgeonTools.png")
            custom_texture_node.name = "SAC Camera_Bokeh_Custom_Texture"

            rgb_curves_node = material_node_tree.nodes.new(type='ShaderNodeRGBCurve')
            # add a new point to the curve
            rgb_curves_node.mapping.curves[3].points.new(0.25, 0.75)
            rgb_curves_node.name = "SAC Camera_Bokeh_Curves"

            transparent_bsdf_node = material_node_tree.nodes.new(type='ShaderNodeBsdfTransparent')
            material_output_node = material_node_tree.nodes.new(type='ShaderNodeOutputMaterial')

            # link the nodes
            link_nodes(material_node_tree, texture_coordinate_node, 'UV', vector_subtract_node, 0)
            link_nodes(material_node_tree, vector_subtract_node, 0, vector_rotate_node, 0)
            link_nodes(material_node_tree, vector_rotate_node, 0, vector_scale_node, 0)
            link_nodes(material_node_tree, vector_scale_node, 0, vector_add_node, 0)
            link_nodes(material_node_tree, vector_add_node, 0, image_texture_node, 0)
            link_nodes(material_node_tree, vector_add_node, 0, custom_texture_node, 0)
            link_nodes(material_node_tree, image_texture_node, 0, switch_node, 6)
            link_nodes(material_node_tree, custom_texture_node, 0, switch_node, 7)
            link_nodes(material_node_tree, switch_node, 2, rgb_curves_node, 1)
            link_nodes(material_node_tree, rgb_curves_node, 0, transparent_bsdf_node, 0)
            link_nodes(material_node_tree, transparent_bsdf_node, 0, material_output_node, 0)

        return {'FINISHED'}
