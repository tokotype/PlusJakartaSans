# Plus Jakarta Sans

[![][Fontbakery]](https://ottta.github.io/PlusJakartaSans.git/fontbakery/fontbakery-report.html)
[![][Universal]](https://ottta.github.io/PlusJakartaSans.git/fontbakery/fontbakery-report.html)
[![][GF Profile]](https://ottta.github.io/PlusJakartaSans.git/fontbakery/fontbakery-report.html)
[![][Outline Correctness]](https://ottta.github.io/PlusJakartaSans.git/fontbakery/fontbakery-report.html)
[![][Shaping]](https://ottta.github.io/PlusJakartaSans.git/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fottta%2FPlusJakartaSans.git%2Fgh-pages%2Fbadges%2Foverall.json
[GF Profile]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fottta%2FPlusJakartaSans.git%2Fgh-pages%2Fbadges%2FGoogleFonts.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fottta%2FPlusJakartaSans.git%2Fgh-pages%2Fbadges%2FOutlineCorrectnessChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fottta%2FPlusJakartaSans.git%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fottta%2FPlusJakartaSans.git%2Fgh-pages%2Fbadges%2FUniversal.json

## About

Plus Jakarta Sans is a font family that takes geometric sans serif styles, designed by Gumpita Rahayu from Tokotype, the fonts were originally commissioned by 6616 Studio for Jakarta Provincial Government program's +Jakarta City of Collaboration identity in 2020.

Taking part of inspiration such as Neuzit Grotesk, Futura, and 1930s grotesque sans serif with almost monoline contrast and pointy curves, the fonts consist modern and clean cut forms, the x-height dimension slight taller to provide clear spaces between caps and x-height, this also equipped with open counter and balanced spaces to preserve the legibility at a range of sizes.

The beauty of diversity captured in typography. Like the city itself, the unique points of this fonts is that in some glyphs has its own diversity and characteristic of various explorations of forms that enrich the expressions and stories that coexist. The charms of Plus Jakarta Sans fonts appear when one looks closer, manifesting in a beauty that emerges once seen as a whole. Each alternate on the family contains several alternates characters, divided into three stylistic alternates which Lancip (Sharp), Lurus (Straight), and Lingkar (Swirl).

As part of Plus Jakarta as a city of collaboration, fonts are made available for public and use it under the SIL Open Font License.

To contribute to the project, Please see <a href="https://github.com/tokotype/PlusJakartaSans">github.com/tokotype/PlusJakartaSans</a> or visit http://www.tokotype.com

![/documentation/img/plusjakartasans.png](/documentation/img/plusjakartasans.png)

![/documentation/img/plusjakartasans-alt.gif](/documentation/img/plusjakartasans-alt.gif)

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://ottta.github.io/PlusJakartaSans.git.

## Changelog

### **20 May 2023 (Taufik Oktama) Plus Jakarta Sans v2.107
- Update font repository to [googlefonts-project-template](https://github.com/googlefonts/googlefonts-project-template)
- Fix inconsistent vertical metrics and make sure all glyphs will not be clipping
- Increase significant version number 2.007 > 2.107
- Write Display String in font info glyphsapp to `false`
- Fix all http to https due to fontbakery warning
- Restructure this README.md

### 19 May 2023 (Gumpita Rahayu) Plus Jakarta Sans v2.700

- Fixed shapeshifting glyphs on 'ohorn' and 'registered symbol'
- Removed tail on 'æ'
- Adjusted vertical metrics to compensate line-height issues
- Add  two strokes on '₦' (Naira symbol)

### 12 November 2021 (Gumpita Rahayu) Plus Jakarta Sans v2.600

- Adding SemiBold instance on static files
- Fixed missing kerning values
- Increasing quote character weight
- Redesigned diacritics glyphs
- Adding Tabular Figures (.tf)

### 21 December 2020 (Gumpita Rahayu) Plus Jakarta Sans v2.500

- Extending ascender character lowercase
- Fixed duplicated alternates


### **4 December 2020 (Gumpita Rahayu) Plus Jakarta Sans v2.400**

- Adding ExtraLight & ExtraLight Italic Master
- Reworking weights and instance
- Adding support for multiple languages (Incl. Vietnamese)
- Encoding based on GF Latin Pro & GF Latin Plus
- Variable fonts support (wght)
- Removed Plus Jakarta Sans Text Version (In addition, Lightest weight added)
- Adding several opentype features stylistic sets glyphs

21 February 2020 (Gumpita Rahayu) Plus Jakarta Sans v1.000

- Open sourced.
- Fine tuning to almost all glyphs.
- First public released.

![/documentation/img/plusjakartasans.gif](/documentation/img/plusjakartasans.gif)

## Contribution

If you want to contribute to develop improvements of this font family, you can fork this project and create an issue or email us at mail@tokotype.com

## License
This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
http://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.