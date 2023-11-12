import pyray as pr
from raylib import colors


class Button:
    def __init__(self, x_center, y_center, width, height, text, color_bg, color_text, font_size=30):
        self.x = x_center
        self.y = y_center
        self.w = width
        self.h = height
        self.t = text
        self.c1 = color_bg
        self.c2 = color_text
        self.f = font_size

    def draw(self):
        pr.draw_rectangle_rounded(
            pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h),
            0.4, 100, self.c1
        )
        pr.draw_text(self.t, self.x - pr.measure_text(self.t, self.f) // 2, self.y - self.f // 2, self.f, self.c2)

        if self.is_hover():
            pr.draw_rectangle_rounded_lines(
                pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h),
                0.4, 100, 4, self.c2
            )
        else:
            pr.draw_rectangle_rounded_lines(
                pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h),
                0.4, 100, 4, colors.BLACK
            )

    def is_hover(self):
        if pr.check_collision_point_rec(
                pr.get_mouse_position(),
                pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)
        ):
            return True
        else:
            return False

    def is_clicked(self):
        if (pr.check_collision_point_rec(
                pr.get_mouse_position(),
                pr.Rectangle(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)
        ) and pr.is_mouse_button_pressed(0)):
            return True
        return False

