from __future__ import annotations
from marble_allocator.core.allocator import Allocator
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp


class CoreSystem:
    def __init__(self, base: MyApp):
        self.__allocator = Allocator(base)

    def update(self, frame_time: float, dt: float):
        self.__allocator.update(frame_time, dt)

    
