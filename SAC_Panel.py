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

from bpy.utils import (
    previews
)

from bpy.types import (
    Context,
    Panel,
)

from .SAC_Settings import SAC_Settings
from .SAC_Functions import (
    frames_to_time,
)

custom_icons = bpy.utils.previews.new()
icon_names = ["Discord", "BlenderMarket", "Gumroad", "Instagram", "Twitter", "Youtube"]

for icon_name in icon_names:
    icon_path = "icons/" + icon_name + ".png"
    custom_icons.load(icon_name, icon_path, 'IMAGE')

# Main


class SAC_PT_Panel:
    bl_label = "Super Advanced Camera"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_options = {"DEFAULT_CLOSED"}


class SAC_PT_SAC_Panel(SAC_PT_Panel, Panel):
    bl_label = "Super Advanced Camera"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="SHADERFX")

    def draw(self, context: Context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("superadvancedcamera.superadvancedcamerainit", icon="SHADERFX")


# Info
class SAC_PT_Info_Panel(SAC_PT_Panel, Panel):
    bl_label = "Info"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="INFO")

    def draw(self, context: Context):
        layout = self.layout
        col = layout.column(align=True)

        found = False

        for node in bpy.context.scene.node_tree.nodes:
            if node.name.startswith("Super Advanced Camera"):
                found = True

                col.label(text="Super Advanced Camera is added.", icon="CHECKMARK")
                if node.mute:
                    col.label(text="Super Advanced Camera is disabled.", icon="ERROR")
                    col.label(text="Unmute the node in the compositor.", icon="INFO")
                else:
                    col.label(text="Super Advanced Camera is enabled.", icon="CHECKMARK")
                    col.label(text="You can now use the Super Advanced Camera.", icon="INFO")
                    col.label(text="Make sure to enable the viewport compositor.", icon="INFO")
                break

        if not found:
            col.label(text="Super Advanced Camera node not found.", icon="ERROR")
            col.label(text="Please initialize the Super Advanced Camera", icon="INFO")


# region Camera
# Camera
class SAC_PT_CAMERA_Panel(SAC_PT_Panel, Panel):
    bl_label = "Camera"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_DATA_CAMERA")

    def draw(self, context: Context):
        settings = context.scene.sac_settings
        layout = self.layout
        col = layout.column(align=True)
        col.prop(settings, "selected_camera")
        if settings.selected_camera == "None":
            col.label(text="No camera found in scene.")
            col.label(text="Please add a camera to the scene.")
            return


# Camera Settings
class SAC_PT_CAMERA_CameraSettings_Panel(SAC_PT_Panel, Panel):
    bl_label = ""
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="Render Settings", icon="SETTINGS")

    def draw(self, context: Context):
        settings = context.scene.sac_settings
        scene = context.scene

        layout = self.layout
        col = layout.column(align=True)

        col.label(text="Resolution")
        row = col.row(align=True)
        row.prop(context.scene.render, "resolution_x", text="Width")
        row.prop(context.scene.render, "resolution_y", text="Height")
        col.prop(context.scene.render, "resolution_percentage", text="Scale")
        col.separator()

        # start frame
        col.label(text="Frames")
        row = col.row(align=True)
        if not scene.use_preview_range:
            row.prop(scene, "frame_start", text="Start")
            row.prop(scene, "frame_end", text="End")
            row.prop(scene, "frame_step", text="Step")

        else:
            row.prop(scene, "frame_preview_start", text="Start")
            row.prop(scene, "frame_preview_end", text="End")
            subrow = row.row(align=True)
            subrow.enabled = False
            subrow.prop(scene, "frame_step", text="Step")
        row = col.row(align=True)
        row.enabled = False
        row.label(text=f"Start: {frames_to_time(scene.frame_start, scene.render.fps//scene.render.fps_base)}")
        row.label(text=f"End: {frames_to_time(scene.frame_end, scene.render.fps//scene.render.fps_base)}")
        row.label(text=f"Total: {frames_to_time((scene.frame_end - scene.frame_start + 1)//scene.frame_step, scene.render.fps//scene.render.fps_base)}")
        col.prop(scene, "use_preview_range", text="Use Preview Range", toggle=True)
        col.separator()

        row = col.row(align=True)
        row.operator("superadvancedcamera.set_start_frame")
        row.operator("superadvancedcamera.set_end_frame")
        col.separator()

        row = col.row(align=True)
        row.prop(scene, "show_subframe", text="Show Subframes")
        subcol = row.column(align=True)
        if scene.show_subframe:
            subcol.prop(scene, "frame_float", text="Current")
        else:
            subcol.prop(scene, "frame_current", text="Current")
        subcol_inactive = subcol.column(align=True)
        subcol_inactive.active = False
        subcol_inactive.label(text=f"Current: {frames_to_time(scene.frame_float, scene.render.fps//scene.render.fps_base)}")
        col.separator()

        row = col.row(align=True)
        row.label(text="Frame Rate: " + str(round(scene.render.fps/scene.render.fps_base, 2)) + " fps")
        row.active = False
        row = col.row(align=True)
        row.prop(scene.render, "fps")
        row.prop(scene.render, "fps_base", text="Base")
        col.separator()

        # time stretching
        col.label(text="Time Stretching")
        col.prop(settings, "Camera_FrameStretching")
        col = col.column()
        row = col.row(align=True)
        row.prop(scene.render, "frame_map_old", text="Original duration")
        row.prop(scene.render, "frame_map_new", text="New duration")
