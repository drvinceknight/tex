### Using columns

(Keywords: columns, side by side,)

It is possible to use columns in \\(\LaTeX\\).

This can be done using the `usepackage{multicol}` package.

```language-latex
\begin{multicols}{3}

    Here is some text in the first column.

    \columnbreak

    Here is an equation in the second column:

    \[
        x ^ 2
    \]

    \columnbreak

    Here is some text in the third column.

\end{multicols}
```

A full document showing this is:

```language-latex
{% include main.tex %}
```
