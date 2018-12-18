# -*- coding: utf-8 -*-
"""
# Заголовок
Markdown текст: *курсив* **жирний** `програмний код` [Посилання](https://jupyter.org)
![рисунок](https://jupyter.org/assets/nav_logo.svg)

    >>> a=2 # програмний код
    >>> a**2
    
LaTeX формула: $a^{i\pi}_{k} + 1 = \frac{\sqrt{x+1}}{\sin x}$

|A |B |C |
|--|--|--|
|1 |2 |3 |

"""
# розкоментуйте наступний рядок для інтерактивності
#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import *
x = np.linspace(1, 9); line, = plt.plot(x, np.sin(x)/x)
def update(A=(0,2,0.1), B="1.0", C=[0,1,2], D=False):
    line.set_ydata((-1 if D else 1)*A*np.sin(float(B)*x+C)/x)
    plt.show()
interact(update);
##
print "неформатований текст"
from IPython.display import display, HTML, Markdown, SVG
# візуалізація коду мовами HTML, Markdown, SVG
display(HTML(u"HTML <b>жирний</b> текст"))
display(Markdown(u"Markdown **жирний** текст"))
display(SVG("""<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40">
<circle r="10" cx="50%" cy="50%" fill="green"/></svg>"""))
