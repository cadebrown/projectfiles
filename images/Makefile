
dir=./
out=./out/

xfc2png=xcf2png

fmt=png

# DO NOT EDIT BELOW HERE


$(dir)%: $(dir)%.xfc
	 $(xfc2png) $< -o $(out)$@.$(fmt)

copy-script: $(CONVERT_SCRIPT)
	cp $(CONVERT_SCRIPT) $(GIMP_SCRIPT_DIR)


