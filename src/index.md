<h3 id="about-latex">About \(\LaTeX\)</h3>

A typesetting language is a language that requires the user to write code that
is then 'translated' to a form that is 'human readable'.

<img class="u-full-width" src="{{root}}/assets/img/compile_diagram.png">

A powerful typesetting language that is popular in scientific writing is
\\(\LaTeX\\) (pronounced: lay-tech).

This resource gives an overview of \\(\LaTeX\\): you can either install
\\(\LaTeX\\) on your own computer:

- [MikTeX](http://miktex.org/) on windows 
- [MacTeX](https://tug.org/mactex/) on OS X


If you do not already have an installed version I recommend
[overleaf.com](https://www.overleaf.com/) a cloud based service.

---

<h3 id="a-basic-document">A basic document</h3>

In the editor type the following:

```language-latex
{% include assets/tex/00/main.tex %}
```

The next step is to *compile* this `tex` file.  For the purposes of this
tutorial I recommend compiling with a modern compiler like `pdflatex` or
`xelatex`. **If you are using a cloud based service compilation usually happens
automatically.**

[main.tex]({{root}}/assets/tex/00/main.tex)
[main.pdf]({{root}}/assets/tex/00/main.pdf)

---

<h3 id="special-characters">Special characters</h3>

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
Modify your \\(\LaTeX\\) file so it looks like:

```language-latex
{% include assets/tex/01/main.tex %}
```

[main.tex]({{root}}/assets/tex/00/main.tex)
[main.pdf]({{root}}/assets/tex/00/main.pdf)

---

<h3 id="the-preamble">The preamble</h3>

In general all the code that comes before the `\begin{document}` statement is
called the 'preamble' and is used to set a title for the document, call certain
packages as well as various other things. The following code (to be inserted in
the preamble of your document) sets a title:

```language-latex
\title{Choose a title}
\author{V Knight}
\date{\today}
```


If you compile your document this won't include the title in the output. To do
so you need to include the following line (in the main body):

```language-latex
\maketitle
```

Here is what your document should look like:

```language-latex
{% include assets/tex/02/main.tex %}
```

[main.tex]({{root}}/assets/tex/02/main.tex)
[main.pdf]({{root}}/assets/tex/02/main.pdf)

---

<h3 id="an-abstract">An abstract</h3>

The following will add an abstract to your document:

```language-latex
\begin{abstract}
This document contains some basic LaTeX code that will be useful to me in the future.
\end{abstract}
```

Here is what your document should look like:

```language-latex
{% include assets/tex/03/main.tex %}
```

[main.tex]({{root}}/assets/tex/03/main.tex)
[main.pdf]({{root}}/assets/tex/03/main.pdf)

----

<h3 id="lists">Lists</h3>

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

Note that in LaTeX indentation is not required it is just good practice. If you
are used to a language like Python where specific environments are delimited by
indentation levels, in LaTeX they are ended by specific end statements
`\end{enumerate}`.

Here is what your document should look like:

```language-latex
{% include assets/tex/04/main.tex %}
```

[main.tex]({{root}}/assets/tex/04/main.tex)
[main.pdf]({{root}}/assets/tex/04/main.pdf)
