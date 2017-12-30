import bpy
import math
import mathutils
import numpy as np


"""
may need to change this
"""
import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append(home + "/projects/chaudio")

sys.path.append("/usr/local/lib/python3.4")
sys.path.append("/usr/lib/python3.4")


# chaudio is a requirement
import chaudio

#audio_file = chaudio.fromfile(home + "/projects/projectfiles/example_arranged.wav")
audio_file = chaudio.fromfile(home + "/Music/flexing_on_you.wav")


audio_file = chaudio.source.Mono(audio_file)

ctx = bpy.context
ops = bpy.ops

objs = [[] for i in range(0, audio_file.channels)]

# similar to gamma correction for photos
def scale(x, n=1.776):
    sg = -1 if x < 0 else +1
    return sg * abs(x) ** (1.0 / n)

prefix = "chaudiovis"



fps = 24

depth = .01
girth = .25
channel_gap = .25

bars = 240
channels = audio_file.channels
frames = int((audio_file.seconds + bars * depth) * fps) + 1

if frames > fps * 10:
    frames = fps * 10

bpy.ops.object.select_all(action='DESELECT')

for ob in bpy.data.objects:
    if ob.name.startswith(prefix):
        ob.select = True
        
bpy.ops.object.delete()


cube_group = bpy.data.groups.new(prefix + "_GROUP")

print ("channels: " + str(channels))

for o in ctx.selected_objects:
    o.select = False

for i in range(0, bars):
    for j in range(0, channels):
        mesh = bpy.ops.mesh.primitive_cube_add()
        ob = bpy.context.object
        me = ob.data
        nm_suffix = '_' + str(j) + '_' + str(i)
        ob.name = prefix + "_obj" + nm_suffix
        me.name = prefix + "_mesh" + nm_suffix
        ob.location = (2 * i * depth, 2 * j * girth + 2 * j * channel_gap, 1)
        
        ob.select = True
        _pos = bpy.context.scene.cursor_location.copy()

        bpy.context.scene.cursor_location = (2 * i * depth, 2 * j * girth, 0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')

        ob.scale[0] *= depth
        ob.scale[1] *= girth
        

        bpy.context.scene.cursor_location = _pos    
        objs[j] += [ob]
        cube_group.objects.link(ob)


samples_per_frameblock = audio_file.hz / fps
#super_sample = int(audio_file.hz * depth)
super_sample = 5

ctx.scene.frame_start = 0
ctx.scene.frame_end = frames

anim_what = 'scale'

print ("calculating points and keyframing...")


for j in range(0, channels):
    for k in range(0, len(objs[j])):
        o = objs[j][k]
        for i in range(0, frames):
            
            samp_idx = int(i * samples_per_frameblock + k * depth * audio_file.hz - depth * bars * audio_file.hz)
            if samp_idx < 0:
                samps = [0]
            else:
                samps = audio_file[j][samp_idx:samp_idx + super_sample]
            
            o.scale[2] = scale(np.median(samps))
            o.keyframe_insert(data_path=anim_what, frame=i)

print ("done")
