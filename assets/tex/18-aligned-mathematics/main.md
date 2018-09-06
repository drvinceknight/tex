### Aligned mathematics

It is possible to create aligned mathematics using:

```language-latex
\begin{align}
    (x+h)^2-x^2 & =x^2+2xh+h^2-x^2 \nonumber\\
                & =2xh+h^2 \nonumber\\
                & =h(2x+h) \nonumber
\end{align}
```

Note that this requires the `amsmath` package.

Annotated text can also be added:

```language-latex
\begin{align}
    (x+h)^2-x^2 & = x^2+2xh+h^2-x^2 && \text{(by distributivity)}\\
                & = 2xh+h^2         && \text{(by subtraction)}\\
                & = h(2x+h)         && \text{(by factorisation)}
\end{align}
```

A full document showing these is:

```language-latex
{% include main.tex %}
```