# Tilt Shift


class SAC_PT_CAMERA_TiltShift_Panel(SAC_PT_Panel, Panel):
    bl_label = ""
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        settings = context.scene.sac_settings

        layout = self.layout
        layout.label(text="Lens Settings", icon="MOD_LATTICE")
        if settings.selected_camera == "None":
            layout.enabled = False
            return

    def draw(self, context: Context):
        settings = context.scene.sac_settings

        layout = self.layout
        if settings.selected_camera == "None":
            layout.label(text="No camera in scene.")
            layout.enabled = False
            return

        camera_object = bpy.data.objects[settings.selected_camera]
        camera_data = bpy.data.cameras[camera_object.data.name]

        if settings.Camera_TiltShift_KeepFrame == True:
            shift_x_text = "Vertical Tilt Shift"
            shift_y_text = "Horizontal Tilt Shift"
        else:
            shift_x_text = "Vertical Lens Shift"
            shift_y_text = "Horizontal Lens Shift"

        col_shift = layout.column(align=False)
        col_shift.label(text="Tilt Shift / Lens Shift")
        col_shift.prop(settings, "Camera_TiltShift_AmountX", text=shift_x_text)
        col_shift.prop(settings, "Camera_TiltShift_AmountY", text=shift_y_text)
        col_shift.prop(settings, "Camera_TiltShift_KeepFrame")

        col_focal = layout.row(align=True)
        col_focal.prop(camera_data, "lens")
        col_focal.prop(camera_data, "angle")

        col_clip = layout.row(align=True)
        col_clip.prop(camera_data, "clip_start", text="Min. Visible Distance")
        col_clip.prop(camera_data, "clip_end", text="Max. Visible Distance")

# Bokeh


