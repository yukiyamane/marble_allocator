from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from direct.showbase.ShowBase import ShowBase
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.path_manager import PathManager
from marble_allocator.graphics.material import ColorStorage, MaterialStorage

@dataclass(frozen=True)
class ResourceContext:
    base: ShowBase
    
    primitive_model: PrimitiveModel = field(init=False)
    font: YamaneFont = field(init=False)
    color_storage: ColorStorage = field(init=False)
    material_storage: MaterialStorage = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "primitive_model", PrimitiveModel(self.base))
        object.__setattr__(self, "font", YamaneFont(self.base))
        object.__setattr__(self, "color_storage", ColorStorage()) 
        object.__setattr__(self, "material_storage", MaterialStorage())






class PrimitiveModel:
    def __init__(self, base: ShowBase):
        self.__tetrahedron = base.loader.loadModel(PathManager.resource_vfs("solids/tetrahedron.egg"))
        self.__octahedron = base.loader.loadModel(PathManager.resource_vfs("solids/octahedron.egg"))
        self.__dodecahedron = base.loader.loadModel(PathManager.resource_vfs("solids/dodecahedron.egg"))
        self.__icosahedron = base.loader.loadModel(PathManager.resource_vfs("solids/icosahedron.egg"))
        self.__cube_2m = base.loader.loadModel(PathManager.resource_vfs("solids/cube_2m.egg"))
        self.__cube_2m_for_emi = base.loader.loadModel(PathManager.resource_vfs("solids/cube_2m_for_emi.egg"))
        self.__cube_2m_origin = base.loader.loadModel(PathManager.resource_vfs("solids/cube_2m_origin_offset.egg"))
        self.__plane_2m = base.loader.loadModel(PathManager.resource_vfs("solids/plane_2m.egg"))
        self.__sphere_2m = base.loader.loadModel(PathManager.resource_vfs("solids/sphere_2m.egg"))
        self.__ico_sphere_2m = base.loader.loadModel(PathManager.resource_vfs("solids/ico_sphere_2m.glb"))
        self.__cylinder_2m = base.loader.loadModel(PathManager.resource_vfs("solids/cylinder_2m.bam"))

    @property
    def tetrahedron(self):
        return self.__tetrahedron
    @property
    def octahedron(self):
        return self.__octahedron
    @property
    def dodecahedron(self):
        return self.__dodecahedron
    @property
    def icosahedron(self):
        return self.__icosahedron
    @property
    def cube_2m(self):
        return self.__cube_2m
    @property
    def cube_2m_for_emi(self):
        return self.__cube_2m_for_emi
    @property
    def cube_2m_origin(self):
        return self.__cube_2m_origin
    @property
    def plane_2m(self):
        return self.__plane_2m
    @property
    def sphere_2m(self):
        return self.__sphere_2m
    @property
    def ico_sphere_2m(self):
        return self.__ico_sphere_2m
    @property
    def cylinder_2m(self):
        return self.__cylinder_2m



class YamaneFont():
    def __init__(self, base: ShowBase) -> None:
        self.__noto_mono = base.loader.loadFont(PathManager.resource_vfs("fonts/noto/NotoSansMonoCJKjp-Bold.otf"))
        self.__noto_mono.setPixelsPerUnit(120)
        self.__noto_mono.setPageSize(1024, 1024)
        self.__mplus_bold = base.loader.loadFont(PathManager.resource_vfs("fonts/mplus/MPLUSRounded1c-Bold.ttf"))
        self.__mplus_bold.setPixelsPerUnit(120)
        self.__mplus_bold.setPageSize(1024, 1024)
        self.__mplus_regular = base.loader.loadFont(PathManager.resource_vfs("fonts/mplus/MPLUSRounded1c-Regular.ttf"))
        self.__mplus_regular.setPixelsPerUnit(120)
        self.__mplus_regular.setPageSize(1024, 1024)
        self.__yujisyuku_regular = base.loader.loadFont(PathManager.resource_vfs("fonts/yujisyuku/YujiSyuku-Regular.ttf"))
        self.__yujisyuku_regular.setPixelsPerUnit(240)
        self.__yujisyuku_regular.setPageSize(2048, 2048)

    @property
    def noto_mono(self):
        return self.__noto_mono
    @property
    def mplus_bold(self):
        return self.__mplus_bold
    @property
    def mplus_regular(self):
        return self.__mplus_regular
    @property
    def yujisyuku_regular(self):
        return self.__yujisyuku_regular
