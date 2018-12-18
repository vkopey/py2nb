# -*- coding: utf-8 -*-
'''
Конвертує Python в Ipython Notebook
Markdown-комірки беруться в \n"""\n
а комірки коду можуть бути розбиті на частини за допомогою \n##\n
Автор: Копей В. Б.
'''

import nbformat, codecs, sys
from nbformat.v4 import new_markdown_cell, new_code_cell, new_notebook
import re

def convert(source):
    with open(source,'r') as f: text=f.read()
    
    pattern1=re.compile(r'(?s)(\n"""\n.*?\n"""\n)')
    pattern2=re.compile(r'\n##\n')  
     
    cells1=re.split(pattern1, text) # перший етап - markdown cell, code cell 
    cells=[] # notebook cells
    for c1 in cells1[1:]: # крім першого рядка
        if re.match(pattern1, c1): # markdown cell
            cells.append(new_markdown_cell(c1[5:-5]))
        else: # code cells
            cells2=re.split(pattern2, c1)
            if cells2[0].startswith('##\n'): cells2[0]=cells2[0][3:] 
            for c2 in cells2: # другий етап - code cell 
                cells.append(new_code_cell(c2))
    
    #print cells
    nb = new_notebook(cells=cells, metadata={'language': 'python',})
    dest=source[:-3]+".ipynb"
    with codecs.open(dest, encoding='utf-8', mode='w') as f:
        nbformat.write(nb, f, 4)


if __name__=='__main__':
    convert(sys.argv[1])