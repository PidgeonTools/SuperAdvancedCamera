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

from bpy.types import (
    Context,
    Panel,
)

from .SAC_Settings import SAC_Settings


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
        layout.operator("superadvancedcamera.superadvancedcamerainit", icon="SHADERFX")


# Colorgrade

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
        layout.prop(settings, "Colorgrade_Color_WhiteLevel")
        layout.prop(settings, "Colorgrade_Color_Temperature")
        layout.prop(settings, "Colorgrade_Color_Tint")
        layout.prop(settings, "Colorgrade_Color_Saturation")
        layout.prop(settings, "Colorgrade_Color_Hue")


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
        layout.prop(settings, "Colorgrade_Light_Exposure")
        layout.prop(settings, "Colorgrade_Light_Contrast")
        layout.prop(settings, "Colorgrade_Light_Highlights")
        layout.prop(settings, "Colorgrade_Light_Shadows")
        layout.prop(settings, "Colorgrade_Light_Whites")
        layout.prop(settings, "Colorgrade_Light_Darks")


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
        layout.prop(settings, "filter_type")

        row = layout.row(align=True)
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
        center_column = layout.row(align=True)
        center_column.label(text="Filter Name:")
        center_column.label(text=f"{scene.new_filter_type}")
        layout.operator("superadvancedcamera.apply_filter", icon="BRUSHES_ALL")
        layout.prop(settings, "Colorgrade_Filter_Mix")
        layout.separator()
        layout.prop(settings, "Colorgrade_Presets_Sharpen")
        layout.prop(settings, "Colorgrade_Presets_Vibrance")
        layout.prop(settings, "Colorgrade_Presets_Saturation")
        layout.prop(settings, "Colorgrade_Presets_HighlightTint")
        layout.prop(settings, "Colorgrade_Presets_ShadowTint")


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
        layout.template_curve_mapping(rgb_curves_node, "mapping", type='COLOR')
        layout.prop(settings, "Colorgrade_Curves_RGB_Intensity")
        layout.template_curve_mapping(hsv_curves_node, "mapping", type='HUE')
        layout.prop(settings, "Colorgrade_Curves_HSV_Intensity")


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
        layout.alignment = "CENTER"
        layout.label(text="Shadows")
        layout.template_color_picker(color_wheel_node_lift, "lift")
        layout.prop(settings, "Colorgrade_Colorwheel_Shadows_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Shadows_Intensity")
        layout.label(text="Midtones")
        layout.template_color_picker(color_wheel_node_gamma, "gamma")
        layout.prop(settings, "Colorgrade_Colorwheel_Midtones_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Midtones_Intensity")
        layout.label(text="Highlights")
        layout.template_color_picker(color_wheel_node_gain, "gain")
        layout.prop(settings, "Colorgrade_Colorwheel_Highlights_Brightness")
        layout.prop(settings, "Colorgrade_Colorwheel_Highlights_Intensity")
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
        layout.operator("wm.url_open", text="Submit your requests", icon="URL").url = "https://go.pidgeontools.com/2023-08-29-sac-survey"


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
class SAC_PT_EFFECTS_Color_Panel(SAC_PT_Panel, Panel):
    bl_label = "Effect Properties"
    bl_parent_id = "SAC_PT_EFFECTS_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="PROPERTIES")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        # Get the current item from the list
        index = context.scene.sac_effect_list_index
        item = context.scene.sac_effect_list[index] if context.scene.sac_effect_list else None
        if item is None:
            return
        node_group_name = f".{item.EffectGroup}_{item.ID}"

        if item is not None:
            layout.label(text=f"These are settings for {item.name}.")
            # Bokah
            if item.EffectGroup == "SAC_BOKEH":
                # warning that this effect is not viewport compatible
                layout.label(text="This effect is not viewport compatible.", icon="ERROR")
                layout.prop(settings, "Effects_Bokeh_MaxSize")
                layout.prop(settings, "Effects_Bokeh_Offset")
                layout.prop(settings, "Effects_Bokeh_Range")
                layout.separator()
                layout.label(text="Bokeh Type")
                layout_bokeh_type = layout.row(align=True)
                layout_bokeh_type.prop(settings, "Effects_Bokeh_Type", expand=True)

                if settings.Effects_Bokeh_Type == "CAMERA":
                    layout.label(text="Camera Bokeh")

                    row = layout.row(align=True)
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

                    layout.prop(settings, "Effects_Bokeh_Rotation")
                    bokeh_type = context.scene.new_bokeh_type.split("_")
                    layout.label(text="Manufacturer: " + bokeh_type[0])
                    layout.label(text="Model: " + bokeh_type[1] + " - " + bokeh_type[3] + " - " + bokeh_type[2])
                    layout.label(text="Aperture: " + bokeh_type[4])
                    layout.label(text="Special thanks to Prof. Dr. Matt Gunn for the Bokeh textures.")
                    layout.operator("superadvancedcamera.apply_effect_bokeh", icon="SEQ_CHROMA_SCOPE")

                elif settings.Effects_Bokeh_Type == "CUSTOM":
                    layout.label(text="Custom Bokeh")
                    bokeh_image = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Bokeh_Custom_Image"]
                    layout.template_ID(bokeh_image, "image", open="image.open")
                    layout.prop(settings, "Effects_Bokeh_Rotation")

                elif settings.Effects_Bokeh_Type == "PROCEDURAL":
                    layout.label(text="Procedural Bokeh")
                    layout.prop(settings, "Effects_Bokeh_Procedural_Flaps")
                    layout.prop(settings, "Effects_Bokeh_Procedural_Angle")
                    layout.prop(settings, "Effects_Bokeh_Procedural_Rounding")
                    layout.prop(settings, "Effects_Bokeh_Procedural_Catadioptric")
                    layout.prop(settings, "Effects_Bokeh_Procedural_Shift")

            # Chromatic Aberration
            elif item.EffectGroup == "SAC_CHROMATICABERRATION":
                layout.prop(settings, "Effects_ChromaticAberration_Amount")
            # Duotone
            elif item.EffectGroup == "SAC_DUOTONE":
                layout.prop(settings, "Effects_Duotone_Color1")
                layout.prop(settings, "Effects_Duotone_Color2")
                layout.prop(settings, "Effects_Duotone_Blend")
            # Emboss
            elif item.EffectGroup == "SAC_EMBOSS":
                layout.prop(settings, "Effects_Emboss_Strength")
            # Film Grain
            elif item.EffectGroup == "SAC_FILMGRAIN":
                layout.prop(settings, "Filmgrain_strength")
                layout.prop(settings, "Filmgrain_dustproportion")
                layout.prop(settings, "Filmgrain_size")
            # Fish Eye
            elif item.EffectGroup == "SAC_FISHEYE":
                layout.prop(settings, "Effects_Fisheye")
            # Fog Glow
            elif item.EffectGroup == "SAC_FOGGLOW":
                layout.prop(settings, "Effects_FogGlow_Strength")
                layout.prop(settings, "Effects_FogGlow_Threshold")
                layout.prop(settings, "Effects_FogGlow_Size")
            # Ghost
            elif item.EffectGroup == "SAC_GHOST":
                layout.prop(settings, "Effects_Ghosts_Strength")
                layout.prop(settings, "Effects_Ghosts_Threshold")
                layout.prop(settings, "Effects_Ghosts_Count")
                layout.prop(settings, "Effects_Ghosts_Distortion")
            # Gradient Map
            elif item.EffectGroup == "SAC_GRADIENTMAP":
                gradient_map_node = bpy.data.node_groups[node_group_name].nodes["SAC Effects_GradientMap"]
                layout.template_color_ramp(gradient_map_node, "color_ramp")
                layout.prop(settings, "Effects_GradientMap_blend")
            # Halftone
            elif item.EffectGroup == "SAC_HALFTONE":
                layout.prop(settings, "Effects_Halftone_value")
                layout.prop(settings, "Effects_Halftone_delta")
                layout.prop(settings, "Effects_Halftone_size")
            # Infrared
            elif item.EffectGroup == "SAC_INFRARED":
                layout.prop(settings, "Effects_Infrared_Blend")
                layout.prop(settings, "Effects_Infrared_Offset")
            # ISO Noise
            elif item.EffectGroup == "SAC_ISONOISE":
                layout.prop(settings, "ISO_strength")
                layout.prop(settings, "ISO_size")
            # Mosaic
            elif item.EffectGroup == "SAC_MOSAIC":
                layout.prop(settings, "Effects_Pixelate_PixelSize")
            # Negative
            elif item.EffectGroup == "SAC_NEGATIVE":
                layout.prop(settings, "Effects_Negative")
            # Overlay
            elif item.EffectGroup == "SAC_OVERLAY":
                overlay_texture = bpy.data.node_groups[node_group_name].nodes["SAC Effects_Overlay_Texture"]
                layout.template_ID(overlay_texture, "image", open="image.open")
                layout.prop(settings, "Effects_Overlay_Strength")
            # Perspective Shift
            elif item.EffectGroup == "SAC_PERSPECTIVESHIFT":
                layout.prop(settings, "Effects_PerspectiveShift_Horizontal")
                layout.prop(settings, "Effects_PerspectiveShift_Vertical")
            # Posterize
            elif item.EffectGroup == "SAC_POSTERIZE":
                layout.prop(settings, "Effects_Posterize_Steps")
            # Streaks
            elif item.EffectGroup == "SAC_STREAKS":
                layout.prop(settings, "Effects_Streaks_Strength")
                layout.prop(settings, "Effects_Streaks_Threshold")
                layout.prop(settings, "Effects_Streaks_Count")
                layout.prop(settings, "Effects_Streaks_Length")
                layout.prop(settings, "Effects_Streaks_Fade")
                layout.prop(settings, "Effects_Streaks_Angle")
                layout.prop(settings, "Effects_Streaks_Distortion")
            # Vignette
            elif item.EffectGroup == "SAC_VIGNETTE":
                layout.prop(settings, "Effects_Vignette_Intensity")
                layout.prop(settings, "Effects_Vignette_Roundness")
                layout.prop(settings, "Effects_Vignette_Feather")
                layout.prop(settings, "Effects_Vignette_Midpoint")
            # Warp
            elif item.EffectGroup == "SAC_WARP":
                layout.prop(settings, "Effects_Warp")
            # Error
            else:
                layout.label(text="Oops, that's not supposed to happen.")
                layout.label(text=f"Effect: {item.EffectGroup} was selected.")
                layout.label(text="Please report this to us.")
                layout.operator("wm.url_open", text="Our Discord", icon="URL").url = "https://discord.gg/cnFdGQP"
        else:
            layout.label(text="No item selected.")


