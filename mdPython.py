# -*- coding: utf-8 -*-
# конвертує документ markdown зі вставками коду в документ markdown зі вставками коду python
import re,sys
source=sys.argv[1]
with open(source,'r') as f: text=f.read()
pattern1=re.compile(r'(?s)\n```(\n.*?\n```\n)')
#text=re.sub(pattern1, r'\n***\n```python'+r'\g<1>***\n' ,text)
#text=re.sub(pattern1, r'\n<table bgcolor="azure" width="5000">\n<tr>\n<td>\n```python'+r'\g<1></td>\n</tr>\n</table>\n' ,text)
#text=re.sub(pattern1, r'\n```{.python .numberLines}'+r'\g<1>\n' ,text)
text=re.sub(pattern1, r'\n:::{custom-style="mytable"}\n```python'+r'\g<1>:::\n' ,text)
with open(source,'w') as f: f.write(text)
