from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.yamane_state_machine import StateMachine, StateContext
from marble_allocator.core.stage import ElectricCountry, IceCountry, SandCountry, ElectricCountryTournament
from marble_allocator.core.marble import Marble
from marble_allocator.graphics.hud import HUD

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp


class Allocator:
    def __init__(self, base: MyApp):
        self.__base = base

        # Bullet ワールド
        self.__physics_world = BulletWorld()
        self.__physics_world.setGravity(Vec3(0, 0, -98.1))


        self.__state_machine = StateMachine(self)
        self.__state_machine.set_next_state(self.__prepare)

        self.__base.accept("g", self.__accept_battle_start)

    def __accept_battle_start(self):
        self.__state_machine.set_next_state(self.__allocate)

    @property
    def marble_list(self):
        return self.__marble_list

    def update(self, current_raw_time: float, dt: float):
        self.__state_machine.update(current_raw_time, dt)

    def __prepare(self, ctx: StateContext):
        if ctx.is_first:
            self.__stage = ElectricCountryTournament(self.__base, self, self.__physics_world)
            self.__marble_list = []
            for i in range(4):
                marble = Marble(self.__base, self.__physics_world, i)
                self.__marble_list.append(marble)
            self.__hud = HUD(self.__base)
            self.__state_machine.set_next_state(self.__idle)

    def __idle(self, ctx: StateContext):
        self.__physics_world.doPhysics(ctx.dt, 1, ctx.dt)
        self.__stage.update_idle(ctx.current_raw_time)
        self.__hud.update(self.__marble_list)

    def __allocate(self, ctx: StateContext):
        if ctx.is_first:
            self.__stage.release()
        self.__physics_world.doPhysics(ctx.dt, 1, ctx.dt)
        self.__stage.update()
        self.__hud.update(self.__marble_list)
