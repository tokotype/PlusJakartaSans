## Fontbakery report

Fontbakery version: 0.7.38

<details>
<summary><b>[15] Family checks</b></summary>
<details>
<summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed?</summary>

* [com.google.fonts/check/fontbakery_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version)

* 🔥 **FAIL** Current Font Bakery version is 0.7.38, while a newer 0.8.3 is already available. Please upgrade it with 'pip install -U fontbakery'

</details>
<details>
<summary>ℹ <b>INFO:</b> Check axis ordering on the STAT table. </summary>

* [com.google.fonts/check/STAT/axis_order](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/axis_order)
<pre>--- Rationale ---
This is (for now) a merely informative check to detect what&#x27;s the axis ordering
declared on the STAT table of fonts in the Google Fonts collection.
We may later update this to enforce some unified axis ordering scheme, yet to be
determined.</pre>

* ℹ **INFO** From a total of 2 font files, 0 of them (0.00%) lack a STAT table.

	And these are the most common STAT axis orderings:
	('wght', 2) [code: summary]

</details>
<details>
<summary>🍞 <b>PASS:</b> Ensure that all variable font files have the same set of axes and axis ranges.</summary>

* [com.google.fonts/check/varfont/consistent_axes](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/consistent_axes)
<pre>--- Rationale ---
In order to facilitate the construction of intuitive and friendly user
interfaces, all variable font files in a given family should have the same set
of variation axes. Also, each axis must have a consistent setting of min/max
value ranges accross all the files.</pre>

* 🍞 **PASS** All looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Does font file include unacceptable control character glyphs?</summary>

* [com.google.fonts/check/family/control_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/control_chars)
<pre>--- Rationale ---
Use of some unacceptable control characters in the U+0000 - U+001F range can
lead to rendering issues on some platforms.
Acceptable control characters are defined as .null (U+0000) and CR (U+000D) for
this test.</pre>

* 🍞 **PASS** Unacceptable control characters were not identified.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking all files are in the same directory.</summary>

* [com.google.fonts/check/family/single_directory](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory)
<pre>--- Rationale ---
If the set of font files passed in the command line is not all in the same
directory, then we warn the user since the tool will interpret the set of files
as belonging to a single family (and it is unlikely that the user would store
the files from a single family spreaded in several separate directories).</pre>

* 🍞 **PASS** All files are in the same directory.

</details>
<details>
<summary>🍞 <b>PASS:</b> Each font in a family must have the same set of vertical metrics values.</summary>

* [com.google.fonts/check/family/vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics)
<pre>--- Rationale ---
We want all fonts within a family to have the same vertical metrics so their
line spacing is consistent across the family.</pre>

* 🍞 **PASS** Vertical metrics are the same across the family.

</details>
<details>
<summary>🍞 <b>PASS:</b> Fonts have equal unicode encodings?</summary>

