### Presentations

It is possible to create high quality presentations in \\(LaTeX\\). To do this
we use the `beamer` document class:

```language-latex
\documentclass{beamer}
\begin{document}

\frame{This is my first slide.}

\frame{This is my second slide.}

\end{document}
```

It is possible to select from a number of different themes (and make your own):

```language-latex
\usetheme{default}
\usetheme{Boadilla}
\usetheme{Madrid}
\usetheme{Montpellier}
\usetheme{Warsaw}
\usetheme{Copenhagen}
\usetheme{Goettingen}
\usetheme{Hannover}
\usetheme{Berkeley}
```

A full document showing this is:

```language-latex
{% include main.tex %}
```