class SAC_PT_CAMERA_Bokeh_Panel(SAC_PT_Panel, Panel):
    bl_label = ""
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        settings = context.scene.sac_settings
        layout = self.layout

        layout.label(text="Use Bokeh", icon="SEQ_CHROMA_SCOPE")

        if settings.selected_camera == "None":
            layout.enabled = False
            return

        camera_object = bpy.data.objects[settings.selected_camera]
        camera_data = bpy.data.cameras[camera_object.data.name]

        layout.prop(camera_data.dof, "use_dof", text="")

    def draw(self, context: Context):
        settings = context.scene.sac_settings
        layout = self.layout
        col = layout.column()

        if settings.selected_camera == "None":
            col.label(text="No camera in scene.")
            col.enabled = False
            return

        camera_object = bpy.data.objects[settings.selected_camera]
        camera_data = bpy.data.cameras[camera_object.data.name]

        col.active = camera_data.dof.use_dof

        col.prop(camera_data.dof, "focus_object")
        col.prop(camera_data.dof, "focus_distance")
        col.prop(camera_data.dof, "aperture_fstop")
        col.separator()

        try:
            plane_object = bpy.data.objects[f"SAC_Bokeh_{settings.selected_camera}"]
        except:
            col.label(text="No Bokeh Plane found.")
            col.label(text="Please apply Bokeh first.")
            col.operator("superadvancedcamera.apply_camera_bokeh", icon="SEQ_CHROMA_SCOPE")
            return
        col.separator()
        col.label(text="Bokeh Type")
        row_bokeh_type = col.row(align=True)
        row_bokeh_type.prop(settings, "Camera_Bokeh_Type", expand=True)
        col.separator(factor=0.5)

        if settings.Camera_Bokeh_Type == "CAMERA":
            row = col.row(align=True)
            left = row.column(align=True)
            left.scale_x = 1
            left.scale_y = 8
            left.operator("superadvancedcamera.previous_camera_bokeh", text="", icon="TRIA_LEFT")
            center = row.column()
            center.template_icon_view(context.scene, "new_camera_bokeh_type", show_labels=True, scale=8.0, scale_popup=4.0)
            right = row.column(align=True)
            right.scale_x = 1
            right.scale_y = 8
            right.operator("superadvancedcamera.next_camera_bokeh", text="", icon="TRIA_RIGHT")

            bokeh_type = context.scene.new_camera_bokeh_type.split("_")
            col_bokeh_description = col.column(align=True)
            col_bokeh_description.active = False

            row_bokeh_description = col_bokeh_description.row(align=True)
            row_bokeh_description.label(text="Manufacturer:")
            row_bokeh_description.label(text=bokeh_type[0])

            row_bokeh_description = col_bokeh_description.row(align=True)
            row_bokeh_description.label(text="Model:")
            row_bokeh_description.label(text=f"{bokeh_type[1]} - {bokeh_type[3]} - {bokeh_type[2]}")

            row_bokeh_description = col_bokeh_description.row(align=True)
            row_bokeh_description.label(text="Aperture:")
            row_bokeh_description.label(text=bokeh_type[4])

            col_bokeh_description.label(text="Special thanks to Prof. Dr. Matt Gunn for the Bokeh textures.")

            col.separator()
            col = col.column()
            col.prop(settings, "Camera_Bokeh_Scale")
            col.prop(settings, "Camera_Bokeh_Rotation")
            col.prop(settings, "Camera_Bokeh_Curves")
            col.separator()
            col.operator("superadvancedcamera.apply_camera_bokeh", icon="SEQ_CHROMA_SCOPE")

        elif settings.Camera_Bokeh_Type == "PROCEDURAL":
            col.prop(camera_data.dof, "aperture_blades")
            col.prop(camera_data.dof, "aperture_rotation")
            col.prop(camera_data.dof, "aperture_ratio")

        elif settings.Camera_Bokeh_Type == "CUSTOM":
            material = bpy.data.materials[f".SAC_Bokeh_{settings.selected_camera}_Material"]
            material_node_tree = material.node_tree
            bokeh_image = material_node_tree.nodes["SAC Camera_Bokeh_Custom_Texture"]

            col.template_ID_preview(bokeh_image, "image", open="image.open", rows=3, cols=8)
            col.prop(settings, "Camera_Bokeh_Scale")
            col.prop(settings, "Camera_Bokeh_Rotation")
            col.prop(settings, "Camera_Bokeh_Curves")

# endregion Camera

# region ColorGrade


class SAC_PT_COLORGRADE_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color Grading"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OPTIONS")

    def draw(self, context: Context):
        layout = self.layout


# Colorgrade - Color
class SAC_PT_COLORGRADE_Color_Panel(SAC_PT_Panel, Panel):
    bl_label = "Color"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="COLOR")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        col = layout.column()
        row = col.row(align=True)
        row.prop(settings, "Colorgrade_Color_WhiteLevel")
        col.prop(settings, "Colorgrade_Color_Temperature")
        col.prop(settings, "Colorgrade_Color_Tint")
        col.prop(settings, "Colorgrade_Color_Saturation")
        col.prop(settings, "Colorgrade_Color_Hue")


# Colorgrade - Light
class SAC_PT_COLORGRADE_Light_Panel(SAC_PT_Panel, Panel):
    bl_label = "Light"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_OB_LIGHT")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        col = layout.column()
        col.prop(settings, "Colorgrade_Light_Exposure")
        col.prop(settings, "Colorgrade_Light_Contrast")
        col.prop(settings, "Colorgrade_Light_Highlights")
        col.prop(settings, "Colorgrade_Light_Shadows")
        col.prop(settings, "Colorgrade_Light_Whites")
        col.prop(settings, "Colorgrade_Light_Darks")


