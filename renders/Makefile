
###
#
# Makefile targets for blender projects
#
#
###

dir=./
out=./out/

fmt=png

blender=blender

# tilesize=
tilesize=
tileorder=
samples=

outputresolution=


# DO NOT EDIT BELOW HERE

Bframe_flags=-F $(shell echo $(fmt) | tr a-z A-Z) -f 0
Bpy_args=-- -tilesize $(tilesize) -outres $(outputresolution) -samples $(samples)

targets=$(subst .blend,,$(wildcard *.blend))

default: $(targets)

$(dir)%: $(dir)%.blend
	$(blender) -b $< -o $(out)$@ -P scripts/tiles.py -P scripts/configure.py $(Bframe_flags) $(Bpy_args)
