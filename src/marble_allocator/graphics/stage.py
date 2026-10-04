from __future__ import annotations
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.graphics.environment import Environment
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp

class ElectricCountryGraphics:
    def __init__(self, base: MyApp, model: NodePath):
        self.__base = base
        self.__ground = self.__base.resource_context.primitive_model.plane_2m.copyTo(self.__base.render)
        self.__ground.setScale(500)
        self.__ground.setMaterial(self.__base.resource_context.material_storage.gray_diff)

        mat = self.__base.resource_context.material_storage.black_diff

        model.setTwoSided(False, 1)
        self.__node_path = model.reparentTo(self.__base.render)

        self.__environment = Environment(base)


class IceCountryGraphics:
    def __init__(self, base: MyApp, model: NodePath):
        self.__base = base
        self.__ground = self.__base.resource_context.primitive_model.plane_2m.copyTo(self.__base.render)
        self.__ground.setScale(500)
        self.__ground.setMaterial(self.__base.resource_context.material_storage.gray_diff)

        mat = self.__base.resource_context.material_storage.black_diff

        model.setTwoSided(False, 1)
        self.__node_path = model.reparentTo(self.__base.render)

        self.__environment = Environment(base)


class SandCountryGraphics:
    def __init__(self, base: MyApp, model: NodePath):
        self.__base = base
        self.__ground = self.__base.resource_context.primitive_model.plane_2m.copyTo(self.__base.render)
        self.__ground.setScale(500)
        self.__ground.setMaterial(self.__base.resource_context.material_storage.gray_diff)

        mat = self.__base.resource_context.material_storage.black_diff

        model.setTwoSided(False, 1)
        self.__node_path = model.reparentTo(self.__base.render)

        self.__environment = Environment(base)


class ElectricCountryTournamentGraphics:
    def __init__(self, base: MyApp, model: NodePath):
        self.__base = base
        self.__ground = self.__base.resource_context.primitive_model.plane_2m.copyTo(self.__base.render)
        self.__ground.setScale(500)
        self.__ground.setMaterial(self.__base.resource_context.material_storage.gray_diff)

        mat = self.__base.resource_context.material_storage.black_diff

        model.setTwoSided(False, 1)
        self.__node_path = model.reparentTo(self.__base.render)

        self.__environment = Environment(base)



class HoleGraphics:
    def __init__(self, base: MyApp, index: int, pos: Point3):
        self.__base = base

        self.__text = TextNode("hole")
        self.__text.setText(str(index + 1))
        self.__text.setTextColor(0, 0, 0, 1)
        self.__text.setFont(self.__base.resource_context.font.noto_mono)
        self.__text.setAlign(TextNode.ACenter)
        self.__node_path = self.__base.render.attachNewNode(self.__text)
        self.__node_path.setScale(10)
        self.__node_path.setPos(pos + Point3(0, 0, 3) + Point3(0, -3, 0))
        self.__node_path.setHpr(0, -90, 0)



class FixedCylinderGraphics:
    def __init__(self, base: MyApp, radius: float, height: float):
        self.__base = base
        self.__node_path: NodePath = self.__base.resource_context.primitive_model.cylinder_2m.copyTo(self.__base.render)
        self.__node_path.setScale(radius, radius, height)
        self.__node_path.setMaterial(self.__base.resource_context.material_storage.black_diff)

    def set_pos(self, pos: Point3):
        self.__node_path.setPos(pos)

    def set_hpr(self, hpr: VBase3):
        self.__node_path.setHpr(hpr)

class FixedBoxGraphics:
    def __init__(self, base: MyApp, radius: VBase3):
        self.__base = base
        self.__node_path: NodePath = self.__base.resource_context.primitive_model.cube_2m.copyTo(self.__base.render)
        self.__node_path.setScale(radius)
        self.__node_path.setMaterial(self.__base.resource_context.material_storage.black_diff)

    def set_pos(self, pos: Point3):
        self.__node_path.setPos(pos)

    def set_hpr(self, hpr: VBase3):
        self.__node_path.setHpr(hpr)