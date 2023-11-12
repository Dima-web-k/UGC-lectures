import pyray as pr
from raylib import colors
from textures import TexturesBG1
from button import Button

class SceneChoise:
    def __init__(self):
        self.bg = TexturesBG1()
        self.scen = 'choise'
        self.buttonST = Button(600, 600, 200, 50, "student", color_bg=colors.RED, color_text=colors.WHITE, font_size=40)
        self.buttonT = Button(600, 500, 200, 50, "Teacher", colors.RED, colors.WHITE, 40)
    def draw(self):
        pr.clear_background(colors.BLACK)
        self.bg.draw()
        self.buttonST.draw()
        self.buttonT.draw()



    def process(self):
       if self.buttonT.is_clicked():
          self.scen = 'teacher1'

    def scene(self):
        return self.scen
