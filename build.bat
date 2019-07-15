@echo off

echo Build HTML
cd pygen
py generate.py
cd ..

echo ...

echo Build CSS
cd css
py build_css.py
cd ..

echo ...

echo Minify HTML
py minify_html.py