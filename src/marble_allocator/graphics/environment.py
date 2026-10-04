from __future__ import annotations
from marble_allocator.shared.util.yamane_prepare import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp

class Environment():
    def __init__(self, base: MyApp):
        self.__base = base
        self.__create_sun_light()
        self.__create_ambient_light()

    def __create_sun_light(self):
        self.__sun_light = DirectionalLight("dlight")
        self.__sun_light.setColor((3, 3, 3, 1))

        self.__sun_lamp = self.__base.render.attachNewNode(self.__sun_light)
        self.__base.render.setLight(self.__sun_lamp)
        #self.__sun_lamp.reparentTo(self.__base.camera)
        self.__sun_lamp.setPos(-100, -100, 200)
        self.__sun_lamp.lookAt(0, 0, 0)
        #self.sun_lamp.setHpr(-120, -30, 0)
        self.__sun_lamp.node().getLens().setFilmSize(500, 500)
        self.__sun_lamp.node().getLens().setNearFar(1, 500)
        self.__sun_lamp.node().showFrustum()
        self.__sun_light.setShadowCaster(True, 1024, 1024)
        #self.__sun_light.setDepthOffset(0.001)
        #self.__base.render.setDepthOffset(-1)
        print("environment")

    def __create_ambient_light(self):
        self.__ambient_light = AmbientLight("my_ambient")
        self.__ambient_light.setColor((0.5, 0.5, 0.5, 1))
        self.__ambient_lamp = self.__base.render.attachNewNode(self.__ambient_light)
        self.__base.render.setLight(self.__ambient_lamp)
