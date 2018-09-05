### Including pictures

To include a picture is straightforward in LaTeX. We make use of the `graphicx`
package. In LaTeX packages are included in the preamble using `usepackage`.
Include the following in the preamble:

```language-latex
\usepackage{graphicx}
```

The following code (somewhere in the body) will include a picture:

```language-latex
\includegraphics{path_to_picture}
```

We can put this in the `center` environment to centre the picture:

```language-latex
\begin{center}
	\includegraphics{path_to_picture}
\end{center}
```

We can also pass options to `includegraphics` to specify the width. For example,
this ensures the picture will be 60% of the width of the page:

```language-latex
\begin{center}
	\includegraphics[width=.6\textwidth]{path_to_picture}
\end{center}
```

Here is an example image:


Images can be in jpg, png and
pdf format when using a modern compiler, here is a picture as an example:
<a href="{{root}}/assets/tex/07-including-pictures/dog.jpg">dog.jpg</a>.

A full document with that images is:

```language-latex
{% include main.tex %}
```
