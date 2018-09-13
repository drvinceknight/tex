### Sections

(Keywords: sections, subsections, label.)
[Video demo](https://www.youtube.com/watch?v=5dGhMXgH1X8)

It is possible to organise parts of a document using 'sections':

```language-latex
\section{My first section}

This is a section with a few subsections.

	\subsection{A part of my first section}

	Here I could write about the problem I'm trying to solve.

	\subsection{Another part of my first section}

	In this subsection I could solve the problem.

		\subsubsection{Further fragmentation...}

\section{My second section}

etc...
```

We can include labels to sections so that we can refer to them:

```language-latex
\section{My first section}\label{first_section}

\section{My second section}\label{second_section}

In Section \ref{first_section} we saw that...
```

When compiling one needs to compile twice:

1. The first time to find all the labels;
2. The second time to match the labels to the references.

If you are using a web service (like overleaf) then this usually happens
automatically.

Note, labels can be using in conjunction with `tabular` (for tables) and
`figure` (for images) environments, these are called  "floats" and are a very
useful feature of LaTeX but are not covered here.

A full document with sections is:

```language-latex
{% include main.tex %}
```
