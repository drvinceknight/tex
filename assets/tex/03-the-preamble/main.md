### The preamble


In general all the code that comes before the `\begin{document}` statement is
called the 'preamble' and is used to set a title for the document, call certain
packages as well as various other things. The following code (to be inserted in
the preamble of your document) sets a title:


```language-latex
\title{Choose a title}
\author{V Knight}
\date{\today}
```


If you compile your document this won't include the title in the output. To
do so you need to include the following line (in the main body):

```language-latex
\maketitle
```

Your full document will now look like:

```language-latex
{% include main.tex %}
```