* [com.google.fonts/check/family/equal_unicode_encodings](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cmap.html#com.google.fonts/check/family/equal_unicode_encodings)

* 🍞 **PASS** Fonts have equal unicode encodings.

</details>
<details>
<summary>🍞 <b>PASS:</b> Make sure all font files have the same version value.</summary>

* [com.google.fonts/check/family/equal_font_versions](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions)

* 🍞 **PASS** All font files have the same version.

</details>
<details>
<summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE proportion?</summary>

* [com.google.fonts/check/family/panose_proportion](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_proportion)

* 🍞 **PASS** Fonts have consistent PANOSE proportion.

</details>
<details>
<summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE family type?</summary>

* [com.google.fonts/check/family/panose_familytype](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_familytype)

* 🍞 **PASS** Fonts have consistent PANOSE family type.

</details>
<details>
<summary>🍞 <b>PASS:</b> Fonts have consistent underline thickness?</summary>

* [com.google.fonts/check/family/underline_thickness](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/post.html#com.google.fonts/check/family/underline_thickness)
<pre>--- Rationale ---
Dave C Lemon (Adobe Type Team) recommends setting the underline thickness to be
consistent across the family.
If thicknesses are not family consistent, words set on the same line which have
different styles look strange.
See also:
https://twitter.com/typenerd1/status/690361887926697986</pre>

* 🍞 **PASS** Fonts have consistent underline thickness.

</details>
<details>
<summary>🍞 <b>PASS:</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts</summary>

* [com.adobe.fonts/check/family/max_4_fonts_per_family_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/family/max_4_fonts_per_family_name)
<pre>--- Rationale ---
Per the OpenType spec:
&#x27;The Font Family name [...] should be shared among at most four fonts that
differ only in weight or style [...]&#x27;</pre>

* 🍞 **PASS** There were no more than 4 fonts per family name.

</details>
<details>
<summary>💤 <b>SKIP:</b> All tabular figures must have the same width across the RIBBI-family.</summary>

* [com.google.fonts/check/family/tnum_horizontal_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/tnum_horizontal_metrics)
<pre>--- Rationale ---
Tabular figures need to have the same metrics in all styles in order to allow
tables to be set with proper typographic control, but to maintain the placement
of decimals and numeric columns between rows.
Here&#x27;s a good explanation of this:
https://www.typography.com/techniques/fonts-for-financials/#tabular-figs</pre>

* 💤 **SKIP** Unfulfilled Conditions: RIBBI_ttFonts

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1</summary>

* [com.adobe.fonts/check/family/bold_italic_unique_for_nameid1](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.adobe.fonts/check/family/bold_italic_unique_for_nameid1)
<pre>--- Rationale ---
Per the OpenType spec: name ID 1 &#x27;is used in combination with Font Subfamily
name (name ID 2), and should be shared among at most four fonts that differ only
in weight or style...
This four-way distinction should also be reflected in the OS/2.fsSelection
field, using bits 0 and 5.</pre>

* 💤 **SKIP** Unfulfilled Conditions: RIBBI_ttFonts

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator_is_available)
<pre>--- Rationale ---
There&#x27;s no reasonable (and legal) way to run the command `ftxvalidator` of the
Apple Font Tool Suite on a non-macOS machine. I.e. on GNU+Linux or Windows etc.
If Font Bakery is not running on an OSX machine, the machine running Font Bakery
could access `ftxvalidator` on OSX, e.g. via ssh or a remote procedure call
(rpc).
There&#x27;s an ssh example implementation at:
https://github.com/googlefonts/fontbakery/blob/main/prebuilt/workarounds
/ftxvalidator/ssh-implementation/ftxvalidator</pre>

* ⚠ **WARN** Could not find ftxvalidator. [code: ftxvalidator-available]

</details>
<br>
</details>
<details>
<summary><b>[192] PlusJakartaSans-Italic[wght].ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Version number has increased since previous release on Google Fonts?</summary>

* [com.google.fonts/check/version_bump](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/version_bump)

* 💔 **ERROR** The condition <FontBakeryCondition:github_gfonts_ttFont> had an error: BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.

</details>
<details>
<summary>💔 <b>ERROR:</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated.</summary>

* [com.google.fonts/check/description/family_update](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/family_update)
<pre>--- Rationale ---
We want to ensure that any significant changes to the font family are properly
mentioned in the DESCRIPTION file.
In general, it means that the contents of the DESCRIPTION.en_us.html file will
typically change if when font files are updated. Please treat this check as a
reminder to do so whenever appropriate!</pre>

* 💔 **ERROR** The condition <FontBakeryCondition:github_gfonts_description> had an error: BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check license file has good copyright string.</summary>

* [com.google.fonts/check/license/OFL_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_copyright)
<pre>--- Rationale ---
An OFL.txt file&#x27;s first line should be the font copyright e.g:
&quot;Copyright 2019 The Montserrat Project Authors
(https://github.com/julietaula/montserrat)&quot;</pre>

* 🔥 **FAIL** First line in license file does not match expected format: "copyright 2020 plus jakarta sans project authors (https://github.com/tokotype/plusjakartasans)"

</details>
<details>
<summary>🔥 <b>FAIL:</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. </summary>

* [com.google.fonts/check/STAT/gf-axisregistry](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/gf-axisregistry)
<pre>--- Rationale ---
Check that particle names and values on STAT table match the fallback names in
each axis entry at the Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry</pre>

* 🔥 **FAIL** STAT table is missing Axis Value Records [code: missing-axis-values]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Ensure variable fonts include an avar table.</summary>

* [com.google.fonts/check/mandatory_avar_table](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mandatory_avar_table)
<pre>--- Rationale ---
Most variable fonts should include an avar table to correctly define axes
progression rates.
For example, a weight axis from 0% to 100% doesn&#x27;t map directly to 100 to 1000,
because a 10% progression from 0% may be too much to define the 200, while 90%
may be too little to define the 900.
If the progression rates of axes is linear, this check can be ignored. Fontmake
will also skip adding an avar table if the progression rates are linear.
However, we still recommend designers visually proof each instance is at the
desired weight, width etc.</pre>

* 🔥 **FAIL** This variable font does not have an avar table. [code: missing-avar]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---
A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.
The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.
Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;
Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.
When in doubt, please choose OFL for new font projects.</pre>

* 🍞 **PASS** Licensing entry on name table is correctly set.
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]

</details>
<details>
<summary>⚠ <b>WARN:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
<pre>--- Rationale ---
A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry
of the name table.
The source of truth for this check is the licensing text found on the NameID 13
entry (LICENSE DESCRIPTION).
The string snippets used for detecting licensing terms are:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;
Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.
When in doubt, please choose OFL for new font projects.</pre>

* 🍞 **PASS** Font has a valid license URL in NAME table.
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description.</summary>

* [com.google.fonts/check/stylisticset_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description)
<pre>--- Rationale ---
Stylistic sets should provide description text. Programs such as InDesign,
TextEdit and Inkscape use that info to display to the users so that they know
what a given stylistic set offers.</pre>

* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss03 lacks a description string on the 'name' table. [code: missing-description]

</details>
<details>
<summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain broken links?</summary>

* [com.google.fonts/check/description/broken_links](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/broken_links)
<pre>--- Rationale ---
The snippet of HTML in the DESCRIPTION.en_us.html file is added to the font
family webpage on the Google Fonts website. For that reason, all hyperlinks in
it must be properly working.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description_html

</details>
<details>
<summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain a upstream Git repo URL?</summary>

* [com.google.fonts/check/description/git_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/git_url)
<pre>--- Rationale ---
The contents of the DESCRIPTION.en-us.html file are displayed on the Google
Fonts website in the about section of each font family specimen page.
Since all of the Google Fonts collection is composed of libre-licensed fonts,
this check enforces a policy that there must be a hypertext link in that page
directing users to the repository where the font project files are made
available.
Such hosting is typically done on sites like Github, Gitlab, GNU Savannah or any
other git-based version control service.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description_html

</details>
<details>
<summary>💤 <b>SKIP:</b> Is this a proper HTML snippet?</summary>

* [com.google.fonts/check/description/valid_html](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/valid_html)
<pre>--- Rationale ---
Sometimes people write malformed HTML markup. This check should ensure the file
is good.
Additionally, when packaging families for being pushed to the `google/fonts` git
repo, if there is no DESCRIPTION.en_us.html file, some older versions of the
`add_font.py` tool insert a dummy description file which contains invalid html.
This file needs to either be replaced with an existing description file or
edited by hand.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html must have more than 200 bytes.</summary>

* [com.google.fonts/check/description/min_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/min_length)

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html must have less than 2000 bytes.</summary>

* [com.google.fonts/check/description/max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/max_length)
<pre>--- Rationale ---
The fonts.google.com catalog specimen pages 2016 to 2020 were placed in a narrow
area of the page.
That meant a maximum limit of 1,000 characters was good, so that the narrow
column did not extent that section of the page to be too long.
But with the &quot;v4&quot; redesign of 2020, the specimen pages allow for longer texts
without upsetting the balance of the page.
So currently the limit before warning is 2,000 characters.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html should end in a linebreak.</summary>

* [com.google.fonts/check/description/eof_linebreak](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/eof_linebreak)
<pre>--- Rationale ---
Some older text-handling tools sometimes misbehave if the last line of data in a
text file is not terminated with a newline character (also known as &#x27;\n&#x27;).
We know that this is a very small detail, but for the sake of keeping all
DESCRIPTION.en_us.html files uniformly formatted throughout the GFonts
collection, we chose to adopt the practice of placing this final linebreak char
on them.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb parse correctly.</summary>

* [com.google.fonts/check/metadata/parses](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/parses)
<pre>--- Rationale ---
The purpose of this check is to ensure that the METADATA.pb file is not
malformed.</pre>

* 💤 **SKIP** Font family at './fonts/vf' lacks a METADATA.pb file. [code: file-not-found]

</details>
<details>
<summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not be 'unknown'.</summary>

* [com.google.fonts/check/metadata/unknown_designer](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unknown_designer)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not contain 'Multiple designers'.</summary>

* [com.google.fonts/check/metadata/multiple_designers](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/multiple_designers)
<pre>--- Rationale ---
For a while the string &quot;Multiple designers&quot; was used as a placeholder on
METADATA.pb files. We should replace all those instances with actual designer
names so that proper credits are displayed on the Google Fonts family specimen
pages.
If there&#x27;s more than a single designer, the designer names must be separated by
commas.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Multiple values in font designer field in METADATA.pb must be separated by commas.</summary>

* [com.google.fonts/check/metadata/designer_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_values)
<pre>--- Rationale ---
We must use commas instead of forward slashes because the server-side code at
the fonts.google.com directory will segment the string on the commas into a list
of names and display the first item in the list as the &quot;principal designer&quot;
while the remaining names are identified as &quot;contributors&quot;.
See eg https://fonts.google.com/specimen/Rubik</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Does METADATA.pb copyright field contain broken links?</summary>

* [com.google.fonts/check/metadata/broken_links](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/broken_links)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb lists all font binaries.</summary>

* [com.google.fonts/check/metadata/undeclared_fonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/undeclared_fonts)
<pre>--- Rationale ---
The set of font binaries available, except the ones on a &quot;static&quot; subdir, must
match exactly those declared on the METADATA.pb file.
Also, to avoid confusion, we expect that font files (other than statics) are not
placed on subdirectories.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb category field is valid.</summary>

* [com.google.fonts/check/metadata/category](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/category)
<pre>--- Rationale ---
There are only five acceptable values for the category field in a METADATA.pb
file:
- MONOSPACE
- SANS_SERIF
- SERIF
- DISPLAY
- HANDWRITING
This check is meant to avoid typos in this field.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check font has a license.</summary>

* [com.google.fonts/check/family/has_license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/has_license)

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure

</details>
<details>
<summary>💤 <b>SKIP:</b> Font has ttfautohint params?</summary>

* [com.google.fonts/check/has_ttfautohint_params](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/has_ttfautohint_params)

* 💤 **SKIP** Font appears to our heuristic as not hinted using ttfautohint. [code: not-hinted]

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Fontfamily is listed on Google Fonts API?</summary>

* [com.google.fonts/check/metadata/listed_on_gfonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/listed_on_gfonts)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only has unique "full_name" values.</summary>

* [com.google.fonts/check/metadata/unique_full_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_full_name_values)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only contains unique style:weight pairs.</summary>

* [com.google.fonts/check/metadata/unique_weight_style_pairs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_weight_style_pairs)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"?</summary>

* [com.google.fonts/check/metadata/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/license)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb should contain at least "menu" and "latin" subsets.</summary>

* [com.google.fonts/check/metadata/menu_and_latin](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/menu_and_latin)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb subsets should be alphabetically ordered.</summary>

* [com.google.fonts/check/metadata/subsets_order](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/subsets_order)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb includes production subsets.</summary>

* [com.google.fonts/check/metadata/includes_production_subsets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/includes_production_subsets)
<pre>--- Rationale ---
Check METADATA.pb file includes the same subsets as the family in production.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, listed_on_gfonts_api

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice is the same in all fonts?</summary>

* [com.google.fonts/check/metadata/copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that METADATA.pb family values are all the same.</summary>

* [com.google.fonts/check/metadata/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/familyname)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: According to Google Fonts standards, families should have a Regular style.</summary>

* [com.google.fonts/check/metadata/has_regular](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/has_regular)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Regular should be 400.</summary>

* [com.google.fonts/check/metadata/regular_is_400](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/regular_is_400)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, has_regular_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checks METADATA.pb font.name field matches family name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/family_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/post_script_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/post_script_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name value matches fullname declared on the name table?</summary>

* [com.google.fonts/check/metadata/nameid/full_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/full_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name value should be same as the family name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/font_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/font_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, style

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ?</summary>

* [com.google.fonts/check/metadata/match_fullname_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_fullname_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values?</summary>

* [com.google.fonts/check/metadata/match_filename_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_filename_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_name_values)

* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_full_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_full_name_values)

* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.filename field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_filename_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_filename_values)

* 💤 **SKIP** Unfulfilled Conditions: style, family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.post_script_name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_post_script_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_post_script_name_values)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright notices match canonical pattern in METADATA.pb</summary>

* [com.google.fonts/check/metadata/valid_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_copyright)
<pre>--- Rationale ---
The expected pattern for the copyright string adheres to the following rules:
* It must say &quot;Copyright&quot; followed by a 4 digit year (optionally followed by a
hyphen and another 4 digit year)
* Then it must say &quot;The &lt;familyname&gt; Project Authors&quot;
* And within parentheses, a URL for a git repository must be provided
* The check is case insensitive and does not validate whether the familyname is
correct, even though we&#x27;d expect it is (and we may soon update the check to
validate that aspect as well!)
Here is an example of a valid copyright string:
&quot;Copyright 2017 The Archivo Black Project Authors
(https://github.com/Omnibus-Type/ArchivoBlack)&quot;</pre>

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'.</summary>

* [com.google.fonts/check/metadata/reserved_font_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/reserved_font_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice shouldn't exceed 500 chars.</summary>

* [com.google.fonts/check/metadata/copyright_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright_max_length)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Font filenames match font.filename entries?</summary>

* [com.google.fonts/check/metadata/filenames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/filenames)
<pre>--- Rationale ---
Note:
This check only looks for files in the current directory.
Font files in subdirectories are checked by these other two checks:
 - com.google.fonts/check/metadata/undeclared_fonts
 - com.google.fonts/check/repo/vf_has_static_fonts
We may want to merge them all into a single check.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.style "italic" matches font internals?</summary>

* [com.google.fonts/check/metadata/italic_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/italic_style)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.style "normal" matches font internals?</summary>

* [com.google.fonts/check/metadata/normal_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/normal_style)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table?</summary>

* [com.google.fonts/check/metadata/nameid/family_and_full_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_and_full_names)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check if fontname is not camel cased.</summary>

* [com.google.fonts/check/metadata/fontname_not_camel_cased](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/fontname_not_camel_cased)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check font name is the same as family name.</summary>

* [com.google.fonts/check/metadata/match_name_familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_name_familyname)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check that font weight has a canonical value.</summary>

* [com.google.fonts/check/metadata/canonical_weight_value](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_weight_value)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb font weights are correct.</summary>

* [com.google.fonts/check/metadata/os2_weightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/os2_weightclass)
<pre>--- Rationale ---
Check METADATA.pb font weights are correct.
For static fonts, the metadata weight should be the same as the static font&#x27;s
OS/2 usWeightClass.
For variable fonts, the weight value should be 400 if the font&#x27;s wght axis range
includes 400, otherwise it should be the value closest to 400.</pre>

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb weight matches postScriptName for static fonts.</summary>

* [com.google.fonts/check/metadata/match_weight_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_weight_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Font styles are named canonically?</summary>

* [com.google.fonts/check/metadata/canonical_style_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_style_names)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Glyphs are similiar to Google Fonts version?</summary>

* [com.google.fonts/check/production_glyphs_similarity](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity)

* 💤 **SKIP** Unfulfilled Conditions: api_gfonts_ttFont

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/fsselection](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection)

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking post.italicAngle value.</summary>

* [com.google.fonts/check/italic_angle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/italic_angle)
<pre>--- Rationale ---
The &#x27;post&#x27; table italicAngle property should be a reasonable amount, likely not
more than -20°, never more than -30°, and never greater than 0°. Note that in
the OpenType specification, the value is negative for a lean rightwards.
https://docs.microsoft.com/en-us/typography/opentype/spec/post</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/mac_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style)
<pre>--- Rationale ---
The values of the flags on the macStyle entry on the &#x27;head&#x27; OpenType table that
describe whether a font is bold and/or italic must be coherent with the actual
style of the font as inferred by its filename.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* 💤 **SKIP** Unfulfilled Conditions: not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright field for this font on METADATA.pb matches all copyright notice entries on the name table ?</summary>

* [com.google.fonts/check/metadata/nameid/copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/copyright)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Font has all mandatory 'name' table entries?</summary>

* [com.google.fonts/check/name/mandatory_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/mandatory_entries)

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---
Checks that the family name infered from the font filename matches the string at
nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise checks
that nameID 1 is the family name + the style name.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)
<pre>--- Rationale ---
Requirements for the FULL_FONT_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style_with_spaces

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: POSTSCRIPT_NAME entries.</summary>

* [com.google.fonts/check/name/postscriptname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/postscriptname)
<pre>--- Rationale ---
Requirements for the POSTSCRIPT_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)
<pre>--- Rationale ---
Requirements for the TYPOGRAPHIC_FAMILY_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---
Hinted fonts must have head table flag bit 3 set.
Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.
Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_hinted

</details>
<details>
<summary>💤 <b>SKIP:</b> Directory name in GFonts repo structure must match NameID 1 of the regular.</summary>

* [com.google.fonts/check/repo/dirname_matches_nameid_1](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/dirname_matches_nameid_1)

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> A static fonts directory with at least two fonts must accompany variable fonts</summary>

* [com.google.fonts/check/repo/vf_has_static_fonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/vf_has_static_fonts)
<pre>--- Rationale ---
Variable font family directories kept in the google/fonts git repo may include a
static/ subdir containing static fonts.
These files are meant to be served for users that still lack support for
variable fonts in their web browsers.</pre>

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure

</details>
<details>
<summary>💤 <b>SKIP:</b> Check upstream.yaml file contains all required fields</summary>

* [com.google/fonts/check/repo/upstream_yaml_has_required_fields](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google/fonts/check/repo/upstream_yaml_has_required_fields)
<pre>--- Rationale ---
If a family has been pushed using the gftools packager, we must check that all
the required fields in the upstream.yaml file have been populated.</pre>

* 💤 **SKIP** Unfulfilled Conditions: upstream_yaml

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts.</summary>

* [com.google.fonts/check/vertical_metrics_regressions](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions)
<pre>--- Rationale ---
If the family already exists on Google Fonts, we need to ensure that the checked
family&#x27;s vertical metrics are similar. This check will test the following schema
which was outlined in Fontbakery issue #1162 [1]:
- The family should visually have the same vertical metrics as the Regular style
hosted on Google Fonts.
- If the family on Google Fonts has differing hhea and typo metrics, the family
being checked should use the typo metrics for both the hhea and typo entries.
- If the family on Google Fonts has use typo metrics not enabled and the family
being checked has it enabled, the hhea and typo metrics should use the family on
Google Fonts winAscent and winDescent values.
- If the upms differ, the values must be scaled so the visual appearance is the
same.
[1] https://github.com/googlefonts/fontbakery/issues/1162</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_remote_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check font follows the Google Fonts CJK vertical metric schema</summary>

* [com.google.fonts/check/cjk_vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics)
<pre>--- Rationale ---
CJK fonts have different vertical metrics when compared to Latin fonts. We
follow the schema developed by dr Ken Lunde for Source Han Sans and the Noto CJK
fonts.
Our documentation includes further information:
https://github.com/googlefonts/gf-docs/tree/main/Spec#cjk-vertical-metrics</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts.</summary>

* [com.google.fonts/check/cjk_vertical_metrics_regressions](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics_regressions)
<pre>--- Rationale ---
Check CJK family has the same vertical metrics as the same family hosted on
Google Fonts.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font, regular_remote_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Does the font contain less than 40 CJK characters?</summary>

* [com.google.fonts/check/cjk_not_enough_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_not_enough_glyphs)
<pre>--- Rationale ---
Hangul has 40 characters and it&#x27;s the smallest CJK writing system.
If a font contains less CJK glyphs than this writing system, we inform the user
that some glyphs may be encoded incorrectly.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate METADATA.pb axes values are within gf-axisregistry bounds. </summary>

* [com.google.fonts/check/metadata/gf-axisregistry_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf-axisregistry_bounds)
<pre>--- Rationale ---
Each axis range in a METADATA.pb file must be registered, and within the bounds
of the axis definition in the Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate METADATA.pb axes tags are defined in gf-axisregistry. </summary>

* [com.google.fonts/check/metadata/gf-axisregistry_valid_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf-axisregistry_valid_tags)
<pre>--- Rationale ---
Ensure all axes in a METADATA.pb file are registered in the Google Fonts Axis
Registry, available at https://github.com/google/fonts/tree/main/axisregistry
Why does Google Fonts have its own Axis Registry?
We support a superset of the OpenType axis registry axis set, and use additional
metadata for each axis. Axes present in a font file but not in this registry
will not function via our API. No variable font is expected to support all of
the axes here.
Any font foundry or distributor library that offers variable fonts has a
implicit, latent, de-facto axis registry, which can be extracted by scanning the
library for axes&#x27; tags, labels, and min/def/max values. While in 2016 Microsoft
originally offered to include more axes in the OpenType 1.8 specification
(github.com/microsoft/OpenTypeDesignVariationAxisTags), as of August 2020, this
effort has stalled. We hope more foundries and distributors will publish
documents like this that make their axes explicit, to encourage of adoption of
variable fonts throughout the industry, and provide source material for a future
update to the OpenType specification&#x27;s axis registry.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate VF axes match the ones declared on METADATA.pb. </summary>

* [com.google.fonts/check/metadata/consistent_axis_enumeration](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/consistent_axis_enumeration)
<pre>--- Rationale ---
All font variation axes present in the font files must be properly declared on
METADATA.pb so that they can be served by the GFonts API.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb does not use escaped strings.</summary>

* [com.google.fonts/check/metadata/escaped_strings](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/escaped_strings)
<pre>--- Rationale ---
In some cases we&#x27;ve seen designer names and other fields with escaped strings in
METADATA files.
Nowadays the strings can be full unicode strings and do not need escaping.</pre>

* 💤 **SKIP** Unfulfilled Conditions: metadata_file

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Designer is listed with the correct name on the Google Fonts catalog of designers?</summary>

* [com.google.fonts/check/metadata/designer_profiles](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_profiles)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking with ftxvalidator.</summary>

* [com.google.fonts/check/ftxvalidator](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator)

* 💤 **SKIP** Unfulfilled Conditions: ftxvalidator_cmd

</details>
<details>
<summary>💤 <b>SKIP:</b> Each font in set of sibling families must have the same set of vertical metrics values.</summary>

* [com.google.fonts/check/superfamily/vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/vertical_metrics)
<pre>--- Rationale ---
We may want all fonts within a super-family (all sibling families) to have the
same vertical metrics so their line spacing is consistent across the
super-family.
This is an experimental extended version of
com.google.fonts/check/superfamily/vertical_metrics and for now it will only
result in WARNs.</pre>

* 💤 **SKIP** Sibling families were not detected.

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure indic fonts have the Indian Rupee Sign glyph. </summary>

* [com.google.fonts/check/rupee](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/rupee)
<pre>--- Rationale ---
Per Bureau of Indian Standards every font supporting one of the official Indian
languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_indic_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Is the CFF subr/gsubr call depth > 10?</summary>

* [com.adobe.fonts/check/cff_call_depth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_call_depth)
<pre>--- Rationale ---
Per &quot;The Type 2 Charstring Format, Technical Note #5177&quot;, the &quot;Subr nesting,
stack limit&quot; is 10.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> Is the CFF2 subr/gsubr call depth > 10?</summary>

* [com.adobe.fonts/check/cff2_call_depth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff2_call_depth)
<pre>--- Rationale ---
Per &quot;The CFF2 CharString Format&quot;, the &quot;Subr nesting, stack limit&quot; is 10.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff2

</details>
<details>
<summary>💤 <b>SKIP:</b> Does the font use deprecated CFF operators or operations?</summary>

* [com.adobe.fonts/check/cff_deprecated_operators](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_deprecated_operators)
<pre>--- Rationale ---
The &#x27;dotsection&#x27; operator and the use of &#x27;endchar&#x27; to build accented characters
from the Adobe Standard Encoding Character Set (&quot;seac&quot;) are deprecated in CFF.
Adobe recommends repairing any fonts that use these, especially endchar-as-seac,
because a rendering issue was discovered in Microsoft Word with a font that
makes use of this operation. The check treats that useage as a FAIL. There are
no known ill effects of using dotsection, so that check is a WARN.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> CFF table FontName must match name table ID 6 (PostScript name).</summary>

* [com.adobe.fonts/check/name/postscript_vs_cff](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_vs_cff)
<pre>--- Rationale ---
The PostScript name entries in the font&#x27;s &#x27;name&#x27; table should match the FontName
string in the &#x27;CFF &#x27; table.
The &#x27;CFF &#x27; table has a lot of information that is duplicated in other tables.
This information should be consistent across tables, because there&#x27;s no
guarantee which table an app will get the data from.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_wght_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wght_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
If a variable font has a &#x27;wght&#x27; (Weight) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be 400.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_wght_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_wdth_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wdth&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
If a variable font has a &#x27;wdth&#x27; (Width) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be 100.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_wdth_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_slnt_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_slnt_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;slnt&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_slnt
If a variable font has a &#x27;slnt&#x27; (Slant) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be zero.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_slnt_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_ital_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_ital_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;ital&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_ital
If a variable font has a &#x27;ital&#x27; (Italic) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be zero.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_ital_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_opsz_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_opsz_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;opsz&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz
If a variable font has an &#x27;opsz&#x27; (Optical Size) axis, then the coordinate of its
&#x27;Regular&#x27; instance is recommended to be a value in the range 10 to 16.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_opsz_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance.</summary>

* [com.google.fonts/check/varfont/bold_wght_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord)
<pre>--- Rationale ---
The Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27; available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght does
not specify a required value for the &#x27;Bold&#x27; instance of a variable font.
But Dave Crossland suggested that we should enforce a required value of 700 in
this case.</pre>

* 💤 **SKIP** Unfulfilled Conditions: bold_wght_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate specifies positive values in its range? </summary>

* [com.google.fonts/check/varfont/slnt_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/slnt_range)
<pre>--- Rationale ---
The OpenType spec says at
https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt that:
[...] the scale for the Slant axis is interpreted as the angle of slant in
counter-clockwise degrees from upright. This means that a typical, right-leaning
oblique design will have a negative slant value. This matches the scale used for
the italicAngle field in the post table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: slnt_axis

</details>
<details>
<summary>💤 <b>SKIP:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.006%% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---
This check detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.
This check is disabled for italic styles, which often contain nearly-upright
lines.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font, is_not_italic

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that texts shape as per expectation</summary>

* [com.google.fonts/check/shaping/regression](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/regression)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
compares expected shaping against actual shaping, reporting any differences.
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that no forbidden glyphs are found while shaping</summary>

* [com.google.fonts/check/shaping/forbidden](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/forbidden)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
reports if any glyphs are generated in the shaping which should not be produced.
(For example, .notdef glyphs, visible viramas, etc.)
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that no collisions are found while shaping</summary>

* [com.google.fonts/check/shaping/collides](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/collides)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
reports instances where the glyphs collide in unexpected ways.
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>ℹ <b>INFO:</b> Show hinting filesize impact.</summary>

* [com.google.fonts/check/hinting_impact](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact)
<pre>--- Rationale ---
This check is merely informative, displaying and useful comparison of filesizes
of hinted versus unhinted font files.</pre>

* ℹ **INFO** Hinting filesize impact:

 |               | ./fonts/vf/PlusJakartaSans-Italic[wght].ttf          |
 |:------------- | ---------------:|
 | Dehinted Size | 177.2kb |
 | Hinted Size   | 177.2kb   |
 | Increase      | 24 bytes      |
 | Change        | 0.0 %  |
 [code: size-impact]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
This check finds which version of ttfautohint was used, by inspecting name table
entries and then finds which version of ttfautohint is currently installed in
the system.</pre>

* ℹ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.006'] [code: version-not-detected]

</details>
<details>
<summary>ℹ <b>INFO:</b> EPAR table present in font?</summary>

* [com.google.fonts/check/epar](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/epar)
<pre>--- Rationale ---
The EPAR table is/was a way of expressing common licensing permissions and
restrictions in metadata; while almost nothing supported it, Dave Crossland
wonders that adding it to everything in Google Fonts could help make it more
popular.
More info is available at:
https://davelab6.github.io/epar/</pre>

* ℹ **INFO** EPAR table not present in font. To learn more see https://github.com/googlefonts/fontbakery/issues/818 [code: lacks-EPAR]

</details>
<details>
<summary>ℹ <b>INFO:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
<pre>--- Rationale ---
Traditionally version 0 &#x27;gasp&#x27; tables were set so that font sizes below 8 ppem
had no grid fitting but did have antialiasing. From 9-16 ppem, just grid
fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled
on. The use of accelerated graphics cards and higher resolution screens make
this approach obsolete. Microsoft&#x27;s DirectWrite pushed this even further with
much improved rendering built into the OS and apps.
In this scenario it makes sense to simply toggle all 4 flags ON for all font
sizes.</pre>

* ℹ **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use grid-fitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®
 [code: ranges]
* 🍞 **PASS** The 'gasp' table is correctly set, with one gaspRange:value of 0xFFFF:0x0F.

</details>
<details>
<summary>ℹ <b>INFO:</b> Check for font-v versioning.</summary>

* [com.google.fonts/check/fontv](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontv)
<pre>--- Rationale ---
The git sha1 tagging and dev/release features of Source Foundry `font-v` tool
are awesome and we would love to consider upstreaming the approach into fontmake
someday. For now we only emit a WARN if a given font does not yet follow the
experimental versioning style, but at some point we may start enforcing it.</pre>

* ℹ **INFO** Version string is: "Version 2.006"
The version string must ideally include a git commit hash and either a "dev" or a "release" suffix such as in the example below:
"Version 1.3; git-0d08353-release" [code: bad-format]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font contains all required tables?</summary>

* [com.google.fonts/check/required_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables)
<pre>--- Rationale ---
Depending on the typeface and coverage of a font, certain tables are recommended
for optimum quality. For example, the performance of a non-linear font is
improved if the VDMX, LTSH, and hdmx tables are present. Non-monospaced Latin
fonts should have a kern table. A gasp table is necessary if a designer wants to
influence the sizes at which grayscaling is used under Windows. A DSIG table
containing a digital signature helps ensure the integrity of the font file. Etc.</pre>

* ℹ **INFO** This font contains the following optional tables:
 - loca
 - prep
 - GPOS
 - GSUB
 - DSIG 
 - gasp [code: required-tables]
* 🍞 **PASS** Font contains all required tables.

</details>
<details>
<summary>ℹ <b>INFO:</b> List all superfamily filepaths</summary>

* [com.google.fonts/check/superfamily/list](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/list)
<pre>--- Rationale ---
This is a merely informative check that lists all sibling families detected by
fontbakery.
Only the fontfiles in these directories will be considered in superfamily-level
checks.</pre>

* ℹ **INFO** ./fonts/vf [code: family-path]

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
<pre>--- Rationale ---
A font&#x27;s filename must be composed in the following manner:
&lt;familyname&gt;-&lt;stylename&gt;.ttf
- Nunito-Regular.ttf,
- Oswald-BoldItalic.ttf
Variable fonts must list the axis tags in alphabetical order in square brackets
and separated by commas:
- Roboto[wdth,wght].ttf
- Familyname-Italic[wght].ttf</pre>

* 🍞 **PASS** ./fonts/vf/PlusJakartaSans-Italic[wght].ttf is named canonically.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 fsType does not impose restrictions.</summary>

* [com.google.fonts/check/fstype](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype)
<pre>--- Rationale ---
The fsType in the OS/2 table is a legacy DRM-related field. Fonts in the Google
Fonts collection must have it set to zero (also known as &quot;Installable
Embedding&quot;). This setting indicates that the fonts can be embedded in documents
and permanently installed by applications on remote systems.
More detailed info is available at:
https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype</pre>

* 🍞 **PASS** OS/2 fsType is properly set to zero.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* 🍞 **PASS** OS/2 VendorID 'TOKO' looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check `Google Fonts Latin Core` glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
<pre>--- Rationale ---
Google Fonts expects that fonts in its collection support at least the minimal
set of characters defined in the `GF-latin-core` glyph-set.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Substitute copyright, registered and trademark symbols in name table entries.</summary>

* [com.google.fonts/check/name/unwanted_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/unwanted_chars)

* 🍞 **PASS** No need to substitute copyright, registered and trademark symbols in name table entries of this font.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)
<pre>--- Rationale ---
Google Fonts expects variable fonts, static ttfs and static otfs to have
differing OS/2 usWeightClass values.
For Variable Fonts, Thin-Black must be 100-900
For static ttfs, Thin-Black can be 100-900 or 250-900
For static otfs, Thin-Black must be 250-900
If static otfs are set lower than 250, text may appear blurry in legacy Windows
applications.
Glyphsapp users can change the usWeightClass value of an instance by adding a
&#x27;weightClass&#x27; customParameter.</pre>