# Colorgrade - Presets
class SAC_PT_COLORGRADE_Presets_Panel(SAC_PT_Panel, Panel):
    bl_label = "Presets"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="PRESET")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        layout = self.layout
        col = layout.column()

        col.prop(settings, "filter_type")

        row = col.row(align=True)
        left = row.column(align=True)
        left.scale_x = 1
        left.scale_y = 8
        left.operator("superadvancedcamera.previous_filter", text="", icon="TRIA_LEFT")
        center = row.column()
        center.template_icon_view(context.scene, "new_filter_type", show_labels=True, scale=8.0, scale_popup=4.0)
        right = row.column(align=True)
        right.scale_x = 1
        right.scale_y = 8
        right.operator("superadvancedcamera.next_filter", text="", icon="TRIA_RIGHT")
        center_column = col.row(align=True)
        center_column.label(text="Filter Name:")
        center_column.label(text=f"{scene.new_filter_type}")

        col.operator("superadvancedcamera.apply_filter", icon="BRUSHES_ALL")
        col.prop(settings, "Colorgrade_Filter_Mix")
        col.prop(settings, "Colorgrade_Filter_Extension")
        col.separator()
        col.prop(settings, "Colorgrade_Presets_Sharpen")
        col.prop(settings, "Colorgrade_Presets_Vibrance")
        col.prop(settings, "Colorgrade_Presets_Saturation")
        col.prop(settings, "Colorgrade_Presets_HighlightTint")
        col.prop(settings, "Colorgrade_Presets_ShadowTint")


# Colorgrade - Curves
class SAC_PT_COLORGRADE_Curves_Panel(SAC_PT_Panel, Panel):
    bl_label = "Curves"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="FCURVE")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        rgb_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_RGB"]
        hsv_curves_node = bpy.data.node_groups[".SAC Curves"].nodes["SAC Colorgrade_Curves_HSV"]

        layout = self.layout
        row = layout.row()
        col = row.column()
        col.label(text="RGB Curves", icon="MOD_INSTANCE")
        col.template_curve_mapping(rgb_curves_node, "mapping", type='COLOR')
        col.prop(settings, "Colorgrade_Curves_RGB_Intensity")
        col.separator(factor=2)
        col.label(text="HSV Curves", icon="MOD_OCEAN")
        col.template_curve_mapping(hsv_curves_node, "mapping", type='HUE')
        col.prop(settings, "Colorgrade_Curves_HSV_Intensity")


# Colorgrade - Colorwheels
class SAC_PT_COLORGRADE_Colorwheels_Panel(SAC_PT_Panel, Panel):
    bl_label = "Colorwheels"
    bl_parent_id = "SAC_PT_COLORGRADE_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MESH_CIRCLE")

    def draw(self, context: Context):
        scene = context.scene
        settings: SAC_Settings = scene.sac_settings

        color_wheel_node_lift = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Shadows"]
        color_wheel_node_gamma = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Midtones"]
        color_wheel_node_gain = bpy.data.node_groups[".SAC Colorwheel"].nodes["SAC Colorgrade_Colorwheel_Highlights"]

        layout = self.layout
        row = layout.row()
        col_1 = row.column()
        col_1.label(text="Shadows", icon="PMARKER")
        col_1.template_color_picker(color_wheel_node_lift, "lift")
        col_1.prop(settings, "Colorgrade_Colorwheel_Shadows_Brightness", text="Brightness")
        col_1.prop(settings, "Colorgrade_Colorwheel_Shadows_Intensity", text="Intensity")
        col_2 = row.column()
        col_2.label(text="Midtones", icon="PMARKER_SEL")
        col_2.template_color_picker(color_wheel_node_gamma, "gamma")
        col_2.prop(settings, "Colorgrade_Colorwheel_Midtones_Brightness", text="Brightness")
        col_2.prop(settings, "Colorgrade_Colorwheel_Midtones_Intensity", text="Intensity")
        col_3 = row.column()
        col_3.label(text="Highlights", icon="PMARKER_ACT")
        col_3.template_color_picker(color_wheel_node_gain, "gain")
        col_3.prop(settings, "Colorgrade_Colorwheel_Highlights_Brightness", text="Brightness")
        col_3.prop(settings, "Colorgrade_Colorwheel_Highlights_Intensity", text="Intensity")
# endregion ColorGrade

# region Effects
# Effects


