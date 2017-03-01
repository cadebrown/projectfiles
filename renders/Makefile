
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

outputresolution=


# DO NOT EDIT BELOW HERE


Bframe_flags=-F $(shell echo $(fmt) | tr a-z A-Z) -f 0
Bpy_args=-- $(tilesize) $(tileorder) $(outputresolution)

$(dir)%: $(dir)%.blend
	$(blender) -b $< -o $(out)$@ -P scripts/tiles.py -P scripts/output.py $(Bframe_flags) $(Bpy_args)
