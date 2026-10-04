from __future__ import annotations
from typing import override
from abc import ABC, abstractmethod
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.path_manager import PathManager
from marble_allocator.shared.util.yamane_state_machine import StateMachine, StateContext
from marble_allocator.graphics.stage import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp
    from marble_allocator.core.allocator import Allocator
    from marble_allocator.core.marble import Marble

class Stage(ABC):
    def __init__(self, base: MyApp, allocator: Allocator, physics_world: BulletWorld) -> None:
        self.__base = base
        self.__allocator = allocator
        self.__physics_world = physics_world
        self.__first_box = FirstBox(base, physics_world)
        self.__fixed_box_1 = FixedBox(base, physics_world, VBase3(30, 2, 30), Point3(0, -32, 30), VBase3(0, 0, 0))    
        self.__fixed_box_2 = FixedBox(base, physics_world, VBase3(2, 30, 30), Point3(32, 0, 30), VBase3(0, 0, 0))  

    @property
    def allocator(self):
        return self.__allocator

    @property
    def first_box(self):
        return self.__first_box

    def _load_static_mesh(self, path: str):
        model = self.__base.loader.loadModel(PathManager.resource_vfs(path), noCache=True)
        geom_node = model.find("**/+GeomNode").node()
        mesh = BulletTriangleMesh()
        for i in range(geom_node.get_num_geoms()):
            geom = geom_node.get_geom(i)
            mesh.add_geom(geom)
        shape = BulletTriangleMeshShape(mesh, dynamic=False)
        body = BulletRigidBodyNode('MeshBody')
        body.addShape(shape)
        body.setStatic(True)
        self.__physics_world.attachRigidBody(body)
        return model

    @abstractmethod
    def update_idle(self, current_real_time: float, ):
        raise NotImplementedError

    @abstractmethod
    def release(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError




class ElectricCountry(Stage):
    def __init__(self, base: MyApp, allocator: Allocator, physics_world: BulletWorld):
        super().__init__(base, allocator, physics_world)
        model = self._load_static_mesh("models/electric_country.glb")
        self.__graphics = ElectricCountryGraphics(base, model)

        self.__hole_list = []
        hole_1 = Hole(base, 0, Point3(13, -13, 7))
        hole_2 = Hole(base, 1, Point3(25, -13, 7))
        hole_3 = Hole(base, 2, Point3(13, -25, 7))
        hole_4 = Hole(base, 3, Point3(25, -25, 7))
        self.__hole_list.append(hole_1)
        self.__hole_list.append(hole_2)
        self.__hole_list.append(hole_3)
        self.__hole_list.append(hole_4)

    @override
    def update_idle(self, current_real_time: float):
        self.first_box.update(current_real_time)

    @override
    def release(self):
        self.first_box.release()
        
    @override
    def update(self):
        marble_list = self.allocator.marble_list
        for i, hole in enumerate(reversed(self.__hole_list)):
            hole.update(marble_list)



class IceCountry(Stage):
    def __init__(self, base: MyApp, allocator: Allocator, physics_world: BulletWorld):
        super().__init__(base, allocator, physics_world)
        model = self._load_static_mesh("models/ice_country.glb")
        self.__graphics = IceCountryGraphics(base, model)

        self.__hole_list = []
        hole_1 = Hole(base, 0, Point3(13, -13, 7))
        hole_2 = Hole(base, 1, Point3(25, -13, 7))
        hole_3 = Hole(base, 2, Point3(13, -25, 7))
        hole_4 = Hole(base, 3, Point3(25, -25, 7))
        self.__hole_list.append(hole_1)
        self.__hole_list.append(hole_2)
        self.__hole_list.append(hole_3)
        self.__hole_list.append(hole_4)

    @override
    def update_idle(self, current_real_time: float):
        self.first_box.update(current_real_time)

    @override
    def release(self):
        self.first_box.release()
        
    @override
    def update(self):
        marble_list = self.allocator.marble_list
        for i, hole in enumerate(reversed(self.__hole_list)):
            hole.update(marble_list)


class SandCountry(Stage):
    def __init__(self, base: MyApp, allocator: Allocator, physics_world: BulletWorld):
        super().__init__(base, allocator, physics_world)
        model = self._load_static_mesh("models/sand_country.glb")
        self.__graphics = SandCountryGraphics(base, model)

        self.__hole_list = []
        hole_1 = Hole(base, 0, Point3(13, -13, 7))
        hole_2 = Hole(base, 1, Point3(25, -13, 7))
        hole_3 = Hole(base, 2, Point3(13, -25, 7))
        hole_4 = Hole(base, 3, Point3(25, -25, 7))
        self.__hole_list.append(hole_1)
        self.__hole_list.append(hole_2)
        self.__hole_list.append(hole_3)
        self.__hole_list.append(hole_4)

    @override
    def update_idle(self, current_real_time: float):
        self.first_box.update(current_real_time)

    @override
    def release(self):
        self.first_box.release()
        
    @override
    def update(self):
        marble_list = self.allocator.marble_list
        for i, hole in enumerate(reversed(self.__hole_list)):
            hole.update(marble_list)


class ElectricCountryTournament(Stage):
    def __init__(self, base: MyApp, allocator: Allocator, physics_world: BulletWorld):
        super().__init__(base, allocator, physics_world)
        model = self._load_static_mesh("models/electric_country_tournament.glb")
        self.__graphics = ElectricCountryTournamentGraphics(base, model)

        self.__hole_list = []
        hole_1 = Hole(base, 0, Point3(25, -25, 37))
        hole_2 = Hole(base, 1, Point3(25, -25, 27))
        hole_3 = Hole(base, 2, Point3(25, -25, 17))
        hole_4 = Hole(base, 3, Point3(25, -25, 7))
        self.__hole_list.append(hole_1)
        self.__hole_list.append(hole_2)
        self.__hole_list.append(hole_3)
        self.__hole_list.append(hole_4)

    @override
    def update_idle(self, current_real_time: float):
        self.first_box.update(current_real_time)

    @override
    def release(self):
        self.first_box.release()

    @override
    def update(self):
        marble_list = self.allocator.marble_list
        for i, hole in enumerate(reversed(self.__hole_list)): #インデックス最後の穴から順番に入らないといけなくする。
            hole.update(marble_list)
            if hole.is_inside is False:
                break

        

class Hole:
    def __init__(self, base: MyApp, i: int, pos: Point3):
        self.__pos = pos
        self.__index = i
        self.__is_inside = False

        self.__graphics = HoleGraphics(base, i, pos)

    @property
    def index(self):
        return self.__index

    @property
    def is_inside(self):
        return self.__is_inside

    @property
    def pos(self):
        return self.__pos

    def update(self, marble_list: list[Marble]):
        if self.__is_inside:
            return

        for marble in marble_list:
            # 既にどこかの穴に入っているボールは対象外
            if marble.status.hole_index is not None:
                continue
            if self.is_in(marble.get_pos()):
                self.__is_inside = True
                marble.hole(self)
                break

    def is_in(self, pos: Point3) -> bool:
        difference = pos - self.__pos
        distance = difference.length()
        return distance < 1.5



class FirstBox:
    def __init__(self, base: MyApp, physics_world: BulletWorld):
        self.__base = base
        self.__physics_world = physics_world

        node = BulletRigidBodyNode("box")

        pos_list = [Point3(0, 0, -20), Point3(0, 0, 20), Point3(0, -20, 0), Point3(0, 20, 0), Point3(-20, 0, 0), Point3(20, 0, 0)]
        hpr_list = [VBase3(0, 90, 0), VBase3(0, 90, 0), VBase3(0, 0, 0), VBase3(0, 0, 0), VBase3(90, 0, 0), VBase3(90, 0, 0)]
        for i in range(6):
            shape = BulletBoxShape(VBase3(20, 2, 20))
            ts = TransformState.makePosHpr(pos_list[i], hpr_list[i])
            node.addShape(shape, ts)
        
        
        node.setRestitution(0.5)
        node.setMass(0)
        node.setKinematic(True)
        ts = TransformState.makePosHpr(Point3(0, 0, 70), VBase3(0, 0, 0))
        node.setTransform(ts)
        physics_world.attachRigidBody(node)

        self.__node = node
        self.__is_released = False

    def update(self, current_real_time: float):
        if self.__is_released:
            return

        degree = current_real_time * 120
        degree %= 360
        ts = TransformState.makePosHpr(Point3(0, 0, 70), VBase3(0, 0, degree))
        self.__node.setTransform(ts)

    def release(self):
        self.__physics_world.removeRigidBody(self.__node)
        self.__is_released = True


    
    

class FixedCylinder():
    def __init__(self, base: MyApp, physics_world: BulletWorld, radius: float, height: float, pos: Point3, hpr: VBase3):
        cylinder_shape = BulletCylinderShape(radius, height)
        cylinder_node = BulletRigidBodyNode("cylinder")
        cylinder_node.addShape(cylinder_shape)
        cylinder_node.setRestitution(1.0)
        cylinder_node.setMass(0)
        cylinder_node.setStatic(True)
        ts = TransformState.makePosHpr(pos, hpr)
        cylinder_node.setTransform(ts)
        physics_world.attachRigidBody(cylinder_node)

        self.__graphics = FixedCylinderGraphics(base, radius, height)
        self.__graphics.set_pos(pos)
        self.__graphics.set_hpr(hpr)


class FixedBox():
    def __init__(self, base: MyApp, physics_world: BulletWorld, radius: VBase3, pos: Point3, hpr: VBase3):
        box_shape = BulletBoxShape(radius)
        box_node = BulletRigidBodyNode("box")
        box_node.addShape(box_shape)
        box_node.setRestitution(1.0)
        box_node.setMass(0)
        box_node.setStatic(True)
        ts = TransformState.makePosHpr(pos, hpr)
        box_node.setTransform(ts)
        physics_world.attachRigidBody(box_node)
        #box_node.setIntoCollideMask(BitMask32.bit(CollisionGroup.WALL))

        #self.__graphics = FixedBoxGraphics(base, radius)
        #self.__graphics.set_pos(pos)
        #self.__graphics.set_hpr(hpr)




"""
class ElectricCountryOld(Stage):
    def __init__(self, base: MyApp, physics_world: BulletWorld) -> None:
        super().__init__(base)

        self.__fixel_box_1 = FixedBox(base, physics_world, VBase3(0.5, 1, 0.5), Point3(0, 0, 5), VBase3(0, 0, 0))
        self.__fixel_box_2 = FixedBox(base, physics_world, VBase3(0.5, 1, 0.5), Point3(-3, 0, 5), VBase3(0, 0, 0))
        self.__fixel_box_3 = FixedBox(base, physics_world, VBase3(0.5, 1, 0.5), Point3(3, 0, 5), VBase3(0, 0, 0))

        self.__fixed_box_4 = FixedBox(base, physics_world, VBase3(0.5, 1, 20), Point3(-6.5, 0, 25), VBase3(0, 0, 0))
        self.__fixed_box_5 = FixedBox(base, physics_world, VBase3(0.5, 1, 20), Point3(6.5, 0, 25), VBase3(0, 0, 0))

        self.__fixed_box_6 = FixedBox(base, physics_world, VBase3(7, 1, 2), Point3(0, 0, 2), VBase3(0, 0, 0))


        self.__fixed_cylinder_1 = FixedCylinder(base, physics_world, 0.5, 1, Point3(-4.5, 0, 12), VBase3(0, 90, 0))
        self.__fixed_cylinder_2 = FixedCylinder(base, physics_world, 0.5, 1, Point3(4.5, 0, 12), VBase3(0, 90, 0))
        self.__fixed_cylinder_3 = FixedCylinder(base, physics_world, 0.5, 1, Point3(-1.5, 0, 12), VBase3(0, 90, 0))
        self.__fixed_cylinder_4 = FixedCylinder(base, physics_world, 0.5, 1, Point3(1.5, 0, 12), VBase3(0, 90, 0))

        self.__fixed_cylinder_5 = FixedCylinder(base, physics_world, 0.5, 1, Point3(3, 0, 15), VBase3(0, 90, 0))
        self.__fixed_cylinder_6 = FixedCylinder(base, physics_world, 0.5, 1, Point3(-3, 0, 15), VBase3(0, 90, 0))
        self.__fixed_cylinder_7 = FixedCylinder(base, physics_world, 0.5, 1, Point3(0, 0, 15), VBase3(0, 90, 0))

        self.__fixed_cylinder_8 = FixedCylinder(base, physics_world, 0.5, 1, Point3(-1.5, 0, 18), VBase3(0, 90, 0))
        self.__fixed_cylinder_9 = FixedCylinder(base, physics_world, 0.5, 1, Point3(1.5, 0, 18), VBase3(0, 90, 0))

        self.__fixed_cylinder_10 = FixedCylinder(base, physics_world, 0.5, 1, Point3(0, 0, 21), VBase3(0, 90, 0))
"""