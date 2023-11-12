import pyray as pr
from raylib import colors
from textures import TexturesBG2
from button import Button
import os
import main_1

class SceneTeacher1:
    def __init__(self):
        self.scen = 'teacher1'
        self.bg = TexturesBG2()
        self.textName = "Letion name"
        self.textClass = "Class"
        self.textDescription = "Short description"
        self.textForward = "Go forward"
        self.NameButton = Button(600,300,300,50,self.textName, colors.RED, colors.WHITE, 40)
        self.ClassButton = Button(600, 200, 200, 50, self.textClass, colors.RED, colors.WHITE, 40)
        self.DescriptionButton = Button(600, 400, 450, 50, self.textDescription, colors.RED, colors.WHITE, 40)
        self.ForwardButton = Button (600, 500, 300, 50, self.textForward, colors.RED, colors.WHITE, 40)

    def draw(self):
        self.bg.draw()
        self.NameButton.draw()
        self.DescriptionButton.draw()
        self.ClassButton.draw()
        self.ForwardButton.draw()
        pr.draw_text("Configure your lection", 650 - 550 // 2, 100 - 50 // 2, 40, colors.WHITE)

    def process(self):
        if  self.NameButton.is_clicked():
            os.system('start inputName.py')
        if self.ForwardButton.is_clicked():
            self.scen = 'stopRecording'
            main_1.main()
    def scene(self):
        return self.scen