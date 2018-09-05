### Drawing pictures

Graphs, pictures and diagrams can thus be created in any software of choice
(Python, inkscape, etc...) and then included as required **but** it
is often easier to draw a picture in LaTeX itself using code. A great package
to do this with is `tikz`. Include the following in the preamble:

```language-latex
\usepackage{tikz}
```

Using this package we start a picture by setting up a tikzpicture environment.

```language-latex
\begin{tikzpicture}

\end{tikzpicture}
```

We then draw various shapes and connectors using the `\draw` command including
coordinates:

```language-latex
\begin{tikzpicture}
	\draw (0,0) -- (0,2); % This draws a line from (0,0) to (0,2)
	\draw (-1,1) -- (1,1); % This draws a line from (-1,1) to (1,1)
	\draw (0,0) -- (1,-1); % This draws a line from (0,0) to (1,-1)
	\draw (0,0) -- (-1,-1); % This draws a line from (0,0) to (-1,-1)
	\draw (0,2.5) circle(.5); % This draws a circle at (0,2.5) with radius .5
\end{tikzpicture}
```

This is very much touching the surface of what can be down with tikz. The
simplest next step is to include various color and thickness options (we can
also center the drawing):

```language-latex
\begin{center}
	\begin{tikzpicture}
		\draw [ultra thick] (0,0) -- (0,2); % This draws a line from (0,0) to (0,2)
		\draw [thin, color=blue] (-1,1) -- (1,1); % This draws a line from (-1,1) to (1,1)
		\draw [thick] (0,0) -- (1,-1); % This draws a line from (0,0) to (1,-1)
		\draw [thick] (0,0) -- (-1,-1); % This draws a line from (0,0) to (-1,-1)
		\draw [color=red, fill=green] (0,2.5) circle(.5); % This draws a circle at (0,2.5) with radius .5
	\end{tikzpicture}
\end{center}
```

A lot more can be done with tikz and there are a variety of great examples,
tutorials online.

A full document with that images is:

```language-latex
{% include main.tex %}
```
