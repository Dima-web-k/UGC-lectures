import pyray as pr
from raylib import colors
from textures import TexturesBG3
from button import Button

class SceneStopRecording:
    def __init__(self):
        self.bg = TexturesBG3()
        self.scen = 'stopRecording'
        self.stopButton = Button(600, 350, 550, 50, "Stop and save recording", colors.RED, colors.WHITE, 40)

    def draw(self):
        pr.clear_background(colors.BLACK)
        self.bg.draw()
        self.stopButton.draw()




    def process(self):
       if self.stopButton.is_clicked():
           self.scen = 'end'

    def scene(self):
        return self.scen
