bl_info = {
    "name": "Zoom To Selection",
    "description": "Adds a right-click option to zoom to the current selection",
    "author": "BlenderMark",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "3D View > Right-click menu",
    "category": "3D View"
}

import bpy


class ZoomToSelection(bpy.types.Operator):
    bl_idname = "view3d.zoom_to_selection"
    bl_label = "Zoom To Selection"
    bl_description = (
        "Zooms the active 3D View to frame the current selection.\n"
        "Works in Object Mode and Edit Mode."
    )

    def execute(self, context):
        bpy.ops.view3d.view_selected(use_all_regions=False)
        return {'FINISHED'}


def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(ZoomToSelection.bl_idname, text="Zoom To Selection")


classes = [
    ZoomToSelection
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)


if __name__ == "__main__":
    register()
