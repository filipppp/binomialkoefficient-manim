from manimlib.imports import *
class ZoomInAndOut(Transform):
    CONFIG = {
        "rate_func": there_and_back,
        "scale_factor": 1.5,
        "color": YELLOW,
    }

    def create_target(self):
        target = self.mobject.copy()
        target.scale_in_place(self.scale_factor)
        return target


class MarkingMobject(TexMobject):
    CONFIG = {
        "tex_to_color_map": {
            "n": BLUE,
            "k": GREEN
        }
    }
    def apply_color_map(self):
        color_map = self.CONFIG["_color_map"]
        for character in color_map.keys():
            color = color_map[character]
            for i in range(len(self)):
                for char_idx in range(len(self[i])):
                    print(len(self[i]))
                    if self[i][char_idx].get_char() == character:
                        self[i][char_idx].set_color(color)

