import bpy
from bpy.types import (
    Context,
    Operator
)
from .Groups.SuperAdvancedCamera import (create_main_group)

class SAC_OT_Initialize(Operator):
    bl_idname = "object.superadvancedcamerainit"
    bl_label = "Initialize SAC for this scene"
    bl_description = ""

    def execute(self, context: Context):
        create_main_group()

        return {'FINISHED'}