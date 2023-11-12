import pyray as pr
from raylib import colors

class TexturesBG1:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.img = self.img = pr.load_image('BG1.png')
        self.tx = pr.load_texture_from_image(self.img)

    def draw(self):
        pr.draw_texture(self.tx, 0, 0, colors.WHITE)

class TexturesBG2:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.img = self.img = pr.load_image('BG2.png')
        self.tx = pr.load_texture_from_image(self.img)

    def draw(self):
        pr.draw_texture(self.tx, 0, 0, colors.WHITE)

class TexturesBG3:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.img = self.img = pr.load_image('BG3.png')
        self.tx = pr.load_texture_from_image(self.img)

    def draw(self):
        pr.draw_texture(self.tx, 0, 0, colors.WHITE)