from __future__ import annotations
from direct.gui.DirectGui import DirectWaitBar, DirectFrame
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage

from typing import Optional
from dataclasses import dataclass
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.path_manager import PathManager
from marble_allocator.graphics.setting import marble_graphics_setting_list

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from marble_allocator.main import MyApp
    from marble_allocator.core.marble import Marble


class HUD:
    def __init__(self, base: MyApp):
        self.__base = base
        #self.__select_ui = SelectUI(base)
        self.__tournament_ui = TournamentUI(base)

    def update(self, marble_list: list[Marble]):
        #self.__select_ui.update(marble_list)
        self.__tournament_ui.update(marble_list)


class SelectUI:
    def __init__(self, base: MyApp):
        self.__base = base
        self.__title = OnscreenText(
            text="Select Special Weapon",
            pos=(0, 0.75),
            scale=0.15,
            fg=(1, 1, 1, 1),
            align=TextNode.ACenter,
            font=self.__base.resource_context.font.mplus_bold,
            parent=self.__base.aspect2d_right,
            sort=10
        )

        #self.__image = OnscreenImage(
        #    image=PathManager.resource_vfs("textures/hud/sub_weapon.png"),
        #    pos=(0, 0, -0.75),
        #    parent=self.__base.aspect2d_right,
        #    scale=(0.4, 0, 0.2),
        #    color= (1, 1, 1, 1)
        #)
        #self.__image.setTransparency(TransparencyAttrib.MAlpha)

        self.__thing_ui_0 = ThingUI(base, "missile", Point3(-0.4, 0, 0.3), (0, 0, 0, 1), 0, "Missile")
        self.__thing_ui_1 = ThingUI(base, "rain", Point3(0.4, 0, 0.3), (0, 0, 0, 1), 1, "Rain")
        self.__thing_ui_2 = ThingUI(base, "electromagnetic_wave", Point3(-0.4, 0, -0.3), (0, 0, 0, 1), 2, "EMP")
        self.__thing_ui_3 = ThingUI(base, "hyper_beam", Point3(0.4, 0, -0.3), (0, 0, 0, 1), 3, "Hyper Beam")

    def update(self, marble_list: list[Marble]):
        for marble in marble_list:
            if marble.status.hole_index == 0:
                self.__thing_ui_0.select(marble)
            if marble.status.hole_index == 1:
                self.__thing_ui_1.select(marble)
            if marble.status.hole_index == 2:
                self.__thing_ui_2.select(marble)
            if marble.status.hole_index == 3:
                self.__thing_ui_3.select(marble)


class TournamentUI:
    def __init__(self, base: MyApp):
        self.__base = base
        self.__tournament_lines_ui = TournamentLinesUI(base)
        self.__tournament_player_ui_list = []
        for i in range(4):
            player_ui = TournamentPlayerUI(base, i)
            self.__tournament_player_ui_list.append(player_ui)
        
    def update(self, marble_list: list[Marble]):
        self.__tournament_lines_ui.update(marble_list)
        
        for marble in marble_list:
            if marble.status.hole_index == 0:
                self.__tournament_player_ui_list[0].select(marble)
            if marble.status.hole_index == 1:
                self.__tournament_player_ui_list[1].select(marble)
            if marble.status.hole_index == 2:
                self.__tournament_player_ui_list[2].select(marble)
            if marble.status.hole_index == 3:
                self.__tournament_player_ui_list[3].select(marble)


class TournamentLinesUI:
    def __init__(self, base: MyApp):
        self.__base = base
        self.__node_path = base.aspect2d_right.attachNewNode("tournament_lines")

        # 線の太さの設定（半分幅: 0.003 -> 全体太さ: 0.006）
        line_t = 0.01

        # X軸の位置定義 (範囲: -0.85 〜 0.60)
        x0 = -0.3   # 1回戦（選手位置）
        x1 = -0.1   # 1回戦の結合縦線
        x2 = 0.1   # 準決勝（勝者位置）
        x3 =  0.2   # 準決勝の結合縦線
        x4 =  0.4   # 優勝者位置

        # Z軸の位置定義 (範囲: -1.0 〜 1.0)
        z_p1 =  0.75 # P1
        z_p2 =  0.25 # P2
        z_p3 = -0.25 # P3
        z_p4 = -0.75 # P4
        
        z_m1 = (z_p1 + z_p2) / 2  # 準決勝1 (0.50)
        z_m2 = (z_p3 + z_p4) / 2  # 準決勝2 (-0.50)
        z_final = 0.00             # 決勝・優勝 (0.00)

        # Helper: 横線（DirectFrame）を作成する関数
        def create_h_line(x_start: float, x_end: float, z: float) -> DirectFrame:
            return DirectFrame(
                frameColor=(1, 1, 1, 1),
                frameSize=(0, x_end - x_start, -line_t, line_t),
                pos=(x_start, 0, z),
                parent=self.__node_path
            )

        # Helper: 縦線（DirectFrame）を作成する関数
        def create_v_line(x: float, z_start: float, z_end: float) -> DirectFrame:
            # z_start > z_end のため下向きに伸ばす
            return DirectFrame(
                frameColor=(1, 1, 1, 1),
                frameSize=(-line_t, line_t, z_end - z_start, 0),
                pos=(x, 0, z_start),
                parent=self.__node_path
            )

        # ==========================================
        # 1回戦 (P1〜P4) → 準決勝 (x0 〜 x2)
        # ==========================================
        # 4本の横線 (x0 -> x1)
        self.l_p1_h = create_h_line(x0, x1, z_p1)
        self.l_p2_h = create_h_line(x0, x1, z_p2)
        self.l_p3_h = create_h_line(x0, x1, z_p3)
        self.l_p4_h = create_h_line(x0, x1, z_p4)

        # 2本の縦線 (P1-P2間, P3-P4間)
        self.l_p1_p2_v = create_v_line(x1, z_p1, z_p2)
        self.l_p3_p4_v = create_v_line(x1, z_p3, z_p4)

        # 準決勝への横線 (x1 -> x2)
        self.l_m1_in = create_h_line(x1, x2, z_m1)
        self.l_m2_in = create_h_line(x1, x2, z_m2)

        # ==========================================
        # 準決勝 → 決勝 (x2 〜 x3)
        # ==========================================
        # 1本の結合縦線 (M1-M2間)
        self.l_m1_m2_v = create_v_line(x3, z_m1, z_m2)

        # 準決勝枠から縦線までの横線 (x2 -> x3)
        self.l_m1_out = create_h_line(x2, x3, z_m1)
        self.l_m2_out = create_h_line(x2, x3, z_m2)

        # ==========================================
        # 決勝 → 優勝者 (x3 〜 x4)
        # ==========================================
        # 縦線中央から優勝位置への横線 (x3 -> x4)
        self.l_final_to_winner = create_h_line(x3, x4, z_final)

        self.__trophy = OnscreenImage(
            image=PathManager.resource_vfs("textures/hud/trophy.png"),
            pos=(x4 + 0.2, 0, z_final),
            parent=self.__node_path,
            scale=0.2,
            color= (1, 1, 0.2, 1)
        )
        self.__trophy.setTransparency(TransparencyAttrib.MAlpha)

    def update(self, marble_list: list[Marble]):
        pass



