### Floats and captions

(Keywords: floats, moving figures, moving tables.)

When including images, pictures and tables it is beneficial to make them
standalone objects that can be referred to throughout the text. This is done in
\\(\LaTeX\\) using the concepts of "floats".

Pictures and diagrams are figures:

```language-latex
Figure~\ref{my_picture} shows a picture.

\begin{figure}
    \begin{center}
        \includegraphics{path_to_picture}
    \end{center}
    \caption{A picture}
    \label{my_picture}
\end{figure}
```

Tables are (surprisingly) tables:

```language-latex
Table~\ref{my_table} shows a table.


\begin{table}
    \begin{center}
        \begin{tabular}{l|c|r|}
            \toprule
            Name        & Gender & Start Time\\
            \midule
            Angelico    & Male   & 1100\\
            Leanne      & Female & 0830\\
            Lisa        & Female & 0730\\
            \bottomrule
        \end{tabular}
    \end{center}
    \caption{A table}
    \label{my_table}
\end{table}
```

Note that these are called "floats" because they are designed to move in the
document to ensure the best use of space. As a result of this it is good
practice to not refer to floats by relative position. For example do not use:
"in the picture below" but "in Figure~\ref{my_picture}".

\\(LaTeX\\) will aim to place floats in an efficient manner however some of the
rules it follows can be broken by passing the following options:

- `h`: try to place the float where it is indicated by the code.
- `t`: the float can be allowed in the top of the page.
- `b`: the float can be allowed in the bottom of the page.
- `p`: the float can be allowed on a page or column by itself.
- `!`: some further restrictions should be ignored.

A full document with a figure and a table, using all those options is:

```language-latex
{% include main.tex %}
```