class SAC_PT_EFFECTS_Panel(SAC_PT_Panel, Panel):
    bl_label = "Effects"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="IMAGE")

    def draw(self, context: Context):
        layout = self.layout


# Effects - List
class SAC_PT_List(SAC_PT_Panel, Panel):
    bl_label = "Effect List"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="LONGDISPLAY")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout = self.layout

        row = layout.row(align=True)
        left = row.column(align=True)
        left.scale_x = 1
        left.scale_y = 8
        left.operator("superadvancedcamera.previous_effect", text="", icon="TRIA_LEFT")
        center = row.column()
        center.template_icon_view(context.scene, "new_effect_type", show_labels=True, scale=8.0, scale_popup=4.0)
        right = row.column(align=True)
        right.scale_x = 1
        right.scale_y = 8
        right.operator("superadvancedcamera.next_effect", text="", icon="TRIA_RIGHT")

        row = layout.row()
        row.template_list("SAC_UL_List", "", scene, "sac_effect_list", scene, "sac_effect_list_index")

        col = row.column(align=True)
        col.scale_x = 1  # Set a fixed width
        col.operator("superadvancedcamera.add_effect", text="", icon='ADD')
        col.operator("superadvancedcamera.remove_effect", text="", icon='REMOVE')
        col.separator()
        col.operator("superadvancedcamera.move_effect_up", text="", icon='TRIA_UP')
        col.operator("superadvancedcamera.move_effect_down", text="", icon='TRIA_DOWN')


