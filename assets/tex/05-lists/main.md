### Lists

There are various ways to obtain lists:

```language-latex
\begin{itemize}
	\item Unordered item number 1
	\item Unordered item number 2
\end{itemize}
```

```language-latex
\begin{enumerate}
	\item Ordered item number 1
	\item Ordered item number 2
\end{enumerate}
```

A full document with both these lists is:

```language-latex
{% include main.tex %}
```

Note that in LaTeX indentation is not required it is just good practice. Unlike
Python where specific environments are delimited by indentation levels, in
LaTeX they are ended by specific end statements `\end{enumerate}`.
