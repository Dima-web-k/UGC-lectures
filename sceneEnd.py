import pyray as pr
from raylib import colors
from textures import TexturesBG1
from button import Button

class SceneEnd:
    def __init__(self):
        self.bg = TexturesBG1()
        self.scen = 'end'
    def draw(self):
        pr.clear_background(colors.BLACK)
        self.bg.draw()
        pr.draw_text("Successfully saved", 650 - 550 // 2, 350 - 50 // 2, 40, colors.BLACK)



    def process(self):
        pass

    def scene(self):
        return self.scen