* 🍞 **PASS** OS/2 usWeightClass is good

</details>
<details>
<summary>🍞 <b>PASS:</b> Check OFL body text is correct.</summary>

* [com.google.fonts/check/license/OFL_body_text](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text)
<pre>--- Rationale ---
Check OFL body text is correct. Often users will accidently delete parts of the
body text.</pre>

* 🍞 **PASS** OFL license body text is correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Description strings in the name table must not exceed 200 characters.</summary>

* [com.google.fonts/check/name/description_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length)
<pre>--- Rationale ---
An old FontLab version had a bug which caused it to store copyright notices in
nameID 10 entries.
In order to detect those and distinguish them from actual legitimate usage of
this name table entry, we expect that such strings do not exceed a reasonable
length of 200 chars.
Longer strings are likely instances of the FontLab bug.</pre>

* 🍞 **PASS** All description name records have reasonably small lengths.

</details>
<details>
<summary>🍞 <b>PASS:</b> Version format is correct in 'name' table?</summary>

* [com.google.fonts/check/name/version_format](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format)

* 🍞 **PASS** Version format in NAME table entries is correct.

</details>
<details>
<summary>🍞 <b>PASS:</b> Make sure family name does not begin with a digit.</summary>

* [com.google.fonts/check/name/familyname_first_char](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname_first_char)
<pre>--- Rationale ---
Font family names which start with a numeral are often not discoverable in
Windows applications.</pre>

* 🍞 **PASS** Font family name first character is not a digit.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there non-ASCII characters in ASCII-only NAME table entries?</summary>

* [com.google.fonts/check/name/ascii_only_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/ascii_only_entries)
<pre>--- Rationale ---
The OpenType spec requires ASCII for the POSTSCRIPT_NAME (nameID 6).
For COPYRIGHT_NOTICE (nameID 0) ASCII is required because that string should be
the same in CFF fonts which also have this requirement in the OpenType spec.
Note:
A common place where we find non-ASCII strings is on name table entries with
NameID &gt; 18, which are expressly for localising the ASCII-only IDs into Hindi /
Arabic / etc.</pre>

* 🍞 **PASS** None of the ASCII-only NAME table entries contain non-ASCII characteres.

</details>
<details>
<summary>🍞 <b>PASS:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🍞 **PASS** Name Table entry: Copyright field 'Copyright 2020 The Plus Jakarta Sans Project Authors (https://github.com/tokotype/PlusJakartaSans)' matches canonical pattern.
* 🍞 **PASS** Name table copyright entries are good

</details>
<details>
<summary>🍞 <b>PASS:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---
Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.
The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.
But values of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.
Additionally, values above 2048 would likely result in unreasonable filesize
increases.</pre>

* 🍞 **PASS** Font em size is good (unitsPerEm = 1000).

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🍞 **PASS** FONT_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)
<pre>--- Rationale ---
Requirements for the TYPOGRAPHIC_SUBFAMILY_NAME entries in the &#x27;name&#x27; table.</pre>

* 🍞 **PASS** TYPOGRAPHIC_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Length of copyright notice must not exceed 500 characters.</summary>

* [com.google.fonts/check/name/copyright_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/copyright_length)
<pre>--- Rationale ---
This is an arbitrary max length for the copyright notice field of the name
table. We simply don&#x27;t want such notices to be too long. Typically such notices
are actually much shorter than this with a length of roughly 70 or 80
characters.</pre>

* 🍞 **PASS** All copyright notice name entries on the 'name' table are shorter than 500 characters.

</details>
<details>
<summary>🍞 <b>PASS:</b> Familyname must be unique according to namecheck.fontdata.com</summary>

* [com.google.fonts/check/fontdata_namecheck](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck)
<pre>--- Rationale ---
We need to check names are not already used, and today the best place to check
that is http://namecheck.fontdata.com</pre>

* 🍞 **PASS** Font familyname seems to be unique.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check a static ttf can be generated from a variable font.</summary>

* [com.google.fonts/check/varfont/generate_static](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/generate_static)
<pre>--- Rationale ---
Google Fonts may serve static fonts which have been generated from variable
fonts. This test will attempt to generate a static ttf using fontTool&#x27;s varLib
mutator.
The target font will be the mean of each axis e.g:
**VF font axes**
- min weight, max weight = 400, 800
- min width, max width = 50, 100
**Target Instance**
- weight = 600
- width = 75</pre>

* 🍞 **PASS** fontTools.varLib.mutator generated a static font instance

</details>
<details>
<summary>🍞 <b>PASS:</b> Check that variable fonts have an HVAR table.</summary>

* [com.google.fonts/check/varfont/has_HVAR](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/has_HVAR)
<pre>--- Rationale ---
Not having a HVAR table can lead to costly text-layout operations on some
platforms, which we want to avoid.
So, all variable fonts on the Google Fonts collection should have an HVAR with
valid values.
More info on the HVAR table can be found at:
https://docs.microsoft.com/en-us/typography/opentype/spec
/otvaroverview#variation-data-tables-and-miscellaneous-requirements</pre>

* 🍞 **PASS** This variable font contains an HVAR table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
<pre>--- Rationale ---
This setup is meant to ensure consistent rendering quality for fonts across all
devices (with different rendering/hinting capabilities).
Below is the snippet of instructions we expect to see in the fonts:
B8 01 FF    PUSHW 0x01FF
85          SCANCTRL (unconditinally turn on
                      dropout control mode)
B0 04       PUSHB 0x04
8D          SCANTYPE (enable smart dropout control)
&quot;Smart dropout control&quot; means activating rules 1, 2 and 5:
Rule 1: If a pixel&#x27;s center falls within the glyph outline,
        that pixel is turned on.
Rule 2: If a contour falls exactly on a pixel&#x27;s center,
        that pixel is turned on.
Rule 5: If a scan line between two adjacent pixel centers
        (either vertical or horizontal) is intersected
        by both an on-Transition contour and an off-Transition
        contour and neither of the pixels was already turned on
        by rules 1 and 2, turn on the pixel which is closer to
        the midpoint between the on-Transition contour and
        off-Transition contour. This is &quot;Smart&quot; dropout control.
For more detailed info (such as other rules not enabled in this snippet), please
refer to the TrueType Instruction Set documentation.</pre>

* 🍞 **PASS** 'prep' table contains instructions enabling smart dropout control.

</details>
<details>
<summary>🍞 <b>PASS:</b> There must not be VTT Talk sources in the font.</summary>

* [com.google.fonts/check/vttclean](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vttclean)
<pre>--- Rationale ---
The goal here is to reduce filesizes and improve pageloading when dealing with
webfonts.
The VTT Talk sources are not necessary at runtime and endup being just dead
weight when left embedded in the font binaries. The sources should be kept on
the project files but stripped out when building release binaries.</pre>

* 🍞 **PASS** There are no tables with VTT Talk sources embedded in the font.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there unwanted Apple tables?</summary>

* [com.google.fonts/check/aat](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/aat)
<pre>--- Rationale ---
Apple&#x27;s TrueType reference manual [1] describes SFNT tables not in the Microsoft
OpenType specification [2] and these can sometimes sneak into final release
files, but Google Fonts should only have OpenType tables.
[1] https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6.html
[2] https://docs.microsoft.com/en-us/typography/opentype/spec/</pre>

* 🍞 **PASS** There are no unwanted AAT tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> All name entries referenced by fvar instances exist on the name table?</summary>

* [com.google.fonts/check/fvar_name_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_name_entries)
<pre>--- Rationale ---
The purpose of this check is to make sure that all name entries referenced by
variable font instances do exist in the name table.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> A variable font must have named instances.</summary>

* [com.google.fonts/check/varfont_has_instances](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_has_instances)
<pre>--- Rationale ---
Named instances must be present in all variable fonts in order not to frustrate
the users&#x27; typical expectations of a traditional static font workflow.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Variable font weight coordinates must be multiples of 100.</summary>

* [com.google.fonts/check/varfont_weight_instances](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_weight_instances)
<pre>--- Rationale ---
The named instances on the weight axis of a variable font must have coordinates
that are multiples of 100 on the design space.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* 🍞 **PASS** All name entries are good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---
There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.
For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright</pre>

* 🍞 **PASS** Name table entries are all single-line (no line-breaks found).

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/rfn)
<pre>--- Rationale ---
Some designers adopt the &quot;Reserved Font Name&quot; clause of the OFL license. This
means that the original author reserves the rights to the family name and other
people can only distribute modified versions using a different family name.
Google Fonts published updates to the fonts in the collection in order to fix
issues and/or implement further improvements to the fonts. It is important to
keep the family name so that users of the webfonts can benefit from the updates.
Since it would forbid such usage scenario, all families in the GFonts collection
are required to not adopt the RFN clause.
This check ensures &quot;Reserved Font Name&quot; is not mentioned in the name table.</pre>

* 🍞 **PASS** None of the name table strings contain "Reserved Font Name".

</details>
<details>
<summary>🍞 <b>PASS:</b> A font repository should not include fontbakery report files</summary>

* [com.google.fonts/check/repo/fb_report](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/fb_report)
<pre>--- Rationale ---
A FontBakery report is ephemeral and so should be used for posting issues on a
bug-tracker instead of being hosted in the font project repository.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> A font repository should not include ZIP files</summary>

* [com.google.fonts/check/repo/zip_files](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/zip_files)
<pre>--- Rationale ---
Sometimes people check in ZIPs into their font project repositories. While we
accept the practice of checking in binaries, we believe that a ZIP is a step too
far ;)
Note: a source purist position is that only source files and build scripts
should be checked in.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances have correct coordinate values</summary>

* [com.google.fonts/check/varfont_instance_coordinates](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_coordinates)

* 🍞 **PASS** Instance coordinates are correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)

* 🍞 **PASS** Instance names are correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances don't have duplicate names</summary>

* [com.google.fonts/check/varfont_duplicate_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_duplicate_instance_names)
<pre>--- Rationale ---
This check&#x27;s purpose is to detect duplicate named instances names in a given
variable font.
Repeating instance names may be the result of instances for several VF axes
defined in `fvar`, but since currently only weight+italic tokens are allowed in
instance names as per GF specs, they ended up repeating.
Instead, only a base set of fonts for the most default representation of the
family can be defined through instances in the `fvar` table, all other instances
will have to be left to access through the `STAT` table.</pre>

* 🍞 **PASS** Instance names are unique

</details>
<details>
<summary>🍞 <b>PASS:</b> Ensure VFs do not contain slnt or ital axes. </summary>

* [com.google.fonts/check/varfont/unsupported_axes](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/unsupported_axes)
<pre>--- Rationale ---
The &#x27;ital&#x27; and &#x27;slnt&#x27; axes are not supported yet in Google Chrome.
For the time being, we need to ensure that VFs do not contain either of these
axes. Once browser support is better, we can deprecate this check.
For more info regarding browser support, see:
https://arrowtype.github.io/vf-slnt-test/</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. </summary>

* [com.google.fonts/check/gf-axisregistry/fvar_axis_defaults](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gf-axisregistry/fvar_axis_defaults)
<pre>--- Rationale ---
Check that axis defaults have a corresponding fallback name registered at the
Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry
This is necessary for the following reasons:
To get ZIP files downloads on Google Fonts to be accurate — otherwise the chosen
default font is not generated. The Newsreader family, for instance, has a
default value on the &#x27;opsz&#x27; axis of 16pt. If 16pt was not a registered fallback
position, then the ZIP file would instead include another position as default
(such as 14pt).
For the Variable fonts to display the correct location on the specimen page.
For VF with no weight axis to be displayed at all. For instance, Ballet, which
has no weight axis, was not appearing in sandbox because default position on
&#x27;opsz&#x27; axis was 16pt, and it was not yet a registered fallback positon.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Check small caps glyphs are available.</summary>

* [com.google.fonts/check/missing_small_caps_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/missing_small_caps_glyphs)
<pre>--- Rationale ---
Ensure small caps glyphs are available if a font declares smcp or c2sc OT
features.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts.</summary>

* [com.google.fonts/check/os2/use_typo_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics)
<pre>--- Rationale ---
All fonts on the Google Fonts collection should have OS/2.fsSelection bit 7
(USE_TYPO_METRICS) set. This requirement is part of the vertical metrics scheme
established as a Google Fonts policy aiming at a common ground supported by all
major font rendering environments.
For more details, read:
https://github.com/googlefonts/gf-docs/blob/main/VerticalMetrics/README.md
Below is the portion of that document that is most relevant to this check:
Use_Typo_Metrics must be enabled. This will force MS Applications to use the
OS/2 Typo values instead of the Win values. By doing this, we can freely set the
Win values to avoid clipping and control the line height with the typo values.
It has the added benefit of future line height compatibility. When a new script
is added, we simply change the Win values to the new yMin and yMax, without
needing to worry if the line height have changed.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🍞 **PASS** No trailing spaces on name table entries.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---
A font&#x27;s winAscent and winDescent values should be greater than the head table&#x27;s
yMax, abs(yMin) values. If they are less than these values, clipping can occur
on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
If the font includes tall/deep writing systems such as Arabic or Devanagari, the
winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.
When the win Metrics are significantly greater than the upm, the linespacing can
appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This
means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).</pre>

