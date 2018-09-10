[![Build
Status](https://travis-ci.org/drvinceknight/tex.svg?branch=master)](https://travis-ci.org/drvinceknight/tex)

# LaTeX: A tutorial based on a set of minimal examples.

This is the source code for a single page website tutorial on the use of LaTeX.

There are two use cases for this material:

- Work through the entire tutorial sequentially;
- Use a specific chapter as is necessary: the fact that this is a single page
  website makes it searchable.

## Source materials

The source materials for the course can be found in `assets/tex` which for each
chapter (usually) contains:

- `main.md`: a markdown file that describes the concept;
- `main.tex`: a latex file showing a minimal example of a given concept.

## Building the site

The single page site is built using Python. A conda environment file containing
all requirements is included: `environment.yml`.

To create the environment:

```
$ conda env create -f environment.yml
```

To build the site:

```
$ source activate tch-tex
$ inv main
```

**Note** this requires `latexmk` to be available: it will build all `main.tex`
files included.

This build process is run by `travis.ci` which ensures that all provided
examples compile.