# endregion Effects

# region Camera
# Camera
class SAC_PT_CAMERA_Panel(SAC_PT_Panel, Panel):
    bl_label = "Camera"
    bl_parent_id = "SAC_PT_SAC_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="OUTLINER_DATA_CAMERA")

    def draw(self, context: Context):
        layout = self.layout


# Tilt Shift
class SAC_PT_CAMERA_TiltShift_Panel(SAC_PT_Panel, Panel):
    bl_label = "Lens Settings"
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        layout = self.layout
        layout.label(text="", icon="MOD_LATTICE")

    def draw(self, context: Context):
        layout = self.layout
        settings = context.scene.sac_settings

        active_obj = bpy.context.view_layer.objects.active
        if active_obj and active_obj.type == 'CAMERA':
            camera = active_obj
            camera_object = bpy.data.objects[camera.name]
            camera_data = bpy.data.cameras[camera_object.data.name]

            if settings.Camera_TiltShift_KeepFrame == True:
                shift_x_text = "Vertical Tilt Shift"
                shift_y_text = "Horizontal Tilt Shift"
            else:
                shift_x_text = "Vertical Lens Shift"
                shift_y_text = "Horizontal Lens Shift"

            layout_shift = layout.column(align=False)
            layout_shift.prop(settings, "Camera_TiltShift_AmountX", text=shift_x_text)
            layout_shift.prop(settings, "Camera_TiltShift_AmountY", text=shift_y_text)
            layout_shift.prop(settings, "Camera_TiltShift_KeepFrame")
            layout.separator()

            layout_focal = layout.column(align=True)
            layout_focal.prop(camera_data, "lens")
            layout_focal.prop(camera_data, "angle")
            layout.separator()

            layout_clip = layout.column(align=True)
            layout_clip.prop(camera_data, "clip_start", text="Min. Visible Distance")
            layout_clip.prop(camera_data, "clip_end", text="Max. Visible Distance")
        else:
            layout.label(text="No camera selected.")