* 🍞 **PASS** OS/2 usWinAscent & usWinDescent values look good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 Metrics match hhea Metrics.</summary>

* [com.google.fonts/check/os2_metrics_match_hhea](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea)
<pre>--- Rationale ---
OS/2 and hhea vertical metric values should match. This will produce the same
linespacing on Mac, GNU+Linux and Windows.
- Mac OS X uses the hhea values.
- Windows uses OS/2 or Win, depending on the OS or fsSelection bit value.
When OS/2 and hhea vertical metrics match, the same linespacing results on
macOS, GNU+Linux and Windows. Unfortunately as of 2018, Google Fonts has
released many fonts with vertical metrics that don&#x27;t match in this way. When we
fix this issue in these existing families, we will create a visible change in
line/paragraph layout for either Windows or macOS users, which will upset some
of them.
But we have a duty to fix broken stuff, and inconsistent paragraph layout is
unacceptably broken when it is possible to avoid it.
If users complain and prefer the old broken version, they have the freedom to
take care of their own situation.</pre>

* 🍞 **PASS** OS/2.sTypoAscender/Descender values match hhea.ascent/descent.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking with ots-sanitize.</summary>

* [com.google.fonts/check/ots](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ots)

* 🍞 **PASS** ots-sanitize passed this file

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains '.notdef' as its first glyph?</summary>

* [com.google.fonts/check/mandatory_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs)
<pre>--- Rationale ---
The OpenType specification v1.8.2 recommends that the first glyph is the
&#x27;.notdef&#x27; glyph without a codepoint assigned and with a drawing.
https://docs.microsoft.com/en-us/typography/opentype/spec
/recom#glyph-0-the-notdef-glyph
Pre-v1.8, it was recommended that fonts should also contain &#x27;space&#x27;, &#x27;CR&#x27; and
&#x27;.null&#x27; glyphs. This might have been relevant for MacOS 9 applications.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)

* 🍞 **PASS** Font contains glyphs for whitespace characters.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font has **proper** whitespace glyph names?</summary>

* [com.google.fonts/check/whitespace_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames)
<pre>--- Rationale ---
This check enforces adherence to recommended whitespace (codepoints 0020 and
00A0) glyph names according to the Adobe Glyph List.</pre>

* 🍞 **PASS** Font has **AGL recommended** names for whitespace glyphs.

</details>
<details>
<summary>🍞 <b>PASS:</b> Whitespace glyphs have ink?</summary>

* [com.google.fonts/check/whitespace_ink](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink)

* 🍞 **PASS** There is no whitespace glyph with ink.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/unwanted_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables)
<pre>--- Rationale ---
Some font editors store source data in their own SFNT tables, and these can
sometimes sneak into final release files, which should only have OpenType spec
tables.</pre>

* 🍞 **PASS** There are no unwanted tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check correctness of STAT table strings </summary>

* [com.google.fonts/check/STAT_strings](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/STAT_strings)
<pre>--- Rationale ---
On the STAT table, the &quot;Italic&quot; keyword must not be used on AxisValues for
variation axes other than &#x27;ital&#x27;.</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Glyph names are all valid?</summary>

* [com.google.fonts/check/valid_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames)
<pre>--- Rationale ---
Microsoft&#x27;s recommendations for OpenType Fonts states the following:
&#x27;NOTE: The PostScript glyph name must be no longer than 31 characters, include
only uppercase or lowercase English letters, European digits, the period or the
underscore, i.e. from the set [A-Za-z0-9_.] and should start with a letter,
except the special glyph name &quot;.notdef&quot; which starts with a period.&#x27;
https://docs.microsoft.com/en-us/typography/opentype/spec/recom#post-table
In practice, though, particularly in modern environments, glyph names can be as
long as 63 characters.
According to the &quot;Adobe Glyph List Specification&quot; available at:
https://github.com/adobe-type-tools/agl-specification</pre>

* 🍞 **PASS** Glyph names are all valid.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains unique glyph names?</summary>

* [com.google.fonts/check/unique_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unique_glyphnames)
<pre>--- Rationale ---
Duplicate glyph names prevent font installation on Mac OS X.</pre>

* 🍞 **PASS** Font contains unique glyph names.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking with fontTools.ttx</summary>

* [com.google.fonts/check/ttx-roundtrip](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ttx-roundtrip)

* 🍞 **PASS** Hey! It all looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check all glyphs have codepoints assigned.</summary>

