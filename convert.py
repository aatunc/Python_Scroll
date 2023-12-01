from PyQt5 import uic

with open("versand.py", "w", encoding="utf-8") as fout:
    uic.compileUi("versand.ui",fout)