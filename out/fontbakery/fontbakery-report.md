## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[1] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** usWinDescent is not the same across the family:
Plus Jakarta Sans Medium Italic: 354
Plus Jakarta Sans Light: 178
Plus Jakarta Sans Medium: 354
Plus Jakarta Sans ExtraBold Italic: 354
Plus Jakarta Sans SemiBold: 354
Plus Jakarta Sans SemiBold Italic: 354
Plus Jakarta Sans ExtraLight Italic: 354
Plus Jakarta Sans: 354
Plus Jakarta Sans Light Italic: 354
Plus Jakarta Sans Bold: 354
Plus Jakarta Sans ExtraLight: 2
Plus Jakarta Sans ExtraBold: 354
Plus Jakarta Sans Italic: 354
Plus Jakarta Sans Bold Italic: 354 [code: usWinDescent-mismatch]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Tbar
	* ae
	* aeacute
	* ampersand
	* arrowboth
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five (U+0035): X=193.0,Y=746.0 (should be at cap-height 745?)

	* five (U+0035): X=573.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=106.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=574.0,Y=746.0 (should be at cap-height 745?)

	* t (U+0074): X=311.0,Y=-1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=78.0,Y=-2.0 (should be at baseline 0?)

	* braceleft (U+007B): X=175.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=94.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=190.0,Y=-2.0 (should be at baseline 0?)

	* macron (U+00AF): X=176.0,Y=743.0 (should be at cap-height 745?)

	* macron (U+00AF): X=464.0,Y=743.0 (should be at cap-height 745?)

	* atilde (U+00E3): X=213.0,Y=744.5 (should be at cap-height 745?)

	* ae (U+00E6): X=287.0,Y=-1.0 (should be at baseline 0?)

	* ntilde (U+00F1): X=215.0,Y=744.5 (should be at cap-height 745?)

	* otilde (U+00F5): X=254.0,Y=744.5 (should be at cap-height 745?)

	* oslash (U+00F8): X=228.5,Y=1.0 (should be at baseline 0?)

	* amacron (U+0101): X=211.0,Y=743.0 (should be at cap-height 745?)

	* amacron (U+0101): X=499.0,Y=743.0 (should be at cap-height 745?)

	* emacron (U+0113): X=231.0,Y=743.0 (should be at cap-height 745?)

	* emacron (U+0113): X=519.0,Y=743.0 (should be at cap-height 745?)

	* itilde (U+0129): X=30.0,Y=744.5 (should be at cap-height 745?)

	* imacron (U+012B): X=28.0,Y=743.0 (should be at cap-height 745?)

	* imacron (U+012B): X=316.0,Y=743.0 (should be at cap-height 745?)

	* omacron (U+014D): X=252.0,Y=743.0 (should be at cap-height 745?)

	* omacron (U+014D): X=540.0,Y=743.0 (should be at cap-height 745?)

	* uni0163 (U+0163): X=311.0,Y=-1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=311.0,Y=-1.0 (should be at baseline 0?)

	* tbar (U+0167): X=311.0,Y=-1.0 (should be at baseline 0?)

	* utilde (U+0169): X=215.0,Y=744.5 (should be at cap-height 745?)

	* umacron (U+016B): X=213.0,Y=743.0 (should be at cap-height 745?)

	* umacron (U+016B): X=501.0,Y=743.0 (should be at cap-height 745?)

	* aeacute (U+01FD): X=287.0,Y=-1.0 (should be at baseline 0?)

	* oslashacute (U+01FF): X=228.5,Y=1.0 (should be at baseline 0?)

	* uni021B (U+021B): X=311.0,Y=-1.0 (should be at baseline 0?)

	* uni022D (U+022D): X=254.0,Y=744.5 (should be at cap-height 745?)

	* uni0233 (U+0233): X=199.0,Y=743.0 (should be at cap-height 745?)

	* uni0233 (U+0233): X=487.0,Y=743.0 (should be at cap-height 745?)

	* tilde (U+02DC): X=206.0,Y=744.5 (should be at cap-height 745?)

	* tildecomb (U+0303): X=206.0,Y=744.5 (should be at cap-height 745?)

	* uni0304 (U+0304): X=176.0,Y=743.0 (should be at cap-height 745?)

	* uni0304 (U+0304): X=464.0,Y=743.0 (should be at cap-height 745?)

	* uni1E15 (U+1E15): X=232.0,Y=743.0 (should be at cap-height 745?)

	* uni1E15 (U+1E15): X=519.0,Y=743.0 (should be at cap-height 745?)

	* uni1E17 (U+1E17): X=224.0,Y=743.0 (should be at cap-height 745?)

	* uni1E17 (U+1E17): X=512.0,Y=743.0 (should be at cap-height 745?)

	* uni1E21 (U+1E21): X=253.0,Y=743.0 (should be at cap-height 745?)

	* uni1E21 (U+1E21): X=541.0,Y=743.0 (should be at cap-height 745?)

	* uni1E4D (U+1E4D): X=254.0,Y=744.5 (should be at cap-height 745?)

	* uni1E4F (U+1E4F): X=254.0,Y=744.5 (should be at cap-height 745?)

	* uni1E51 (U+1E51): X=252.0,Y=743.0 (should be at cap-height 745?)

	* uni1E51 (U+1E51): X=539.0,Y=743.0 (should be at cap-height 745?)

	* uni1E53 (U+1E53): X=245.0,Y=743.0 (should be at cap-height 745?)

	* uni1E53 (U+1E53): X=533.0,Y=743.0 (should be at cap-height 745?)

	* uni1E65 (U+1E65): X=158.0,Y=743.0 (should be at cap-height 745?)

	* uni1E65 (U+1E65): X=270.0,Y=743.0 (should be at cap-height 745?)

	* uni1E6D (U+1E6D): X=311.0,Y=-1.0 (should be at baseline 0?)

	* uni1E6F (U+1E6F): X=311.0,Y=-1.0 (should be at baseline 0?)

	* uni1E79 (U+1E79): X=215.0,Y=744.5 (should be at cap-height 745?)

	* uni1E7B (U+1E7B): X=213.0,Y=743.0 (should be at cap-height 745?)

	* uni1E7B (U+1E7B): X=500.0,Y=743.0 (should be at cap-height 745?)

	* uni1E97 (U+1E97): X=311.0,Y=-1.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=233.0,Y=744.5 (should be at cap-height 745?)

	* uni1EE1 (U+1EE1): X=254.0,Y=744.5 (should be at cap-height 745?)

	* uni1EEF (U+1EEF): X=215.0,Y=744.5 (should be at cap-height 745?)

	* uni1EF9 (U+1EF9): X=201.0,Y=744.5 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=379.0,Y=744.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=91.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=370.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<425.0,220.0>--<417.0,220.0>>

	* e (U+0065) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* ae (U+00E6) contains a short segment L<<419.0,342.0>--<421.0,359.0>>

	* egrave (U+00E8) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* eacute (U+00E9) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* ecircumflex (U+00EA) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* edieresis (U+00EB) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* emacron (U+0113) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* ebreve (U+0115) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* edotaccent (U+0117) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* eogonek (U+0119) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* ecaron (U+011B) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* Eng (U+014A) contains a short segment B<<401.0,-220.0>-<392.0,-220.0>-<379.0,-219.0>>

	* Eng (U+014A) contains a short segment B<<379.0,-219.0>-<366.0,-218.0>-<358.0,-216.0>>

	* eng (U+014B) contains a short segment B<<221.0,-133.0>-<231.0,-134.0>-<241.0,-134.5>>

	* eng (U+014B) contains a short segment B<<241.0,-134.5>-<251.0,-135.0>-<259.0,-135.0>>

	* florin (U+0192) contains a short segment B<<60.5,73.5>-<71.0,73.0>-<76.0,73.0>>

	* florin (U+0192) contains a short segment B<<488.0,671.5>-<477.0,672.0>-<473.0,672.0>>

	* Aringacute (U+01FA) contains a short segment B<<445.0,1043.0>-<447.0,1043.0>-<448.0,1043.0>>

	* aringacute (U+01FB) contains a short segment B<<369.0,836.0>-<371.0,836.0>-<372.0,836.0>>

	* aeacute (U+01FD) contains a short segment L<<419.0,342.0>--<421.0,359.0>>

	* uni0205 (U+0205) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni0207 (U+0207) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni0259 (U+0259) contains a short segment L<<468.0,297.0>--<469.0,303.0>>

	* uni0E3F (U+0E3F) contains a short segment L<<437.0,745.0>--<450.0,745.0>>

	* uni1E15 (U+1E15) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1E17 (U+1E17) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1E1D (U+1E1D) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1E42 (U+1E42) contains a short segment L<<425.0,220.0>--<417.0,220.0>>

	* uni1EB9 (U+1EB9) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EBB (U+1EBB) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EBD (U+1EBD) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EBF (U+1EBF) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EC1 (U+1EC1) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EC3 (U+1EC3) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EC5 (U+1EC5) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* uni1EC7 (U+1EC7) contains a short segment L<<147.0,242.0>--<147.0,236.0>>

	* colonmonetary (U+20A1) contains a short segment B<<416.0,-12.0>-<413.0,-12.0>-<410.0,-12.0>>

	* colonmonetary (U+20A1) contains a short segment L<<462.0,666.0>--<462.0,666.0>>

	* Euro (U+20AC) contains a short segment L<<133.0,333.0>--<133.0,339.0>>

	* Euro (U+20AC) contains a short segment B<<230.0,342.0>-<230.0,337.0>-<231.0,333.0>>

	* uni20B5 (U+20B5) contains a short segment B<<416.0,-12.0>-<413.0,-12.0>-<411.0,-12.0>>

	* uni20BE (U+20BE) contains a short segment B<<456.0,756.0>-<469.0,757.0>-<482.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<505.0,664.0>-<491.0,666.0>-<476.0,666.0>>

	* trademark (U+2122) contains a short segment L<<675.0,414.0>--<664.0,414.0>>

	* estimated (U+212E) contains a short segment B<<215.0,341.0>-<210.0,341.0>-<210.0,335.0>>

	* estimated (U+212E) contains a short segment B<<210.0,140.0>-<210.0,133.0>-<211.5,129.5>>

	* estimated (U+212E) contains a short segment B<<211.5,129.5>-<213.0,126.0>-<220.0,118.0>>

	* estimated (U+212E) contains a short segment B<<673.0,360.0>-<677.0,360.0>-<677.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<666.0,630.0>--<676.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<317.0,541.0>--<307.0,541.0>>

	* integral (U+222B) contains a short segment B<<36.5,-94.5>-<47.0,-95.0>-<51.0,-95.0>>

	* integral (U+222B) contains a short segment B<<487.5,671.5>-<477.0,672.0>-<473.0,672.0>>

	* fi (U+FB01) contains a short segment B<<423.0,669.0>-<415.0,671.0>-<404.5,671.5>>

	* fi (U+FB01) contains a short segment B<<404.5,671.5>-<394.0,672.0>-<390.0,672.0>>

	* fl (U+FB02) contains a short segment B<<423.0,669.0>-<415.0,671.0>-<404.5,671.5>> 

	* fl (U+FB02) contains a short segment B<<404.5,671.5>-<394.0,672.0>-<390.0,672.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[17] PlusJakartaSans-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 178 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Euro
	* Hbar
	* Oslash
	* Oslashacute
	* ae
	* aeacute
	* ampersand
	* colonmonetary
	* dollar
	* f_f_i
	* lira
	* notequal
	* notequal.case
	* oslash
	* oslashacute
	* peseta
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20BA
	* uni20BE
	* uni20BF and yen
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* y (U+0079): X=233.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=114.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=190.0,Y=1.0 (should be at baseline 0?)

	* questiondown (U+00BF): X=238.0,Y=-226.0 (should be at descender -228?)

	* questiondown (U+00BF): X=238.0,Y=-226.0 (should be at descender -228?)

	* Atilde (U+00C3): X=265.0,Y=973.0 (should be at ascender 972?)

	* Ntilde (U+00D1): X=309.0,Y=973.0 (should be at ascender 972?)

	* Otilde (U+00D5): X=381.0,Y=973.0 (should be at ascender 972?)

	* acircumflex (U+00E2): X=294.0,Y=743.0 (should be at cap-height 745?)

	* ecircumflex (U+00EA): X=312.0,Y=743.0 (should be at cap-height 745?)

	* icircumflex (U+00EE): X=96.0,Y=743.0 (should be at cap-height 745?)

	* ocircumflex (U+00F4): X=330.0,Y=743.0 (should be at cap-height 745?)

	* ucircumflex (U+00FB): X=287.0,Y=743.0 (should be at cap-height 745?)

	* yacute (U+00FD): X=233.0,Y=1.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=233.0,Y=1.0 (should be at baseline 0?)

	* ccircumflex (U+0109): X=326.0,Y=743.0 (should be at cap-height 745?)

	* gcircumflex (U+011D): X=332.0,Y=743.0 (should be at cap-height 745?)

	* Itilde (U+0128): X=67.0,Y=973.0 (should be at ascender 972?)

	* jcircumflex (U+0135): X=114.0,Y=743.0 (should be at cap-height 745?)

	* scircumflex (U+015D): X=255.0,Y=743.0 (should be at cap-height 745?)

	* Utilde (U+0168): X=288.0,Y=973.0 (should be at ascender 972?)

	* wcircumflex (U+0175): X=393.0,Y=743.0 (should be at cap-height 745?)

	* ycircumflex (U+0177): X=233.0,Y=1.0 (should be at baseline 0?)

	* ycircumflex (U+0177): X=267.0,Y=743.0 (should be at cap-height 745?)

	* uni0203 (U+0203): X=184.5,Y=744.5 (should be at cap-height 745?)

	* uni0203 (U+0203): X=402.5,Y=744.5 (should be at cap-height 745?)

	* uni0207 (U+0207): X=202.5,Y=744.5 (should be at cap-height 745?)

	* uni0207 (U+0207): X=420.5,Y=744.5 (should be at cap-height 745?)

	* uni020B (U+020B): X=-13.5,Y=744.5 (should be at cap-height 745?)

	* uni020B (U+020B): X=204.5,Y=744.5 (should be at cap-height 745?)

	* uni020F (U+020F): X=220.5,Y=744.5 (should be at cap-height 745?)

	* uni020F (U+020F): X=438.5,Y=744.5 (should be at cap-height 745?)

	* uni0213 (U+0213): X=93.5,Y=744.5 (should be at cap-height 745?)

	* uni0213 (U+0213): X=311.5,Y=744.5 (should be at cap-height 745?)

	* uni0217 (U+0217): X=177.5,Y=744.5 (should be at cap-height 745?)

	* uni0217 (U+0217): X=395.5,Y=744.5 (should be at cap-height 745?)

	* uni022C (U+022C): X=381.0,Y=973.0 (should be at ascender 972?)

	* uni0233 (U+0233): X=233.0,Y=1.0 (should be at baseline 0?)

	* circumflex (U+02C6): X=258.0,Y=743.0 (should be at cap-height 745?)

	* uni0302 (U+0302): X=258.0,Y=743.0 (should be at cap-height 745?)

	* uni0311 (U+0311): X=141.5,Y=744.5 (should be at cap-height 745?)

	* uni0311 (U+0311): X=359.5,Y=744.5 (should be at cap-height 745?)

	* uni1E4C (U+1E4C): X=381.0,Y=973.0 (should be at ascender 972?)

	* uni1E4E (U+1E4E): X=381.0,Y=973.0 (should be at ascender 972?)

	* uni1E78 (U+1E78): X=288.0,Y=973.0 (should be at ascender 972?)

	* uni1E8F (U+1E8F): X=233.0,Y=1.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=404.0,Y=746.0 (should be at cap-height 745?)

	* uni1EAD (U+1EAD): X=294.0,Y=743.0 (should be at cap-height 745?)

	* uni1EBC (U+1EBC): X=269.0,Y=973.0 (should be at ascender 972?)

	* uni1EC3 (U+1EC3): X=421.0,Y=746.0 (should be at cap-height 745?)

	* uni1EC7 (U+1EC7): X=312.0,Y=743.0 (should be at cap-height 745?)

	* uni1ED5 (U+1ED5): X=440.0,Y=746.0 (should be at cap-height 745?)

	* uni1ED9 (U+1ED9): X=330.0,Y=743.0 (should be at cap-height 745?)

	* uni1EE0 (U+1EE0): X=381.0,Y=973.0 (should be at ascender 972?)

	* uni1EEE (U+1EEE): X=288.0,Y=973.0 (should be at ascender 972?)

	* ygrave (U+1EF3): X=233.0,Y=1.0 (should be at baseline 0?)

	* uni1EF5 (U+1EF5): X=233.0,Y=1.0 (should be at baseline 0?)

	* uni1EF7 (U+1EF7): X=233.0,Y=1.0 (should be at baseline 0?)

	* uni1EF8 (U+1EF8): X=253.0,Y=973.0 (should be at ascender 972?)

	* uni1EF9 (U+1EF9): X=233.0,Y=1.0 (should be at baseline 0?)

	* colonmonetary (U+20A1): X=523.0,Y=744.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=549.0,Y=743.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=34.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=299.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment L<<164.0,211.0>--<164.0,218.0>>

	* M (U+004D) contains a short segment L<<415.0,238.0>--<412.0,238.0>>

	* questiondown (U+00BF) contains a short segment L<<323.0,320.0>--<323.0,313.0>>

	* Eng (U+014A) contains a short segment B<<478.0,-220.0>-<469.0,-220.0>-<457.5,-219.0>>

	* Eng (U+014A) contains a short segment B<<457.5,-219.0>-<446.0,-218.0>-<439.0,-215.0>>

	* eng (U+014B) contains a short segment B<<305.0,-219.0>-<294.0,-218.0>-<286.0,-215.0>>

	* uni018F (U+018F) contains a short segment L<<141.0,334.0>--<141.0,329.0>>

	* uni1E42 (U+1E42) contains a short segment L<<415.0,238.0>--<412.0,238.0>>

	* colonmonetary (U+20A1) contains a short segment L<<428.0,757.0>--<429.0,757.0>>

	* trademark (U+2122) contains a short segment L<<625.0,428.0>--<618.0,428.0>>

	* estimated (U+212E) contains a short segment B<<212.0,341.0>-<207.0,341.0>-<207.0,335.0>>

	* estimated (U+212E) contains a short segment B<<207.0,140.0>-<207.0,133.0>-<208.0,129.5>>

	* estimated (U+212E) contains a short segment B<<208.0,129.5>-<209.0,126.0>-<217.0,118.0>>

	* estimated (U+212E) contains a short segment B<<670.0,360.0>-<674.0,360.0>-<674.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<641.0,630.0>--<651.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<267.0,573.0>--<257.0,573.0>>

	* fi (U+FB01) contains a short segment B<<350.0,698.0>-<342.0,699.0>-<331.0,700.0>>

	* fi (U+FB01) contains a short segment B<<331.0,700.0>-<320.0,701.0>-<314.0,701.0>>

	* fl (U+FB02) contains a short segment B<<350.0,698.0>-<342.0,699.0>-<331.0,700.0>> 

	* fl (U+FB02) contains a short segment B<<331.0,700.0>-<320.0,701.0>-<314.0,701.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<106.0,211.0>--<102.0,745.0>>

	* exclam (U+0021): L<<167.0,745.0>--<163.0,211.0>>

	* exclamdown (U+00A1): L<<102.0,-214.0>--<106.0,320.0>> 

	* exclamdown (U+00A1): L<<163.0,320.0>--<167.0,-214.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Tbar
	* ae
	* aeacute
	* ampersand
	* arrowboth
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* emptyset
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* braceleft (U+007B): X=116.0,Y=-2.0 (should be at baseline 0?)

	* braceleft (U+007B): X=214.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=131.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=228.0,Y=-2.0 (should be at baseline 0?)

	* section (U+00A7): X=353.5,Y=1.5 (should be at baseline 0?)

	* macron (U+00AF): X=110.0,Y=743.0 (should be at cap-height 745?)

	* macron (U+00AF): X=397.0,Y=743.0 (should be at cap-height 745?)

	* atilde (U+00E3): X=152.5,Y=744.5 (should be at cap-height 745?)

	* ntilde (U+00F1): X=148.5,Y=744.5 (should be at cap-height 745?)

	* otilde (U+00F5): X=185.5,Y=744.5 (should be at cap-height 745?)

	* amacron (U+0101): X=151.0,Y=743.0 (should be at cap-height 745?)

	* amacron (U+0101): X=438.0,Y=743.0 (should be at cap-height 745?)

	* emacron (U+0113): X=164.0,Y=743.0 (should be at cap-height 745?)

	* emacron (U+0113): X=451.0,Y=743.0 (should be at cap-height 745?)

	* itilde (U+0129): X=-37.5,Y=744.5 (should be at cap-height 745?)

	* imacron (U+012B): X=-39.0,Y=743.0 (should be at cap-height 745?)

	* imacron (U+012B): X=248.0,Y=743.0 (should be at cap-height 745?)

	* omacron (U+014D): X=184.0,Y=743.0 (should be at cap-height 745?)

	* omacron (U+014D): X=471.0,Y=743.0 (should be at cap-height 745?)

	* utilde (U+0169): X=148.5,Y=744.5 (should be at cap-height 745?)

	* umacron (U+016B): X=147.0,Y=743.0 (should be at cap-height 745?)

	* umacron (U+016B): X=434.0,Y=743.0 (should be at cap-height 745?)

	* uni022D (U+022D): X=185.5,Y=744.5 (should be at cap-height 745?)

	* uni0233 (U+0233): X=133.0,Y=743.0 (should be at cap-height 745?)

	* uni0233 (U+0233): X=420.0,Y=743.0 (should be at cap-height 745?)

	* tilde (U+02DC): X=139.5,Y=744.5 (should be at cap-height 745?)

	* tildecomb (U+0303): X=139.5,Y=744.5 (should be at cap-height 745?)

	* uni0304 (U+0304): X=110.0,Y=743.0 (should be at cap-height 745?)

	* uni0304 (U+0304): X=397.0,Y=743.0 (should be at cap-height 745?)

	* uni1E15 (U+1E15): X=164.0,Y=743.0 (should be at cap-height 745?)

	* uni1E15 (U+1E15): X=452.0,Y=743.0 (should be at cap-height 745?)

	* uni1E17 (U+1E17): X=158.0,Y=743.0 (should be at cap-height 745?)

	* uni1E17 (U+1E17): X=445.0,Y=743.0 (should be at cap-height 745?)

	* uni1E21 (U+1E21): X=186.0,Y=743.0 (should be at cap-height 745?)

	* uni1E21 (U+1E21): X=473.0,Y=743.0 (should be at cap-height 745?)

	* uni1E4D (U+1E4D): X=185.5,Y=744.5 (should be at cap-height 745?)

	* uni1E4F (U+1E4F): X=185.5,Y=744.5 (should be at cap-height 745?)

	* uni1E51 (U+1E51): X=184.0,Y=743.0 (should be at cap-height 745?)

	* uni1E51 (U+1E51): X=472.0,Y=743.0 (should be at cap-height 745?)

	* uni1E53 (U+1E53): X=178.0,Y=743.0 (should be at cap-height 745?)

	* uni1E53 (U+1E53): X=465.0,Y=743.0 (should be at cap-height 745?)

	* uni1E65 (U+1E65): X=92.0,Y=743.0 (should be at cap-height 745?)

	* uni1E65 (U+1E65): X=204.0,Y=743.0 (should be at cap-height 745?)

	* uni1E79 (U+1E79): X=148.5,Y=744.5 (should be at cap-height 745?)

	* uni1E7B (U+1E7B): X=146.0,Y=743.0 (should be at cap-height 745?)

	* uni1E7B (U+1E7B): X=434.0,Y=743.0 (should be at cap-height 745?)

	* uni1EBD (U+1EBD): X=165.5,Y=744.5 (should be at cap-height 745?)

	* uni1EE1 (U+1EE1): X=185.5,Y=744.5 (should be at cap-height 745?)

	* uni1EEF (U+1EEF): X=148.5,Y=744.5 (should be at cap-height 745?)

	* uni1EF9 (U+1EF9): X=134.5,Y=744.5 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=333.0,Y=743.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=546.0,Y=744.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=24.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=302.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<432.0,220.0>--<424.0,220.0>>

	* ae (U+00E6) contains a short segment B<<928.0,292.0>-<928.0,281.0>-<927.0,267.5>>

	* Eng (U+014A) contains a short segment B<<470.0,-220.0>-<461.0,-220.0>-<447.5,-219.0>>

	* Eng (U+014A) contains a short segment B<<447.5,-219.0>-<434.0,-218.0>-<426.0,-216.0>>

	* uni018F (U+018F) contains a short segment L<<169.0,318.0>--<169.0,315.0>>

	* aeacute (U+01FD) contains a short segment B<<928.0,292.0>-<928.0,281.0>-<927.0,267.5>>

	* uni1E42 (U+1E42) contains a short segment L<<432.0,220.0>--<424.0,220.0>>

	* uni20AA (U+20AA) contains a short segment B<<459.0,91.0>-<468.0,91.0>-<474.5,97.0>>

	* uni20AA (U+20AA) contains a short segment B<<474.5,97.0>-<481.0,103.0>-<481.0,113.0>>

	* uni20AA (U+20AA) contains a short segment B<<355.0,632.0>-<355.0,641.0>-<349.5,647.0>>

	* uni20AA (U+20AA) contains a short segment B<<349.5,647.0>-<344.0,653.0>-<335.0,653.0>>

	* uni20BA (U+20BA) contains a short segment L<<235.0,90.0>--<252.0,90.0>>

	* uni20BE (U+20BE) contains a short segment B<<408.0,756.0>-<423.0,757.0>-<439.0,757.0>>

	* trademark (U+2122) contains a short segment L<<654.0,414.0>--<643.0,414.0>>

	* estimated (U+212E) contains a short segment B<<201.0,341.0>-<196.0,341.0>-<196.0,335.0>>

	* estimated (U+212E) contains a short segment B<<196.0,140.0>-<196.0,133.0>-<197.0,129.5>>

	* estimated (U+212E) contains a short segment B<<197.0,129.5>-<198.0,126.0>-<206.0,118.0>>

	* estimated (U+212E) contains a short segment B<<659.0,360.0>-<663.0,360.0>-<663.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<662.0,630.0>--<672.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<243.0,541.0>--<233.0,541.0>>

	* fi (U+FB01) contains a short segment B<<364.0,669.0>-<356.0,671.0>-<345.0,671.5>>

	* fi (U+FB01) contains a short segment B<<345.0,671.5>-<334.0,672.0>-<328.0,672.0>>

	* fl (U+FB02) contains a short segment B<<341.5,755.5>-<355.0,754.0>-<364.0,752.0>>

	* fl (U+FB02) contains a short segment B<<364.0,669.0>-<356.0,671.0>-<345.0,671.5>> 

	* fl (U+FB02) contains a short segment B<<345.0,671.5>-<334.0,672.0>-<328.0,672.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Aringacute
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* M
	* Oslash
	* Oslashacute
	* Q
	* Q.ss03
	* Tbar
	* W
	* Wacute
	* Wcircumflex
	* Wdieresis
	* Wgrave
	* ae
	* aeacute
	* ampersand
	* aringacute
	* aringacute.ss01
	* aringacute.ss02
	* aringacute.ss03
	* arrowboth
	* arrowdown
	* arrowleft
	* arrowright
	* arrowup
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* h.ss01
	* hbar
	* hbar.ss01
	* hbar.ss03
	* hcircumflex.ss01
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* partialdiff
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni030A0301
	* uni0E3F
	* uni1E25.ss01
	* uni1E2B.ss01
	* uni1E42
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2196
	* uni2197
	* uni2198
	* uni2199
	* uni21A9
	* uni21AA
	* uni21B0
	* uni21B1
	* uni21B2
	* uni21B3
	* uni2B0E
	* uni2B10 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans ExtraBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=438.0,Y=747.0 (should be at cap-height 745?)

	* seven (U+0037): X=93.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=600.0,Y=746.0 (should be at cap-height 745?)

	* a (U+0061): X=282.5,Y=1.0 (should be at baseline 0?)

	* d (U+0064): X=372.5,Y=-0.5 (should be at baseline 0?)

	* h (U+0068): X=300.0,Y=544.5 (should be at x-height 546?)

	* section (U+00A7): X=442.0,Y=0.5 (should be at baseline 0?)

	* Atilde (U+00C3): X=552.5,Y=971.5 (should be at ascender 972?)

	* Ntilde (U+00D1): X=557.5,Y=971.5 (should be at ascender 972?)

	* Otilde (U+00D5): X=627.5,Y=971.5 (should be at ascender 972?)

	* agrave (U+00E0): X=282.5,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=282.5,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=282.5,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=282.5,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=282.5,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=282.5,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=383.5,Y=746.0 (should be at cap-height 745?)

	* amacron (U+0101): X=282.5,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=282.5,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=282.5,Y=1.0 (should be at baseline 0?)

	* dcaron (U+010F): X=372.5,Y=-0.5 (should be at baseline 0?)

	* dcroat (U+0111): X=372.5,Y=-0.5 (should be at baseline 0?)

	* Itilde (U+0128): X=330.5,Y=971.5 (should be at ascender 972?)

	* Utilde (U+0168): X=548.5,Y=971.5 (should be at ascender 972?)

	* uring (U+016F): X=391.5,Y=746.0 (should be at cap-height 745?)

	* uni01C6 (U+01C6): X=372.5,Y=-0.5 (should be at baseline 0?)

	* aringacute (U+01FB): X=282.5,Y=1.0 (should be at baseline 0?)

	* aringacute (U+01FB): X=383.5,Y=746.0 (should be at cap-height 745?)

	* uni0201 (U+0201): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni0203 (U+0203): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni022C (U+022C): X=627.5,Y=971.5 (should be at ascender 972?)

	* uni022D (U+022D): X=256.0,Y=970.0 (should be at ascender 972?)

	* uni022D (U+022D): X=596.0,Y=970.0 (should be at ascender 972?)

	* ring (U+02DA): X=350.5,Y=746.0 (should be at cap-height 745?)

	* uni030A (U+030A): X=350.5,Y=746.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=195.0,Y=743.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=199.0,Y=743.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=214.5,Y=744.5 (should be at cap-height 745?)

	* uni0E3F (U+0E3F): X=456.0,Y=744.0 (should be at cap-height 745?)

	* uni1E0D (U+1E0D): X=372.5,Y=-0.5 (should be at baseline 0?)

	* uni1E0F (U+1E0F): X=372.5,Y=-0.5 (should be at baseline 0?)

	* uni1E4C (U+1E4C): X=627.5,Y=971.5 (should be at ascender 972?)

	* uni1E4E (U+1E4E): X=627.5,Y=971.5 (should be at ascender 972?)

	* uni1E78 (U+1E78): X=548.5,Y=971.5 (should be at ascender 972?)

	* uni1EA1 (U+1EA1): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EA2 (U+1EA2): X=401.0,Y=973.0 (should be at ascender 972?)

	* uni1EA2 (U+1EA2): X=375.0,Y=971.5 (should be at ascender 972?)

	* uni1EA3 (U+1EA3): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EA5 (U+1EA5): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EA7 (U+1EA7): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EA8 (U+1EA8): X=615.0,Y=974.0 (should be at ascender 972?)

	* uni1EA9 (U+1EA9): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=625.0,Y=747.0 (should be at cap-height 745?)

	* uni1EAB (U+1EAB): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EAD (U+1EAD): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EAE (U+1EAE): X=417.5,Y=973.5 (should be at ascender 972?)

	* uni1EAF (U+1EAF): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EB0 (U+1EB0): X=416.5,Y=973.5 (should be at ascender 972?)

	* uni1EB1 (U+1EB1): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EB2 (U+1EB2): X=417.5,Y=973.5 (should be at ascender 972?)

	* uni1EB3 (U+1EB3): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EB5 (U+1EB5): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EB7 (U+1EB7): X=282.5,Y=1.0 (should be at baseline 0?)

	* uni1EBA (U+1EBA): X=352.0,Y=973.0 (should be at ascender 972?)

	* uni1EBA (U+1EBA): X=326.0,Y=971.5 (should be at ascender 972?)

	* uni1EBC (U+1EBC): X=503.5,Y=971.5 (should be at ascender 972?)

	* uni1EC2 (U+1EC2): X=566.0,Y=974.0 (should be at ascender 972?)

	* uni1EC3 (U+1EC3): X=639.0,Y=747.0 (should be at cap-height 745?)

	* uni1EC8 (U+1EC8): X=179.0,Y=973.0 (should be at ascender 972?)

	* uni1EC8 (U+1EC8): X=153.0,Y=971.5 (should be at ascender 972?)

	* uni1ECE (U+1ECE): X=476.0,Y=973.0 (should be at ascender 972?)

	* uni1ECE (U+1ECE): X=450.0,Y=971.5 (should be at ascender 972?)

	* uni1ED4 (U+1ED4): X=690.0,Y=974.0 (should be at ascender 972?)

	* uni1ED5 (U+1ED5): X=661.0,Y=747.0 (should be at cap-height 745?)

	* uni1EDE (U+1EDE): X=476.0,Y=973.0 (should be at ascender 972?)

	* uni1EDE (U+1EDE): X=450.0,Y=971.5 (should be at ascender 972?)

	* uni1EE0 (U+1EE0): X=627.5,Y=971.5 (should be at ascender 972?)

	* uni1EE6 (U+1EE6): X=397.0,Y=973.0 (should be at ascender 972?)

	* uni1EE6 (U+1EE6): X=371.0,Y=971.5 (should be at ascender 972?)

	* uni1EEC (U+1EEC): X=397.0,Y=973.0 (should be at ascender 972?)

	* uni1EEC (U+1EEC): X=371.0,Y=971.5 (should be at ascender 972?)

	* uni1EEE (U+1EEE): X=548.5,Y=971.5 (should be at ascender 972?)

	* uni1EF6 (U+1EF6): X=371.0,Y=973.0 (should be at ascender 972?)

	* uni1EF6 (U+1EF6): X=345.0,Y=971.5 (should be at ascender 972?)

	* uni1EF8 (U+1EF8): X=522.5,Y=971.5 (should be at ascender 972?)

	* uni2077 (U+2077): X=77.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=439.0,Y=746.0 (should be at cap-height 745?)

	* uni208D (U+208D): X=192.0,Y=-1.5 (should be at baseline 0?)

	* colonmonetary (U+20A1): X=324.0,Y=-2.0 (should be at baseline 0?)

	* uni20B5 (U+20B5): X=325.0,Y=-2.0 (should be at baseline 0?)

	* uni20BE (U+20BE): X=378.0,Y=744.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=598.0,Y=743.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=79.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=371.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* six (U+0036) contains a short segment B<<349.0,478.0>-<352.0,478.0>-<355.0,478.0>>

	* nine (U+0039) contains a short segment B<<286.0,267.0>-<283.0,267.0>-<280.0,267.0>>

	* M (U+004D) contains a short segment L<<454.0,190.0>--<434.0,190.0>>

	* a (U+0061) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* f (U+0066) contains a short segment L<<159.0,546.0>--<161.0,558.0>>

	* f (U+0066) contains a short segment B<<425.0,627.0>-<418.0,627.0>-<413.0,627.0>>

	* t (U+0074) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* ordfeminine (U+00AA) contains a short segment L<<317.0,606.0>--<318.0,615.0>>

	* agrave (U+00E0) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* aacute (U+00E1) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* acircumflex (U+00E2) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* atilde (U+00E3) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* adieresis (U+00E4) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* aring (U+00E5) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* ae (U+00E6) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* amacron (U+0101) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* abreve (U+0103) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* aogonek (U+0105) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* eng (U+014B) contains a short segment B<<225.0,-90.0>-<233.0,-91.0>-<241.0,-91.5>>

	* eng (U+014B) contains a short segment B<<241.0,-91.5>-<249.0,-92.0>-<255.0,-92.0>>

	* uni0163 (U+0163) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* tcaron (U+0165) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* tbar (U+0167) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* florin (U+0192) contains a short segment B<<101.0,118.5>-<108.0,118.0>-<113.0,118.0>>

	* florin (U+0192) contains a short segment B<<531.0,627.0>-<524.0,627.0>-<519.0,627.0>>

	* Uhorn (U+01AF) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* aringacute (U+01FB) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* aeacute (U+01FD) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni0201 (U+0201) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni0203 (U+0203) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni021B (U+021B) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* uni031B (U+031B) contains a short segment L<<195.0,743.0>--<199.0,743.0>>

	* uni1E42 (U+1E42) contains a short segment L<<454.0,190.0>--<434.0,190.0>>

	* uni1E6D (U+1E6D) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* uni1E6F (U+1E6F) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* uni1E97 (U+1E97) contains a short segment L<<56.0,546.0>--<58.0,546.0>>

	* uni1EA1 (U+1EA1) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EA3 (U+1EA3) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EA5 (U+1EA5) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EA7 (U+1EA7) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EA9 (U+1EA9) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EAB (U+1EAB) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EAD (U+1EAD) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EAF (U+1EAF) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EB1 (U+1EB1) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EB3 (U+1EB3) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EB5 (U+1EB5) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EB7 (U+1EB7) contains a short segment L<<387.0,346.0>--<389.0,360.0>>

	* uni1EE8 (U+1EE8) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* uni1EEA (U+1EEA) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* uni1EEC (U+1EEC) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* uni1EEE (U+1EEE) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* uni1EF0 (U+1EF0) contains a short segment B<<707.0,745.0>-<717.0,745.0>-<729.5,748.5>>

	* lira (U+20A4) contains a short segment L<<163.0,488.0>--<166.0,509.0>>

	* uni20AA (U+20AA) contains a short segment B<<400.0,154.0>-<408.0,154.0>-<415.0,160.5>>

	* uni20AA (U+20AA) contains a short segment B<<415.0,160.5>-<422.0,167.0>-<423.0,175.0>>

	* uni20AD (U+20AD) contains a short segment L<<288.0,418.0>--<303.0,418.0>>

	* uni20B1 (U+20B1) contains a short segment L<<695.0,523.0>--<695.0,520.0>>

	* uni20B1 (U+20B1) contains a short segment B<<539.0,520.0>-<539.0,520.0>-<539.0,520.5>>

	* uni20B1 (U+20B1) contains a short segment B<<539.0,520.5>-<539.0,521.0>-<539.0,523.0>>

	* uni20BE (U+20BE) contains a short segment B<<470.0,757.0>-<476.0,757.0>-<483.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<483.0,757.0>-<496.0,757.0>-<509.0,756.0>>

	* uni20BE (U+20BE) contains a short segment B<<490.0,617.0>-<481.0,617.0>-<472.0,617.0>>

	* uni20BE (U+20BE) contains a short segment B<<472.0,617.0>-<461.0,617.0>-<450.0,616.0>>

	* estimated (U+212E) contains a short segment B<<198.0,341.0>-<193.0,341.0>-<193.0,335.0>>

	* estimated (U+212E) contains a short segment B<<193.0,140.0>-<193.0,133.0>-<194.5,129.5>>

	* estimated (U+212E) contains a short segment B<<194.5,129.5>-<196.0,126.0>-<203.0,118.0>>

	* estimated (U+212E) contains a short segment B<<656.0,360.0>-<660.0,360.0>-<660.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<704.0,630.0>--<714.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<341.0,500.0>--<331.0,500.0>>

	* integral (U+222B) contains a short segment B<<78.5,-49.5>-<86.0,-50.0>-<90.0,-50.0>>

	* integral (U+222B) contains a short segment B<<532.0,627.0>-<525.0,627.0>-<520.0,627.0>>

	* fi (U+FB01) contains a short segment L<<159.0,546.0>--<161.0,558.0>>

	* fi (U+FB01) contains a short segment B<<442.0,625.0>-<432.0,627.0>-<425.0,627.0>>

	* fi (U+FB01) contains a short segment B<<425.0,627.0>-<418.0,627.0>-<413.0,627.0>>

	* fl (U+FB02) contains a short segment L<<159.0,546.0>--<161.0,558.0>>

	* fl (U+FB02) contains a short segment B<<442.0,625.0>-<432.0,627.0>-<425.0,627.0>> 

	* fl (U+FB02) contains a short segment B<<425.0,627.0>-<418.0,627.0>-<413.0,627.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Tbar
	* ae
	* aeacute
	* ampersand
	* arrowboth
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2198 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* uni00B3 (U+00B3): X=53.0,Y=746.0 (should be at cap-height 745?)

	* uni00B3 (U+00B3): X=373.0,Y=746.0 (should be at cap-height 745?)

	* cedilla (U+00B8): X=168.0,Y=-226.0 (should be at descender -228?)

	* uni00B9 (U+00B9): X=18.0,Y=746.0 (should be at cap-height 745?)

	* uni00B9 (U+00B9): X=216.0,Y=746.0 (should be at cap-height 745?)

	* Ccedilla (U+00C7): X=377.0,Y=-226.0 (should be at descender -228?)

	* Oslash (U+00D8): X=546.5,Y=743.0 (should be at cap-height 745?)

	* Oslash (U+00D8): X=331.5,Y=2.0 (should be at baseline 0?)

	* ccedilla (U+00E7): X=275.0,Y=-226.0 (should be at descender -228?)

	* oslash (U+00F8): X=245.5,Y=-1.0 (should be at baseline 0?)

	* Scedilla (U+015E): X=291.0,Y=-226.0 (should be at descender -228?)

	* scedilla (U+015F): X=209.0,Y=-226.0 (should be at descender -228?)

	* uni0162 (U+0162): X=219.0,Y=-226.0 (should be at descender -228?)

	* uni0163 (U+0163): X=245.0,Y=-226.0 (should be at descender -228?)

	* Oslashacute (U+01FE): X=546.5,Y=743.0 (should be at cap-height 745?)

	* Oslashacute (U+01FE): X=331.5,Y=2.0 (should be at baseline 0?)

	* oslashacute (U+01FF): X=245.5,Y=-1.0 (should be at baseline 0?)

	* breve (U+02D8): X=247.0,Y=747.0 (should be at cap-height 745?)

	* breve (U+02D8): X=358.0,Y=747.0 (should be at cap-height 745?)

	* uni0306 (U+0306): X=247.0,Y=747.0 (should be at cap-height 745?)

	* uni0306 (U+0306): X=358.0,Y=747.0 (should be at cap-height 745?)

	* hookabovecomb (U+0309): X=221.0,Y=747.0 (should be at cap-height 745?)

	* uni0327 (U+0327): X=168.0,Y=-226.0 (should be at descender -228?)

	* uni032E (U+032E): X=199.0,Y=-227.5 (should be at descender -228?)

	* uni1E08 (U+1E08): X=377.0,Y=-226.0 (should be at descender -228?)

	* uni1E09 (U+1E09): X=275.0,Y=-226.0 (should be at descender -228?)

	* uni1E1C (U+1E1C): X=275.0,Y=-226.0 (should be at descender -228?)

	* uni1E1D (U+1E1D): X=260.0,Y=-226.0 (should be at descender -228?)

	* uni1E2A (U+1E2A): X=264.0,Y=-227.5 (should be at descender -228?)

	* uni1E2B (U+1E2B): X=190.0,Y=-227.5 (should be at descender -228?)

	* uni1EA3 (U+1EA3): X=289.0,Y=747.0 (should be at cap-height 745?)

	* uni1EAB (U+1EAB): X=298.5,Y=971.5 (should be at ascender 972?)

	* uni1EAF (U+1EAF): X=239.0,Y=747.0 (should be at cap-height 745?)

	* uni1EAF (U+1EAF): X=350.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB1 (U+1EB1): X=239.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB1 (U+1EB1): X=350.5,Y=747.0 (should be at cap-height 745?)

	* uni1EB3 (U+1EB3): X=239.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB3 (U+1EB3): X=350.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB5 (U+1EB5): X=297.5,Y=971.5 (should be at ascender 972?)

	* uni1EB5 (U+1EB5): X=239.0,Y=744.0 (should be at cap-height 745?)

	* uni1EB5 (U+1EB5): X=350.0,Y=744.0 (should be at cap-height 745?)

	* uni1EBB (U+1EBB): X=301.0,Y=747.0 (should be at cap-height 745?)

	* uni1EC5 (U+1EC5): X=311.5,Y=971.5 (should be at ascender 972?)

	* uni1EC9 (U+1EC9): X=103.0,Y=747.0 (should be at cap-height 745?)

	* uni1ECF (U+1ECF): X=321.0,Y=747.0 (should be at cap-height 745?)

	* uni1ED7 (U+1ED7): X=331.5,Y=971.5 (should be at ascender 972?)

	* uni1EDF (U+1EDF): X=321.0,Y=747.0 (should be at cap-height 745?)

	* uni1EE7 (U+1EE7): X=288.0,Y=747.0 (should be at cap-height 745?)

	* uni1EED (U+1EED): X=288.0,Y=747.0 (should be at cap-height 745?)

	* uni1EF7 (U+1EF7): X=279.0,Y=747.0 (should be at cap-height 745?)

	* uni2074 (U+2074): X=264.0,Y=746.0 (should be at cap-height 745?)

	* uni2074 (U+2074): X=366.0,Y=746.0 (should be at cap-height 745?)

	* uni2075 (U+2075): X=93.0,Y=746.0 (should be at cap-height 745?)

	* uni2075 (U+2075): X=379.0,Y=746.0 (should be at cap-height 745?)

	* uni2076 (U+2076): X=241.0,Y=746.0 (should be at cap-height 745?)

	* uni2076 (U+2076): X=358.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=20.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=367.0,Y=746.0 (should be at cap-height 745?)

	* colonmonetary (U+20A1): X=330.0,Y=-1.0 (should be at baseline 0?)

	* uni20BE (U+20BE): X=332.0,Y=743.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=547.0,Y=744.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=20.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=303.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<443.0,210.0>--<431.0,210.0>>

	* ae (U+00E6) contains a short segment L<<399.0,343.0>--<399.0,364.0>>

	* Eng (U+014A) contains a short segment B<<467.0,-221.0>-<456.0,-221.0>-<442.0,-220.0>>

	* Eng (U+014A) contains a short segment B<<442.0,-220.0>-<428.0,-219.0>-<420.0,-216.0>>

	* aeacute (U+01FD) contains a short segment L<<399.0,343.0>--<399.0,364.0>>

	* uni0E3F (U+0E3F) contains a short segment L<<380.0,745.0>--<391.0,745.0>>

	* uni1E42 (U+1E42) contains a short segment L<<443.0,210.0>--<431.0,210.0>>

	* colonmonetary (U+20A1) contains a short segment B<<424.0,650.0>-<422.0,650.0>-<421.0,649.0>>

	* uni20BA (U+20BA) contains a short segment L<<246.0,105.0>--<265.0,105.0>>

	* uni20BE (U+20BE) contains a short segment B<<412.0,756.0>-<426.0,757.0>-<440.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<440.0,757.0>-<453.0,757.0>-<467.0,756.0>>

	* uni20BE (U+20BE) contains a short segment B<<467.0,648.0>-<453.0,650.0>-<439.0,650.0>>

	* uni20BE (U+20BE) contains a short segment B<<439.0,650.0>-<425.0,650.0>-<412.0,648.0>>

	* trademark (U+2122) contains a short segment L<<672.0,409.0>--<659.0,409.0>>

	* estimated (U+212E) contains a short segment B<<195.0,341.0>-<190.0,341.0>-<190.0,335.0>>

	* estimated (U+212E) contains a short segment B<<190.0,140.0>-<190.0,133.0>-<191.5,129.5>>

	* estimated (U+212E) contains a short segment B<<191.5,129.5>-<193.0,126.0>-<200.0,118.0>>

	* estimated (U+212E) contains a short segment B<<653.0,360.0>-<657.0,360.0>-<657.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<675.0,630.0>--<685.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<235.0,528.0>--<225.0,528.0>>

	* fi (U+FB01) contains a short segment B<<372.0,654.0>-<364.0,656.0>-<354.0,656.5>>

	* fi (U+FB01) contains a short segment B<<354.0,656.5>-<344.0,657.0>-<338.0,657.0>>

	* fl (U+FB02) contains a short segment B<<349.0,755.5>-<363.0,754.0>-<372.0,752.0>>

	* fl (U+FB02) contains a short segment B<<372.0,654.0>-<364.0,656.0>-<354.0,656.5>> 

	* fl (U+FB02) contains a short segment B<<354.0,656.5>-<344.0,657.0>-<338.0,657.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Tbar
	* ae
	* aeacute
	* ampersand
	* arrowboth
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2198 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* dollar (U+0024): X=434.0,Y=747.0 (should be at cap-height 745?)

	* five (U+0035): X=187.0,Y=746.0 (should be at cap-height 745?)

	* five (U+0035): X=577.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=102.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=583.0,Y=746.0 (should be at cap-height 745?)

	* Q (U+0051): X=537.0,Y=1.0 (should be at baseline 0?)

	* q (U+0071): X=385.0,Y=2.0 (should be at baseline 0?)

	* t (U+0074): X=325.0,Y=-1.0 (should be at baseline 0?)

	* y (U+0079): X=49.0,Y=542.0 (should be at x-height 541?)

	* y (U+0079): X=166.0,Y=542.0 (should be at x-height 541?)

	* y (U+0079): X=469.0,Y=542.0 (should be at x-height 541?)

	* y (U+0079): X=596.0,Y=542.0 (should be at x-height 541?)

	* uni00B3 (U+00B3): X=106.0,Y=746.0 (should be at cap-height 745?)

	* uni00B3 (U+00B3): X=432.0,Y=746.0 (should be at cap-height 745?)

	* cedilla (U+00B8): X=98.0,Y=-226.0 (should be at descender -228?)

	* uni00B9 (U+00B9): X=84.0,Y=746.0 (should be at cap-height 745?)

	* uni00B9 (U+00B9): X=284.0,Y=746.0 (should be at cap-height 745?)

	* Ccedilla (U+00C7): X=337.0,Y=-226.0 (should be at descender -228?)

	* atilde (U+00E3): X=444.5,Y=746.0 (should be at cap-height 745?)

	* ccedilla (U+00E7): X=228.0,Y=-226.0 (should be at descender -228?)

	* ntilde (U+00F1): X=448.5,Y=746.0 (should be at cap-height 745?)

	* otilde (U+00F5): X=483.5,Y=746.0 (should be at cap-height 745?)

	* itilde (U+0129): X=265.5,Y=746.0 (should be at cap-height 745?)

	* Scedilla (U+015E): X=208.0,Y=-226.0 (should be at descender -228?)

	* scedilla (U+015F): X=139.0,Y=-226.0 (should be at descender -228?)

	* uni0162 (U+0162): X=150.0,Y=-226.0 (should be at descender -228?)

	* uni0163 (U+0163): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni0163 (U+0163): X=177.0,Y=-226.0 (should be at descender -228?)

	* tcaron (U+0165): X=325.0,Y=-1.0 (should be at baseline 0?)

	* tbar (U+0167): X=325.0,Y=-1.0 (should be at baseline 0?)

	* utilde (U+0169): X=448.5,Y=746.0 (should be at cap-height 745?)

	* uni021B (U+021B): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni022D (U+022D): X=483.5,Y=746.0 (should be at cap-height 745?)

	* breve (U+02D8): X=313.0,Y=747.0 (should be at cap-height 745?)

	* breve (U+02D8): X=425.0,Y=747.0 (should be at cap-height 745?)

	* tilde (U+02DC): X=455.5,Y=746.0 (should be at cap-height 745?)

	* tildecomb (U+0303): X=455.5,Y=746.0 (should be at cap-height 745?)

	* uni0306 (U+0306): X=313.0,Y=747.0 (should be at cap-height 745?)

	* uni0306 (U+0306): X=425.0,Y=747.0 (should be at cap-height 745?)

	* hookabovecomb (U+0309): X=402.0,Y=743.0 (should be at cap-height 745?)

	* uni0327 (U+0327): X=98.0,Y=-226.0 (should be at descender -228?)

	* uni032E (U+032E): X=132.0,Y=-227.0 (should be at descender -228?)

	* uni1E08 (U+1E08): X=337.0,Y=-226.0 (should be at descender -228?)

	* uni1E09 (U+1E09): X=228.0,Y=-226.0 (should be at descender -228?)

	* uni1E1C (U+1E1C): X=206.0,Y=-226.0 (should be at descender -228?)

	* uni1E1D (U+1E1D): X=191.0,Y=-226.0 (should be at descender -228?)

	* uni1E2A (U+1E2A): X=197.0,Y=-227.0 (should be at descender -228?)

	* uni1E2B (U+1E2B): X=123.0,Y=-227.0 (should be at descender -228?)

	* uni1E4D (U+1E4D): X=483.5,Y=746.0 (should be at cap-height 745?)

	* uni1E4F (U+1E4F): X=483.5,Y=746.0 (should be at cap-height 745?)

	* uni1E6D (U+1E6D): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni1E6F (U+1E6F): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni1E79 (U+1E79): X=448.5,Y=746.0 (should be at cap-height 745?)

	* uni1E97 (U+1E97): X=325.0,Y=-1.0 (should be at baseline 0?)

	* uni1EA3 (U+1EA3): X=465.0,Y=743.0 (should be at cap-height 745?)

	* uni1EAB (U+1EAB): X=392.0,Y=971.5 (should be at ascender 972?)

	* uni1EAF (U+1EAF): X=301.5,Y=747.0 (should be at cap-height 745?)

	* uni1EAF (U+1EAF): X=412.5,Y=747.0 (should be at cap-height 745?)

	* uni1EB1 (U+1EB1): X=301.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB1 (U+1EB1): X=412.0,Y=747.0 (should be at cap-height 745?)

	* uni1EB3 (U+1EB3): X=301.5,Y=747.0 (should be at cap-height 745?)

	* uni1EB3 (U+1EB3): X=412.5,Y=747.0 (should be at cap-height 745?)

	* uni1EB5 (U+1EB5): X=391.0,Y=971.5 (should be at ascender 972?)

	* uni1EB5 (U+1EB5): X=300.5,Y=744.0 (should be at cap-height 745?)

	* uni1EB5 (U+1EB5): X=411.5,Y=744.0 (should be at cap-height 745?)

	* uni1EBB (U+1EBB): X=483.0,Y=743.0 (should be at cap-height 745?)

	* uni1EBD (U+1EBD): X=462.5,Y=746.0 (should be at cap-height 745?)

	* uni1EC5 (U+1EC5): X=410.0,Y=971.5 (should be at ascender 972?)

	* uni1EC9 (U+1EC9): X=286.0,Y=743.0 (should be at cap-height 745?)

	* uni1ECF (U+1ECF): X=504.0,Y=743.0 (should be at cap-height 745?)

	* uni1ED7 (U+1ED7): X=431.0,Y=971.5 (should be at ascender 972?)

	* uni1EDF (U+1EDF): X=504.0,Y=743.0 (should be at cap-height 745?)

	* uni1EE1 (U+1EE1): X=483.5,Y=746.0 (should be at cap-height 745?)

	* uni1EE7 (U+1EE7): X=469.0,Y=743.0 (should be at cap-height 745?)

	* uni1EED (U+1EED): X=469.0,Y=743.0 (should be at cap-height 745?)

	* uni1EEF (U+1EEF): X=448.5,Y=746.0 (should be at cap-height 745?)

	* uni1EF7 (U+1EF7): X=460.0,Y=743.0 (should be at cap-height 745?)

	* uni1EF9 (U+1EF9): X=439.5,Y=746.0 (should be at cap-height 745?)

	* uni2074 (U+2074): X=330.0,Y=746.0 (should be at cap-height 745?)

	* uni2074 (U+2074): X=434.0,Y=746.0 (should be at cap-height 745?)

	* uni2075 (U+2075): X=150.0,Y=746.0 (should be at cap-height 745?)

	* uni2075 (U+2075): X=431.0,Y=746.0 (should be at cap-height 745?)

	* uni2076 (U+2076): X=295.0,Y=746.0 (should be at cap-height 745?)

	* uni2076 (U+2076): X=418.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=86.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=434.0,Y=746.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=379.0,Y=744.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=594.0,Y=743.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=87.0,Y=746.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=370.0,Y=746.0 (should be at cap-height 745?)

	* arrowupdn (U+2195): X=408.0,Y=-229.0 (should be at descender -228?) 

	* arrowupdn (U+2195): X=357.0,Y=-229.0 (should be at descender -228?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<435.0,210.0>--<423.0,210.0>>

	* f (U+0066) contains a short segment B<<411.5,656.5>-<402.0,657.0>-<398.0,657.0>>

	* t (U+0074) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* ordfeminine (U+00AA) contains a short segment L<<335.0,608.0>--<336.0,618.0>>

	* ae (U+00E6) contains a short segment L<<409.0,344.0>--<411.0,360.0>>

	* Eng (U+014A) contains a short segment B<<398.0,-221.0>-<387.0,-221.0>-<373.0,-220.0>>

	* Eng (U+014A) contains a short segment B<<373.0,-220.0>-<359.0,-219.0>-<352.0,-216.0>>

	* eng (U+014B) contains a short segment B<<223.0,-118.0>-<232.0,-120.0>-<241.0,-120.5>>

	* eng (U+014B) contains a short segment B<<241.0,-120.5>-<250.0,-121.0>-<258.0,-121.0>>

	* uni0163 (U+0163) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* tcaron (U+0165) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* tbar (U+0167) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* florin (U+0192) contains a short segment B<<74.5,88.5>-<84.0,88.0>-<88.0,88.0>>

	* florin (U+0192) contains a short segment B<<502.5,656.5>-<493.0,657.0>-<489.0,657.0>>

	* aeacute (U+01FD) contains a short segment L<<409.0,344.0>--<411.0,360.0>>

	* uni021B (U+021B) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* uni0E3F (U+0E3F) contains a short segment L<<443.0,745.0>--<445.0,745.0>>

	* uni1E42 (U+1E42) contains a short segment L<<435.0,210.0>--<423.0,210.0>>

	* uni1E6D (U+1E6D) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* uni1E6F (U+1E6F) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* uni1E97 (U+1E97) contains a short segment L<<64.0,541.0>--<76.0,541.0>>

	* uni20AA (U+20AA) contains a short segment B<<422.0,112.0>-<430.0,112.0>-<438.0,119.0>>

	* Euro (U+20AC) contains a short segment L<<128.0,338.0>--<128.0,339.0>>

	* Euro (U+20AC) contains a short segment B<<244.0,344.0>-<244.0,340.0>-<244.0,338.0>>

	* uni20B1 (U+20B1) contains a short segment B<<676.0,538.0>-<676.0,531.0>-<676.0,524.0>>

	* uni20B2 (U+20B2) contains a short segment L<<413.0,-12.0>--<413.0,-12.0>>

	* uni20BE (U+20BE) contains a short segment B<<460.0,756.0>-<471.0,757.0>-<483.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<500.0,648.0>-<488.0,650.0>-<474.0,650.0>>

	* uni20BE (U+20BE) contains a short segment B<<474.0,650.0>-<460.0,650.0>-<445.0,648.0>>

	* trademark (U+2122) contains a short segment L<<692.0,409.0>--<679.0,409.0>>

	* estimated (U+212E) contains a short segment B<<210.0,341.0>-<205.0,341.0>-<205.0,335.0>>

	* estimated (U+212E) contains a short segment B<<205.0,140.0>-<205.0,133.0>-<206.0,129.5>>

	* estimated (U+212E) contains a short segment B<<206.0,129.5>-<207.0,126.0>-<215.0,118.0>>

	* estimated (U+212E) contains a short segment B<<668.0,360.0>-<672.0,360.0>-<672.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<679.0,630.0>--<689.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<325.0,528.0>--<315.0,528.0>>

	* integral (U+222B) contains a short segment B<<50.5,-79.5>-<60.0,-80.0>-<64.0,-80.0>>

	* integral (U+222B) contains a short segment B<<502.5,656.5>-<493.0,657.0>-<489.0,657.0>>

	* fi (U+FB01) contains a short segment B<<429.0,655.0>-<421.0,656.0>-<411.5,656.5>>

	* fi (U+FB01) contains a short segment B<<411.5,656.5>-<402.0,657.0>-<398.0,657.0>>

	* fl (U+FB02) contains a short segment B<<429.0,655.0>-<421.0,656.0>-<411.5,656.5>> 

	* fl (U+FB02) contains a short segment B<<411.5,656.5>-<402.0,657.0>-<398.0,657.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[15] PlusJakartaSans-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* colonmonetary
	* uni20A6
	* uni20A9
	* uni20B1 and uni20B3
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans ExtraLight' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* dollar (U+0024) contains a short segment B<<357.0,757.0>-<361.0,757.0>-<366.0,757.0>>

	* dollar (U+0024) contains a short segment B<<310.0,-12.0>-<306.0,-12.0>-<303.0,-12.0>>

	* dollar (U+0024) contains a short segment L<<309.0,31.0>--<311.0,31.0>>

	* question (U+003F) contains a short segment L<<180.0,208.0>--<181.0,212.0>>

	* M (U+004D) contains a short segment L<<408.0,246.0>--<406.0,246.0>>

	* e (U+0065) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* cent (U+00A2) contains a short segment L<<326.0,140.0>--<327.0,140.0>>

	* cent (U+00A2) contains a short segment B<<327.0,98.0>-<323.0,98.0>-<320.0,98.0>>

	* questiondown (U+00BF) contains a short segment L<<293.0,318.0>--<292.0,314.0>>

	* ae (U+00E6) contains a short segment L<<450.0,334.0>--<453.0,356.0>>

	* egrave (U+00E8) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* eacute (U+00E9) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* ecircumflex (U+00EA) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* edieresis (U+00EB) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* emacron (U+0113) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* ebreve (U+0115) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* edotaccent (U+0117) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* eogonek (U+0119) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* ecaron (U+011B) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* eng (U+014B) contains a short segment B<<244.0,-218.0>-<234.0,-216.0>-<226.0,-214.0>>

	* eng (U+014B) contains a short segment B<<228.0,-174.0>-<236.0,-175.0>-<245.5,-176.0>>

	* eng (U+014B) contains a short segment B<<245.5,-176.0>-<255.0,-177.0>-<262.0,-177.0>>

	* uni018F (U+018F) contains a short segment B<<738.0,388.0>-<738.0,393.0>-<738.0,399.0>>

	* uni018F (U+018F) contains a short segment B<<143.0,324.0>-<143.0,322.0>-<143.0,317.0>>

	* aeacute (U+01FD) contains a short segment L<<450.0,334.0>--<453.0,356.0>>

	* uni0205 (U+0205) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni0207 (U+0207) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni0259 (U+0259) contains a short segment B<<516.0,277.0>-<516.0,280.0>-<516.0,284.0>>

	* uni1E15 (U+1E15) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1E17 (U+1E17) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1E1D (U+1E1D) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1E42 (U+1E42) contains a short segment L<<408.0,246.0>--<406.0,246.0>>

	* uni1EB9 (U+1EB9) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EBB (U+1EBB) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EBD (U+1EBD) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EBF (U+1EBF) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EC1 (U+1EC1) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EC3 (U+1EC3) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EC5 (U+1EC5) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* uni1EC7 (U+1EC7) contains a short segment B<<112.0,249.0>-<112.0,246.0>-<112.0,242.0>>

	* Euro (U+20AC) contains a short segment B<<145.0,318.0>-<145.0,328.0>-<145.0,339.0>>

	* Euro (U+20AC) contains a short segment B<<195.0,342.0>-<195.0,330.0>-<196.0,318.0>>

	* uni20B2 (U+20B2) contains a short segment B<<476.0,757.0>-<479.0,757.0>-<481.0,757.0>>

	* uni20B2 (U+20B2) contains a short segment B<<424.0,-12.0>-<421.0,-12.0>-<418.0,-12.0>>

	* uni20B2 (U+20B2) contains a short segment L<<425.0,36.0>--<426.0,36.0>>

	* uni20B5 (U+20B5) contains a short segment B<<404.0,36.0>-<410.0,36.0>-<417.0,36.0>>

	* uni20B5 (U+20B5) contains a short segment B<<418.0,-12.0>-<408.0,-12.0>-<397.0,-11.0>>

	* uni20BF (U+20BF) contains a short segment B<<455.0,745.0>-<461.0,745.0>-<467.0,745.0>>

	* trademark (U+2122) contains a short segment L<<638.0,435.0>--<634.0,435.0>>

	* estimated (U+212E) contains a short segment B<<233.0,341.0>-<228.0,341.0>-<228.0,335.0>>

	* estimated (U+212E) contains a short segment B<<228.0,140.0>-<228.0,133.0>-<229.5,129.5>>

	* estimated (U+212E) contains a short segment B<<229.5,129.5>-<231.0,126.0>-<238.0,118.0>>

	* estimated (U+212E) contains a short segment B<<691.0,360.0>-<695.0,360.0>-<695.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<636.0,630.0>--<646.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<309.0,590.0>--<299.0,590.0>>

	* fi (U+FB01) contains a short segment B<<409.0,711.0>-<401.0,713.0>-<391.5,713.5>>

	* fi (U+FB01) contains a short segment B<<391.5,713.5>-<382.0,714.0>-<375.0,714.0>>

	* fl (U+FB02) contains a short segment B<<409.0,711.0>-<401.0,713.0>-<391.5,713.5>> 

	* fl (U+FB02) contains a short segment B<<391.5,713.5>-<382.0,714.0>-<375.0,714.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[15] PlusJakartaSans-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Euro
	* Hbar
	* Oslash
	* Oslashacute
	* ae
	* aeacute
	* ampersand
	* cent
	* colonmonetary
	* dollar
	* emptyset
	* f_f_i
	* f_f_l
	* lira
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20BA
	* uni20BE
	* uni20BF and yen
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* braceleft (U+007B): X=112.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=192.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=125.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=205.0,Y=1.0 (should be at baseline 0?)

	* uni00B5 (U+00B5): X=199.0,Y=-0.5 (should be at baseline 0?)

	* cedilla (U+00B8): X=207.0,Y=-230.0 (should be at descender -228?)

	* cedilla (U+00B8): X=207.0,Y=-230.0 (should be at descender -228?)

	* Ccedilla (U+00C7): X=440.0,Y=-230.0 (should be at descender -228?)

	* Ccedilla (U+00C7): X=440.0,Y=-230.0 (should be at descender -228?)

	* ccedilla (U+00E7): X=334.0,Y=-230.0 (should be at descender -228?)

	* ccedilla (U+00E7): X=334.0,Y=-230.0 (should be at descender -228?)

	* oslash (U+00F8): X=243.0,Y=1.0 (should be at baseline 0?)

	* Aogonek (U+0104): X=569.0,Y=-230.0 (should be at descender -228?)

	* Aogonek (U+0104): X=569.0,Y=-230.0 (should be at descender -228?)

	* aogonek (U+0105): X=428.0,Y=-230.0 (should be at descender -228?)

	* aogonek (U+0105): X=428.0,Y=-230.0 (should be at descender -228?)

	* Eogonek (U+0118): X=438.0,Y=-230.0 (should be at descender -228?)

	* Eogonek (U+0118): X=438.0,Y=-230.0 (should be at descender -228?)

	* eogonek (U+0119): X=291.0,Y=-230.0 (should be at descender -228?)

	* eogonek (U+0119): X=291.0,Y=-230.0 (should be at descender -228?)

	* Iogonek (U+012E): X=108.0,Y=-230.0 (should be at descender -228?)

	* Iogonek (U+012E): X=108.0,Y=-230.0 (should be at descender -228?)

	* iogonek (U+012F): X=90.0,Y=-230.0 (should be at descender -228?)

	* iogonek (U+012F): X=90.0,Y=-230.0 (should be at descender -228?)

	* Scedilla (U+015E): X=351.0,Y=-230.0 (should be at descender -228?)

	* Scedilla (U+015E): X=351.0,Y=-230.0 (should be at descender -228?)

	* scedilla (U+015F): X=267.0,Y=-230.0 (should be at descender -228?)

	* scedilla (U+015F): X=267.0,Y=-230.0 (should be at descender -228?)

	* uni0162 (U+0162): X=268.0,Y=-230.0 (should be at descender -228?)

	* uni0162 (U+0162): X=268.0,Y=-230.0 (should be at descender -228?)

	* uni0163 (U+0163): X=286.0,Y=-230.0 (should be at descender -228?)

	* uni0163 (U+0163): X=286.0,Y=-230.0 (should be at descender -228?)

	* Uogonek (U+0172): X=340.0,Y=-230.0 (should be at descender -228?)

	* Uogonek (U+0172): X=340.0,Y=-230.0 (should be at descender -228?)

	* uogonek (U+0173): X=429.0,Y=-230.0 (should be at descender -228?)

	* uogonek (U+0173): X=429.0,Y=-230.0 (should be at descender -228?)

	* uni01EA (U+01EA): X=459.0,Y=-230.0 (should be at descender -228?)

	* uni01EA (U+01EA): X=459.0,Y=-230.0 (should be at descender -228?)

	* uni01EB (U+01EB): X=348.0,Y=-230.0 (should be at descender -228?)

	* uni01EB (U+01EB): X=348.0,Y=-230.0 (should be at descender -228?)

	* oslashacute (U+01FF): X=243.0,Y=1.0 (should be at baseline 0?)

	* ogonek (U+02DB): X=220.0,Y=-230.0 (should be at descender -228?)

	* ogonek (U+02DB): X=220.0,Y=-230.0 (should be at descender -228?)

	* hookabovecomb (U+0309): X=167.0,Y=743.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=242.0,Y=747.0 (should be at cap-height 745?)

	* uni0327 (U+0327): X=207.0,Y=-230.0 (should be at descender -228?)

	* uni0327 (U+0327): X=207.0,Y=-230.0 (should be at descender -228?)

	* uni0328 (U+0328): X=220.0,Y=-230.0 (should be at descender -228?)

	* uni0328 (U+0328): X=220.0,Y=-230.0 (should be at descender -228?)

	* uni1E08 (U+1E08): X=440.0,Y=-230.0 (should be at descender -228?)

	* uni1E08 (U+1E08): X=440.0,Y=-230.0 (should be at descender -228?)

	* uni1E09 (U+1E09): X=334.0,Y=-230.0 (should be at descender -228?)

	* uni1E09 (U+1E09): X=334.0,Y=-230.0 (should be at descender -228?)

	* uni1E1C (U+1E1C): X=340.0,Y=-230.0 (should be at descender -228?)

	* uni1E1C (U+1E1C): X=340.0,Y=-230.0 (should be at descender -228?)

	* uni1E1D (U+1E1D): X=320.0,Y=-230.0 (should be at descender -228?)

	* uni1E1D (U+1E1D): X=320.0,Y=-230.0 (should be at descender -228?)

	* uni1EA3 (U+1EA3): X=265.0,Y=743.0 (should be at cap-height 745?)

	* uni1EAB (U+1EAB): X=242.0,Y=970.0 (should be at ascender 972?)

	* uni1EB5 (U+1EB5): X=240.0,Y=970.0 (should be at ascender 972?)

	* uni1EBB (U+1EBB): X=279.0,Y=743.0 (should be at cap-height 745?)

	* uni1EC5 (U+1EC5): X=256.0,Y=970.0 (should be at ascender 972?)

	* uni1EC9 (U+1EC9): X=70.0,Y=743.0 (should be at cap-height 745?)

	* uni1ECF (U+1ECF): X=299.0,Y=743.0 (should be at cap-height 745?)

	* uni1ED7 (U+1ED7): X=276.0,Y=970.0 (should be at ascender 972?)

	* uni1EDF (U+1EDF): X=299.0,Y=743.0 (should be at cap-height 745?)

	* uni1EE7 (U+1EE7): X=258.0,Y=743.0 (should be at cap-height 745?)

	* uni1EED (U+1EED): X=258.0,Y=743.0 (should be at cap-height 745?)

	* uni1EF7 (U+1EF7): X=239.0,Y=743.0 (should be at cap-height 745?)

	* colonmonetary (U+20A1): X=329.0,Y=1.0 (should be at baseline 0?)

	* uni20BE (U+20BE): X=334.0,Y=743.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=544.0,Y=743.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=28.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=302.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment L<<167.0,214.0>--<167.0,224.0>>

	* M (U+004D) contains a short segment L<<420.0,230.0>--<416.0,230.0>>

	* questiondown (U+00BF) contains a short segment L<<332.0,322.0>--<332.0,312.0>>

	* ae (U+00E6) contains a short segment B<<928.0,293.0>-<928.0,283.0>-<927.0,270.5>>

	* Eng (U+014A) contains a short segment B<<473.0,-220.0>-<466.0,-220.0>-<453.5,-219.0>>

	* Eng (U+014A) contains a short segment B<<453.5,-219.0>-<441.0,-218.0>-<433.0,-216.0>>

	* eng (U+014B) contains a short segment B<<320.0,-220.0>-<313.0,-220.0>-<300.5,-219.0>>

	* aeacute (U+01FD) contains a short segment B<<928.0,293.0>-<928.0,283.0>-<927.0,270.5>>

	* uni1E42 (U+1E42) contains a short segment L<<420.0,230.0>--<416.0,230.0>>

	* colonmonetary (U+20A1) contains a short segment B<<428.0,682.0>-<426.0,682.0>-<424.0,682.0>>

	* uni20AA (U+20AA) contains a short segment B<<472.0,70.0>-<482.0,70.0>-<488.5,77.0>>

	* uni20AA (U+20AA) contains a short segment B<<488.5,77.0>-<495.0,84.0>-<495.0,94.0>>

	* uni20AA (U+20AA) contains a short segment B<<360.0,651.0>-<360.0,661.0>-<354.0,667.5>>

	* uni20AA (U+20AA) contains a short segment B<<354.0,667.5>-<348.0,674.0>-<339.0,674.0>>

	* uni20BA (U+20BA) contains a short segment L<<224.0,75.0>--<239.0,75.0>>

	* trademark (U+2122) contains a short segment L<<636.0,420.0>--<627.0,420.0>>

	* estimated (U+212E) contains a short segment B<<206.0,341.0>-<201.0,341.0>-<201.0,335.0>>

	* estimated (U+212E) contains a short segment B<<201.0,140.0>-<201.0,133.0>-<202.5,129.5>>

	* estimated (U+212E) contains a short segment B<<202.5,129.5>-<204.0,126.0>-<211.0,118.0>>

	* estimated (U+212E) contains a short segment B<<664.0,360.0>-<668.0,360.0>-<668.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<649.0,630.0>--<659.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<251.0,555.0>--<241.0,555.0>>

	* fi (U+FB01) contains a short segment B<<334.0,755.5>-<347.0,754.0>-<355.0,752.0>>

	* fi (U+FB01) contains a short segment B<<355.0,684.0>-<348.0,686.0>-<336.0,686.5>>

	* fi (U+FB01) contains a short segment B<<336.0,686.5>-<324.0,687.0>-<319.0,687.0>>

	* fl (U+FB02) contains a short segment B<<311.0,757.0>-<321.0,757.0>-<334.0,755.5>>

	* fl (U+FB02) contains a short segment B<<334.0,755.5>-<347.0,754.0>-<355.0,752.0>>

	* fl (U+FB02) contains a short segment B<<355.0,684.0>-<348.0,686.0>-<336.0,686.5>> 

	* fl (U+FB02) contains a short segment B<<336.0,686.5>-<324.0,687.0>-<319.0,687.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[16] PlusJakartaSans-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Euro
	* Hbar
	* Oslash
	* Oslashacute
	* ampersand
	* colonmonetary
	* dollar
	* f_f_i
	* lira
	* notequal
	* notequal.case
	* oslash
	* oslashacute
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20BA
	* uni20BE
	* uni20BF and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans Light' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* five (U+0035): X=202.0,Y=746.0 (should be at cap-height 745?)

	* five (U+0035): X=567.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=110.0,Y=746.0 (should be at cap-height 745?)

	* seven (U+0037): X=557.0,Y=746.0 (should be at cap-height 745?)

	* t (U+0074): X=287.0,Y=-2.0 (should be at baseline 0?)

	* y (U+0079): X=58.0,Y=532.0 (should be at x-height 531?)

	* y (U+0079): X=122.0,Y=532.0 (should be at x-height 531?)

	* y (U+0079): X=485.0,Y=532.0 (should be at x-height 531?)

	* y (U+0079): X=555.0,Y=532.0 (should be at x-height 531?)

	* braceleft (U+007B): X=78.0,Y=1.0 (should be at baseline 0?)

	* braceright (U+007D): X=153.0,Y=1.0 (should be at baseline 0?)

	* questiondown (U+00BF): X=182.0,Y=-226.0 (should be at descender -228?)

	* questiondown (U+00BF): X=182.0,Y=-226.0 (should be at descender -228?)

	* Atilde (U+00C3): X=364.0,Y=973.0 (should be at ascender 972?)

	* Aring (U+00C5): X=381.5,Y=971.0 (should be at ascender 972?)

	* Ntilde (U+00D1): X=409.0,Y=973.0 (should be at ascender 972?)

	* Otilde (U+00D5): X=482.0,Y=973.0 (should be at ascender 972?)

	* Itilde (U+0128): X=167.0,Y=973.0 (should be at ascender 972?)

	* uni0163 (U+0163): X=287.0,Y=-2.0 (should be at baseline 0?)

	* tcaron (U+0165): X=287.0,Y=-2.0 (should be at baseline 0?)

	* tbar (U+0167): X=287.0,Y=-2.0 (should be at baseline 0?)

	* Utilde (U+0168): X=388.0,Y=973.0 (should be at ascender 972?)

	* Uring (U+016E): X=405.5,Y=971.0 (should be at ascender 972?)

	* Aringacute (U+01FA): X=381.5,Y=971.0 (should be at ascender 972?)

	* uni0203 (U+0203): X=242.5,Y=744.0 (should be at cap-height 745?)

	* uni0203 (U+0203): X=462.5,Y=743.0 (should be at cap-height 745?)

	* uni0207 (U+0207): X=267.5,Y=744.0 (should be at cap-height 745?)

	* uni0207 (U+0207): X=487.5,Y=743.0 (should be at cap-height 745?)

	* uni020B (U+020B): X=51.5,Y=744.0 (should be at cap-height 745?)

	* uni020B (U+020B): X=271.5,Y=743.0 (should be at cap-height 745?)

	* uni020F (U+020F): X=286.5,Y=744.0 (should be at cap-height 745?)

	* uni020F (U+020F): X=506.5,Y=743.0 (should be at cap-height 745?)

	* uni0213 (U+0213): X=158.5,Y=744.0 (should be at cap-height 745?)

	* uni0213 (U+0213): X=378.5,Y=743.0 (should be at cap-height 745?)

	* uni0217 (U+0217): X=242.5,Y=744.0 (should be at cap-height 745?)

	* uni0217 (U+0217): X=462.5,Y=743.0 (should be at cap-height 745?)

	* uni021B (U+021B): X=287.0,Y=-2.0 (should be at baseline 0?)

	* uni022C (U+022C): X=482.0,Y=973.0 (should be at ascender 972?)

	* uni0311 (U+0311): X=205.5,Y=744.0 (should be at cap-height 745?)

	* uni0311 (U+0311): X=425.5,Y=743.0 (should be at cap-height 745?)

	* uni1E4C (U+1E4C): X=482.0,Y=973.0 (should be at ascender 972?)

	* uni1E4E (U+1E4E): X=482.0,Y=973.0 (should be at ascender 972?)

	* uni1E6D (U+1E6D): X=287.0,Y=-2.0 (should be at baseline 0?)

	* uni1E6F (U+1E6F): X=287.0,Y=-2.0 (should be at baseline 0?)

	* uni1E78 (U+1E78): X=388.0,Y=973.0 (should be at ascender 972?)

	* uni1E97 (U+1E97): X=287.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=465.0,Y=746.0 (should be at cap-height 745?)

	* uni1EBC (U+1EBC): X=369.0,Y=973.0 (should be at ascender 972?)

	* uni1EC3 (U+1EC3): X=490.0,Y=746.0 (should be at cap-height 745?)

	* uni1ED5 (U+1ED5): X=509.0,Y=746.0 (should be at cap-height 745?)

	* uni1EE0 (U+1EE0): X=482.0,Y=973.0 (should be at ascender 972?)

	* uni1EEE (U+1EEE): X=388.0,Y=973.0 (should be at ascender 972?)

	* uni1EF8 (U+1EF8): X=352.0,Y=973.0 (should be at ascender 972?)

	* uni20BE (U+20BE): X=382.0,Y=743.0 (should be at cap-height 745?)

	* uni20BF (U+20BF): X=405.0,Y=1.0 (should be at baseline 0?)

	* seveneighths (U+215E): X=102.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=367.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* dollar (U+0024) contains a short segment B<<357.0,757.0>-<360.0,757.0>-<363.0,757.0>>

	* question (U+003F) contains a short segment L<<183.0,211.0>--<185.0,218.0>>

	* M (U+004D) contains a short segment L<<412.0,238.0>--<409.0,238.0>>

	* e (U+0065) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* questiondown (U+00BF) contains a short segment L<<304.0,320.0>--<302.0,313.0>>

	* ae (U+00E6) contains a short segment L<<440.0,338.0>--<443.0,358.0>>

	* egrave (U+00E8) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* eacute (U+00E9) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* ecircumflex (U+00EA) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* edieresis (U+00EB) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* emacron (U+0113) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* ebreve (U+0115) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* edotaccent (U+0117) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* eogonek (U+0119) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* ecaron (U+011B) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* Eng (U+014A) contains a short segment B<<410.0,-220.0>-<401.0,-220.0>-<389.5,-219.0>>

	* Eng (U+014A) contains a short segment B<<389.5,-219.0>-<378.0,-218.0>-<372.0,-215.0>>

	* florin (U+0192) contains a short segment B<<43.5,45.5>-<54.0,45.0>-<59.0,45.0>>

	* aeacute (U+01FD) contains a short segment L<<440.0,338.0>--<443.0,358.0>>

	* uni0205 (U+0205) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni0207 (U+0207) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni0259 (U+0259) contains a short segment B<<499.0,284.0>-<500.0,289.0>-<500.0,294.0>>

	* uni1E15 (U+1E15) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1E17 (U+1E17) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1E1D (U+1E1D) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1E42 (U+1E42) contains a short segment L<<412.0,238.0>--<409.0,238.0>>

	* uni1EB9 (U+1EB9) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EBB (U+1EBB) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EBD (U+1EBD) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EBF (U+1EBF) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EC1 (U+1EC1) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EC3 (U+1EC3) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EC5 (U+1EC5) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* uni1EC7 (U+1EC7) contains a short segment B<<123.0,247.0>-<123.0,242.0>-<123.0,237.0>>

	* colonmonetary (U+20A1) contains a short segment B<<467.0,696.0>-<463.0,696.0>-<461.0,695.0>>

	* Euro (U+20AC) contains a short segment B<<142.0,323.0>-<141.0,331.0>-<142.0,339.0>>

	* Euro (U+20AC) contains a short segment B<<206.0,342.0>-<206.0,332.0>-<206.0,323.0>>

	* uni20B2 (U+20B2) contains a short segment B<<420.0,-12.0>-<416.0,-12.0>-<413.0,-12.0>>

	* uni20B2 (U+20B2) contains a short segment L<<422.0,50.0>--<425.0,50.0>>

	* uni20B5 (U+20B5) contains a short segment L<<412.0,50.0>--<418.0,50.0>>

	* uni20B5 (U+20B5) contains a short segment B<<417.0,-12.0>-<410.0,-12.0>-<403.0,-12.0>>

	* trademark (U+2122) contains a short segment L<<648.0,428.0>--<642.0,428.0>>

	* estimated (U+212E) contains a short segment B<<227.0,341.0>-<222.0,341.0>-<222.0,335.0>>

	* estimated (U+212E) contains a short segment B<<222.0,140.0>-<222.0,133.0>-<223.5,129.5>>

	* estimated (U+212E) contains a short segment B<<223.5,129.5>-<225.0,126.0>-<232.0,118.0>>

	* estimated (U+212E) contains a short segment B<<685.0,360.0>-<689.0,360.0>-<689.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<645.0,630.0>--<655.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<309.0,573.0>--<299.0,573.0>>

	* fi (U+FB01) contains a short segment B<<413.0,698.0>-<405.0,699.0>-<394.5,700.0>>

	* fi (U+FB01) contains a short segment B<<394.5,700.0>-<384.0,701.0>-<379.0,701.0>>

	* fl (U+FB02) contains a short segment B<<413.0,698.0>-<405.0,699.0>-<394.5,700.0>> 

	* fl (U+FB02) contains a short segment B<<394.5,700.0>-<384.0,701.0>-<379.0,701.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[15] PlusJakartaSans-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Aringacute
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Q.ss03
	* Tbar
	* ae
	* aeacute
	* ampersand
	* aringacute
	* aringacute.ss01
	* aringacute.ss02
	* aringacute.ss03
	* arrowboth
	* arrowdown
	* arrowleft
	* arrowright
	* arrowup
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2196
	* uni2197
	* uni2198
	* uni2199
	* uni21A9
	* uni21AA
	* uni21B0
	* uni21B1
	* uni21B2
	* uni21B3
	* uni2B0E
	* uni2B10 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<455.0,200.0>--<439.0,200.0>>

	* t (U+0074) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* ordfeminine (U+00AA) contains a short segment L<<280.0,606.0>--<280.0,616.0>>

	* ae (U+00E6) contains a short segment L<<389.0,344.0>--<389.0,362.0>>

	* Eng (U+014A) contains a short segment B<<463.0,-221.0>-<450.0,-221.0>-<436.0,-220.0>>

	* Eng (U+014A) contains a short segment B<<436.0,-220.0>-<422.0,-219.0>-<413.0,-217.0>>

	* uni0163 (U+0163) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* tcaron (U+0165) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* tbar (U+0167) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* aeacute (U+01FD) contains a short segment L<<389.0,344.0>--<389.0,362.0>>

	* uni021B (U+021B) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* uni0E3F (U+0E3F) contains a short segment L<<385.0,745.0>--<386.0,745.0>>

	* uni1E42 (U+1E42) contains a short segment L<<455.0,200.0>--<439.0,200.0>>

	* uni1E6D (U+1E6D) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* uni1E6F (U+1E6F) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* uni1E97 (U+1E97) contains a short segment L<<22.0,544.0>--<32.0,544.0>>

	* uni2076 (U+2076) contains a short segment B<<221.0,558.0>-<225.0,559.0>-<230.0,559.0>>

	* uni2086 (U+2086) contains a short segment B<<221.0,334.0>-<225.0,335.0>-<230.0,335.0>>

	* colonmonetary (U+20A1) contains a short segment B<<422.0,633.0>-<420.0,633.0>-<419.0,633.0>>

	* uni20BA (U+20BA) contains a short segment L<<257.0,120.0>--<277.0,120.0>>

	* uni20BE (U+20BE) contains a short segment B<<416.0,756.0>-<428.0,757.0>-<440.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<440.0,757.0>-<452.0,757.0>-<464.0,756.0>>

	* uni20BE (U+20BE) contains a short segment B<<464.0,632.0>-<451.0,633.0>-<439.0,633.0>>

	* uni20BE (U+20BE) contains a short segment B<<439.0,633.0>-<427.0,633.0>-<416.0,632.0>>

	* trademark (U+2122) contains a short segment L<<690.0,403.0>--<674.0,403.0>>

	* estimated (U+212E) contains a short segment B<<190.0,341.0>-<185.0,341.0>-<185.0,335.0>>

	* estimated (U+212E) contains a short segment B<<185.0,140.0>-<185.0,133.0>-<186.0,129.5>>

	* estimated (U+212E) contains a short segment B<<186.0,129.5>-<187.0,126.0>-<195.0,118.0>>

	* estimated (U+212E) contains a short segment B<<648.0,360.0>-<652.0,360.0>-<652.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<687.0,630.0>--<697.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<226.0,514.0>--<216.0,514.0>>

	* fi (U+FB01) contains a short segment L<<124.0,544.0>--<124.0,562.0>> 

	* fl (U+FB02) contains a short segment L<<124.0,544.0>--<124.0,562.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<964.0,120.0>--<963.0,0.0>>

	* AEacute (U+01FC): L<<964.0,120.0>--<963.0,0.0>>

	* OE (U+0152): L<<1193.0,120.0>--<1192.0,0.0>> 

	* uni20BE (U+20BE): L<<807.0,480.0>--<661.0,479.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] PlusJakartaSans-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 2 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* colonmonetary
	* oslash
	* oslashacute
	* uni20A6
	* uni20A9
	* uni20B1 and uni20B3
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* y (U+0079): X=240.0,Y=2.0 (should be at baseline 0?)

	* braceleft (U+007B): X=116.0,Y=1.0 (should be at baseline 0?)

	* braceleft (U+007B): X=166.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=125.0,Y=-1.0 (should be at baseline 0?)

	* braceright (U+007D): X=175.0,Y=1.0 (should be at baseline 0?)

	* Acircumflex (U+00C2): X=322.0,Y=973.0 (should be at ascender 972?)

	* Ecircumflex (U+00CA): X=329.0,Y=973.0 (should be at ascender 972?)

	* Icircumflex (U+00CE): X=124.0,Y=973.0 (should be at ascender 972?)

	* Ocircumflex (U+00D4): X=442.0,Y=973.0 (should be at ascender 972?)

	* Ucircumflex (U+00DB): X=345.0,Y=973.0 (should be at ascender 972?)

	* atilde (U+00E3): X=395.0,Y=746.0 (should be at cap-height 745?)

	* atilde (U+00E3): X=435.0,Y=746.0 (should be at cap-height 745?)

	* ntilde (U+00F1): X=387.0,Y=746.0 (should be at cap-height 745?)

	* ntilde (U+00F1): X=427.0,Y=746.0 (should be at cap-height 745?)

	* otilde (U+00F5): X=433.0,Y=746.0 (should be at cap-height 745?)

	* otilde (U+00F5): X=473.0,Y=746.0 (should be at cap-height 745?)

	* yacute (U+00FD): X=240.0,Y=2.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=240.0,Y=2.0 (should be at baseline 0?)

	* Ccircumflex (U+0108): X=430.0,Y=973.0 (should be at ascender 972?)

	* Gcircumflex (U+011C): X=417.0,Y=973.0 (should be at ascender 972?)

	* Hcircumflex (U+0124): X=369.0,Y=973.0 (should be at ascender 972?)

	* hcircumflex (U+0125): X=111.0,Y=973.0 (should be at ascender 972?)

	* itilde (U+0129): X=194.0,Y=746.0 (should be at cap-height 745?)

	* itilde (U+0129): X=234.0,Y=746.0 (should be at cap-height 745?)

	* Jcircumflex (U+0134): X=257.0,Y=973.0 (should be at ascender 972?)

	* Scircumflex (U+015C): X=320.0,Y=973.0 (should be at ascender 972?)

	* utilde (U+0169): X=387.0,Y=746.0 (should be at cap-height 745?)

	* utilde (U+0169): X=427.0,Y=746.0 (should be at cap-height 745?)

	* Wcircumflex (U+0174): X=494.0,Y=973.0 (should be at ascender 972?)

	* Ycircumflex (U+0176): X=312.0,Y=973.0 (should be at ascender 972?)

	* ycircumflex (U+0177): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni022D (U+022D): X=433.0,Y=746.0 (should be at cap-height 745?)

	* uni022D (U+022D): X=473.0,Y=746.0 (should be at cap-height 745?)

	* uni0233 (U+0233): X=240.0,Y=2.0 (should be at baseline 0?)

	* tilde (U+02DC): X=347.0,Y=746.0 (should be at cap-height 745?)

	* tilde (U+02DC): X=387.0,Y=746.0 (should be at cap-height 745?)

	* tildecomb (U+0303): X=347.0,Y=746.0 (should be at cap-height 745?)

	* tildecomb (U+0303): X=387.0,Y=746.0 (should be at cap-height 745?)

	* uni032E (U+032E): X=240.0,Y=-230.0 (should be at descender -228?)

	* uni032E (U+032E): X=240.0,Y=-230.0 (should be at descender -228?)

	* uni1E2A (U+1E2A): X=369.0,Y=-230.0 (should be at descender -228?)

	* uni1E2A (U+1E2A): X=369.0,Y=-230.0 (should be at descender -228?)

	* uni1E2B (U+1E2B): X=285.0,Y=-230.0 (should be at descender -228?)

	* uni1E2B (U+1E2B): X=285.0,Y=-230.0 (should be at descender -228?)

	* uni1E4D (U+1E4D): X=433.0,Y=746.0 (should be at cap-height 745?)

	* uni1E4D (U+1E4D): X=473.0,Y=746.0 (should be at cap-height 745?)

	* uni1E4F (U+1E4F): X=433.0,Y=746.0 (should be at cap-height 745?)

	* uni1E4F (U+1E4F): X=473.0,Y=746.0 (should be at cap-height 745?)

	* uni1E79 (U+1E79): X=387.0,Y=746.0 (should be at cap-height 745?)

	* uni1E79 (U+1E79): X=427.0,Y=746.0 (should be at cap-height 745?)

	* uni1E8F (U+1E8F): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni1EA2 (U+1EA2): X=244.0,Y=971.0 (should be at ascender 972?)

	* uni1EA9 (U+1EA9): X=466.5,Y=747.0 (should be at cap-height 745?)

	* uni1EAC (U+1EAC): X=322.0,Y=973.0 (should be at ascender 972?)

	* uni1EBA (U+1EBA): X=251.0,Y=971.0 (should be at ascender 972?)

	* uni1EBD (U+1EBD): X=416.0,Y=746.0 (should be at cap-height 745?)

	* uni1EBD (U+1EBD): X=456.0,Y=746.0 (should be at cap-height 745?)

	* uni1EC3 (U+1EC3): X=487.5,Y=747.0 (should be at cap-height 745?)

	* uni1EC6 (U+1EC6): X=329.0,Y=973.0 (should be at ascender 972?)

	* uni1EC8 (U+1EC8): X=46.0,Y=971.0 (should be at ascender 972?)

	* uni1ECE (U+1ECE): X=364.0,Y=971.0 (should be at ascender 972?)

	* uni1ED5 (U+1ED5): X=504.5,Y=747.0 (should be at cap-height 745?)

	* uni1ED8 (U+1ED8): X=442.0,Y=973.0 (should be at ascender 972?)

	* uni1EDE (U+1EDE): X=364.0,Y=971.0 (should be at ascender 972?)

	* uni1EE1 (U+1EE1): X=433.0,Y=746.0 (should be at cap-height 745?)

	* uni1EE1 (U+1EE1): X=473.0,Y=746.0 (should be at cap-height 745?)

	* uni1EE6 (U+1EE6): X=267.0,Y=971.0 (should be at ascender 972?)

	* uni1EEC (U+1EEC): X=267.0,Y=971.0 (should be at ascender 972?)

	* uni1EEF (U+1EEF): X=387.0,Y=746.0 (should be at cap-height 745?)

	* uni1EEF (U+1EEF): X=427.0,Y=746.0 (should be at cap-height 745?)

	* ygrave (U+1EF3): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni1EF5 (U+1EF5): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni1EF6 (U+1EF6): X=234.0,Y=971.0 (should be at ascender 972?)

	* uni1EF7 (U+1EF7): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni1EF9 (U+1EF9): X=240.0,Y=2.0 (should be at baseline 0?)

	* uni1EF9 (U+1EF9): X=367.0,Y=746.0 (should be at cap-height 745?) 

	* uni1EF9 (U+1EF9): X=407.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* three (U+0033) contains a short segment B<<294.0,404.0>-<285.0,404.0>-<272.5,403.0>>

	* question (U+003F) contains a short segment L<<160.0,208.0>--<160.0,212.0>>

	* M (U+004D) contains a short segment L<<410.0,246.0>--<408.0,246.0>>

	* questiondown (U+00BF) contains a short segment L<<314.0,318.0>--<314.0,314.0>>

	* uni1E42 (U+1E42) contains a short segment L<<410.0,246.0>--<408.0,246.0>>

	* colonmonetary (U+20A1) contains a short segment B<<421.0,757.0>-<425.0,757.0>-<430.0,757.0>>

	* colonmonetary (U+20A1) contains a short segment B<<438.0,-12.0>-<434.0,-12.0>-<430.0,-12.0>>

	* uni20BF (U+20BF) contains a short segment B<<400.0,745.0>-<403.0,745.0>-<406.0,745.0>>

	* uni20BF (U+20BF) contains a short segment L<<406.0,0.0>--<400.0,0.0>>

	* trademark (U+2122) contains a short segment L<<613.0,435.0>--<609.0,435.0>>

	* estimated (U+212E) contains a short segment B<<217.0,341.0>-<212.0,341.0>-<212.0,335.0>>

	* estimated (U+212E) contains a short segment B<<212.0,140.0>-<212.0,133.0>-<213.5,129.5>>

	* estimated (U+212E) contains a short segment B<<213.5,129.5>-<215.0,126.0>-<222.0,118.0>>

	* estimated (U+212E) contains a short segment B<<675.0,360.0>-<679.0,360.0>-<679.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<632.0,630.0>--<642.0,630.0>> 

	* uni21AA (U+21AA) contains a short segment L<<282.0,590.0>--<272.0,590.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni20BF (U+20BF): L<<406.0,0.0>--<400.0,0.0>> -> L<<400.0,0.0>--<281.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<105.0,208.0>--<103.0,745.0>>

	* exclam (U+0021): L<<153.0,745.0>--<150.0,208.0>>

	* exclamdown (U+00A1): L<<103.0,-219.0>--<105.0,318.0>> 

	* exclamdown (U+00A1): L<<150.0,318.0>--<153.0,-219.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[17] PlusJakartaSans-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Aringacute
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Q.ss03
	* Tbar
	* ae
	* aeacute
	* ampersand
	* aringacute
	* aringacute.ss01
	* aringacute.ss02
	* aringacute.ss03
	* arrowboth
	* arrowdown
	* arrowleft
	* arrowright
	* arrowup
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f_i
	* f_f_l
	* franc
	* h.ss01
	* hbar
	* hbar.ss01
	* hbar.ss03
	* hcircumflex.ss01
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* partialdiff
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni030A0301
	* uni0E3F
	* uni1E25.ss01
	* uni1E2B.ss01
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2196
	* uni2197
	* uni2198
	* uni2199
	* uni21A9
	* uni21AA
	* uni21B0
	* uni21B1
	* uni21B2
	* uni21B3
	* uni2B0E
	* uni2B10 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning information. [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* Q (U+0051): X=545.0,Y=1.0 (should be at baseline 0?)

	* p (U+0070): X=274.5,Y=1.5 (should be at baseline 0?)

	* q (U+0071): X=398.5,Y=1.5 (should be at baseline 0?)

	* questiondown (U+00BF): X=70.0,Y=-2.0 (should be at baseline 0?)

	* questiondown (U+00BF): X=225.0,Y=2.0 (should be at baseline 0?)

	* Atilde (U+00C3): X=390.0,Y=970.5 (should be at ascender 972?)

	* Atilde (U+00C3): X=454.0,Y=970.5 (should be at ascender 972?)

	* Ntilde (U+00D1): X=395.0,Y=970.5 (should be at ascender 972?)

	* Ntilde (U+00D1): X=459.0,Y=970.5 (should be at ascender 972?)

	* Otilde (U+00D5): X=463.0,Y=970.5 (should be at ascender 972?)

	* Otilde (U+00D5): X=527.0,Y=970.5 (should be at ascender 972?)

	* aring (U+00E5): X=322.5,Y=744.0 (should be at cap-height 745?)

	* aring (U+00E5): X=267.0,Y=744.0 (should be at cap-height 745?)

	* thorn (U+00FE): X=274.5,Y=1.5 (should be at baseline 0?)

	* Itilde (U+0128): X=168.0,Y=970.5 (should be at ascender 972?)

	* Itilde (U+0128): X=232.0,Y=970.5 (should be at ascender 972?)

	* Utilde (U+0168): X=386.0,Y=970.5 (should be at ascender 972?)

	* Utilde (U+0168): X=450.0,Y=970.5 (should be at ascender 972?)

	* uring (U+016F): X=327.5,Y=744.0 (should be at cap-height 745?)

	* uring (U+016F): X=272.0,Y=744.0 (should be at cap-height 745?)

	* aringacute (U+01FB): X=322.5,Y=744.0 (should be at cap-height 745?)

	* aringacute (U+01FB): X=267.0,Y=744.0 (should be at cap-height 745?)

	* uni022C (U+022C): X=463.0,Y=970.5 (should be at ascender 972?)

	* uni022C (U+022C): X=527.0,Y=970.5 (should be at ascender 972?)

	* uni022D (U+022D): X=156.0,Y=970.0 (should be at ascender 972?)

	* uni022D (U+022D): X=496.0,Y=970.0 (should be at ascender 972?)

	* ring (U+02DA): X=286.5,Y=744.0 (should be at cap-height 745?)

	* ring (U+02DA): X=231.0,Y=744.0 (should be at cap-height 745?)

	* hookabovecomb (U+0309): X=386.0,Y=747.0 (should be at cap-height 745?)

	* uni030A (U+030A): X=286.5,Y=744.0 (should be at cap-height 745?)

	* uni030A (U+030A): X=231.0,Y=744.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=129.0,Y=743.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=133.0,Y=743.0 (should be at cap-height 745?)

	* uni031B (U+031B): X=150.5,Y=744.5 (should be at cap-height 745?)

	* uni1E4C (U+1E4C): X=463.0,Y=970.5 (should be at ascender 972?)

	* uni1E4C (U+1E4C): X=527.0,Y=970.5 (should be at ascender 972?)

	* uni1E4E (U+1E4E): X=463.0,Y=970.5 (should be at ascender 972?)

	* uni1E4E (U+1E4E): X=527.0,Y=970.5 (should be at ascender 972?)

	* uni1E78 (U+1E78): X=386.0,Y=970.5 (should be at ascender 972?)

	* uni1E78 (U+1E78): X=450.0,Y=970.5 (should be at ascender 972?)

	* uni1EA2 (U+1EA2): X=303.0,Y=973.0 (should be at ascender 972?)

	* uni1EA2 (U+1EA2): X=277.5,Y=971.5 (should be at ascender 972?)

	* uni1EA3 (U+1EA3): X=423.0,Y=747.0 (should be at cap-height 745?)

	* uni1EA8 (U+1EA8): X=517.0,Y=974.0 (should be at ascender 972?)

	* uni1EBA (U+1EBA): X=254.0,Y=973.0 (should be at ascender 972?)

	* uni1EBA (U+1EBA): X=228.5,Y=971.5 (should be at ascender 972?)

	* uni1EBB (U+1EBB): X=434.0,Y=747.0 (should be at cap-height 745?)

	* uni1EBC (U+1EBC): X=341.0,Y=970.5 (should be at ascender 972?)

	* uni1EBC (U+1EBC): X=405.0,Y=970.5 (should be at ascender 972?)

	* uni1EC2 (U+1EC2): X=468.0,Y=974.0 (should be at ascender 972?)

	* uni1EC8 (U+1EC8): X=81.0,Y=973.0 (should be at ascender 972?)

	* uni1EC8 (U+1EC8): X=55.5,Y=971.5 (should be at ascender 972?)

	* uni1EC9 (U+1EC9): X=247.0,Y=747.0 (should be at cap-height 745?)

	* uni1ECE (U+1ECE): X=376.0,Y=973.0 (should be at ascender 972?)

	* uni1ECE (U+1ECE): X=350.5,Y=971.5 (should be at ascender 972?)

	* uni1ECF (U+1ECF): X=454.0,Y=747.0 (should be at cap-height 745?)

	* uni1ED4 (U+1ED4): X=590.0,Y=974.0 (should be at ascender 972?)

	* uni1EDE (U+1EDE): X=376.0,Y=973.0 (should be at ascender 972?)

	* uni1EDE (U+1EDE): X=350.5,Y=971.5 (should be at ascender 972?)

	* uni1EDF (U+1EDF): X=454.0,Y=747.0 (should be at cap-height 745?)

	* uni1EE0 (U+1EE0): X=463.0,Y=970.5 (should be at ascender 972?)

	* uni1EE0 (U+1EE0): X=527.0,Y=970.5 (should be at ascender 972?)

	* uni1EE6 (U+1EE6): X=299.0,Y=973.0 (should be at ascender 972?)

	* uni1EE6 (U+1EE6): X=273.5,Y=971.5 (should be at ascender 972?)

	* uni1EE7 (U+1EE7): X=428.0,Y=747.0 (should be at cap-height 745?)

	* uni1EEC (U+1EEC): X=299.0,Y=973.0 (should be at ascender 972?)

	* uni1EEC (U+1EEC): X=273.5,Y=971.5 (should be at ascender 972?)

	* uni1EED (U+1EED): X=428.0,Y=747.0 (should be at cap-height 745?)

	* uni1EEE (U+1EEE): X=386.0,Y=970.5 (should be at ascender 972?)

	* uni1EEE (U+1EEE): X=450.0,Y=970.5 (should be at ascender 972?)

	* uni1EF6 (U+1EF6): X=273.0,Y=973.0 (should be at ascender 972?)

	* uni1EF6 (U+1EF6): X=247.5,Y=971.5 (should be at ascender 972?)

	* uni1EF7 (U+1EF7): X=429.0,Y=747.0 (should be at cap-height 745?)

	* uni1EF8 (U+1EF8): X=360.0,Y=970.5 (should be at ascender 972?)

	* uni1EF8 (U+1EF8): X=424.0,Y=970.5 (should be at ascender 972?)

	* uni2077 (U+2077): X=11.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=373.0,Y=746.0 (should be at cap-height 745?)

	* colonmonetary (U+20A1): X=331.0,Y=-2.0 (should be at baseline 0?)

	* uni20BE (U+20BE): X=330.0,Y=743.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=550.0,Y=744.0 (should be at cap-height 745?)

	* seveneighths (U+215E): X=11.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=303.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* six (U+0036) contains a short segment B<<318.0,478.0>-<324.0,478.0>-<330.0,478.0>>

	* nine (U+0039) contains a short segment B<<286.0,267.0>-<280.0,267.0>-<274.0,267.0>>

	* M (U+004D) contains a short segment L<<466.0,190.0>--<446.0,190.0>>

	* a (U+0061) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* f (U+0066) contains a short segment L<<121.0,546.0>--<121.0,554.0>>

	* t (U+0074) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* ordfeminine (U+00AA) contains a short segment L<<271.0,605.0>--<271.0,613.0>>

	* agrave (U+00E0) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* aacute (U+00E1) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* acircumflex (U+00E2) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* atilde (U+00E3) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* adieresis (U+00E4) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* aring (U+00E5) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* ae (U+00E6) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* amacron (U+0101) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* abreve (U+0103) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* aogonek (U+0105) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni0163 (U+0163) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* tcaron (U+0165) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* tbar (U+0167) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* Ohorn (U+01A0) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* aringacute (U+01FB) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* aeacute (U+01FD) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni0201 (U+0201) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni0203 (U+0203) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni021B (U+021B) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* uni031B (U+031B) contains a short segment L<<129.0,743.0>--<133.0,743.0>>

	* uni0E3F (U+0E3F) contains a short segment L<<390.0,465.0>--<392.0,465.0>>

	* uni1E42 (U+1E42) contains a short segment L<<466.0,190.0>--<446.0,190.0>>

	* uni1E6D (U+1E6D) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* uni1E6F (U+1E6F) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* uni1E97 (U+1E97) contains a short segment L<<18.0,546.0>--<23.0,546.0>>

	* uni1EA1 (U+1EA1) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EA3 (U+1EA3) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EA5 (U+1EA5) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EA7 (U+1EA7) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EA9 (U+1EA9) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EAB (U+1EAB) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EAD (U+1EAD) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EAF (U+1EAF) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EB1 (U+1EB1) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EB3 (U+1EB3) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EB5 (U+1EB5) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EB7 (U+1EB7) contains a short segment L<<378.0,345.0>--<378.0,360.0>>

	* uni1EDA (U+1EDA) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* uni1EDC (U+1EDC) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* uni1EDE (U+1EDE) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* uni1EE0 (U+1EE0) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* uni1EE2 (U+1EE2) contains a short segment B<<639.0,757.0>-<645.0,757.0>-<656.0,758.5>>

	* lira (U+20A4) contains a short segment L<<133.0,488.0>--<133.0,505.0>>

	* Euro (U+20AC) contains a short segment B<<103.0,348.0>-<102.0,360.0>-<102.0,373.0>>

	* Euro (U+20AC) contains a short segment B<<102.0,373.0>-<102.0,386.0>-<103.0,398.0>>

	* Euro (U+20AC) contains a short segment B<<257.0,398.0>-<256.0,386.0>-<256.0,373.0>>

	* Euro (U+20AC) contains a short segment B<<256.0,373.0>-<256.0,360.0>-<257.0,348.0>>

	* uni20AD (U+20AD) contains a short segment L<<268.0,418.0>--<291.0,418.0>>

	* uni20AD (U+20AD) contains a short segment L<<286.0,328.0>--<268.0,328.0>>

	* uni20B1 (U+20B1) contains a short segment B<<663.0,523.0>-<663.0,515.0>-<663.0,507.0>>

	* uni20B1 (U+20B1) contains a short segment B<<663.0,507.0>-<663.0,500.0>-<663.0,493.0>>

	* uni20BA (U+20BA) contains a short segment L<<268.0,135.0>--<290.0,135.0>>

	* uni20BE (U+20BE) contains a short segment B<<420.0,757.0>-<430.0,757.0>-<440.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<440.0,757.0>-<450.0,757.0>-<460.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<460.0,616.0>-<450.0,617.0>-<439.0,617.0>>

	* uni20BE (U+20BE) contains a short segment B<<439.0,617.0>-<429.0,617.0>-<420.0,616.0>>

	* estimated (U+212E) contains a short segment B<<184.0,341.0>-<179.0,341.0>-<179.0,335.0>>

	* estimated (U+212E) contains a short segment B<<179.0,140.0>-<179.0,133.0>-<180.5,129.5>>

	* estimated (U+212E) contains a short segment B<<180.5,129.5>-<182.0,126.0>-<189.0,118.0>>

	* estimated (U+212E) contains a short segment B<<642.0,360.0>-<646.0,360.0>-<646.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<700.0,630.0>--<710.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<218.0,500.0>--<208.0,500.0>>

	* fi (U+FB01) contains a short segment L<<121.0,546.0>--<121.0,554.0>> 

	* fl (U+FB02) contains a short segment L<<121.0,546.0>--<121.0,554.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<971.0,135.0>--<970.0,0.0>>

	* AEacute (U+01FC): L<<971.0,135.0>--<970.0,0.0>> 

	* OE (U+0152): L<<1185.0,135.0>--<1184.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[14] PlusJakartaSans-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Euro
	* Hbar
	* Oslash
	* Oslashacute
	* ae
	* aeacute
	* ampersand
	* cent
	* colonmonetary
	* dollar
	* emptyset
	* f_f
	* f_f_i
	* f_f_l
	* hbar.ss01
	* lira
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20BA
	* uni20BE
	* uni20BF and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* question (U+003F) contains a short segment L<<186.0,214.0>--<188.0,224.0>>

	* at (U+0040) contains a short segment B<<680.5,78.0>-<697.0,70.0>-<715.0,70.0>>

	* M (U+004D) contains a short segment L<<415.0,230.0>--<411.0,230.0>>

	* e (U+0065) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* questiondown (U+00BF) contains a short segment L<<314.0,322.0>--<312.0,312.0>>

	* ae (U+00E6) contains a short segment L<<430.0,341.0>--<432.0,359.0>>

	* egrave (U+00E8) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* eacute (U+00E9) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* ecircumflex (U+00EA) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* edieresis (U+00EB) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* emacron (U+0113) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* ebreve (U+0115) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* edotaccent (U+0117) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* eogonek (U+0119) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* ecaron (U+011B) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* Eng (U+014A) contains a short segment B<<404.0,-220.0>-<397.0,-220.0>-<384.5,-219.0>>

	* Eng (U+014A) contains a short segment B<<384.5,-219.0>-<372.0,-218.0>-<365.0,-216.0>>

	* florin (U+0192) contains a short segment B<<47.5,59.0>-<59.0,58.0>-<63.0,58.0>>

	* florin (U+0192) contains a short segment B<<473.5,686.5>-<462.0,687.0>-<458.0,687.0>>

	* aeacute (U+01FD) contains a short segment L<<430.0,341.0>--<432.0,359.0>>

	* uni0205 (U+0205) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni0207 (U+0207) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni0259 (U+0259) contains a short segment B<<483.0,291.0>-<483.0,297.0>-<483.0,304.0>>

	* uni1E15 (U+1E15) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1E17 (U+1E17) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1E1D (U+1E1D) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1E42 (U+1E42) contains a short segment L<<415.0,230.0>--<411.0,230.0>>

	* uni1EB9 (U+1EB9) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EBB (U+1EBB) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EBD (U+1EBD) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EBF (U+1EBF) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EC1 (U+1EC1) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EC3 (U+1EC3) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EC5 (U+1EC5) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* uni1EC7 (U+1EC7) contains a short segment B<<134.0,245.0>-<134.0,239.0>-<134.0,232.0>>

	* colonmonetary (U+20A1) contains a short segment B<<417.0,-12.0>-<413.0,-12.0>-<410.0,-12.0>>

	* Euro (U+20AC) contains a short segment B<<138.0,328.0>-<138.0,333.0>-<138.0,339.0>>

	* Euro (U+20AC) contains a short segment B<<217.0,341.0>-<217.0,334.0>-<217.0,328.0>>

	* uni20B2 (U+20B2) contains a short segment B<<415.0,-12.0>-<412.0,-12.0>-<408.0,-12.0>>

	* uni20B2 (U+20B2) contains a short segment L<<419.0,63.0>--<423.0,63.0>>

	* uni20B5 (U+20B5) contains a short segment B<<417.0,-12.0>-<413.0,-12.0>-<409.0,-12.0>>

	* uni20BE (U+20BE) contains a short segment B<<451.0,756.0>-<467.0,757.0>-<482.0,757.0>>

	* trademark (U+2122) contains a short segment L<<658.0,420.0>--<649.0,420.0>>

	* estimated (U+212E) contains a short segment B<<221.0,341.0>-<216.0,341.0>-<216.0,335.0>>

	* estimated (U+212E) contains a short segment B<<216.0,140.0>-<216.0,133.0>-<217.5,129.5>>

	* estimated (U+212E) contains a short segment B<<217.5,129.5>-<219.0,126.0>-<226.0,118.0>>

	* estimated (U+212E) contains a short segment B<<679.0,360.0>-<683.0,360.0>-<683.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<653.0,630.0>--<663.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<309.0,555.0>--<299.0,555.0>>

	* fi (U+FB01) contains a short segment B<<416.0,684.0>-<409.0,686.0>-<397.5,686.5>>

	* fi (U+FB01) contains a short segment B<<397.5,686.5>-<386.0,687.0>-<382.0,687.0>>

	* fl (U+FB02) contains a short segment B<<416.0,684.0>-<409.0,686.0>-<397.5,686.5>> 

	* fl (U+FB02) contains a short segment B<<397.5,686.5>-<386.0,687.0>-<382.0,687.0>> [code: found-short-segments]
</div></details><br></div></details><details><summary><b>[15] PlusJakartaSans-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions">com.google.fonts/check/vertical_metrics_regressions</a>)</summary><div>


* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoAscender is 972 when it should be 1038 [code: bad-typo-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: OS/2 sTypoDescender is -228 when it should be -222 [code: bad-typo-descender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Ascender is 972 when it should be 1038 [code: bad-hhea-ascender]
* 🔥 **FAIL** Plus Jakarta Sans Regular: hhea Descender is -228 when it should be -222 [code: bad-hhea-descender]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 358, but got 354 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* Aringacute
	* Dcroat
	* Eth
	* Euro
	* Hbar
	* K.ss01
	* Lslash
	* Oslash
	* Oslashacute
	* Q
	* Q.ss03
	* Tbar
	* ae
	* aeacute
	* ampersand
	* aringacute
	* aringacute.ss01
	* aringacute.ss02
	* aringacute.ss03
	* arrowboth
	* arrowdown
	* arrowleft
	* arrowright
	* arrowup
	* arrowupdn
	* cent
	* colonmonetary
	* dcroat
	* dollar
	* dong
	* emptyset
	* eth
	* f_f
	* f_f_i
	* f_f_l
	* franc
	* hbar
	* hbar.ss01
	* hbar.ss03
	* infinity
	* k.ss01
	* kgreenlandic
	* lira
	* lslash
	* lslash.ss01
	* lslash.ss03
	* notequal
	* notequal.case
	* notequalinferior
	* notequalsuperior
	* oslash
	* oslashacute
	* peseta
	* section
	* sterling
	* uni0136.ss01
	* uni0137.ss01
	* uni0E3F
	* uni20A6
	* uni20A9
	* uni20AD
	* uni20AE
	* uni20B1
	* uni20B2
	* uni20B3
	* uni20B5
	* uni20B9
	* uni20BA
	* uni20BC
	* uni20BD
	* uni20BE
	* uni20BF
	* uni2113
	* uni2196
	* uni2197
	* uni2198
	* uni2199
	* uni21A9
	* uni21AA
	* uni21B0
	* uni21B1
	* uni21B2
	* uni21B3
	* uni2B0E
	* uni2B10 and yen
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Plus Jakarta Sans' / SUBFAMILY_NAME = 'Bold Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* M (U+004D) contains a short segment L<<444.0,200.0>--<428.0,200.0>>

	* a (U+0061) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* f (U+0066) contains a short segment B<<418.5,641.5>-<410.0,642.0>-<405.0,642.0>>

	* t (U+0074) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* ordfeminine (U+00AA) contains a short segment L<<326.0,607.0>--<327.0,617.0>>

	* agrave (U+00E0) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* aacute (U+00E1) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* acircumflex (U+00E2) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* atilde (U+00E3) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* adieresis (U+00E4) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* aring (U+00E5) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* ae (U+00E6) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* amacron (U+0101) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* abreve (U+0103) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* aogonek (U+0105) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* Eng (U+014A) contains a short segment B<<394.0,-221.0>-<381.0,-221.0>-<367.0,-220.0>>

	* Eng (U+014A) contains a short segment B<<367.0,-220.0>-<353.0,-219.0>-<345.0,-217.0>>

	* eng (U+014B) contains a short segment B<<224.0,-104.0>-<233.0,-106.0>-<241.5,-106.0>>

	* eng (U+014B) contains a short segment B<<241.5,-106.0>-<250.0,-106.0>-<256.0,-106.0>>

	* uni0163 (U+0163) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* tcaron (U+0165) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* tbar (U+0167) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* florin (U+0192) contains a short segment B<<87.5,103.5>-<96.0,103.0>-<101.0,103.0>>

	* florin (U+0192) contains a short segment B<<517.0,641.5>-<509.0,642.0>-<504.0,642.0>>

	* Uhorn (U+01AF) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* aringacute (U+01FB) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* aeacute (U+01FD) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni0201 (U+0201) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni0203 (U+0203) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni021B (U+021B) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* uni1E42 (U+1E42) contains a short segment L<<444.0,200.0>--<428.0,200.0>>

	* uni1E6D (U+1E6D) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* uni1E6F (U+1E6F) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* uni1E97 (U+1E97) contains a short segment L<<60.0,544.0>--<67.0,544.0>>

	* uni1EA1 (U+1EA1) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EA3 (U+1EA3) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EA5 (U+1EA5) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EA7 (U+1EA7) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EA9 (U+1EA9) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EAB (U+1EAB) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EAD (U+1EAD) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EAF (U+1EAF) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EB1 (U+1EB1) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EB3 (U+1EB3) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EB5 (U+1EB5) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EB7 (U+1EB7) contains a short segment L<<398.0,345.0>--<400.0,360.0>>

	* uni1EE8 (U+1EE8) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* uni1EEA (U+1EEA) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* uni1EEC (U+1EEC) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* uni1EEE (U+1EEE) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* uni1EF0 (U+1EF0) contains a short segment B<<699.0,745.0>-<709.0,745.0>-<722.5,749.0>>

	* uni2076 (U+2076) contains a short segment L<<263.0,558.0>--<267.0,559.0>>

	* uni2079 (U+2079) contains a short segment L<<219.0,411.0>--<215.0,411.0>>

	* uni2086 (U+2086) contains a short segment L<<232.0,334.0>--<236.0,335.0>>

	* uni2089 (U+2089) contains a short segment L<<188.0,187.0>--<184.0,187.0>>

	* uni20AA (U+20AA) contains a short segment B<<411.0,133.0>-<419.0,133.0>-<426.5,139.5>>

	* uni20AA (U+20AA) contains a short segment B<<426.5,139.5>-<434.0,146.0>-<435.0,155.0>>

	* Euro (U+20AC) contains a short segment B<<258.0,346.0>-<258.0,343.0>-<258.0,343.0>>

	* uni20B1 (U+20B1) contains a short segment B<<685.0,530.0>-<686.0,527.0>-<686.0,522.0>>

	* uni20BE (U+20BE) contains a short segment B<<465.0,757.0>-<474.0,757.0>-<483.0,757.0>>

	* uni20BE (U+20BE) contains a short segment B<<483.0,757.0>-<498.0,757.0>-<512.0,756.0>>

	* uni20BE (U+20BE) contains a short segment B<<495.0,633.0>-<484.0,633.0>-<473.0,633.0>>

	* uni20BE (U+20BE) contains a short segment B<<473.0,633.0>-<460.0,633.0>-<447.0,632.0>>

	* trademark (U+2122) contains a short segment L<<709.0,403.0>--<693.0,403.0>>

	* estimated (U+212E) contains a short segment B<<204.0,341.0>-<199.0,341.0>-<199.0,335.0>>

	* estimated (U+212E) contains a short segment B<<199.0,140.0>-<199.0,133.0>-<200.0,129.5>>

	* estimated (U+212E) contains a short segment B<<200.0,129.5>-<201.0,126.0>-<209.0,118.0>>

	* estimated (U+212E) contains a short segment B<<662.0,360.0>-<666.0,360.0>-<666.0,366.0>>

	* uni21A9 (U+21A9) contains a short segment L<<691.0,630.0>--<701.0,630.0>>

	* uni21AA (U+21AA) contains a short segment L<<333.0,514.0>--<323.0,514.0>>

	* integral (U+222B) contains a short segment B<<64.5,-64.5>-<73.0,-65.0>-<77.0,-65.0>>

	* integral (U+222B) contains a short segment B<<517.5,641.5>-<509.0,642.0>-<504.0,642.0>>

	* fi (U+FB01) contains a short segment L<<162.0,544.0>--<165.0,563.0>>

	* fi (U+FB01) contains a short segment B<<436.0,640.0>-<427.0,641.0>-<418.5,641.5>>

	* fi (U+FB01) contains a short segment B<<418.5,641.5>-<410.0,642.0>-<405.0,642.0>>

	* fl (U+FB02) contains a short segment L<<162.0,544.0>--<165.0,563.0>>

	* fl (U+FB02) contains a short segment B<<420.0,755.5>-<435.0,754.0>-<444.0,751.0>>

	* fl (U+FB02) contains a short segment B<<436.0,640.0>-<427.0,641.0>-<418.5,641.5>> 

	* fl (U+FB02) contains a short segment B<<418.5,641.5>-<410.0,642.0>-<405.0,642.0>> [code: found-short-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 57 | 166 | 1612 | 85 | 1260 | 0 |
| 0% | 2% | 5% | 51% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