* [com.google.fonts/check/all_glyphs_have_codepoints](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cmap.html#com.google.fonts/check/all_glyphs_have_codepoints)

* 🍞 **PASS** All glyphs have a codepoint value assigned.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking unitsPerEm value is reasonable.</summary>

* [com.google.fonts/check/unitsperem](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/head.html#com.google.fonts/check/unitsperem)
<pre>--- Rationale ---
According to the OpenType spec:
The value of unitsPerEm at the head table must be a value between 16 and 16384.
Any value in this range is valid.
In fonts that have TrueType outlines, a power of 2 is recommended as this allows
performance optimizations in some rasterizers.
But 1000 is a commonly used value. And 2000 may become increasingly more common
on Variable Fonts.</pre>

* 🍞 **PASS** The unitsPerEm value (1000) on the 'head' table is reasonable.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking font version fields (head and name table).</summary>

* [com.google.fonts/check/font_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/head.html#com.google.fonts/check/font_version)

* 🍞 **PASS** All font version fields match.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check if OS/2 xAvgCharWidth is correct.</summary>

* [com.google.fonts/check/xavgcharwidth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth)

* 🍞 **PASS** OS/2 xAvgCharWidth value is correct.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits.</summary>

* [com.adobe.fonts/check/fsselection_matches_macstyle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.adobe.fonts/check/fsselection_matches_macstyle)
<pre>--- Rationale ---
The bold and italic bits in OS/2.fsSelection must match the bold and italic bits
in head.macStyle per the OpenType spec.</pre>

* 🍞 **PASS** The OS/2.fsSelection and head.macStyle bold and italic settings match.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check code page character ranges</summary>

* [com.google.fonts/check/code_pages](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/code_pages)
<pre>--- Rationale ---
At least some programs (such as Word and Sublime Text) under Windows 7 do not
recognize fonts unless code page bits are properly set on the ulCodePageRange1
(and/or ulCodePageRange2) fields of the OS/2 table.
More specifically, the fonts are selectable in the font menu, but whichever
Windows API these applications use considers them unsuitable for any character
set, so anything set in these fonts is rendered with a fallback font of Arial.
This check currently does not identify which code pages should be set.
Auto-detecting coverage is not trivial since the OpenType specification leaves
the interpretation of whether a given code page is &quot;functional&quot; or not open to
the font developer to decide.
So here we simply detect as a FAIL when a given font has no code page declared
at all.</pre>

* 🍞 **PASS** At least one code page is defined.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font has correct post table version?</summary>

* [com.google.fonts/check/post_table_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/post.html#com.google.fonts/check/post_table_version)
<pre>--- Rationale ---
Apple recommends against using &#x27;post&#x27; table format 3 under most circumstances,
as it can create problems with some printer drivers and PDF documents. The
savings in disk space usually does not justify the potential loss in
functionality.
Source:
https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6post.html
The CFF2 table does not contain glyph names, so variable OTFs should be allowed
to use post table version 2.
This check expects:
- Version 2 for TTF or OTF CFF2 Variable fonts
- Version 3 for OTF</pre>

* 🍞 **PASS** Font has post table version 2.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table for empty records.</summary>

* [com.adobe.fonts/check/name/empty_records](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/empty_records)
<pre>--- Rationale ---
Check the name table for empty records, as this can cause problems in Adobe
apps.</pre>

* 🍞 **PASS** No empty name table records found.

</details>
<details>
<summary>🍞 <b>PASS:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)

* 🍞 **PASS** Description strings in the name table do not contain any copyright string.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---
There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)
Requirements for monospace fonts:
* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm
* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm
* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2
* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397
Also we should report an error for glyphs not of average width.
Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave a
font a monospace flag in Panose, Microsoft Word would ignore the actual advance
widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140</pre>

* 🍞 **PASS** Font is not monospaced and all related metadata look good. [code: good]

</details>
<details>
<summary>🍞 <b>PASS:</b> Does full font name begin with the font family name?</summary>

* [com.google.fonts/check/name/match_familyname_fullfont](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont)

* 🍞 **PASS** Full font name begins with the font family name.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font follows the family naming recommendations?</summary>

* [com.google.fonts/check/family_naming_recommendations](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/family_naming_recommendations)

* 🍞 **PASS** Font follows the family naming recommendations.

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table ID 6 (PostScript name) must be consistent across platforms.</summary>

* [com.adobe.fonts/check/name/postscript_name_consistency](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_name_consistency)
<pre>--- Rationale ---
The PostScript name entries in the font&#x27;s &#x27;name&#x27; table should be consistent
across platforms.
This is the TTF/CFF2 equivalent of the CFF &#x27;postscript_name_cff_vs_name&#x27; check.</pre>

* 🍞 **PASS** Entries in the "name" table for ID 6 (PostScript name) are consistent.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does the number of glyphs in the loca table match the maxp table?</summary>

* [com.google.fonts/check/loca/maxp_num_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/loca.html#com.google.fonts/check/loca/maxp_num_glyphs)

* 🍞 **PASS** 'loca' table matches numGlyphs in 'maxp' table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)

* 🍞 **PASS** OS/2 sTypoLineGap and hhea lineGap are both 0.

</details>
<details>
<summary>🍞 <b>PASS:</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables?</summary>

* [com.google.fonts/check/maxadvancewidth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/maxadvancewidth)

* 🍞 **PASS** MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
<pre>--- Rationale ---
Microsoft Office 2013 and below products expect fonts to have a digital
signature declared in a DSIG table in order to implement OpenType features. The
EOL date for Microsoft Office 2013 products is 4/11/2023. This issue does not
impact Microsoft Office 2016 and above products.
This checks verifies that this signature is available in the font.
A fake signature is enough to address this issue. If needed, a dummy table can
be added to the font with the `gftools fix-dsig` script available at
https://github.com/googlefonts/gftools
Reference: https://github.com/googlefonts/fontbakery/issues/1845</pre>

* 🍞 **PASS** Digital Signature (DSIG) exists.

</details>
<details>
<summary>🍞 <b>PASS:</b> Space and non-breaking space have the same width?</summary>

* [com.google.fonts/check/whitespace_widths](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hmtx.html#com.google.fonts/check/whitespace_widths)

* 🍞 **PASS** Space and non-breaking space have the same width.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---
Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.</pre>

* 🍞 **PASS** Font does not has spacing glyphs in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---
Mark characters should be in the GDEF mark glyph class.</pre>

* 🍞 **PASS** Font does not have mark characters not in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---
Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.</pre>

* 🍞 **PASS** Font does not have non-mark characters in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* 🍞 **PASS** GPOS table check for kerning information passed.

</details>
<details>
<summary>🍞 <b>PASS:</b> Is there a usable "kern" table declared in the font?</summary>

* [com.google.fonts/check/kern_table](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/kern.html#com.google.fonts/check/kern_table)
<pre>--- Rationale ---
Even though all fonts should have their kerning implemented in the GPOS table,
there may be kerning info at the kern table as well.
Some applications such as MS PowerPoint require kerning info on the kern table.
More specifically, they require a format 0 kern subtable from a kern table
version 0 with only glyphs defined in the cmap table, which is the only one that
Windows understands (and which is also the simplest and more limited of all the
kern subtables).
Google Fonts ingests fonts made for download and use on desktops, and does all
web font optimizations in the serving pipeline (using libre libraries that
anyone can replicate.)
Ideally, TTFs intended for desktop users (and thus the ones intended for Google
Fonts) should have both KERN and GPOS tables.
Given all of the above, we currently treat kerning on a v0 kern table as a
good-to-have (but optional) feature.</pre>

* 🍞 **PASS** Font does not declare an optional "kern" table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Is there any unused data at the end of the glyf table?</summary>

* [com.google.fonts/check/glyf_unused_data](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_unused_data)

* 🍞 **PASS** There is no unused data at the end of the glyf table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* 🍞 **PASS** All glyph paths have coordinates within bounds!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check glyphs do not have duplicate components which have the same x,y coordinates.</summary>

* [com.google.fonts/check/glyf_non_transformed_duplicate_components](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components)
<pre>--- Rationale ---
There have been cases in which fonts had faulty double quote marks, with each of
them containing two single quote marks as components with the same x, y
coordinates which makes them visually look like single quote marks.
This check ensures that glyphs do not contain duplicate components which have
the same x,y coordinates.</pre>

* 🍞 **PASS** Glyphs do not contain duplicate components which have the same x,y coordinates.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check glyphs do not have components which are themselves components.</summary>

* [com.google.fonts/check/glyf_nested_components](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_nested_components)
<pre>--- Rationale ---
There have been bugs rendering variable fonts with nested components.
Additionally, some static fonts with nested components have been reported to
have rendering and printing issues.
For more info, see:
* https://github.com/googlefonts/fontbakery/issues/2961
* https://github.com/arrowtype/recursive/issues/412</pre>

* 🍞 **PASS** Glyphs do not contain nested components.

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances.</summary>

* [com.google.fonts/check/varfont/wght_valid_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wght_valid_range)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
On the &#x27;wght&#x27; (Weight) axis, the valid coordinate range is 1-1000.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wdth' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances.</summary>

* [com.google.fonts/check/varfont/wdth_valid_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wdth_valid_range)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wdth&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
On the &#x27;wdth&#x27; (Width) axis, the valid coordinate range is 1-1000</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> All fvar axes have a correspondent Axis Record on STAT table? </summary>

* [com.google.fonts/check/varfont/stat_axis_record_for_each_axis](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/stat.html#com.google.fonts/check/varfont/stat_axis_record_for_each_axis)
<pre>--- Rationale ---
cording to the OpenType spec, there must be an Axis Record for every axis
defined in the fvar table.
tps://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-records</pre>

* 🍞 **PASS** STAT table has all necessary Axis Records

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* 🍞 **PASS** So many Y-coordinates of points were close to boundaries that this was probably by design.

</details>
<br>
</details>
<details>
<summary><b>[192] PlusJakartaSans[wght].ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Version number has increased since previous release on Google Fonts?</summary>

* [com.google.fonts/check/version_bump](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/version_bump)

* 💔 **ERROR** The condition <FontBakeryCondition:github_gfonts_ttFont> had an error: BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.

</details>
<details>
<summary>💔 <b>ERROR:</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated.</summary>

* [com.google.fonts/check/description/family_update](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/family_update)
<pre>--- Rationale ---
We want to ensure that any significant changes to the font family are properly
mentioned in the DESCRIPTION file.
In general, it means that the contents of the DESCRIPTION.en_us.html file will
typically change if when font files are updated. Please treat this check as a
reminder to do so whenever appropriate!</pre>

* 💔 **ERROR** The condition <FontBakeryCondition:github_gfonts_description> had an error: BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check license file has good copyright string.</summary>

* [com.google.fonts/check/license/OFL_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_copyright)
<pre>--- Rationale ---
An OFL.txt file&#x27;s first line should be the font copyright e.g:
&quot;Copyright 2019 The Montserrat Project Authors
(https://github.com/julietaula/montserrat)&quot;</pre>

* 🔥 **FAIL** First line in license file does not match expected format: "copyright 2020 plus jakarta sans project authors (https://github.com/tokotype/plusjakartasans)"

</details>
<details>
<summary>🔥 <b>FAIL:</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. </summary>

* [com.google.fonts/check/STAT/gf-axisregistry](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/STAT/gf-axisregistry)
<pre>--- Rationale ---
Check that particle names and values on STAT table match the fallback names in
each axis entry at the Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry</pre>

* 🔥 **FAIL** STAT table is missing Axis Value Records [code: missing-axis-values]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Ensure variable fonts include an avar table.</summary>

* [com.google.fonts/check/mandatory_avar_table](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mandatory_avar_table)
<pre>--- Rationale ---
Most variable fonts should include an avar table to correctly define axes
progression rates.
For example, a weight axis from 0% to 100% doesn&#x27;t map directly to 100 to 1000,
because a 10% progression from 0% may be too much to define the 200, while 90%
may be too little to define the 900.
If the progression rates of axes is linear, this check can be ignored. Fontmake
will also skip adding an avar table if the progression rates are linear.
However, we still recommend designers visually proof each instance is at the
desired weight, width etc.</pre>

* 🔥 **FAIL** This variable font does not have an avar table. [code: missing-avar]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/name/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license)
<pre>--- Rationale ---
A known licensing description must be provided in the NameID 14 (LICENSE
DESCRIPTION) entries of the name table.
The source of truth for this check (to determine which license is in use) is a
file placed side-by-side to your font project including the licensing terms.
Depending on the chosen license, one of the following string snippets is
expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the name
table:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;
Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.
When in doubt, please choose OFL for new font projects.</pre>

* 🍞 **PASS** Licensing entry on name table is correctly set.
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]

</details>
<details>
<summary>⚠ <b>WARN:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
<pre>--- Rationale ---
A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry
of the name table.
The source of truth for this check is the licensing text found on the NameID 13
entry (LICENSE DESCRIPTION).
The string snippets used for detecting licensing terms are:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;
Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.
When in doubt, please choose OFL for new font projects.</pre>

* 🍞 **PASS** Font has a valid license URL in NAME table.
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/kerning_for_non_ligated_sequences](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences)
<pre>--- Rationale ---
Fonts with ligatures should have kerning on the corresponding non-ligated
sequences for text where ligatures aren&#x27;t used (eg
https://github.com/impallari/Raleway/issues/14).</pre>

* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + f
	- f + i
	- i + f
	- f + l
	- l + f
	- i + l

   [code: lacks-kern-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description.</summary>

* [com.google.fonts/check/stylisticset_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description)
<pre>--- Rationale ---
Stylistic sets should provide description text. Programs such as InDesign,
TextEdit and Inkscape use that info to display to the users so that they know
what a given stylistic set offers.</pre>

* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss02 lacks a description string on the 'name' table. [code: missing-description]
* ⚠ **WARN** The stylistic set ss03 lacks a description string on the 'name' table. [code: missing-description]

</details>
<details>
<summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain broken links?</summary>

* [com.google.fonts/check/description/broken_links](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/broken_links)
<pre>--- Rationale ---
The snippet of HTML in the DESCRIPTION.en_us.html file is added to the font
family webpage on the Google Fonts website. For that reason, all hyperlinks in
it must be properly working.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description_html

</details>
<details>
<summary>💤 <b>SKIP:</b> Does DESCRIPTION file contain a upstream Git repo URL?</summary>

* [com.google.fonts/check/description/git_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/git_url)
<pre>--- Rationale ---
The contents of the DESCRIPTION.en-us.html file are displayed on the Google
Fonts website in the about section of each font family specimen page.
Since all of the Google Fonts collection is composed of libre-licensed fonts,
this check enforces a policy that there must be a hypertext link in that page
directing users to the repository where the font project files are made
available.
Such hosting is typically done on sites like Github, Gitlab, GNU Savannah or any
other git-based version control service.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description_html

</details>
<details>
<summary>💤 <b>SKIP:</b> Is this a proper HTML snippet?</summary>

* [com.google.fonts/check/description/valid_html](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/valid_html)
<pre>--- Rationale ---
Sometimes people write malformed HTML markup. This check should ensure the file
is good.
Additionally, when packaging families for being pushed to the `google/fonts` git
repo, if there is no DESCRIPTION.en_us.html file, some older versions of the
`add_font.py` tool insert a dummy description file which contains invalid html.
This file needs to either be replaced with an existing description file or
edited by hand.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html must have more than 200 bytes.</summary>

* [com.google.fonts/check/description/min_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/min_length)

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html must have less than 2000 bytes.</summary>

* [com.google.fonts/check/description/max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/max_length)
<pre>--- Rationale ---
The fonts.google.com catalog specimen pages 2016 to 2020 were placed in a narrow
area of the page.
That meant a maximum limit of 1,000 characters was good, so that the narrow
column did not extent that section of the page to be too long.
But with the &quot;v4&quot; redesign of 2020, the specimen pages allow for longer texts
without upsetting the balance of the page.
So currently the limit before warning is 2,000 characters.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> DESCRIPTION.en_us.html should end in a linebreak.</summary>

* [com.google.fonts/check/description/eof_linebreak](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/eof_linebreak)
<pre>--- Rationale ---
Some older text-handling tools sometimes misbehave if the last line of data in a
text file is not terminated with a newline character (also known as &#x27;\n&#x27;).
We know that this is a very small detail, but for the sake of keeping all
DESCRIPTION.en_us.html files uniformly formatted throughout the GFonts
collection, we chose to adopt the practice of placing this final linebreak char
on them.</pre>

* 💤 **SKIP** Unfulfilled Conditions: description

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb parse correctly.</summary>

* [com.google.fonts/check/metadata/parses](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/parses)
<pre>--- Rationale ---
The purpose of this check is to ensure that the METADATA.pb file is not
malformed.</pre>

* 💤 **SKIP** Font family at './fonts/vf' lacks a METADATA.pb file. [code: file-not-found]

</details>
<details>
<summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not be 'unknown'.</summary>

* [com.google.fonts/check/metadata/unknown_designer](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unknown_designer)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Font designer field in METADATA.pb must not contain 'Multiple designers'.</summary>

* [com.google.fonts/check/metadata/multiple_designers](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/multiple_designers)
<pre>--- Rationale ---
For a while the string &quot;Multiple designers&quot; was used as a placeholder on
METADATA.pb files. We should replace all those instances with actual designer
names so that proper credits are displayed on the Google Fonts family specimen
pages.
If there&#x27;s more than a single designer, the designer names must be separated by
commas.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Multiple values in font designer field in METADATA.pb must be separated by commas.</summary>

* [com.google.fonts/check/metadata/designer_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_values)
<pre>--- Rationale ---
We must use commas instead of forward slashes because the server-side code at
the fonts.google.com directory will segment the string on the commas into a list
of names and display the first item in the list as the &quot;principal designer&quot;
while the remaining names are identified as &quot;contributors&quot;.
See eg https://fonts.google.com/specimen/Rubik</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Does METADATA.pb copyright field contain broken links?</summary>

* [com.google.fonts/check/metadata/broken_links](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/broken_links)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb lists all font binaries.</summary>

* [com.google.fonts/check/metadata/undeclared_fonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/undeclared_fonts)
<pre>--- Rationale ---
The set of font binaries available, except the ones on a &quot;static&quot; subdir, must
match exactly those declared on the METADATA.pb file.
Also, to avoid confusion, we expect that font files (other than statics) are not
placed on subdirectories.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb category field is valid.</summary>

* [com.google.fonts/check/metadata/category](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/category)
<pre>--- Rationale ---
There are only five acceptable values for the category field in a METADATA.pb
file:
- MONOSPACE
- SANS_SERIF
- SERIF
- DISPLAY
- HANDWRITING
This check is meant to avoid typos in this field.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check font has a license.</summary>

* [com.google.fonts/check/family/has_license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/family/has_license)

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure

</details>
<details>
<summary>💤 <b>SKIP:</b> Font has ttfautohint params?</summary>

* [com.google.fonts/check/has_ttfautohint_params](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/has_ttfautohint_params)

* 💤 **SKIP** Font appears to our heuristic as not hinted using ttfautohint. [code: not-hinted]

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Fontfamily is listed on Google Fonts API?</summary>

* [com.google.fonts/check/metadata/listed_on_gfonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/listed_on_gfonts)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only has unique "full_name" values.</summary>

* [com.google.fonts/check/metadata/unique_full_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_full_name_values)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: check if fonts field only contains unique style:weight pairs.</summary>

* [com.google.fonts/check/metadata/unique_weight_style_pairs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unique_weight_style_pairs)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"?</summary>

* [com.google.fonts/check/metadata/license](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/license)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb should contain at least "menu" and "latin" subsets.</summary>

* [com.google.fonts/check/metadata/menu_and_latin](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/menu_and_latin)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb subsets should be alphabetically ordered.</summary>

* [com.google.fonts/check/metadata/subsets_order](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/subsets_order)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb includes production subsets.</summary>

* [com.google.fonts/check/metadata/includes_production_subsets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/includes_production_subsets)
<pre>--- Rationale ---
Check METADATA.pb file includes the same subsets as the family in production.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, listed_on_gfonts_api

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice is the same in all fonts?</summary>

* [com.google.fonts/check/metadata/copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that METADATA.pb family values are all the same.</summary>

* [com.google.fonts/check/metadata/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/familyname)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: According to Google Fonts standards, families should have a Regular style.</summary>

* [com.google.fonts/check/metadata/has_regular](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/has_regular)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Regular should be 400.</summary>

* [com.google.fonts/check/metadata/regular_is_400](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/regular_is_400)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, has_regular_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checks METADATA.pb font.name field matches family name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/family_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/post_script_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/post_script_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name value matches fullname declared on the name table?</summary>

* [com.google.fonts/check/metadata/nameid/full_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/full_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name value should be same as the family name declared on the name table.</summary>

* [com.google.fonts/check/metadata/nameid/font_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/font_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, style

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ?</summary>

* [com.google.fonts/check/metadata/match_fullname_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_fullname_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values?</summary>

* [com.google.fonts/check/metadata/match_filename_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_filename_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_name_values)

* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.full_name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_full_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_full_name_values)

* 💤 **SKIP** Unfulfilled Conditions: style, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.filename field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_filename_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_filename_values)

* 💤 **SKIP** Unfulfilled Conditions: style, family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.post_script_name field contains font name in right format?</summary>

* [com.google.fonts/check/metadata/valid_post_script_name_values](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_post_script_name_values)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright notices match canonical pattern in METADATA.pb</summary>

* [com.google.fonts/check/metadata/valid_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/valid_copyright)
<pre>--- Rationale ---
The expected pattern for the copyright string adheres to the following rules:
* It must say &quot;Copyright&quot; followed by a 4 digit year (optionally followed by a
hyphen and another 4 digit year)
* Then it must say &quot;The &lt;familyname&gt; Project Authors&quot;
* And within parentheses, a URL for a git repository must be provided
* The check is case insensitive and does not validate whether the familyname is
correct, even though we&#x27;d expect it is (and we may soon update the check to
validate that aspect as well!)
Here is an example of a valid copyright string:
&quot;Copyright 2017 The Archivo Black Project Authors
(https://github.com/Omnibus-Type/ArchivoBlack)&quot;</pre>

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'.</summary>

* [com.google.fonts/check/metadata/reserved_font_name](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/reserved_font_name)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Copyright notice shouldn't exceed 500 chars.</summary>

* [com.google.fonts/check/metadata/copyright_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/copyright_max_length)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Font filenames match font.filename entries?</summary>

* [com.google.fonts/check/metadata/filenames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/filenames)
<pre>--- Rationale ---
Note:
This check only looks for files in the current directory.
Font files in subdirectories are checked by these other two checks:
 - com.google.fonts/check/metadata/undeclared_fonts
 - com.google.fonts/check/repo/vf_has_static_fonts
We may want to merge them all into a single check.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.style "italic" matches font internals?</summary>

* [com.google.fonts/check/metadata/italic_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/italic_style)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.style "normal" matches font internals?</summary>

* [com.google.fonts/check/metadata/normal_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/normal_style)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table?</summary>

* [com.google.fonts/check/metadata/nameid/family_and_full_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/family_and_full_names)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check if fontname is not camel cased.</summary>

* [com.google.fonts/check/metadata/fontname_not_camel_cased](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/fontname_not_camel_cased)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check font name is the same as family name.</summary>

* [com.google.fonts/check/metadata/match_name_familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_name_familyname)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata, font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Check that font weight has a canonical value.</summary>

* [com.google.fonts/check/metadata/canonical_weight_value](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_weight_value)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Check METADATA.pb font weights are correct.</summary>

* [com.google.fonts/check/metadata/os2_weightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/os2_weightclass)
<pre>--- Rationale ---
Check METADATA.pb font weights are correct.
For static fonts, the metadata weight should be the same as the static font&#x27;s
OS/2 usWeightClass.
For variable fonts, the weight value should be 400 if the font&#x27;s wght axis range
includes 400, otherwise it should be the value closest to 400.</pre>

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb weight matches postScriptName for static fonts.</summary>

* [com.google.fonts/check/metadata/match_weight_postscript](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/match_weight_postscript)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Font styles are named canonically?</summary>

* [com.google.fonts/check/metadata/canonical_style_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/canonical_style_names)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Glyphs are similiar to Google Fonts version?</summary>

* [com.google.fonts/check/production_glyphs_similarity](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity)

* 💤 **SKIP** Unfulfilled Conditions: api_gfonts_ttFont

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/fsselection](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fsselection)

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking post.italicAngle value.</summary>

* [com.google.fonts/check/italic_angle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/italic_angle)
<pre>--- Rationale ---
The &#x27;post&#x27; table italicAngle property should be a reasonable amount, likely not
more than -20°, never more than -30°, and never greater than 0°. Note that in
the OpenType specification, the value is negative for a lean rightwards.
https://docs.microsoft.com/en-us/typography/opentype/spec/post</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/mac_style](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mac_style)
<pre>--- Rationale ---
The values of the flags on the macStyle entry on the &#x27;head&#x27; OpenType table that
describe whether a font is bold and/or italic must be coherent with the actual
style of the font as inferred by its filename.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* 💤 **SKIP** Unfulfilled Conditions: not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Copyright field for this font on METADATA.pb matches all copyright notice entries on the name table ?</summary>

* [com.google.fonts/check/metadata/nameid/copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/nameid/copyright)

* 💤 **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Font has all mandatory 'name' table entries?</summary>

* [com.google.fonts/check/name/mandatory_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/mandatory_entries)

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: FONT_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/familyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname)
<pre>--- Rationale ---
Checks that the family name infered from the font filename matches the string at
nameID 1 (NAMEID_FONT_FAMILY_NAME) if it conforms to RIBBI and otherwise checks
that nameID 1 is the family name + the style name.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: FULL_FONT_NAME entries.</summary>

* [com.google.fonts/check/name/fullfontname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/fullfontname)
<pre>--- Rationale ---
Requirements for the FULL_FONT_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style_with_spaces

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: POSTSCRIPT_NAME entries.</summary>

* [com.google.fonts/check/name/postscriptname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/postscriptname)
<pre>--- Rationale ---
Requirements for the POSTSCRIPT_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicfamilyname)
<pre>--- Rationale ---
Requirements for the TYPOGRAPHIC_FAMILY_NAME entries in the &#x27;name&#x27; table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: style

</details>
<details>
<summary>💤 <b>SKIP:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted)
<pre>--- Rationale ---
Hinted fonts must have head table flag bit 3 set.
Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of
Head::flags decides whether PPEM should be rounded. This bit should always be
set for hinted fonts.
Note:
Bit 3 = Force ppem to integer values for all internal scaler math;
        May use fractional ppem sizes if this bit is clear;</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_hinted

</details>
<details>
<summary>💤 <b>SKIP:</b> Directory name in GFonts repo structure must match NameID 1 of the regular.</summary>

* [com.google.fonts/check/repo/dirname_matches_nameid_1](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/dirname_matches_nameid_1)

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure, not is_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> A static fonts directory with at least two fonts must accompany variable fonts</summary>

* [com.google.fonts/check/repo/vf_has_static_fonts](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/vf_has_static_fonts)
<pre>--- Rationale ---
Variable font family directories kept in the google/fonts git repo may include a
static/ subdir containing static fonts.
These files are meant to be served for users that still lack support for
variable fonts in their web browsers.</pre>

* 💤 **SKIP** Unfulfilled Conditions: gfonts_repo_structure

</details>
<details>
<summary>💤 <b>SKIP:</b> Check upstream.yaml file contains all required fields</summary>

* [com.google/fonts/check/repo/upstream_yaml_has_required_fields](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google/fonts/check/repo/upstream_yaml_has_required_fields)
<pre>--- Rationale ---
If a family has been pushed using the gftools packager, we must check that all
the required fields in the upstream.yaml file have been populated.</pre>

* 💤 **SKIP** Unfulfilled Conditions: upstream_yaml

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts.</summary>

* [com.google.fonts/check/vertical_metrics_regressions](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics_regressions)
<pre>--- Rationale ---
If the family already exists on Google Fonts, we need to ensure that the checked
family&#x27;s vertical metrics are similar. This check will test the following schema
which was outlined in Fontbakery issue #1162 [1]:
- The family should visually have the same vertical metrics as the Regular style
hosted on Google Fonts.
- If the family on Google Fonts has differing hhea and typo metrics, the family
being checked should use the typo metrics for both the hhea and typo entries.
- If the family on Google Fonts has use typo metrics not enabled and the family
being checked has it enabled, the hhea and typo metrics should use the family on
Google Fonts winAscent and winDescent values.
- If the upms differ, the values must be scaled so the visual appearance is the
same.
[1] https://github.com/googlefonts/fontbakery/issues/1162</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_remote_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Check font follows the Google Fonts CJK vertical metric schema</summary>

* [com.google.fonts/check/cjk_vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics)
<pre>--- Rationale ---
CJK fonts have different vertical metrics when compared to Latin fonts. We
follow the schema developed by dr Ken Lunde for Source Han Sans and the Noto CJK
fonts.
Our documentation includes further information:
https://github.com/googlefonts/gf-docs/tree/main/Spec#cjk-vertical-metrics</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts.</summary>

* [com.google.fonts/check/cjk_vertical_metrics_regressions](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_vertical_metrics_regressions)
<pre>--- Rationale ---
Check CJK family has the same vertical metrics as the same family hosted on
Google Fonts.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font, regular_remote_style

</details>
<details>
<summary>💤 <b>SKIP:</b> Does the font contain less than 40 CJK characters?</summary>

* [com.google.fonts/check/cjk_not_enough_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/cjk_not_enough_glyphs)
<pre>--- Rationale ---
Hangul has 40 characters and it&#x27;s the smallest CJK writing system.
If a font contains less CJK glyphs than this writing system, we inform the user
that some glyphs may be encoded incorrectly.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate METADATA.pb axes values are within gf-axisregistry bounds. </summary>

* [com.google.fonts/check/metadata/gf-axisregistry_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf-axisregistry_bounds)
<pre>--- Rationale ---
Each axis range in a METADATA.pb file must be registered, and within the bounds
of the axis definition in the Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate METADATA.pb axes tags are defined in gf-axisregistry. </summary>

* [com.google.fonts/check/metadata/gf-axisregistry_valid_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/gf-axisregistry_valid_tags)
<pre>--- Rationale ---
Ensure all axes in a METADATA.pb file are registered in the Google Fonts Axis
Registry, available at https://github.com/google/fonts/tree/main/axisregistry
Why does Google Fonts have its own Axis Registry?
We support a superset of the OpenType axis registry axis set, and use additional
metadata for each axis. Axes present in a font file but not in this registry
will not function via our API. No variable font is expected to support all of
the axes here.
Any font foundry or distributor library that offers variable fonts has a
implicit, latent, de-facto axis registry, which can be extracted by scanning the
library for axes&#x27; tags, labels, and min/def/max values. While in 2016 Microsoft
originally offered to include more axes in the OpenType 1.8 specification
(github.com/microsoft/OpenTypeDesignVariationAxisTags), as of August 2020, this
effort has stalled. We hope more foundries and distributors will publish
documents like this that make their axes explicit, to encourage of adoption of
variable fonts throughout the industry, and provide source material for a future
update to the OpenType specification&#x27;s axis registry.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Validate VF axes match the ones declared on METADATA.pb. </summary>

* [com.google.fonts/check/metadata/consistent_axis_enumeration](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/consistent_axis_enumeration)
<pre>--- Rationale ---
All font variation axes present in the font files must be properly declared on
METADATA.pb so that they can be served by the GFonts API.</pre>

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure METADATA.pb does not use escaped strings.</summary>

* [com.google.fonts/check/metadata/escaped_strings](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/escaped_strings)
<pre>--- Rationale ---
In some cases we&#x27;ve seen designer names and other fields with escaped strings in
METADATA files.
Nowadays the strings can be full unicode strings and do not need escaping.</pre>

* 💤 **SKIP** Unfulfilled Conditions: metadata_file

</details>
<details>
<summary>💤 <b>SKIP:</b> METADATA.pb: Designer is listed with the correct name on the Google Fonts catalog of designers?</summary>

* [com.google.fonts/check/metadata/designer_profiles](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/designer_profiles)

* 💤 **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>💤 <b>SKIP:</b> Checking with ftxvalidator.</summary>

* [com.google.fonts/check/ftxvalidator](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator)

* 💤 **SKIP** Unfulfilled Conditions: ftxvalidator_cmd

</details>
<details>
<summary>💤 <b>SKIP:</b> Each font in set of sibling families must have the same set of vertical metrics values.</summary>

* [com.google.fonts/check/superfamily/vertical_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/vertical_metrics)
<pre>--- Rationale ---
We may want all fonts within a super-family (all sibling families) to have the
same vertical metrics so their line spacing is consistent across the
super-family.
This is an experimental extended version of
com.google.fonts/check/superfamily/vertical_metrics and for now it will only
result in WARNs.</pre>

* 💤 **SKIP** Sibling families were not detected.

</details>
<details>
<summary>💤 <b>SKIP:</b> Ensure indic fonts have the Indian Rupee Sign glyph. </summary>

* [com.google.fonts/check/rupee](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/rupee)
<pre>--- Rationale ---
Per Bureau of Indian Standards every font supporting one of the official Indian
languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_indic_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Is the CFF subr/gsubr call depth > 10?</summary>

* [com.adobe.fonts/check/cff_call_depth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_call_depth)
<pre>--- Rationale ---
Per &quot;The Type 2 Charstring Format, Technical Note #5177&quot;, the &quot;Subr nesting,
stack limit&quot; is 10.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> Is the CFF2 subr/gsubr call depth > 10?</summary>

* [com.adobe.fonts/check/cff2_call_depth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff2_call_depth)
<pre>--- Rationale ---
Per &quot;The CFF2 CharString Format&quot;, the &quot;Subr nesting, stack limit&quot; is 10.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff2

</details>
<details>
<summary>💤 <b>SKIP:</b> Does the font use deprecated CFF operators or operations?</summary>

* [com.adobe.fonts/check/cff_deprecated_operators](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_deprecated_operators)
<pre>--- Rationale ---
The &#x27;dotsection&#x27; operator and the use of &#x27;endchar&#x27; to build accented characters
from the Adobe Standard Encoding Character Set (&quot;seac&quot;) are deprecated in CFF.
Adobe recommends repairing any fonts that use these, especially endchar-as-seac,
because a rendering issue was discovered in Microsoft Word with a font that
makes use of this operation. The check treats that useage as a FAIL. There are
no known ill effects of using dotsection, so that check is a WARN.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> CFF table FontName must match name table ID 6 (PostScript name).</summary>

* [com.adobe.fonts/check/name/postscript_vs_cff](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_vs_cff)
<pre>--- Rationale ---
The PostScript name entries in the font&#x27;s &#x27;name&#x27; table should match the FontName
string in the &#x27;CFF &#x27; table.
The &#x27;CFF &#x27; table has a lot of information that is duplicated in other tables.
This information should be consistent across tables, because there&#x27;s no
guarantee which table an app will get the data from.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_wdth_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wdth&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
If a variable font has a &#x27;wdth&#x27; (Width) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be 100.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_wdth_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_slnt_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_slnt_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;slnt&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_slnt
If a variable font has a &#x27;slnt&#x27; (Slant) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be zero.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_slnt_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_ital_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_ital_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;ital&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_ital
If a variable font has a &#x27;ital&#x27; (Italic) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be zero.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_ital_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_opsz_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_opsz_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;opsz&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz
If a variable font has an &#x27;opsz&#x27; (Optical Size) axis, then the coordinate of its
&#x27;Regular&#x27; instance is recommended to be a value in the range 10 to 16.</pre>

* 💤 **SKIP** Unfulfilled Conditions: regular_opsz_coord

</details>
<details>
<summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate specifies positive values in its range? </summary>

* [com.google.fonts/check/varfont/slnt_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/slnt_range)
<pre>--- Rationale ---
The OpenType spec says at
https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt that:
[...] the scale for the Slant axis is interpreted as the angle of slant in
counter-clockwise degrees from upright. This means that a typical, right-leaning
oblique design will have a negative slant value. This matches the scale used for
the italicAngle field in the post table.</pre>

* 💤 **SKIP** Unfulfilled Conditions: slnt_axis

</details>
<details>
<summary>💤 <b>SKIP:</b> Are any segments inordinately short?</summary>

* [com.google.fonts/check/outline_short_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments)
<pre>--- Rationale ---
This check looks for outline segments which seem particularly short (less than
0.006%% of the overall path length).
This check is not run for variable fonts, as they may legitimately have short
segments. As this check is liable to generate significant numbers of false
positives, it will pass if there are more than 100 reported short segments.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do any segments have colinear vectors?</summary>

* [com.google.fonts/check/outline_colinear_vectors](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors)
<pre>--- Rationale ---
This check looks for consecutive line segments which have the same angle. This
normally happens if an outline point has been added by accident.
This check is not run for variable fonts, as they may legitimately have colinear
vectors.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do outlines contain any jaggy segments?</summary>

* [com.google.fonts/check/outline_jaggy_segments](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments)
<pre>--- Rationale ---
This check heuristically detects outline segments which form a particularly
small angle, indicative of an outline error. This may cause false positives in
cases such as extreme ink traps, so should be regarded as advisory and backed up
by manual inspection.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Do outlines contain any semi-vertical or semi-horizontal lines?</summary>

* [com.google.fonts/check/outline_semi_vertical](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical)
<pre>--- Rationale ---
This check detects line segments which are nearly, but not quite, exactly
horizontal or vertical. Sometimes such lines are created by design, but often
they are indicative of a design error.
This check is disabled for italic styles, which often contain nearly-upright
lines.</pre>

* 💤 **SKIP** Unfulfilled Conditions: is_not_variable_font

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that texts shape as per expectation</summary>

* [com.google.fonts/check/shaping/regression](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/regression)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
compares expected shaping against actual shaping, reporting any differences.
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that no forbidden glyphs are found while shaping</summary>

* [com.google.fonts/check/shaping/forbidden](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/forbidden)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
reports if any glyphs are generated in the shaping which should not be produced.
(For example, .notdef glyphs, visible viramas, etc.)
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>💤 <b>SKIP:</b> Check that no collisions are found while shaping</summary>

* [com.google.fonts/check/shaping/collides](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/collides)
<pre>--- Rationale ---
Fonts with complex layout rules can benefit from regression tests to ensure that
the rules are behaving as designed. This checks runs a shaping test suite and
reports instances where the glyphs collide in unexpected ways.
Shaping test suites should be written by the font engineer and referenced in the
fontbakery configuration file. For more information about write shaping test
files and how to configure fontbakery to read the shaping test suites, see
https://simoncozens.github.io/tdd-for-otl/</pre>

* 💤 **SKIP** Shaping test directory not defined in configuration file

</details>
<details>
<summary>ℹ <b>INFO:</b> Show hinting filesize impact.</summary>

* [com.google.fonts/check/hinting_impact](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/hinting_impact)
<pre>--- Rationale ---
This check is merely informative, displaying and useful comparison of filesizes
of hinted versus unhinted font files.</pre>

* ℹ **INFO** Hinting filesize impact:

 |               | ./fonts/vf/PlusJakartaSans[wght].ttf          |
 |:------------- | ---------------:|
 | Dehinted Size | 172.3kb |
 | Hinted Size   | 172.4kb   |
 | Increase      | 24 bytes      |
 | Change        | 0.0 %  |
 [code: size-impact]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
This check finds which version of ttfautohint was used, by inspecting name table
entries and then finds which version of ttfautohint is currently installed in
the system.</pre>

* ℹ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.006'] [code: version-not-detected]

</details>
<details>
<summary>ℹ <b>INFO:</b> EPAR table present in font?</summary>

* [com.google.fonts/check/epar](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/epar)
<pre>--- Rationale ---
The EPAR table is/was a way of expressing common licensing permissions and
restrictions in metadata; while almost nothing supported it, Dave Crossland
wonders that adding it to everything in Google Fonts could help make it more
popular.
More info is available at:
https://davelab6.github.io/epar/</pre>

* ℹ **INFO** EPAR table not present in font. To learn more see https://github.com/googlefonts/fontbakery/issues/818 [code: lacks-EPAR]

</details>
<details>
<summary>ℹ <b>INFO:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
<pre>--- Rationale ---
Traditionally version 0 &#x27;gasp&#x27; tables were set so that font sizes below 8 ppem
had no grid fitting but did have antialiasing. From 9-16 ppem, just grid
fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled
on. The use of accelerated graphics cards and higher resolution screens make
this approach obsolete. Microsoft&#x27;s DirectWrite pushed this even further with
much improved rendering built into the OS and apps.
In this scenario it makes sense to simply toggle all 4 flags ON for all font
sizes.</pre>

* ℹ **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use grid-fitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®
 [code: ranges]
* 🍞 **PASS** The 'gasp' table is correctly set, with one gaspRange:value of 0xFFFF:0x0F.

</details>
<details>
<summary>ℹ <b>INFO:</b> Check for font-v versioning.</summary>

* [com.google.fonts/check/fontv](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontv)
<pre>--- Rationale ---
The git sha1 tagging and dev/release features of Source Foundry `font-v` tool
are awesome and we would love to consider upstreaming the approach into fontmake
someday. For now we only emit a WARN if a given font does not yet follow the
experimental versioning style, but at some point we may start enforcing it.</pre>

* ℹ **INFO** Version string is: "Version 2.006"
The version string must ideally include a git commit hash and either a "dev" or a "release" suffix such as in the example below:
"Version 1.3; git-0d08353-release" [code: bad-format]

</details>
<details>
<summary>ℹ <b>INFO:</b> Font contains all required tables?</summary>

* [com.google.fonts/check/required_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables)
<pre>--- Rationale ---
Depending on the typeface and coverage of a font, certain tables are recommended
for optimum quality. For example, the performance of a non-linear font is
improved if the VDMX, LTSH, and hdmx tables are present. Non-monospaced Latin
fonts should have a kern table. A gasp table is necessary if a designer wants to
influence the sizes at which grayscaling is used under Windows. A DSIG table
containing a digital signature helps ensure the integrity of the font file. Etc.</pre>

* ℹ **INFO** This font contains the following optional tables:
 - loca
 - prep
 - GPOS
 - GSUB
 - DSIG 
 - gasp [code: required-tables]
* 🍞 **PASS** Font contains all required tables.

</details>
<details>
<summary>ℹ <b>INFO:</b> List all superfamily filepaths</summary>

* [com.google.fonts/check/superfamily/list](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/list)
<pre>--- Rationale ---
This is a merely informative check that lists all sibling families detected by
fontbakery.
Only the fontfiles in these directories will be considered in superfamily-level
checks.</pre>

* ℹ **INFO** ./fonts/vf [code: family-path]

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
<pre>--- Rationale ---
A font&#x27;s filename must be composed in the following manner:
&lt;familyname&gt;-&lt;stylename&gt;.ttf
- Nunito-Regular.ttf,
- Oswald-BoldItalic.ttf
Variable fonts must list the axis tags in alphabetical order in square brackets
and separated by commas:
- Roboto[wdth,wght].ttf
- Familyname-Italic[wght].ttf</pre>

* 🍞 **PASS** ./fonts/vf/PlusJakartaSans[wght].ttf is named canonically.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 fsType does not impose restrictions.</summary>

* [com.google.fonts/check/fstype](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fstype)
<pre>--- Rationale ---
The fsType in the OS/2 table is a legacy DRM-related field. Fonts in the Google
Fonts collection must have it set to zero (also known as &quot;Installable
Embedding&quot;). This setting indicates that the fonts can be embedded in documents
and permanently installed by applications on remote systems.
More detailed info is available at:
https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fstype</pre>

* 🍞 **PASS** OS/2 fsType is properly set to zero.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* 🍞 **PASS** OS/2 VendorID 'TOKO' looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check `Google Fonts Latin Core` glyph coverage.</summary>

* [com.google.fonts/check/glyph_coverage](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage)
<pre>--- Rationale ---
Google Fonts expects that fonts in its collection support at least the minimal
set of characters defined in the `GF-latin-core` glyph-set.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Substitute copyright, registered and trademark symbols in name table entries.</summary>

* [com.google.fonts/check/name/unwanted_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/unwanted_chars)

* 🍞 **PASS** No need to substitute copyright, registered and trademark symbols in name table entries of this font.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)
<pre>--- Rationale ---
Google Fonts expects variable fonts, static ttfs and static otfs to have
differing OS/2 usWeightClass values.
For Variable Fonts, Thin-Black must be 100-900
For static ttfs, Thin-Black can be 100-900 or 250-900
For static otfs, Thin-Black must be 250-900
If static otfs are set lower than 250, text may appear blurry in legacy Windows
applications.
Glyphsapp users can change the usWeightClass value of an instance by adding a
&#x27;weightClass&#x27; customParameter.</pre>

* 🍞 **PASS** OS/2 usWeightClass is good

</details>
<details>
<summary>🍞 <b>PASS:</b> Check OFL body text is correct.</summary>

* [com.google.fonts/check/license/OFL_body_text](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text)
<pre>--- Rationale ---
Check OFL body text is correct. Often users will accidently delete parts of the
body text.</pre>

* 🍞 **PASS** OFL license body text is correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Description strings in the name table must not exceed 200 characters.</summary>

* [com.google.fonts/check/name/description_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length)
<pre>--- Rationale ---
An old FontLab version had a bug which caused it to store copyright notices in
nameID 10 entries.
In order to detect those and distinguish them from actual legitimate usage of
this name table entry, we expect that such strings do not exceed a reasonable
length of 200 chars.
Longer strings are likely instances of the FontLab bug.</pre>

* 🍞 **PASS** All description name records have reasonably small lengths.

</details>
<details>
<summary>🍞 <b>PASS:</b> Version format is correct in 'name' table?</summary>

* [com.google.fonts/check/name/version_format](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/version_format)

* 🍞 **PASS** Version format in NAME table entries is correct.

</details>
<details>
<summary>🍞 <b>PASS:</b> Make sure family name does not begin with a digit.</summary>

* [com.google.fonts/check/name/familyname_first_char](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/familyname_first_char)
<pre>--- Rationale ---
Font family names which start with a numeral are often not discoverable in
Windows applications.</pre>

* 🍞 **PASS** Font family name first character is not a digit.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there non-ASCII characters in ASCII-only NAME table entries?</summary>

* [com.google.fonts/check/name/ascii_only_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/ascii_only_entries)
<pre>--- Rationale ---
The OpenType spec requires ASCII for the POSTSCRIPT_NAME (nameID 6).
For COPYRIGHT_NOTICE (nameID 0) ASCII is required because that string should be
the same in CFF fonts which also have this requirement in the OpenType spec.
Note:
A common place where we find non-ASCII strings is on name table entries with
NameID &gt; 18, which are expressly for localising the ASCII-only IDs into Hindi /
Arabic / etc.</pre>

* 🍞 **PASS** None of the ASCII-only NAME table entries contain non-ASCII characteres.

</details>
<details>
<summary>🍞 <b>PASS:</b> Copyright notices match canonical pattern in fonts</summary>

* [com.google.fonts/check/font_copyright](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_copyright)

* 🍞 **PASS** Name Table entry: Copyright field 'Copyright 2020 The Plus Jakarta Sans Project Authors (https://github.com/tokotype/PlusJakartaSans)' matches canonical pattern.
* 🍞 **PASS** Name table copyright entries are good

</details>
<details>
<summary>🍞 <b>PASS:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/unitsperem_strict](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/unitsperem_strict)
<pre>--- Rationale ---
Even though the OpenType spec allows unitsPerEm to be any value between 16 and
16384, the Google Fonts project aims at a narrower set of reasonable values.
The spec suggests usage of powers of two in order to get some performance
improvements on legacy renderers, so those values are acceptable.
But values of 500 or 1000 are also acceptable, with the added benefit that it
makes upm math easier for designers, while the performance hit of not using a
power of two is most likely negligible nowadays.
Additionally, values above 2048 would likely result in unreasonable filesize
increases.</pre>

* 🍞 **PASS** Font em size is good (unitsPerEm = 1000).

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🍞 **PASS** FONT_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)
<pre>--- Rationale ---
Requirements for the TYPOGRAPHIC_SUBFAMILY_NAME entries in the &#x27;name&#x27; table.</pre>

