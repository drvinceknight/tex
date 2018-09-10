### Page formatting

(Keywords: header, margin, footer, page, geometry.)

It is possible to modify margins, footer and header size of \\(\LaTeX\\) pages.

This is done using the geometry package.

```language-latex
\usepackage[margin=1.5cm, includefoot, footskip=30pt]{geometry}
```

This sets a margin size, include a footer and sets the distance between the text
and the footer.

There are numerous other options that can be passed to the geometry package.
Some of these are:

- `textwidth`: The width of the text
- `headheight`: Height of the header
- `top`: Distance from text to top

A full document showing this is:

```language-latex
{% include main.tex %}
```