# Effects - Color
class SAC_PT_EFFECTS_Properties_Panel(SAC_PT_Panel, Panel):
    bl_label = ""
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None

        layout = self.layout
        if item == None:
            layout.label(text="Effect Properties", icon="PROPERTIES")
            layout.active = False
            return
        layout.active = not item.mute
        layout.label(text=f"Effect Properties: {item.name}", icon="PROPERTIES")

    def draw(self, context: Context):
        settings = context.scene.sac_settings
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None

        layout = self.layout
        col = layout.column()

        if item is None:
            col.label(text="No effect selected.")
            col.active = False
            return

        layout.active = not item.mute

        node_group_name = f".{item.EffectGroup}_{item.ID}"

        # col.label(text=f"These are settings for {item.name}.")
        # Bokeh
        if item.EffectGroup == "SAC_BOKEH":
            col.label(text="This effect is not viewport compatible.", icon="ERROR")
            col.prop(settings, "Effects_Bokeh_MaxSize")
            col.prop(settings, "Effects_Bokeh_Offset")
            col.prop(settings, "Effects_Bokeh_Range")
            col.separator()
            col.label(text="Bokeh Type")
            row_bokeh_type = col.row(align=True)
            row_bokeh_type.prop(settings, "Effects_Bokeh_Type", expand=True)
            col.separator(factor=0.5)

            if settings.Effects_Bokeh_Type == "CAMERA":
                row = col.row(align=True)
                left = row.column(align=True)
                left.scale_x = 1
                left.scale_y = 8
                left.operator("superadvancedcamera.previous_effect_bokeh", text="", icon="TRIA_LEFT")
                center = row.column()
                center.template_icon_view(context.scene, "new_bokeh_type", show_labels=True, scale=8.0, scale_popup=4.0)
                right = row.column(align=True)
                right.scale_x = 1
                right.scale_y = 8
                right.operator("superadvancedcamera.next_effect_bokeh", text="", icon="TRIA_RIGHT")

                bokeh_type = context.scene.new_bokeh_type.split("_")
                col_bokeh_description = col.column(align=True)
                col_bokeh_description.active = False

                row_bokeh_description = col_bokeh_description.row(align=True)
                row_bokeh_description.label(text="Manufacturer:")
                row_bokeh_description.label(text=bokeh_type[0])

                row_bokeh_description = col_bokeh_description.row(align=True)
                row_bokeh_description.label(text="Model:")
                row_bokeh_description.label(text=f"{bokeh_type[1]} - {bokeh_type[3]} - {bokeh_type[2]}")

                row_bokeh_description = col_bokeh_description.row(align=True)
                row_bokeh_description.label(text="Aperture:")
                row_bokeh_description.label(text=bokeh_type[4])

                col_bokeh_description.label(text="Special thanks to Prof. Dr. Matt Gunn for the Bokeh textures.")
                col.prop(settings, "Effects_Bokeh_Rotation")
                col.separator()
                col.operator("superadvancedcamera.apply_effect_bokeh", icon="SEQ_CHROMA_SCOPE")

            elif settings.Effects_Bokeh_Type == "CUSTOM":
                bokeh_image = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Custom_Image"]
                col.template_ID_preview(bokeh_image, "image", open="image.open")
                col.prop(settings, "Effects_Bokeh_Rotation")

            elif settings.Effects_Bokeh_Type == "PROCEDURAL":
                col.prop(settings, "Effects_Bokeh_Procedural_Flaps")
                col.prop(settings, "Effects_Bokeh_Procedural_Angle")
                col.prop(settings, "Effects_Bokeh_Procedural_Rounding")
                col.prop(settings, "Effects_Bokeh_Procedural_Catadioptric")
                col.prop(settings, "Effects_Bokeh_Procedural_Shift")

        # Chromatic Aberration
        elif item.EffectGroup == "SAC_CHROMATICABERRATION":
            col.prop(settings, "Effects_ChromaticAberration_Amount")
        # Duotone
        elif item.EffectGroup == "SAC_DUOTONE":
            col.prop(settings, "Effects_Duotone_Color1")
            col.prop(settings, "Effects_Duotone_Color2")
            col.prop(settings, "Effects_Duotone_Blend")
        # Emboss
        elif item.EffectGroup == "SAC_EMBOSS":
            col.prop(settings, "Effects_Emboss_Strength")
        # Film Grain
        elif item.EffectGroup == "SAC_FILMGRAIN":
            col.prop(settings, "Filmgrain_strength")
            col.prop(settings, "Filmgrain_dustproportion")
            col.prop(settings, "Filmgrain_size")
        # Fish Eye
        elif item.EffectGroup == "SAC_FISHEYE":
            col.prop(settings, "Effects_Fisheye")
        # Fog Glow
        elif item.EffectGroup == "SAC_FOGGLOW":
            col.prop(settings, "Effects_FogGlow_Strength")
            col.prop(settings, "Effects_FogGlow_Threshold")
            col.prop(settings, "Effects_FogGlow_Size")
        # Ghost
        elif item.EffectGroup == "SAC_GHOST":
            col.prop(settings, "Effects_Ghosts_Strength")
            col.prop(settings, "Effects_Ghosts_Threshold")
            col.prop(settings, "Effects_Ghosts_Count")
            col.prop(settings, "Effects_Ghosts_Distortion")
        # Gradient Map
        elif item.EffectGroup == "SAC_GRADIENTMAP":
            row = col.row(align=True)
            left = row.column(align=True)
            left.scale_x = 1
            left.scale_y = 8
            left.operator("superadvancedcamera.previous_gradient", text="", icon="TRIA_LEFT")
            center = row.column()
            center.template_icon_view(context.scene, "new_gradient_type", show_labels=True, scale=8.0, scale_popup=4.0)
            right = row.column(align=True)
            right.scale_x = 1
            right.scale_y = 8
            right.operator("superadvancedcamera.next_gradient", text="", icon="TRIA_RIGHT")
            center_column = col.row(align=True)
            center_column.label(text="Gradient Name:")
            center_column.label(text=f"{context.scene.new_gradient_type}")
            col.operator("superadvancedcamera.apply_gradient", icon="NODE_TEXTURE")
            col.separator()
            gradient_map_node = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap"]
            col.template_color_ramp(gradient_map_node, "color_ramp")
            col.separator()
            col.prop(settings, "Effects_GradientMap_blend")
        # Halftone
        elif item.EffectGroup == "SAC_HALFTONE":
            col.prop(settings, "Effects_Halftone_value")
            col.prop(settings, "Effects_Halftone_delta")
            col.prop(settings, "Effects_Halftone_size")
        # Infrared
        elif item.EffectGroup == "SAC_INFRARED":
            col.prop(settings, "Effects_Infrared_Blend")
            col.prop(settings, "Effects_Infrared_Offset")
        # ISO Noise
        elif item.EffectGroup == "SAC_ISONOISE":
            col.prop(settings, "ISO_strength")
            col.prop(settings, "ISO_size")
        # Mosaic
        elif item.EffectGroup == "SAC_MOSAIC":
            col.prop(settings, "Effects_Pixelate_PixelSize")
        # Negative
        elif item.EffectGroup == "SAC_NEGATIVE":
            col.prop(settings, "Effects_Negative")
        # Overlay
        elif item.EffectGroup == "SAC_OVERLAY":
            overlay_texture = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay_Texture"]
            col.template_ID(overlay_texture, "image", open="image.open")
            col.prop(settings, "Effects_Overlay_Strength")
        # Perspective Shift
        elif item.EffectGroup == "SAC_PERSPECTIVESHIFT":
            col.prop(settings, "Effects_PerspectiveShift_Horizontal")
            col.prop(settings, "Effects_PerspectiveShift_Vertical")
        # Posterize
        elif item.EffectGroup == "SAC_POSTERIZE":
            col.prop(settings, "Effects_Posterize_Steps")
        # Streaks
        elif item.EffectGroup == "SAC_STREAKS":
            col.prop(settings, "Effects_Streaks_Strength")
            col.prop(settings, "Effects_Streaks_Threshold")
            col.prop(settings, "Effects_Streaks_Count")
            col.prop(settings, "Effects_Streaks_Length")
            col.prop(settings, "Effects_Streaks_Fade")
            col.prop(settings, "Effects_Streaks_Angle")
            col.prop(settings, "Effects_Streaks_Distortion")
        # Vignette
        elif item.EffectGroup == "SAC_VIGNETTE":
            col.prop(settings, "Effects_Vignette_Intensity")
            col.prop(settings, "Effects_Vignette_Roundness")
            col.prop(settings, "Effects_Vignette_Feather")
            col.prop(settings, "Effects_Vignette_Midpoint")
        # Warp
        elif item.EffectGroup == "SAC_WARP":
            col.prop(settings, "Effects_Warp")
        # Error
        else:
            col.label(text="Oops, that's not supposed to happen.")
            col.label(text=f"Effect: {item.EffectGroup} was selected.")
            col.label(text="Please report this to us.")
            col.operator("wm.url_open", text="Our Discord", icon_value=custom_icons["Discord"].icon_id).url = "https://discord.gg/cnFdGQP"

