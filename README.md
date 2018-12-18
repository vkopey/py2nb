# py2nb
Simple generator of Jupyter Notebook documents from marked up Python code

Python program for generating interactive Jupyter Notebook documents (.ipynb v4) from the simple marked Python code. The program has the ability to further convert .ipynb to HTML and docx formats. The program can be used to facilitate the creation and editing of documents based on Jupyter Notebook. In comparison with analogues, the program has a simple and clear algorithm based on regular expressions, which allows its simple modification for other tasks. An additional advantage is the simple way of marking Python code on cells, which consists in placing Markdown text blocks in multiline Python literals in quotes `"""..."""` and separating code blocks with `##`.

Requirements:

Python 2.7, Jupyter Notebook 5.0.0, pandoc 2.2.1 (for converting to .docx)

Install:

Copy files to one folder. Edit file paths in convertExec.bat and convertNoExec.bat. For converting to .docx put `reference.docx` to `c:\Users\<username>\AppData\Roaming\Pandoc`. 

Usage (see Examples):

`convertExec simple.py`

Or without Notebook execution:

`convertNoExec simple.py`
