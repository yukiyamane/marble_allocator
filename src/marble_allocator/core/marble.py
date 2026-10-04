from __future__ import annotations
from typing import override, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass
import random

from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.yamane_state_machine import StateMachine, StateContext
from marble_allocator.graphics.marble import MarbleGraphics

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp
    from marble_allocator.core.allocator import Allocator
    from marble_allocator.core.stage import Hole




@dataclass
class MarbleStatus:
    hole_index : Optional[int] = None

    
class MarblePhysics():
    def __init__(self, base: MyApp, physics_world: BulletWorld, index: int):
        shape = BulletSphereShape(4.9)
        node = BulletRigidBodyNode("marble")
        node.addShape(shape)
        node.setRestitution(1.0)
        node.setMass(10)
        node.setStatic(False)
        physics_world.attachRigidBody(node)
        self.__node = node
        self.__node_path = base.render.attachNewNode(node)

        pos_list = [Point3(6, 6, 65), (-6, -6, 65), (6, 6, 77), (-6, -6, 77)]
        random.shuffle(pos_list)
        self.__node_path.setPos(pos_list[index])

    @property
    def node_path(self) -> NodePath:
        return self.__node_path

    def get_pos(self) -> Point3:
        return self.__node_path.getPos()

    def get_hpr(self) -> VBase3:
        return self.__node_path.getHpr()

    def fix(self, pos: Point3):
        # 1. 位置を穴の中心に合わせる
        self.__node_path.setPos(pos)

        # 2. 物理演算の速度・回転速度をゼロにする
        self.__node.setLinearVelocity(Vec3(0, 0, 0))
        self.__node.setAngularVelocity(Vec3(0, 0, 0))

        # 3. 物理シミュレーションから切り離して完全固定化する
        self.__node.setKinematic(True)


class Marble():
    def __init__(self, base: MyApp, physics_world: BulletWorld, index: int):
        self.__index = index
        self.__status = MarbleStatus()
        self.__physics = MarblePhysics(base, physics_world, index)
        self.__graphics = MarbleGraphics(base, self.__physics.node_path, index)

    @property
    def index(self) -> int:
        return self.__index

    @property
    def status(self) -> MarbleStatus:
        return self.__status

    def get_pos(self) -> Point3:
        return self.__physics.get_pos()

    def hole(self, hole: Hole):
        self.__status.hole_index = hole.index
        self.__physics.fix(hole.pos)

    def update(self, dt: float):
        pass