### Inline mathematics

(Keywords: mathematics, inline.)
[Video demo](https://www.youtube.com/watch?v=TkVms4xO_cs)

Typesetting mathematics is \\(\LaTeX\\)'s strength. Here is an example of
including some "inline" mathematics:

```language-latex
Mathematics can be typed in to \LaTeX\ as $x^2$ and/or
\((a+b)^2=a^2+2ab+b^2\).
```

Note that using `\(` and `\)` is preferred over `$`. One of the reasons is that
it is easier for humans (and machines) to find the start and end of some
mathematics.

A full document making use of inline mathematics is:

```language-latex
{% include main.tex %}
```
