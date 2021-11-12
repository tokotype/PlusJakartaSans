#!/bin/sh


set -e

rm -rf ./fonts/static ./fonts/vf ./fonts/webfonts

mkdir -p ./fonts/static ./fonts/vf ./fonts/webfonts 


echo "Generating VFs"

fontmake -g sources/PlusJakartaSans.glyphs -o variable --round-instances --output-path ./fonts/vf/PlusJakartaSans\[wght\].ttf
fontmake -g sources/PlusJakartaSans-Italic.glyphs -o variable --round-instances --output-path ./fonts/vf/PlusJakartaSans-Italic\[wght\].ttf


echo "Generating Statics" ##run fixes on statics as well. 

fontmake -g sources/PlusJakartaSans.glyphs -o ttf --round-instances -a --keep-direction -i --output-dir ./fonts/static/
fontmake -g sources/PlusJakartaSans-Italic.glyphs -o ttf --round-instances -a --keep-direction -i --output-dir ./fonts/static/


echo "Statics Built" ##run fixes on statics as well. 

echo "Removing Build UFOS"

rm -rf master_ufo/ instance_ufo/

echo "Build UFOS Removed"

echo "Post processing"

vfs=$(ls ./fonts/vf/*.ttf)
for vf in $vfs
do
	gftools fix-dsig -f $vf;
	gftools fix-nonhinting $vf "$vf.fix";
	mv "$vf.fix" $vf;
	ttx -f -x "MVAR" $vf; # Drop MVAR. Table has issue in DW
	rtrip=$(basename -s .ttf $vf)
	new_file=./fonts/vf/$rtrip.ttx;
	rm $vf;
	ttx $new_file
	rm ./fonts/vf/*.ttx
done
 rm ./fonts/vf/*backup*.ttf


stat=$(ls ./fonts/static/*.ttf)
for st in $stat
do
	gftools fix-dsig -f $st;
	gftools fix-hinting $st; #if this doesn't work rename as done above and figure diff solution.
	mv "$st.fix" $st;
	ttx -f -x "MVAR" $st; # Drop MVAR. Table has issue in DW
	rtrip=$(basename -s .ttf $st)
	new_file=./fonts/static/$rtrip.ttx;
	rm $st;
	ttx $new_file
	rm ./fonts/static/*.ttx
done
# rm ./fonts/vf/static/*backup*.ttf


echo "Post processing complete"

echo "running fb"
fontbakery check-googlefonts ./fonts/vf/*.ttf --ghmarkdown PlusJakartaSans-vf-checks.md 
echo "finish vf check"

echo "show dir now run static fb checks"
fontbakery check-googlefonts ./fonts/static/*.ttf --ghmarkdown PlusJakartaSans_ttf_checks.md
echo "fb checks done"

mv fonts ../