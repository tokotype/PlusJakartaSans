#!/bin/sh
set -e

echo "Generating Static fonts"
mkdir -p ../exports
fontmake -g PlusJakartaSans-Display.glyphs -i -o ttf --output-dir ../exports/
fontmake -g PlusJakartaSans-Text.glyphs -i -o ttf --output-dir ../exports/

rm -rf master_ufo/ instance_ufo/


echo "Post processing"
ttfs=$(ls ../exports/*.ttf)
for ttf in $ttfs
do
	gftools fix-dsig -f $ttf;
	ttfautohint $ttf $ttf.fix
	mv "$ttf.fix" $ttf;
	gftools fix-hinting $ttf
	mv "$ttf.fix" $ttf;
done



