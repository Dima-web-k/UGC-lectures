import eel
import sys
import webbrowser
import os, random
from student import pat

eel.init("web_student")

print(pat)
print(random.choice(os.listdir(pat)))
eel.name(pat + '\\' + os.listdir(pat)[0], os.listdir(pat)[0])

eel.start("play.html", size=(960,540))