@echo off

.\build_html.bat

echo ...

echo Build CSS
cd css
py build_css.py
cd ..

echo ...

REM echo Minify HTML
REM py minify_html.py