### Special characters

(Keywords: quotes, characters, comments.)

The following keys are used to type text in a source file:

```language-latex
a-z A-Z 0-9
+ = * / ( ) [ ]
```

The following punctuation marks:

```language-latex
' ? ! : ` ' -
```

Finally there are 13 special keys that are used in commands:

```language-latex
# $ % & ~ _ ^ \ { } @ " |
```

For example, `%` sign is used to denote comments in LaTeX (like `#` in Python).

```language-latex
\begin{document} % This line start the document
```

Note also that to include text in quotes a different character for the opening
and closing quote needs to be used:

```language-latex
Here is how to use `single quotes' and here is how to use double ``quotes''.
```

A document showing these two things together is:

```language-latex
{% include main.tex %}
```
