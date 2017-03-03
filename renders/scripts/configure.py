import bpy
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-tilesize', type=int, nargs='*')
parser.add_argument('-outres', type=int, nargs='*')
parser.add_argument('-samples', type=int, nargs='*')

args, unknown = parser.parse_known_args(sys.argv[sys.argv.index("--")+1:])

def is_valid(vv):
    return vv is not None and len(vv) > 0

if is_valid(args.tilesize):
    bpy.context.scene.render.tile_x = args.tilesize[0]
    bpy.context.scene.render.tile_y = args.tilesize[1]
    
if is_valid(args.samples):
    bpy.context.scene.cycles.samples = args.samples[0]

if is_valid(args.outres):
    bpy.context.scene.render.resolution_x = args.outres[0]
    bpy.context.scene.render.resolution_y = args.outres[1]
    bpy.context.scene.render.resolution_percentage = 100
    