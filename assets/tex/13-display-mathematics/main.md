### Displayed mathematics

(Keywords: mathematics, display.)
[Video demo](https://www.youtube.com/watch?v=DzPS2OnJjIk)

To include mathematics in a "displayed" style use the following:

```language-latex
Here is an integral:

\[
    \int_{0}^{5}x ^ 2dx
\]

Here is a summation:

$$
    \sum_{i=1}^{n}i=\frac{n(n+1)}{2}
$$
```

Note that using `\[` and `\]` is preferred over `$$`. One of the reasons is that
it is easier for humans (and machines) to find the start and end of some
mathematics.

A full document making use of displayed mathematics is:

```language-latex
{% include main.tex %}
```
