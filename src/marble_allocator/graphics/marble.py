from __future__ import annotations
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.graphics.setting import marble_graphics_setting_list
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from marble_allocator.main import MyApp




class MarbleGraphics:
    def __init__(self, base: MyApp, physics_node_path: NodePath, index: int):
        self.__base = base
        self.__physics_node_path = physics_node_path
        self.__node_path: NodePath = self.__base.resource_context.primitive_model.sphere_2m.copyTo(self.__physics_node_path)
        self.__node_path.setScale(4.9)

        graphics_setting = marble_graphics_setting_list[index]
        self.__node_path.setMaterial(graphics_setting.material)


        