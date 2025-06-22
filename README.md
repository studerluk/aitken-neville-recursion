# Hardware implementation of the Aitken-Neville recursion

Interpolation is often key to perform analytical operations such as
_Integration_ and _Derivation_ which in turn are often key for
time critical applications or live analysis of data. One such interpolation
method is the Newton polynomial interpolation which uses the divided
difference in the Aitken-Neville recursion. This method consists of fairly
simple arithmetic operations and algorithms. Translating these algorithms into
hardware might prove to speedup the calculation of the Newton coefficients for
the interpolation polynomial.

## Requirements
```
sudo dnf install texlive \
	latexmk \
	texlive-german \
	texlive-e-french \
	texlive-bfh-ci \
	texlive-translations \
	texlive-anyfontsize \
	texlive-sourceserifpro \
	texlive-nunito \
	texlive-tcolorbox \
	texlive-tikzfill \
	texlive-fontawesome \
	texlive-siunitx \
	texlive-wrapfig \
	texlive-multirow \
	texlive-blindtext \
	texlive-glossaries-extra \
	texlive-glossaries-english \
	texlive-tocvsec2 \
	texlive-svg \
	texlive-abstract \
	texlive-hyphenat
```

## Quick Start
```
latexmk
```