* 🍞 **PASS** TYPOGRAPHIC_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Length of copyright notice must not exceed 500 characters.</summary>

* [com.google.fonts/check/name/copyright_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/copyright_length)
<pre>--- Rationale ---
This is an arbitrary max length for the copyright notice field of the name
table. We simply don&#x27;t want such notices to be too long. Typically such notices
are actually much shorter than this with a length of roughly 70 or 80
characters.</pre>

* 🍞 **PASS** All copyright notice name entries on the 'name' table are shorter than 500 characters.

</details>
<details>
<summary>🍞 <b>PASS:</b> Familyname must be unique according to namecheck.fontdata.com</summary>

* [com.google.fonts/check/fontdata_namecheck](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck)
<pre>--- Rationale ---
We need to check names are not already used, and today the best place to check
that is http://namecheck.fontdata.com</pre>

* 🍞 **PASS** Font familyname seems to be unique.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check a static ttf can be generated from a variable font.</summary>

* [com.google.fonts/check/varfont/generate_static](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/generate_static)
<pre>--- Rationale ---
Google Fonts may serve static fonts which have been generated from variable
fonts. This test will attempt to generate a static ttf using fontTool&#x27;s varLib
mutator.
The target font will be the mean of each axis e.g:
**VF font axes**
- min weight, max weight = 400, 800
- min width, max width = 50, 100
**Target Instance**
- weight = 600
- width = 75</pre>

