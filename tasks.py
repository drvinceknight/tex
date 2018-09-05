import pathlib

from invoke import task

@task
def build_pdf(c):
    assets = pathlib.Path("./assets")
    for p in assets.glob("./tex/**/main.tex"):
        print(f"Compiling {p}")
        c.run(f"cd {p.parents[0]}; latexmk -pdf main.tex")

@task
def main(c):
    build_pdf(c)
    c.run("python main.py")