# endregion Effects


# Solcials
class SAC_PT_SOCIALS_Panel(SAC_PT_Panel, Panel):
    bl_label = "Our Socials"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="FUND")

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("wm.url_open", text="Join our Discord!", icon_value=custom_icons["Discord"].icon_id).url = "https://discord.gg/cnFdGQP"
        col.operator("wm.url_open", text="Submit your requests!", icon="TEXT").url = "https://go.pidgeontools.com/2023-08-29-sac-survey"
        row = col.row()
        row.operator("wm.url_open", text="YouTube", icon_value=custom_icons["Youtube"].icon_id).url = "https://www.youtube.com/channel/UCgLo3l_ZzNZ2BCQMYXLiIOg"
        row.operator("wm.url_open", text="BlenderMarket", icon_value=custom_icons["BlenderMarket"].icon_id).url = "https://blendermarket.com/creators/kevin-lorengel"
        row.operator("wm.url_open", text="Instagram", icon_value=custom_icons["Instagram"].icon_id).url = "https://www.instagram.com/pidgeontools/"
        row.operator("wm.url_open", text="Twitter", icon_value=custom_icons["Twitter"].icon_id).url = "https://twitter.com/PidgeonTools"
        col.operator("wm.url_open", text="Support and Feedback!", icon="HELP").url = "https://discord.gg/cnFdGQP"


classes = (
    SAC_PT_SAC_Panel,
    SAC_PT_CAMERA_Panel,
    SAC_PT_CAMERA_CameraSettings_Panel,
    SAC_PT_CAMERA_TiltShift_Panel,
    SAC_PT_CAMERA_Bokeh_Panel,
    SAC_PT_COLORGRADE_Panel,
    SAC_PT_COLORGRADE_Color_Panel,
    SAC_PT_COLORGRADE_Light_Panel,
    SAC_PT_COLORGRADE_Presets_Panel,
    SAC_PT_COLORGRADE_Curves_Panel,
    SAC_PT_COLORGRADE_Colorwheels_Panel,
    SAC_PT_EFFECTS_Panel,
    SAC_PT_List,
    SAC_PT_EFFECTS_Properties_Panel,
    SAC_PT_Info_Panel,
    SAC_PT_SOCIALS_Panel
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

    bpy.utils.previews.remove(custom_icons)