* 🍞 **PASS** fontTools.varLib.mutator generated a static font instance

</details>
<details>
<summary>🍞 <b>PASS:</b> Check that variable fonts have an HVAR table.</summary>

* [com.google.fonts/check/varfont/has_HVAR](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/has_HVAR)
<pre>--- Rationale ---
Not having a HVAR table can lead to costly text-layout operations on some
platforms, which we want to avoid.
So, all variable fonts on the Google Fonts collection should have an HVAR with
valid values.
More info on the HVAR table can be found at:
https://docs.microsoft.com/en-us/typography/opentype/spec
/otvaroverview#variation-data-tables-and-miscellaneous-requirements</pre>

* 🍞 **PASS** This variable font contains an HVAR table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
<pre>--- Rationale ---
This setup is meant to ensure consistent rendering quality for fonts across all
devices (with different rendering/hinting capabilities).
Below is the snippet of instructions we expect to see in the fonts:
B8 01 FF    PUSHW 0x01FF
85          SCANCTRL (unconditinally turn on
                      dropout control mode)
B0 04       PUSHB 0x04
8D          SCANTYPE (enable smart dropout control)
&quot;Smart dropout control&quot; means activating rules 1, 2 and 5:
Rule 1: If a pixel&#x27;s center falls within the glyph outline,
        that pixel is turned on.
Rule 2: If a contour falls exactly on a pixel&#x27;s center,
        that pixel is turned on.
Rule 5: If a scan line between two adjacent pixel centers
        (either vertical or horizontal) is intersected
        by both an on-Transition contour and an off-Transition
        contour and neither of the pixels was already turned on
        by rules 1 and 2, turn on the pixel which is closer to
        the midpoint between the on-Transition contour and
        off-Transition contour. This is &quot;Smart&quot; dropout control.
For more detailed info (such as other rules not enabled in this snippet), please
refer to the TrueType Instruction Set documentation.</pre>

* 🍞 **PASS** 'prep' table contains instructions enabling smart dropout control.

</details>
<details>
<summary>🍞 <b>PASS:</b> There must not be VTT Talk sources in the font.</summary>

* [com.google.fonts/check/vttclean](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vttclean)
<pre>--- Rationale ---
The goal here is to reduce filesizes and improve pageloading when dealing with
webfonts.
The VTT Talk sources are not necessary at runtime and endup being just dead
weight when left embedded in the font binaries. The sources should be kept on
the project files but stripped out when building release binaries.</pre>

* 🍞 **PASS** There are no tables with VTT Talk sources embedded in the font.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there unwanted Apple tables?</summary>

* [com.google.fonts/check/aat](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/aat)
<pre>--- Rationale ---
Apple&#x27;s TrueType reference manual [1] describes SFNT tables not in the Microsoft
OpenType specification [2] and these can sometimes sneak into final release
files, but Google Fonts should only have OpenType tables.
[1] https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6.html
[2] https://docs.microsoft.com/en-us/typography/opentype/spec/</pre>

* 🍞 **PASS** There are no unwanted AAT tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> All name entries referenced by fvar instances exist on the name table?</summary>

* [com.google.fonts/check/fvar_name_entries](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fvar_name_entries)
<pre>--- Rationale ---
The purpose of this check is to make sure that all name entries referenced by
variable font instances do exist in the name table.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> A variable font must have named instances.</summary>

* [com.google.fonts/check/varfont_has_instances](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_has_instances)
<pre>--- Rationale ---
Named instances must be present in all variable fonts in order not to frustrate
the users&#x27; typical expectations of a traditional static font workflow.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Variable font weight coordinates must be multiples of 100.</summary>

* [com.google.fonts/check/varfont_weight_instances](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_weight_instances)
<pre>--- Rationale ---
The named instances on the weight axis of a variable font must have coordinates
that are multiples of 100 on the design space.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/ligature_carets](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/ligature_carets)
<pre>--- Rationale ---
All ligatures in a font must have corresponding caret (text cursor) positions
defined in the GDEF table, otherwhise, users may experience issues with caret
rendering.
If using GlyphsApp or UFOs, ligature carets can be defined as anchors with names
starting with &#x27;caret_&#x27;. These can be compiled with fontmake as of version
v2.4.0.</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Combined length of family and style must not exceed 27 characters.</summary>

