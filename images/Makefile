
dir=./
out=./out/

xfc2png=xcf2png

fmt=png

targets=$(subst .xfc,,$(wildcard *.xfc))

# DO NOT EDIT BELOW HERE


default: $(targets)

$(dir)%: $(dir)%.xfc
	 $(xfc2png) $< -o $(out)$@.$(fmt)

