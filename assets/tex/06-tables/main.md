### Tables

(Keywords: tables, tabular, booktabs.)
[Video demo](https://www.youtube.com/watch?v=bSIAUkCD948)

The following code creates a simple table (note the `c`, `r`, and `l` tags that
indicate text alignment, experiment by changing these):

```language-latex
\begin{tabular}{|l|c|r|}
	\hline
	Name     & Gender & Start Time\\
	\hline
	Angelico & Male   & 1100\\
	\hline
	Leanne   & Female & 0830\\
	\hline
	Lisa     & Female & 0730\\
	\hline
\end{tabular}
```

The above makes use of the basic tables available in \\(\LaTeX\\). The
`booktabs` packages allows for improved aesthetics. To use this requires
`\usepackage{booktabs}` in the preamble:

```language-latex
\begin{tabular}{l|c|r|}
	\toprule
	Name        & Gender & Start Time\\
	\midrule
	Angelico    & Male   & 1100\\
	Leanne      & Female & 0830\\
	Lisa        & Female & 0730\\
	\bottomrule
\end{tabular}
```

A full document with this table is:

```language-latex
{% include main.tex %}
```

In general in LaTeX `\\` is used to denote a 'new line'.
