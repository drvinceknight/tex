### Including code

(Keywords: code, listing.)

It is possible to include code in \\(\LaTeX\\).

One approach is to use the `listings` library. To use this requires
`\usepackage{listings}` in the preamble:


```language-latex
\begin{lstlisting}
def fibonacci(n):
    if n in [0, 1]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(5):
    print(n, fibonacci(n))
\end{lstlisting}
```

Another approach is to use the `minted` library. To use this requires
`\usepackage{minted}` in the preamble:


```language-latex
\begin{minted}{python}
def fibonacci(n):
    if n in [0, 1]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(5):
    print(n, fibonacci(n))
\end{minted}
```


A full document showing these is:

```language-latex
{% include main.tex %}
```
