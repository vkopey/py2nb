setlocal
set fn=%~n1
echo %fn%
e:\Anaconda2\python.exe py2nb.py %fn%.py
e:\Anaconda2\Scripts\jupyter-nbconvert --inplace %fn%.ipynb
e:\Anaconda2\Scripts\jupyter-nbconvert --to markdown %fn%.ipynb
e:\Anaconda2\python.exe mdPython.py %fn%.md
e:\Portable\pandoc-2.2.1\pandoc.exe %fn%.md --from markdown+tex_math_dollars -s -o %fn%.docx
REM e:\Portable\pandoc-2.2.1\pandoc.exe %fn%.md --from markdown --to html5 --mathjax -s -o %fn%.html
e:\Portable\pandoc-2.2.1\pandoc.exe %fn%.md --from markdown --to html5 --mathml -s -o %fn%.html