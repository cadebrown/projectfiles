import bpy
import math
import mathutils
ctx = bpy.context
ops = bpy.ops

objs = ctx.selected_objects

ctx.scene.frame_start = 0
ctx.scene.frame_end = 60

ctx.scene.frame_current = 0

ops.anim.keyframe_insert_menu(type='Rotation')
for i in range(0, 60):
    ctx.scene.frame_current = i
    for o in objs:
        o.rotation_euler = mathutils.Euler((i / 60.0, 0, 0), 'XYZ')
    #ops.transform.translate((0, 0, 1.0 / 60))
    ops.anim.keyframe_insert_menu(type='Rotation')

