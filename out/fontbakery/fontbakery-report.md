## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[11] PlusJakartaSans-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[12] PlusJakartaSans-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[10] PlusJakartaSans-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[12] PlusJakartaSans-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* g (U+0067): X=325.0,Y=-220.0 (should be at descender -222?)

	* g (U+0067): X=325.0,Y=-220.0 (should be at descender -222?)

	* j (U+006A): X=-14.0,Y=-221.0 (should be at descender -222?)

	* j (U+006A): X=-41.0,Y=-220.0 (should be at descender -222?)

	* j (U+006A): X=-14.0,Y=-221.0 (should be at descender -222?)

	* y (U+0079): X=127.0,Y=-221.0 (should be at descender -222?)

	* y (U+0079): X=127.0,Y=-221.0 (should be at descender -222?)

	* Oslash (U+00D8): X=544.0,Y=744.0 (should be at cap-height 745?)

	* Oslash (U+00D8): X=334.0,Y=1.0 (should be at baseline 0?)

	* oslash (U+00F8): X=247.5,Y=-2.0 (should be at baseline 0?)

	* yacute (U+00FD): X=127.0,Y=-221.0 (should be at descender -222?)

	* yacute (U+00FD): X=127.0,Y=-221.0 (should be at descender -222?)

	* ydieresis (U+00FF): X=127.0,Y=-221.0 (should be at descender -222?)

	* ydieresis (U+00FF): X=127.0,Y=-221.0 (should be at descender -222?)

	* gcircumflex (U+011D): X=325.0,Y=-220.0 (should be at descender -222?)

	* gcircumflex (U+011D): X=325.0,Y=-220.0 (should be at descender -222?)

	* gbreve (U+011F): X=325.0,Y=-220.0 (should be at descender -222?)

	* gbreve (U+011F): X=325.0,Y=-220.0 (should be at descender -222?)

	* gdotaccent (U+0121): X=325.0,Y=-220.0 (should be at descender -222?)

	* gdotaccent (U+0121): X=325.0,Y=-220.0 (should be at descender -222?)

	* uni0123 (U+0123): X=325.0,Y=-220.0 (should be at descender -222?)

	* uni0123 (U+0123): X=325.0,Y=-220.0 (should be at descender -222?)

	* jcircumflex (U+0135): X=-14.0,Y=-221.0 (should be at descender -222?)

	* jcircumflex (U+0135): X=-41.0,Y=-220.0 (should be at descender -222?)

	* jcircumflex (U+0135): X=-14.0,Y=-221.0 (should be at descender -222?)

	* Eng (U+014A): X=463.0,Y=-221.0 (should be at descender -222?)

	* Eng (U+014A): X=436.0,Y=-220.0 (should be at descender -222?)

	* Eng (U+014A): X=463.0,Y=-221.0 (should be at descender -222?)

	* eng (U+014B): X=331.0,Y=-221.0 (should be at descender -222?)

	* eng (U+014B): X=303.5,Y=-220.0 (should be at descender -222?)

	* eng (U+014B): X=331.0,Y=-221.0 (should be at descender -222?)

	* ycircumflex (U+0177): X=127.0,Y=-221.0 (should be at descender -222?)

	* ycircumflex (U+0177): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni01C8 (U+01C8): X=529.0,Y=-221.0 (should be at descender -222?)

	* uni01C8 (U+01C8): X=502.0,Y=-220.0 (should be at descender -222?)

	* uni01C8 (U+01C8): X=529.0,Y=-221.0 (should be at descender -222?)

	* uni01C9 (U+01C9): X=238.0,Y=-221.0 (should be at descender -222?)

	* uni01C9 (U+01C9): X=211.0,Y=-220.0 (should be at descender -222?)

	* uni01C9 (U+01C9): X=238.0,Y=-221.0 (should be at descender -222?)

	* uni01CB (U+01CB): X=727.0,Y=-221.0 (should be at descender -222?)

	* uni01CB (U+01CB): X=700.0,Y=-220.0 (should be at descender -222?)

	* uni01CB (U+01CB): X=727.0,Y=-221.0 (should be at descender -222?)

	* uni01CC (U+01CC): X=579.0,Y=-221.0 (should be at descender -222?)

	* uni01CC (U+01CC): X=552.0,Y=-220.0 (should be at descender -222?)

	* uni01CC (U+01CC): X=579.0,Y=-221.0 (should be at descender -222?)

	* gcaron (U+01E7): X=325.0,Y=-220.0 (should be at descender -222?)

	* gcaron (U+01E7): X=325.0,Y=-220.0 (should be at descender -222?)

	* Oslashacute (U+01FE): X=544.0,Y=744.0 (should be at cap-height 745?)

	* Oslashacute (U+01FE): X=334.0,Y=1.0 (should be at baseline 0?)

	* oslashacute (U+01FF): X=247.5,Y=-2.0 (should be at baseline 0?)

	* uni022A (U+022A): X=278.0,Y=1040.0 (should be at ascender 1038?)

	* uni022A (U+022A): X=600.0,Y=1040.0 (should be at ascender 1038?)

	* uni0230 (U+0230): X=278.0,Y=1040.0 (should be at ascender 1038?)

	* uni0230 (U+0230): X=600.0,Y=1040.0 (should be at ascender 1038?)

	* uni0233 (U+0233): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni0233 (U+0233): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni0237 (U+0237): X=-14.0,Y=-221.0 (should be at descender -222?)

	* uni0237 (U+0237): X=-41.0,Y=-220.0 (should be at descender -222?)

	* uni0237 (U+0237): X=-14.0,Y=-221.0 (should be at descender -222?)

	* uni1E21 (U+1E21): X=325.0,Y=-220.0 (should be at descender -222?)

	* uni1E21 (U+1E21): X=325.0,Y=-220.0 (should be at descender -222?)

	* uni1E4E (U+1E4E): X=261.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E4E (U+1E4E): X=399.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E4E (U+1E4E): X=479.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E4E (U+1E4E): X=616.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E66 (U+1E66): X=251.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E66 (U+1E66): X=389.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E7A (U+1E7A): X=182.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E7A (U+1E7A): X=319.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E7A (U+1E7A): X=399.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E7A (U+1E7A): X=537.0,Y=1037.0 (should be at ascender 1038?)

	* uni1E8F (U+1E8F): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1E8F (U+1E8F): X=127.0,Y=-221.0 (should be at descender -222?)

	* ygrave (U+1EF3): X=127.0,Y=-221.0 (should be at descender -222?)

	* ygrave (U+1EF3): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF5 (U+1EF5): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF5 (U+1EF5): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF7 (U+1EF7): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF7 (U+1EF7): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF9 (U+1EF9): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni1EF9 (U+1EF9): X=127.0,Y=-221.0 (should be at descender -222?)

	* uni2077 (U+2077): X=15.0,Y=746.0 (should be at cap-height 745?)

	* uni2077 (U+2077): X=370.0,Y=746.0 (should be at cap-height 745?)

	* colonmonetary (U+20A1): X=330.0,Y=-1.0 (should be at baseline 0?)

	* uni20BE (U+20BE): X=331.0,Y=743.0 (should be at cap-height 745?)

	* uni20BE (U+20BE): X=549.0,Y=744.0 (should be at cap-height 745?)

	* uni20BF (U+20BF): X=415.0,Y=1.0 (should be at baseline 0?)

	* seveneighths (U+215E): X=15.0,Y=746.0 (should be at cap-height 745?) 

	* seveneighths (U+215E): X=303.0,Y=746.0 (should be at cap-height 745?) [code: found-misalignments]
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
</div></details><br></div></details><details><summary><b>[13] PlusJakartaSans-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[12] PlusJakartaSans-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[10] PlusJakartaSans-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
</div></details><br></div></details><details><summary><b>[11] PlusJakartaSans-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
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
| 0 | 28 | 129 | 1612 | 85 | 1326 | 0 |
| 0% | 1% | 4% | 51% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
