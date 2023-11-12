import eel
import sys
import webbrowser
import os, random

pat = None

eel.init("web_student")

@eel.expose
def main(i):
    global pat 
    pat = os.getcwd() + '\\classes\\' + i
    webbrowser.open(pat)
    print(pat)

eel.start("index.html",port=3000, size=(960,540))