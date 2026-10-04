from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.graphics.material import ColorStorage, MaterialStorage, ColorData



@dataclass(frozen=True)
class MarbleGraphicsSetting:
    name: str
    material: Material
    color_light: ColorData
    color_mid: ColorData
    color_dark: ColorData

marble_graphics_setting_list = [
    MarbleGraphicsSetting("Orange", MaterialStorage.ink_orange_diff, ColorStorage.ink_orange_light, ColorStorage.ink_orange, ColorStorage.ink_orange_dark),
    MarbleGraphicsSetting("Blue", MaterialStorage.ink_blue_diff, ColorStorage.ink_blue_light, ColorStorage.ink_blue, ColorStorage.ink_blue_dark),
    MarbleGraphicsSetting("Pink", MaterialStorage.ink_pink_diff, ColorStorage.ink_pink_light, ColorStorage.ink_pink, ColorStorage.ink_pink_dark),
    MarbleGraphicsSetting("Green", MaterialStorage.ink_green_diff, ColorStorage.ink_green_light, ColorStorage.ink_green, ColorStorage.ink_green_dark),
]    

