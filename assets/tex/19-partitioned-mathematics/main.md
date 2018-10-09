### Partitioned statements

(Keywords: partitioned, mathematics.)
[Video demo](https://youtu.be/QKae6y-Hlwc)

It is possible to create partitioned statements for case dependent expressions:

```language-latex
\[
    1 + (-1) ^ n =
        \begin{cases}
            0, & \text{if \(n\) odd}\\
            2, & \text{if \(n\) even}
        \end{cases}
\]
```

Note that this requires the `amsmath` package.

A full document showing this is:

```language-latex
{% include main.tex %}
```