class TournamentPlayerUI:
    def __init__(self, base: MyApp, index: int):
        self.__base = base
        self.__index = index
        
        self.__node_path = base.aspect2d_right.attachNewNode("tournament_player_ui")

        pos_list = [Point3(-0.55, 0, 0.75), Point3(-0.55, 0, 0.25), Point3(-0.55, 0, -0.25), Point3(-0.55, 0, -0.75)]
        pos = pos_list[index]
        self.__node_path.setPos(pos)
        
        self.__frame_back = DirectFrame(frameColor=(1,1,1,1),
                                        frameSize=(-0.27, 0.27, -0.12, 0.12),
                                        pos=(0, 0, 0),
                                        parent=self.__node_path)
        self.__frame_back.hide()
        self.__frame_back.setBin("fixed", -3)
        self.__frame_back.setDepthTest(False)
        self.__frame_back.setDepthWrite(False)

        self.__frame = DirectFrame(frameColor=(1,1,1,1),
                                        frameSize=(-0.25, 0.25, -0.1, 0.1),
                                        pos=(0, 0, 0),
                                        parent=self.__node_path)

        self.__frame.setBin("fixed", -1)
        self.__frame.setDepthTest(False)
        self.__frame.setDepthWrite(False)

        self.__name = OnscreenText(
            text=f"",
            pos=(0, -0.035),
            scale=0.12,
            fg=(1, 1, 1, 1),
            align=TextNode.ACenter,
            font=self.__base.resource_context.font.mplus_bold,
            parent=self.__node_path,
            sort=10
        )
        self.__node_path.setBin("fixed", 100)
        self.__node_path.setDepthTest(False)
        self.__node_path.setDepthWrite(False)

    def select(self, marble: Marble):
        setting = marble_graphics_setting_list[marble.index]
        self.__name.setText(setting.name)
        color = setting.color_mid.float_rgb + (1, )
        self.__name["fg"] = color
        self.__frame_back["frameColor"] = color
        self.__frame_back.show()


class ThingUI:
    def __init__(self, base: MyApp, image_file_name: str, pos: Point3, color: tuple[float, float, float, float], index: int, name: str):
        self.__base = base
        self.__node_path = base.aspect2d_right.attachNewNode("thing_ui")
        self.__node_path.setPos(pos)

        self.__frame_back = DirectFrame(frameColor=(1,1,1,1),
                                        frameSize=(-0.32, 0.32, -0.22, 0.22),
                                        pos=(0, 0, 0),
                                        parent=self.__node_path)
        self.__frame_back.hide()
        self.__frame_back.setBin("fixed", -3)
        self.__frame_back.setDepthTest(False)
        self.__frame_back.setDepthWrite(False)


        self.__frame = DirectFrame(frameColor=(1,1,1,1),
                                        frameSize=(-0.3, 0.3, -0.2, 0.2),
                                        pos=(0, 0, 0),
                                        parent=self.__node_path)

        self.__frame.setBin("fixed", -1)
        self.__frame.setDepthTest(False)
        self.__frame.setDepthWrite(False)


        self.__icon = OnscreenImage(
            image=PathManager.resource_vfs(f"textures/hud/{image_file_name}.png"),
            pos=(0, 0, -0.04),
            parent=self.__node_path,
            scale=0.12,
            color=color,
            sort=10
        )
        self.__icon.setTransparency(TransparencyAttrib.MAlpha)

        self.__name = OnscreenText(
            text=f"{index+1}: {name}",
            pos=(0, 0.12),
            scale=0.06,
            fg=color,
            align=TextNode.ACenter,
            font=self.__base.resource_context.font.mplus_bold,
            parent=self.__node_path,
            sort=10
        )
        self.__node_path.setBin("fixed", 100)
        self.__node_path.setDepthTest(False)
        self.__node_path.setDepthWrite(False)



    def update(self):
        pass

    def select(self, marble: Marble):
        setting = marble_graphics_setting_list[marble.index]
        color_mid = setting.color_mid.float_rgb

        self.__frame_back["frameColor"] = color_mid + (1, )
        self.__frame_back.show()

        self.__icon["color"] = color_mid + (1, )
        self.__name["fg"] = color_mid + (1, )