* [com.google.fonts/check/name/family_and_style_max_length](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length)
<pre>--- Rationale ---
According to a GlyphsApp tutorial [1], in order to make sure all versions of
Windows recognize it as a valid font file, we must make sure that the
concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style
(NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20
characters.
After discussing the problem in more detail at `FontBakery issue #2179 [2] we
decided that allowing up to 27 chars would still be on the safe side, though.
[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances
[2] https://github.com/googlefonts/fontbakery/issues/2179</pre>

* 🍞 **PASS** All name entries are good.

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/name/line_breaks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks)
<pre>--- Rationale ---
There are some entries on the name table that may include more than one line of
text. The Google Fonts team, though, prefers to keep the name table entries
short and simple without line breaks.
For instance, some designers like to include the full text of a font license in
the &quot;copyright notice&quot; entry, but for the GFonts collection this entry should
only mention year, author and other basic info in a manner enforced by
com.google.fonts/check/font_copyright</pre>

* 🍞 **PASS** Name table entries are all single-line (no line-breaks found).

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/name/rfn](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/rfn)
<pre>--- Rationale ---
Some designers adopt the &quot;Reserved Font Name&quot; clause of the OFL license. This
means that the original author reserves the rights to the family name and other
people can only distribute modified versions using a different family name.
Google Fonts published updates to the fonts in the collection in order to fix
issues and/or implement further improvements to the fonts. It is important to
keep the family name so that users of the webfonts can benefit from the updates.
Since it would forbid such usage scenario, all families in the GFonts collection
are required to not adopt the RFN clause.
This check ensures &quot;Reserved Font Name&quot; is not mentioned in the name table.</pre>

* 🍞 **PASS** None of the name table strings contain "Reserved Font Name".

</details>
<details>
<summary>🍞 <b>PASS:</b> A font repository should not include fontbakery report files</summary>

* [com.google.fonts/check/repo/fb_report](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/fb_report)
<pre>--- Rationale ---
A FontBakery report is ephemeral and so should be used for posting issues on a
bug-tracker instead of being hosted in the font project repository.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> A font repository should not include ZIP files</summary>

* [com.google.fonts/check/repo/zip_files](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/repo/zip_files)
<pre>--- Rationale ---
Sometimes people check in ZIPs into their font project repositories. While we
accept the practice of checking in binaries, we believe that a ZIP is a step too
far ;)
Note: a source purist position is that only source files and build scripts
should be checked in.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances have correct coordinate values</summary>

* [com.google.fonts/check/varfont_instance_coordinates](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_coordinates)

* 🍞 **PASS** Instance coordinates are correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances have correct names</summary>

* [com.google.fonts/check/varfont_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_instance_names)

* 🍞 **PASS** Instance names are correct

</details>
<details>
<summary>🍞 <b>PASS:</b> Check variable font instances don't have duplicate names</summary>

* [com.google.fonts/check/varfont_duplicate_instance_names](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont_duplicate_instance_names)
<pre>--- Rationale ---
This check&#x27;s purpose is to detect duplicate named instances names in a given
variable font.
Repeating instance names may be the result of instances for several VF axes
defined in `fvar`, but since currently only weight+italic tokens are allowed in
instance names as per GF specs, they ended up repeating.
Instead, only a base set of fonts for the most default representation of the
family can be defined through instances in the `fvar` table, all other instances
will have to be left to access through the `STAT` table.</pre>

* 🍞 **PASS** Instance names are unique

</details>
<details>
<summary>🍞 <b>PASS:</b> Ensure VFs do not contain slnt or ital axes. </summary>

* [com.google.fonts/check/varfont/unsupported_axes](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/unsupported_axes)
<pre>--- Rationale ---
The &#x27;ital&#x27; and &#x27;slnt&#x27; axes are not supported yet in Google Chrome.
For the time being, we need to ensure that VFs do not contain either of these
axes. Once browser support is better, we can deprecate this check.
For more info regarding browser support, see:
https://arrowtype.github.io/vf-slnt-test/</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. </summary>

* [com.google.fonts/check/gf-axisregistry/fvar_axis_defaults](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gf-axisregistry/fvar_axis_defaults)
<pre>--- Rationale ---
Check that axis defaults have a corresponding fallback name registered at the
Google Fonts Axis Registry, available at
https://github.com/google/fonts/tree/main/axisregistry
This is necessary for the following reasons:
To get ZIP files downloads on Google Fonts to be accurate — otherwise the chosen
default font is not generated. The Newsreader family, for instance, has a
default value on the &#x27;opsz&#x27; axis of 16pt. If 16pt was not a registered fallback
position, then the ZIP file would instead include another position as default
(such as 14pt).
For the Variable fonts to display the correct location on the specimen page.
For VF with no weight axis to be displayed at all. For instance, Ballet, which
has no weight axis, was not appearing in sandbox because default position on
&#x27;opsz&#x27; axis was 16pt, and it was not yet a registered fallback positon.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Check small caps glyphs are available.</summary>

* [com.google.fonts/check/missing_small_caps_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/missing_small_caps_glyphs)
<pre>--- Rationale ---
Ensure small caps glyphs are available if a font declares smcp or c2sc OT
features.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts.</summary>

* [com.google.fonts/check/os2/use_typo_metrics](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/os2/use_typo_metrics)
<pre>--- Rationale ---
All fonts on the Google Fonts collection should have OS/2.fsSelection bit 7
(USE_TYPO_METRICS) set. This requirement is part of the vertical metrics scheme
established as a Google Fonts policy aiming at a common ground supported by all
major font rendering environments.
For more details, read:
https://github.com/googlefonts/gf-docs/blob/main/VerticalMetrics/README.md
Below is the portion of that document that is most relevant to this check:
Use_Typo_Metrics must be enabled. This will force MS Applications to use the
OS/2 Typo values instead of the Win values. By doing this, we can freely set the
Win values to avoid clipping and control the line height with the typo values.
It has the added benefit of future line height compatibility. When a new script
is added, we simply change the Win values to the new yMin and yMax, without
needing to worry if the line height have changed.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table records must not have trailing spaces.</summary>

* [com.google.fonts/check/name/trailing_spaces](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces)

* 🍞 **PASS** No trailing spaces on name table entries.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/family/win_ascent_and_descent](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent)
<pre>--- Rationale ---
A font&#x27;s winAscent and winDescent values should be greater than the head table&#x27;s
yMax, abs(yMin) values. If they are less than these values, clipping can occur
on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
If the font includes tall/deep writing systems such as Arabic or Devanagari, the
winAscent and winDescent can be greater than the yMax and abs(yMin) to
accommodate vowel marks.
When the win Metrics are significantly greater than the upm, the linespacing can
appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7
(Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This
means the font developer can control the linespacing with the typo values,
whilst avoiding clipping by setting the win values to values greater than the
yMax and abs(yMin).</pre>

* 🍞 **PASS** OS/2 usWinAscent & usWinDescent values look good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking OS/2 Metrics match hhea Metrics.</summary>

* [com.google.fonts/check/os2_metrics_match_hhea](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea)
<pre>--- Rationale ---
OS/2 and hhea vertical metric values should match. This will produce the same
linespacing on Mac, GNU+Linux and Windows.
- Mac OS X uses the hhea values.
- Windows uses OS/2 or Win, depending on the OS or fsSelection bit value.
When OS/2 and hhea vertical metrics match, the same linespacing results on
macOS, GNU+Linux and Windows. Unfortunately as of 2018, Google Fonts has
released many fonts with vertical metrics that don&#x27;t match in this way. When we
fix this issue in these existing families, we will create a visible change in
line/paragraph layout for either Windows or macOS users, which will upset some
of them.
But we have a duty to fix broken stuff, and inconsistent paragraph layout is
unacceptably broken when it is possible to avoid it.
If users complain and prefer the old broken version, they have the freedom to
take care of their own situation.</pre>

* 🍞 **PASS** OS/2.sTypoAscender/Descender values match hhea.ascent/descent.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking with ots-sanitize.</summary>

* [com.google.fonts/check/ots](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ots)

* 🍞 **PASS** ots-sanitize passed this file

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains '.notdef' as its first glyph?</summary>

* [com.google.fonts/check/mandatory_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs)
<pre>--- Rationale ---
The OpenType specification v1.8.2 recommends that the first glyph is the
&#x27;.notdef&#x27; glyph without a codepoint assigned and with a drawing.
https://docs.microsoft.com/en-us/typography/opentype/spec
/recom#glyph-0-the-notdef-glyph
Pre-v1.8, it was recommended that fonts should also contain &#x27;space&#x27;, &#x27;CR&#x27; and
&#x27;.null&#x27; glyphs. This might have been relevant for MacOS 9 applications.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/whitespace_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs)

* 🍞 **PASS** Font contains glyphs for whitespace characters.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font has **proper** whitespace glyph names?</summary>

* [com.google.fonts/check/whitespace_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames)
<pre>--- Rationale ---
This check enforces adherence to recommended whitespace (codepoints 0020 and
00A0) glyph names according to the Adobe Glyph List.</pre>

* 🍞 **PASS** Font has **AGL recommended** names for whitespace glyphs.

</details>
<details>
<summary>🍞 <b>PASS:</b> Whitespace glyphs have ink?</summary>

* [com.google.fonts/check/whitespace_ink](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink)

* 🍞 **PASS** There is no whitespace glyph with ink.

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/unwanted_tables](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables)
<pre>--- Rationale ---
Some font editors store source data in their own SFNT tables, and these can
sometimes sneak into final release files, which should only have OpenType spec
tables.</pre>

* 🍞 **PASS** There are no unwanted tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check correctness of STAT table strings </summary>

* [com.google.fonts/check/STAT_strings](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/STAT_strings)
<pre>--- Rationale ---
On the STAT table, the &quot;Italic&quot; keyword must not be used on AxisValues for
variation axes other than &#x27;ital&#x27;.</pre>

* 🍞 **PASS** Looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Glyph names are all valid?</summary>

* [com.google.fonts/check/valid_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames)
<pre>--- Rationale ---
Microsoft&#x27;s recommendations for OpenType Fonts states the following:
&#x27;NOTE: The PostScript glyph name must be no longer than 31 characters, include
only uppercase or lowercase English letters, European digits, the period or the
underscore, i.e. from the set [A-Za-z0-9_.] and should start with a letter,
except the special glyph name &quot;.notdef&quot; which starts with a period.&#x27;
https://docs.microsoft.com/en-us/typography/opentype/spec/recom#post-table
In practice, though, particularly in modern environments, glyph names can be as
long as 63 characters.
According to the &quot;Adobe Glyph List Specification&quot; available at:
https://github.com/adobe-type-tools/agl-specification</pre>

* 🍞 **PASS** Glyph names are all valid.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font contains unique glyph names?</summary>

* [com.google.fonts/check/unique_glyphnames](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unique_glyphnames)
<pre>--- Rationale ---
Duplicate glyph names prevent font installation on Mac OS X.</pre>

* 🍞 **PASS** Font contains unique glyph names.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking with fontTools.ttx</summary>

* [com.google.fonts/check/ttx-roundtrip](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ttx-roundtrip)

* 🍞 **PASS** Hey! It all looks good!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check all glyphs have codepoints assigned.</summary>

* [com.google.fonts/check/all_glyphs_have_codepoints](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/cmap.html#com.google.fonts/check/all_glyphs_have_codepoints)

* 🍞 **PASS** All glyphs have a codepoint value assigned.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking unitsPerEm value is reasonable.</summary>

* [com.google.fonts/check/unitsperem](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/head.html#com.google.fonts/check/unitsperem)
<pre>--- Rationale ---
According to the OpenType spec:
The value of unitsPerEm at the head table must be a value between 16 and 16384.
Any value in this range is valid.
In fonts that have TrueType outlines, a power of 2 is recommended as this allows
performance optimizations in some rasterizers.
But 1000 is a commonly used value. And 2000 may become increasingly more common
on Variable Fonts.</pre>

* 🍞 **PASS** The unitsPerEm value (1000) on the 'head' table is reasonable.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking font version fields (head and name table).</summary>

* [com.google.fonts/check/font_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/head.html#com.google.fonts/check/font_version)

* 🍞 **PASS** All font version fields match.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check if OS/2 xAvgCharWidth is correct.</summary>

* [com.google.fonts/check/xavgcharwidth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth)

* 🍞 **PASS** OS/2 xAvgCharWidth value is correct.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits.</summary>

* [com.adobe.fonts/check/fsselection_matches_macstyle](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.adobe.fonts/check/fsselection_matches_macstyle)
<pre>--- Rationale ---
The bold and italic bits in OS/2.fsSelection must match the bold and italic bits
in head.macStyle per the OpenType spec.</pre>

* 🍞 **PASS** The OS/2.fsSelection and head.macStyle bold and italic settings match.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check code page character ranges</summary>

* [com.google.fonts/check/code_pages](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/os2.html#com.google.fonts/check/code_pages)
<pre>--- Rationale ---
At least some programs (such as Word and Sublime Text) under Windows 7 do not
recognize fonts unless code page bits are properly set on the ulCodePageRange1
(and/or ulCodePageRange2) fields of the OS/2 table.
More specifically, the fonts are selectable in the font menu, but whichever
Windows API these applications use considers them unsuitable for any character
set, so anything set in these fonts is rendered with a fallback font of Arial.
This check currently does not identify which code pages should be set.
Auto-detecting coverage is not trivial since the OpenType specification leaves
the interpretation of whether a given code page is &quot;functional&quot; or not open to
the font developer to decide.
So here we simply detect as a FAIL when a given font has no code page declared
at all.</pre>

* 🍞 **PASS** At least one code page is defined.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font has correct post table version?</summary>

* [com.google.fonts/check/post_table_version](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/post.html#com.google.fonts/check/post_table_version)
<pre>--- Rationale ---
Apple recommends against using &#x27;post&#x27; table format 3 under most circumstances,
as it can create problems with some printer drivers and PDF documents. The
savings in disk space usually does not justify the potential loss in
functionality.
Source:
https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6post.html
The CFF2 table does not contain glyph names, so variable OTFs should be allowed
to use post table version 2.
This check expects:
- Version 2 for TTF or OTF CFF2 Variable fonts
- Version 3 for OTF</pre>

* 🍞 **PASS** Font has post table version 2.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check name table for empty records.</summary>

* [com.adobe.fonts/check/name/empty_records](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/empty_records)
<pre>--- Rationale ---
Check the name table for empty records, as this can cause problems in Adobe
apps.</pre>

* 🍞 **PASS** No empty name table records found.

</details>
<details>
<summary>🍞 <b>PASS:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/name/no_copyright_on_description](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description)

* 🍞 **PASS** Description strings in the name table do not contain any copyright string.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/monospace](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/monospace)
<pre>--- Rationale ---
There are various metadata in the OpenType spec to specify if a font is
monospaced or not. If the font is not truly monospaced, then no monospaced
metadata should be set (as sometimes they mistakenly are...)
Requirements for monospace fonts:
* post.isFixedPitch - &quot;Set to 0 if the font is proportionally spaced, non-zero
if the font is not proportionally spaced (monospaced)&quot;
  www.microsoft.com/typography/otspec/post.htm
* hhea.advanceWidthMax must be correct, meaning no glyph&#x27;s width value is
greater.
  www.microsoft.com/typography/otspec/hhea.htm
* OS/2.panose.bProportion must be set to 9 (monospace). Spec says: &quot;The PANOSE
definition contains ten digits each of which currently describes up to sixteen
variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font
mapper to determine family type. It also uses bProportion to determine if the
font is monospaced.&quot;
  www.microsoft.com/typography/otspec/os2.htm#pan
  monotypecom-test.monotype.de/services/pan2
* OS/2.xAvgCharWidth must be set accurately.
  &quot;OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by
Windows GDI&quot;
  http://typedrawers.com/discussion/comment/15397/#Comment_15397
Also we should report an error for glyphs not of average width.
Please also note:
Thomas Phinney told us that a few years ago (as of December 2019), if you gave a
font a monospace flag in Panose, Microsoft Word would ignore the actual advance
widths and treat it as monospaced. Source:
https://typedrawers.com/discussion/comment/45140/#Comment_45140</pre>

* 🍞 **PASS** Font is not monospaced and all related metadata look good. [code: good]

</details>
<details>
<summary>🍞 <b>PASS:</b> Does full font name begin with the font family name?</summary>

* [com.google.fonts/check/name/match_familyname_fullfont](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont)

* 🍞 **PASS** Full font name begins with the font family name.

</details>
<details>
<summary>🍞 <b>PASS:</b> Font follows the family naming recommendations?</summary>

* [com.google.fonts/check/family_naming_recommendations](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.google.fonts/check/family_naming_recommendations)

* 🍞 **PASS** Font follows the family naming recommendations.

</details>
<details>
<summary>🍞 <b>PASS:</b> Name table ID 6 (PostScript name) must be consistent across platforms.</summary>

* [com.adobe.fonts/check/name/postscript_name_consistency](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_name_consistency)
<pre>--- Rationale ---
The PostScript name entries in the font&#x27;s &#x27;name&#x27; table should be consistent
across platforms.
This is the TTF/CFF2 equivalent of the CFF &#x27;postscript_name_cff_vs_name&#x27; check.</pre>

* 🍞 **PASS** Entries in the "name" table for ID 6 (PostScript name) are consistent.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does the number of glyphs in the loca table match the maxp table?</summary>

* [com.google.fonts/check/loca/maxp_num_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/loca.html#com.google.fonts/check/loca/maxp_num_glyphs)

* 🍞 **PASS** 'loca' table matches numGlyphs in 'maxp' table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/linegaps](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps)

* 🍞 **PASS** OS/2 sTypoLineGap and hhea lineGap are both 0.

</details>
<details>
<summary>🍞 <b>PASS:</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables?</summary>

* [com.google.fonts/check/maxadvancewidth](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hhea.html#com.google.fonts/check/maxadvancewidth)

* 🍞 **PASS** MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/dsig](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig)
<pre>--- Rationale ---
Microsoft Office 2013 and below products expect fonts to have a digital
signature declared in a DSIG table in order to implement OpenType features. The
EOL date for Microsoft Office 2013 products is 4/11/2023. This issue does not
impact Microsoft Office 2016 and above products.
This checks verifies that this signature is available in the font.
A fake signature is enough to address this issue. If needed, a dummy table can
be added to the font with the `gftools fix-dsig` script available at
https://github.com/googlefonts/gftools
Reference: https://github.com/googlefonts/fontbakery/issues/1845</pre>

* 🍞 **PASS** Digital Signature (DSIG) exists.

</details>
<details>
<summary>🍞 <b>PASS:</b> Space and non-breaking space have the same width?</summary>

* [com.google.fonts/check/whitespace_widths](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/hmtx.html#com.google.fonts/check/whitespace_widths)

* 🍞 **PASS** Space and non-breaking space have the same width.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class)</summary>

* [com.google.fonts/check/gdef_spacing_marks](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks)
<pre>--- Rationale ---
Glyphs in the GDEF mark glyph class should be non-spacing.
Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
positioning that was only intended for building composite glyphs during design.</pre>

* 🍞 **PASS** Font does not has spacing glyphs in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class</summary>

* [com.google.fonts/check/gdef_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars)
<pre>--- Rationale ---
Mark characters should be in the GDEF mark glyph class.</pre>

* 🍞 **PASS** Font does not have mark characters not in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check GDEF mark glyph class doesn't have characters that are not marks)</summary>

* [com.google.fonts/check/gdef_non_mark_chars](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars)
<pre>--- Rationale ---
Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned
if they have mark anchors.
Only combining mark glyphs should be in that class. Any non-mark glyph must not
be in that class, in particular spacing glyphs.</pre>

* 🍞 **PASS** Font does not have non-mark characters in the GDEF mark glyph class.

</details>
<details>
<summary>🍞 <b>PASS:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value</summary>

* [com.google.fonts/check/gpos_kerning_info](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info)

* 🍞 **PASS** GPOS table check for kerning information passed.

</details>
<details>
<summary>🍞 <b>PASS:</b> Is there a usable "kern" table declared in the font?</summary>

* [com.google.fonts/check/kern_table](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/kern.html#com.google.fonts/check/kern_table)
<pre>--- Rationale ---
Even though all fonts should have their kerning implemented in the GPOS table,
there may be kerning info at the kern table as well.
Some applications such as MS PowerPoint require kerning info on the kern table.
More specifically, they require a format 0 kern subtable from a kern table
version 0 with only glyphs defined in the cmap table, which is the only one that
Windows understands (and which is also the simplest and more limited of all the
kern subtables).
Google Fonts ingests fonts made for download and use on desktops, and does all
web font optimizations in the serving pipeline (using libre libraries that
anyone can replicate.)
Ideally, TTFs intended for desktop users (and thus the ones intended for Google
Fonts) should have both KERN and GPOS tables.
Given all of the above, we currently treat kerning on a v0 kern table as a
good-to-have (but optional) feature.</pre>

* 🍞 **PASS** Font does not declare an optional "kern" table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Is there any unused data at the end of the glyf table?</summary>

* [com.google.fonts/check/glyf_unused_data](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_unused_data)

* 🍞 **PASS** There is no unused data at the end of the glyf table.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/points_out_of_bounds](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds)

* 🍞 **PASS** All glyph paths have coordinates within bounds!

</details>
<details>
<summary>🍞 <b>PASS:</b> Check glyphs do not have duplicate components which have the same x,y coordinates.</summary>

* [com.google.fonts/check/glyf_non_transformed_duplicate_components](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components)
<pre>--- Rationale ---
There have been cases in which fonts had faulty double quote marks, with each of
them containing two single quote marks as components with the same x, y
coordinates which makes them visually look like single quote marks.
This check ensures that glyphs do not contain duplicate components which have
the same x,y coordinates.</pre>

* 🍞 **PASS** Glyphs do not contain duplicate components which have the same x,y coordinates.

</details>
<details>
<summary>🍞 <b>PASS:</b> Check glyphs do not have components which are themselves components.</summary>

* [com.google.fonts/check/glyf_nested_components](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_nested_components)
<pre>--- Rationale ---
There have been bugs rendering variable fonts with nested components.
Additionally, some static fonts with nested components have been reported to
have rendering and printing issues.
For more info, see:
* https://github.com/googlefonts/fontbakery/issues/2961
* https://github.com/arrowtype/recursive/issues/412</pre>

* 🍞 **PASS** Glyphs do not contain nested components.

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance.</summary>

* [com.google.fonts/check/varfont/regular_wght_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wght_coord)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
If a variable font has a &#x27;wght&#x27; (Weight) axis, then the coordinate of its
&#x27;Regular&#x27; instance is required to be 400.</pre>

* 🍞 **PASS** Regular:wght is 400.

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance.</summary>

* [com.google.fonts/check/varfont/bold_wght_coord](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord)
<pre>--- Rationale ---
The Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27; available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght does
not specify a required value for the &#x27;Bold&#x27; instance of a variable font.
But Dave Crossland suggested that we should enforce a required value of 700 in
this case.</pre>

* 🍞 **PASS** Bold:wght is 700.

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances.</summary>

* [com.google.fonts/check/varfont/wght_valid_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wght_valid_range)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wght&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
On the &#x27;wght&#x27; (Weight) axis, the valid coordinate range is 1-1000.</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> The variable font 'wdth' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances.</summary>

* [com.google.fonts/check/varfont/wdth_valid_range](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wdth_valid_range)
<pre>--- Rationale ---
According to the Open-Type spec&#x27;s registered design-variation tag &#x27;wdth&#x27;
available at
https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
On the &#x27;wdth&#x27; (Width) axis, the valid coordinate range is 1-1000</pre>

* 🍞 **PASS** OK

</details>
<details>
<summary>🍞 <b>PASS:</b> All fvar axes have a correspondent Axis Record on STAT table? </summary>

* [com.google.fonts/check/varfont/stat_axis_record_for_each_axis](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/stat.html#com.google.fonts/check/varfont/stat_axis_record_for_each_axis)
<pre>--- Rationale ---
cording to the OpenType spec, there must be an Axis Record for every axis
defined in the fvar table.
tps://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-records</pre>

* 🍞 **PASS** STAT table has all necessary Axis Records

</details>
<details>
<summary>🍞 <b>PASS:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* 🍞 **PASS** So many Y-coordinates of points were close to boundaries that this was probably by design.

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 4 | 7 | 9 | 188 | 15 | 176 | 0 |
| 1% | 2% | 2% | 47% | 4% | 44% | 0% |
