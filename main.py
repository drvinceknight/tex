"""
Script to build the website.

There is a single page written in a markdown template that reads in the LaTeX
source code from tex dir
"""
import collections
import pathlib
import re

import jinja2
import markdown

ROOT = "tex"
Chapter = collections.namedtuple("chapter", ["content", 
                                             "title", 
                                             "stem", 
                                             "source"])

def render_template(template_file, template_vars, output_path, ROOT=ROOT):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    if "root" not in template_vars:
        template_vars["root"] = ROOT
    output_path.write_text(template.render(template_vars))

def obtain_html_and_title(path, ROOT=ROOT):
    """
    Convert a given directory with a `main.md` file in it and potentially a
    `main.tex` file in it to html.
    """
    stem=path.stem
    markdown_path = path / pathlib.Path("main.md")
    md = markdown_path.read_text()
    md = md.replace("{{root}}", "/" + ROOT)

    pattern = re.compile(r'\{% include (.*?).%\}')
    for match in re.finditer(pattern, md):
        tex_path = path / pathlib.Path(match.group(1))
        tex_source = tex_path.read_text()
        md = md.replace(match.group(0), tex_source)

    html = markdown.markdown(md, extensions=['markdown.extensions.fenced_code'])
    title = html[html.index("<h3>") + 4: html.index("</h3>")]
    html = html.replace("<h3>", f"<h3 id={path.stem}>")

    return html, title

def make_index(src, out):
    """
    Write the `index.html` file in root of `out`
    """
    chapters = []
    for chapter_path in sorted(src.glob("*")):
        content, title = obtain_html_and_title(chapter_path)
        stem = chapter_path.stem
        source = (chapter_path / "main.tex").is_file()
        chapters.append(Chapter(content, title, stem, source))
    render_template(template_file="home.html",
                    template_vars={"chapters": chapters},
                    output_path=out / "index.html")


if __name__ == "__main__":
    src = pathlib.Path("./assets/tex/")
    out = pathlib.Path(".")

    make_index(src=src, out=out)
