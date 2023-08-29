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
    bl_label = "Initialize SAC for this scene"
    bl_description = ""

    def execute(self, context: Context):
        connect_renderLayer_node()

        return {'FINISHED'}
