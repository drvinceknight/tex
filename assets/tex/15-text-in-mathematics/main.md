### Text in mathematics

(Keywords: text, mbox, mathematics.)
[Video demo](https://www.youtube.com/watch?v=hSaf-aJscUw)

To include text within mathematics we can use the `text`
command from the `amsmath` package:

```language-latex
\[
	x^2 = 1 \text{ implies} x=\pm 1
\]
```

Be sure to include `usepackage{amsmath}` in the preamble.

Another command that does this is `mbox` which does not require the amsmath package.

A full document making use of `\text` is:

```language-latex
{% include main.tex %}
```