# Bokeh


class SAC_PT_CAMERA_Bokeh_Panel(SAC_PT_Panel, Panel):
    bl_label = ""
    bl_parent_id = "SAC_PT_CAMERA_Panel"

    def draw_header(self, context: Context):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj and active_obj.type == 'CAMERA':
            camera = active_obj
            camera_object = bpy.data.objects[camera.name]
            camera_data = bpy.data.cameras[camera_object.data.name]

        layout = self.layout
        layout.prop(camera_data.dof, "use_dof", text="Bokeh", icon="SEQ_CHROMA_SCOPE")

    def draw(self, context: Context):
        active_obj = bpy.context.view_layer.objects.active
        if active_obj and active_obj.type == 'CAMERA':
            camera = active_obj
            camera_object = bpy.data.objects[camera.name]
            camera_data = bpy.data.cameras[camera_object.data.name]

        layout = self.layout
        layout.active = camera_data.dof.use_dof
        settings = context.scene.sac_settings

        layout.prop(camera_data.dof, "focus_object")
        layout.prop(camera_data.dof, "focus_distance")
        layout.prop(camera_data.dof, "aperture_fstop")
        layout.separator()

        layout.operator("superadvancedcamera.apply_camera_bokeh", icon="SEQ_CHROMA_SCOPE")
        try:
            plane_object = bpy.data.objects[f"{camera.name}_Bokeh_Plane"]
        except:
            layout.label(text="No Bokeh Plane found.")
            layout.label(text="Please apply Bokeh first.")
            return
        layout.separator()
        layout.label(text="Bokeh Type")
        layout_bokeh_type = layout.row(align=True)
        layout_bokeh_type.prop(settings, "Camera_Bokeh_Type", expand=True)

        if settings.Camera_Bokeh_Type == "CAMERA":
            row = layout.row(align=True)
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
            layout.label(text="Manufacturer: " + bokeh_type[0])
            layout.label(text="Model: " + bokeh_type[1] + " - " + bokeh_type[3] + " - " + bokeh_type[2])
            layout.label(text="Aperture: " + bokeh_type[4])
            layout.label(text="Special thanks to Prof. Dr. Matt Gunn for the Bokeh textures.")
            layout.separator()
            layout.prop(settings, "Camera_Bokeh_Scale")
            layout.prop(settings, "Camera_Bokeh_Rotation")
            layout.prop(settings, "Camera_Bokeh_Curves")
        elif settings.Camera_Bokeh_Type == "PROCEDURAL":
            layout.prop(camera_data.dof, "aperture_blades")
            layout.prop(camera_data.dof, "aperture_rotation")
            layout.prop(camera_data.dof, "aperture_ratio")
        elif settings.Camera_Bokeh_Type == "CUSTOM":

            material = bpy.data.materials[f".{camera.name}_Bokeh_Plane_Material"]
            material_node_tree = material.node_tree

            bokeh_image = material_node_tree.nodes["SAC Camera_Bokeh_Custom_Texture"]
            layout.template_ID(bokeh_image, "image", open="image.open")
            layout.prop(settings, "Camera_Bokeh_Scale")
            layout.prop(settings, "Camera_Bokeh_Rotation")
            layout.prop(settings, "Camera_Bokeh_Curves")
# endregion Camera


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
    SAC_PT_EFFECTS_Color_Panel,
    SAC_PT_CAMERA_Panel,
    SAC_PT_CAMERA_TiltShift_Panel,
    SAC_PT_CAMERA_Bokeh_Panel,
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
