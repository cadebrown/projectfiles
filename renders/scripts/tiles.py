import bpy
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-ts', metavar='--tile-size', type=int, nargs=2, default=None, help='Tile sizes')
parser.add_argument('-to', metavar='--tile-order', type=str, nargs=1, default=None, help='Tile ordering')

args, unknown = parser.parse_known_args(sys.argv[sys.argv.index("--")+1:])

if args.ts is not None:
    for scene in bpy.data.scenes:
        scene.render.tile_x = args.ts[0]
        scene.render.tile_y = args.ts[1]
    
if args.to is not None:
    for scene in bpy.data.scenes:
        scene.cycles.tile_order = args.to
