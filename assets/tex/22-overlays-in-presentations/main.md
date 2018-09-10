### Titles and sections with presentations

Most of the LaTeX code you have learnt so far an be used without much change in
a beamer presentation within the `frame` environment. There are however a few
particularities:

To make a title, you need to use the `\titlepage` instead of the `\maketitle` command:

```language-latex
\frame{
	\titlepage
}
```

We can also have frame titles and sections as before in a Beamer document:

```language-latex
\frame{\frametitle{Overview}
	\tableofcontents
}

\section{Simple Beamer}
\frame{\frametitle{My first slide}}
```

There are various other commands and tools that can be used in Beamer. In
particular take a look at the `pause`, `only` and `onslide` commands.

A full document showing this is:

```language-latex
{% include main.tex %}
```
