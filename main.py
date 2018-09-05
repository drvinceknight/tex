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

def render_template(template_file, template_vars, output_path, ROOT=ROOT):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./src/templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    if "root" not in template_vars:
        template_vars["root"] = ROOT
    output_path.write_text(template.render(template_vars))

def obtain_html(path, ROOT=ROOT):
    """
    Convert a markdown file to html
    """
    md = path.read_text()
    md = md.replace("{{root}}", "/" + ROOT)

    pattern = re.compile(r'\{% include (.*?).%\}')
    for match in re.finditer(pattern, md):
        tex_path = pathlib.Path(match.group(1))
        tex_source = tex_path.read_text()
        md = md.replace(match.group(0), tex_source)

    return markdown.markdown(md, extensions=['markdown.extensions.fenced_code'])

def make_index(src, out):
    """
    Write the `index.html` file in root of `out`
    """
    content = obtain_html(path=src / "index.md")
    render_template(template_file="home.html",
                    template_vars={"content": content},
                    output_path=out / "index.html")


if __name__ == "__main__":
    src = pathlib.Path("./src")
    out = pathlib.Path(".")

    make_index(src=src, out=out)
