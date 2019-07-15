from os import listdir, system

paths = listdir(".")

minify = "html-minifier --collapse-whitespace --remove-comments --remove-optional-tags --remove-redundant-attributes --remove-script-type-attributes --remove-tag-whitespace --use-short-doctype --minify-css true --minify-js true"

for path in paths:
    if path.endswith(".html"):
        print(f"Minify {path}")
        system(f"{minify} {path} -o {path}")