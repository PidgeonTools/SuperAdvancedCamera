bl_info = {
    "name": "Super Advanced Compositor",
    "author": "Kevin Lorengel, Slinc",
    "version": (0, 0, 1),
    "blender": (3, 6, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Compositor",
}

import bpy

from .SAC_Settings import (
    SAC_Settings
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

classes = (
    SAC_PT_SAC_Panel,
    SAC_PT_COLORGRADE_Panel,
    SAC_PT_COLORGRADE_Color_Panel,
    SAC_PT_COLORGRADE_Light_Panel,
    SAC_PT_COLORGRADE_Presets_Panel,
    SAC_PT_COLORGRADE_Curves_Panel,
    SAC_PT_COLORGRADE_Colorwheels_Panel,
    SAC_PT_EFFECTS_Panel,

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