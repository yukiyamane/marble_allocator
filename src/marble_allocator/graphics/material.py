from enum import Enum
from dataclasses import dataclass
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.graphics.util.yamane_color import ColorConverter


@dataclass(frozen=True)
class ColorData():
    name: str
    degree_hsv: tuple[int, int, int]
    float_rgb: tuple[float, float, float]
    float_rgb_linear: tuple[float, float, float]
    byte_rgb: tuple[int, int, int]
    byte_rgb_linear: tuple[int, int, int]
    hex: str

    @classmethod
    def from_degree_hsv(cls, name: str, degree_hsv: tuple[int, int, int]): #degree_hsvはリニアではない　ガンマ補正後を入力
        return cls(name, 
                   degree_hsv, 
                   ColorConverter.hsv_deg_srgb_to_rgb_srgb(degree_hsv), 
                   ColorConverter.hsv_deg_srgb_to_rgb_linear(degree_hsv),
                   ColorConverter.rgb_float_to_byte(ColorConverter.hsv_deg_srgb_to_rgb_srgb(degree_hsv)),
                   ColorConverter.rgb_float_to_byte(ColorConverter.hsv_deg_srgb_to_rgb_linear(degree_hsv)),
                   ColorConverter.rgb_float_to_hex(ColorConverter.hsv_deg_srgb_to_rgb_srgb(degree_hsv)))


@dataclass(frozen=True)
class ColorStorage():
    black = ColorData.from_degree_hsv("black", (0, 0, 0))
    white = ColorData.from_degree_hsv("white", (0, 0, 100))
    gray = ColorData.from_degree_hsv("gray", (0, 0, 50))
    vivid_red = ColorData.from_degree_hsv("vivid_red", (0, 80, 100))
    vivid_orange = ColorData.from_degree_hsv("vivid_orange", (24, 80, 100))
    vivid_yellow = ColorData.from_degree_hsv("vivid_yellow", (60, 80, 100))
    vivid_green = ColorData.from_degree_hsv("vivid_green", (120, 80, 100))
    vivid_cyan = ColorData.from_degree_hsv("vivid_cyan", (180, 80, 100))
    vivid_blue = ColorData.from_degree_hsv("vivid_blue", (236, 80, 90))
    vivid_purple = ColorData.from_degree_hsv("vivid_purple", (264, 80, 100))
    vivid_pink = ColorData.from_degree_hsv("vivid_pink", (307, 35, 100))

    pale_gray = ColorData.from_degree_hsv("pale_gray", (0, 0, 90))
    pale_red = ColorData.from_degree_hsv("pale_red", (5, 20, 100))
    pale_orange = ColorData.from_degree_hsv("pale_orange", (28, 20, 100))

    pale_green = ColorData.from_degree_hsv("pale_green", (123, 20, 100))
    pale_cyan = ColorData.from_degree_hsv("pale_cyan", (185, 20, 100))
    pale_blue = ColorData.from_degree_hsv("pale_blue", (237, 40, 70))
    pale_purple = ColorData.from_degree_hsv("pale_purple", (260, 20, 100))
    

    bright_red = ColorData.from_degree_hsv("blight_red", (0, 60, 100))
    bright_blue = ColorData.from_degree_hsv("blight_blue", (231, 60, 100))

    dark_purple = ColorData.from_degree_hsv("dark_purple", (256, 80, 40))



    ink_blue = ColorData.from_degree_hsv("ink_blue", (237, 73, 76))
    ink_blue_light = ColorData.from_degree_hsv("ink_blue_light", (237, 50, 100))
    ink_blue_dark = ColorData.from_degree_hsv("ink_blue_dark", (237, 60, 50))
    
    ink_orange = ColorData.from_degree_hsv("ink_orange", (21, 78, 94))
    ink_orange_light = ColorData.from_degree_hsv("ink_orange_light", (21, 60, 100))
    ink_orange_dark = ColorData.from_degree_hsv("ink_orange_dark", (21, 70, 50))

    ink_pink = ColorData.from_degree_hsv("ink_pink", (331, 72, 90))
    ink_pink_light = ColorData.from_degree_hsv("ink_pink_light", (331, 50, 100))
    ink_pink_dark = ColorData.from_degree_hsv("ink_pink_dark", (331, 60, 50))

    ink_green = ColorData.from_degree_hsv("ink_green", (115, 75, 84))
    ink_green_light = ColorData.from_degree_hsv("ink_green_light", (115, 50, 100))
    ink_green_dark = ColorData.from_degree_hsv("ink_green_dark", (115, 60, 50))

        


