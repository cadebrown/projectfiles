import bpy
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-ores', metavar='--output-resolution', type=int, nargs=2, default=None, help='Tile sizes')

args, unknown = parser.parse_known_args(sys.argv[sys.argv.index("--")+1:])

if args.ores is not None:
    print ("asdjifalishudfiauosdfhaisdohfuaisduhfh")
    for scene in bpy.data.scenes:
        scene.render.resolution_x = args.ores[0]
        scene.render.resolution_y = args.ores[1]
        scene.render.image_settings.file_format = 'H264'