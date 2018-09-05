### Tables

The following code creates a simple table (note the `c`, `r`, and `l` tags that
indicate text alignment, experiment by changing these):

```language-latex
\begin{tabular}{|l|c|r|}
	\hline
	Name & Gender & Start Time\\
	\hline
	Angelico & Male & 1100\\
	\hline
	Leanne & Female & 0830\\
	\hline
	Lisa & Female & 0730\\
	\hline
\end{tabular}
```

A full document with this table is:

```language-latex
{% include main.tex %}
```

In general in LaTeX `\\` is used to denote a 'new line'.