class MaterialFactory:
    @staticmethod
    def create_diffuse(degree_hsv: tuple[int, int, int], roughness: float = 1.0):
        float_rgb_linear = ColorConverter.hsv_deg_srgb_to_rgb_linear(degree_hsv)
        mat = Material()
        mat.set_base_color(Vec4(*float_rgb_linear, 1))
        mat.set_metallic(0)
        mat.set_emission(Vec4(0, 0, 0, 1))
        mat.set_roughness(roughness)
        return mat

    @staticmethod
    def create_diffuse_2(degree_hsv: tuple[int, int, int], roughness: float = 1.0):
        float_rgb_linear = ColorConverter.hsv_deg_srgb_to_rgb_linear(degree_hsv)
        mat = Material()
        mat.setDiffuse(Vec4(*float_rgb_linear, 1))
        mat.setAmbient(Vec4(*float_rgb_linear, 1))
        mat.setEmission(Vec4(0, 0, 0, 1))
        #mat.setShininess(0.2)
        return mat

    @staticmethod
    def create_metallic(degree_hsv: tuple[int, int, int], roughness: float = 0.2):
        float_rgb_linear = ColorConverter.hsv_deg_srgb_to_rgb_linear(degree_hsv)
        mat = Material()
        mat.set_base_color(Vec4(*float_rgb_linear, 1))
        mat.set_metallic(1)
        mat.set_emission(Vec4(0, 0, 0, 1))
        mat.set_roughness(roughness)
        return mat


@dataclass(frozen=True)
class MaterialStorage():
    gray_diff = MaterialFactory.create_diffuse((0, 0, 50))
    black_diff = MaterialFactory.create_diffuse((0, 0, 20))
    white_diff = MaterialFactory.create_diffuse((0, 0, 80))

    ink_blue_diff = MaterialFactory.create_diffuse(ColorStorage.ink_blue.degree_hsv)
    ink_blue_light_diff = MaterialFactory.create_diffuse(ColorStorage.ink_blue_light.degree_hsv, 0.1)
    ink_blue_dark_diff = MaterialFactory.create_diffuse(ColorStorage.ink_blue_dark.degree_hsv)
    ink_orange_diff = MaterialFactory.create_diffuse(ColorStorage.ink_orange.degree_hsv)
    ink_orange_light_diff = MaterialFactory.create_diffuse(ColorStorage.ink_orange_light.degree_hsv, 0.1)
    ink_orange_dark_diff = MaterialFactory.create_diffuse(ColorStorage.ink_orange_dark.degree_hsv)

    ink_pink_diff = MaterialFactory.create_diffuse(ColorStorage.ink_pink.degree_hsv)
    ink_pink_light_diff = MaterialFactory.create_diffuse(ColorStorage.ink_pink_light.degree_hsv, 0.1)
    ink_pink_dark_diff = MaterialFactory.create_diffuse(ColorStorage.ink_pink_dark.degree_hsv)
    
    ink_green_diff = MaterialFactory.create_diffuse(ColorStorage.ink_green.degree_hsv)
    ink_green_light_diff = MaterialFactory.create_diffuse(ColorStorage.ink_green_light.degree_hsv, 0.1)
    ink_green_dark_diff = MaterialFactory.create_diffuse(ColorStorage.ink_green_dark.degree_hsv)



class MaterialStorageOld():
    def __init__(self, base: ShowBase, color_storage: ColorStorage):

        """
        self.rainbow = Material()
        self.rainbow.setDiffuse((0, 0, 0, 1))
        self.rainbow.setAmbient((0, 0, 0, 1))
        self.r_time = 0
        self.base.taskMgr.add(self.update_rainbow, "update")
        """
    """
    def update_rainbow(self, task):
        dt = globalClock.getDt()
        velocity = 120
        self.r_time += dt * velocity 
        if 360 < self.r_time:
            self.r_time -= 360
        hue = self.r_time
        color = yamane_color.convert_hsv_to_rgb_normed((hue, 50, 100))
        self.rainbow.setEmission(color)
        return task.cont
    
    def update_fire(self, task):
        return task.cont
    
    def update_blink(self, task):
        theta = 120 * task.time
        theta %= 360
        sin = math.sin(math.radians(theta))
        v = abs(sin)
        color = yamane_color.convert_hsv_to_rgb_normed((0, 0, v * 100))
        self.black_white_emi.setEmission(color)
        return task.cont
    """
