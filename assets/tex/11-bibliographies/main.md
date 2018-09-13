### Bibliographies

(Keywords: bibtex, bibliography, cite.)
[Video demo](https://www.youtube.com/watch?v=JwXQb25cpqA)

To create a bibliography we need to store the bibliographic information in a
separate 'bibtex' file. In this file you include bibliographic information for
the various references you might have.

The following is the code for a book on LaTeX. Save the following in a
separate file: `bibliography.bib`:

```language-latex
{% include bibliography.bib %}
```

We can then reference the 'key' (for the above it is Gratzer2007) for any
document in the bibliography file using the following:

A very helpful reference for LaTeX is \cite{Gratzer2007}.

Note that there are a variety of tools that will give you bibtex code for
any given reference (Google Scholar, JabRef, Zotero, Mendeley etc...).

We need to however include a pointer towards the bibliography, at the end
of the document include:

```language-latex
\bibliographystyle{plain}
\bibliography{bibliography.bib}
```

We now need to compile a document twice (as above to find all internal
references for sections, figure etc...) **and then** we compile the
bibliography with `bibtex` and then we need to compile one last time to match
the bibliography items with the citations.

<img class="u-small-width" src="{{root}}/assets/img/compilation-with-bibtex-diagram.png">

If you are using overleaf then this happens automatically.

A full document with sections is:

```language-latex
{% include main.tex %}
```
