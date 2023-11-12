import pyray as pr
from raylib import colors
from sceneChoise import SceneChoise
from sceneTeacher1 import SceneTeacher1
from sceneStopRecording import SceneStopRecording
from sceneEnd import SceneEnd
class Application:
    pr.set_target_fps(60)

    def __init__(self):
        pr.init_window(1201, 701, "UGC lectures")
        pr.set_target_fps(60)
        self.scenes = {
            'choise' : SceneChoise(),
            'teacher1' : SceneTeacher1(),
            'stopRecording' : SceneStopRecording(),
            'end' : SceneEnd()
        }
        self.current_scene = 'choise'

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            self.scenes[self.current_scene].draw()
            self.scenes[self.current_scene].process()
            self.current_scene = self.scenes[self.current_scene].scene()
            pr.end_drawing()
        pr.close_window()


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
