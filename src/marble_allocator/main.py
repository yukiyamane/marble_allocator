# pyrefly: ignore [missing-import]
from panda3d.core import loadPrcFileData
loadPrcFileData("", 
"""
textures-power-2 None
bullet-filter-algorithm groups-mask
bullet-enable-contact-events true
""")

from direct.showbase.ShowBase import ShowBase
import simplepbr
import gltf
from ctypes import windll
import os
import sys
import pathlib
# プロジェクトのルートディレクトリ（基準パス）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from direct.filter.FilterManager import FilterManager, FrameBufferProperties
from marble_allocator.shared.util.yamane_prepare import *
from marble_allocator.shared.util.path_manager import PathManager
from marble_allocator.core.core_system import CoreSystem
from marble_allocator.graphics.resource_context import ResourceContext

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        if self.loader is None:
            return        

        self.prepare_screen()
        pipeline = simplepbr.init(exposure=0, use_normal_maps=True)
        #LUT stuff
        #self.manager=FilterManager(self.win, self.cam)    
        self.manager = pipeline._filtermgr
        #self.setupLUT('./resource/lut/contrast_up.png')        
        self.color_grading()
        #self.render.set_shader_auto()






        self.properties = WindowProperties()
        self.properties.setTitle("Marble Allocator")

        self.accept("space", self.oobe)
        self.disableMouse()

        if self.loader is None:
            return
        self.axis: NodePath = self.loader.loadModel("models/zup-axis")
        self.axis.setPos(0, 0, 0)
        self.axis.setScale((1, 1, 1))

        is_debug = False
        if is_debug:
            self.properties.setSize(1280, 720)
            self.setFrameRateMeter(True)
            #self.setSceneGraphAnalyzerMeter(True)
            self.axis.reparentTo(self.render)
        else:
            self.properties.setSize(1280, 720)

        self.properties.setFixedSize(True)


        if self.win is not None:
            self.win.requestProperties(self.properties)


        lens = self.camLens
        lens.setNear(2)   # 近クリップ
        lens.setFar(2000.0)  # 遠クリップ
        lens.setFov(30)
        self.camera.setPos(120, -120, 120)
        self.camera.setHpr(45, -30, 0)




        self.__resource_context = ResourceContext(self)
        self.__core_system = CoreSystem(self)


        self.taskMgr.add(self.__update, "update_master")
        self.accept("q", self.debug_analyze)
        self.accept("s", self.debug_screenshot)

    def prepare_screen(self):
        if self.win is None:
            return

        # 1. 既存の全画面DisplayRegionをすべて無効化
        for dr in self.win.getDisplayRegions():
            dr.setActive(False)

        W, H = 1280, 720

        # =========================================================
        # 1. 左半分 (3D用) の作成
        # =========================================================
        dr_left = self.win.makeDisplayRegion(0.0, 0.5, 0.0, 1.0)
        dr_left.setSort(1)
        #dr_left.setClearColorActive(True)
        #dr_left.setClearDepthActive(True)
        #dr_left.setClearColor((0.0, 0.0, 0.0, 1.0))

        # ★重要: デフォルトカメラのレンズを流用せず、左半分専用のレンズを新しく作る
        # これにより、Panda3Dの内部干渉や歪みを完全に排除できます
        lens3d = PerspectiveLens()
        
        # 左半分（幅512、高さ576）の正確なアスペクト比を計算
        aspect_left = (W * 0.5) / H
        lens3d.setAspectRatio(aspect_left)
        
        # 視野角（Fov）を元のコード（self.camLens.setFov(30)）に合わせて設定
        lens3d.setFov(30)
        
        # カメラノードに新しい歪みのないレンズを適用
        self.cam.node().setLens(lens3d)
        dr_left.setCamera(self.cam)

        # =========================================================
        # 2. 右半分 (2D用) の作成
        # =========================================================
        dr_right = self.win.makeDisplayRegion(0.5, 1.0, 0.0, 1.0)
        dr_right.setSort(2)
        dr_right.setClearColorActive(True)
        dr_right.setClearDepthActive(True)
        dr_right.setClearColor((0.03, 0.08, 0.12, 1.0)) # グレー背景

        cam2 = self.makeCamera(self.win)
        lens2d = OrthographicLens()
        
        # 2D側のフィルムサイズも右半分の比率に合わせる
        region_aspect = (W * 0.5) / H
        lens2d.setFilmSize(region_aspect * 2.0, 2.0)
        lens2d.setNearFar(-1000, 1000)
        
        cam2.node().setLens(lens2d)
        dr_right.setCamera(cam2)
        cam2.reparentTo(self.render2d)

        # 右半分のアスペクト比に合わせた独自の aspect2d ルートノードを作成します
        # これをベースにすることで、右半分の中央が (0,0)、上下が -1〜1、左右が比率に合わせた綺麗な座標系になります
        #region_aspect = (W * 0.5) / H
        self.aspect2d_right = self.render2d.attachNewNode("aspect2d_right")
        #self.aspect2d_right.setScale(1.0 / region_aspect, 1.0, 1.0)

    @property
    def resource_context(self):
        return self.__resource_context

    def debug_screenshot(self):
        self.movie(namePrefix='image', duration=1, fps=1, format='png')
        logger.info("screen_shot")

    def debug_analyze(self):
        self.render.analyze()

    def color_grading(self):
        fbprops = FrameBufferProperties()
        fbprops.setFloatColor(True)  # 16bit float

        colortex = Texture()
        self.quad = self.manager.renderSceneInto(colortex=colortex, fbprops=fbprops)
        if self.quad is None:
            return
        self.quad.setShader(Shader.load(Shader.SLGLSL, PathManager.resource_vfs("shaders/color_grading_v.glsl"), PathManager.resource_vfs("shaders/color_grading_f.glsl")))
        self.quad.setShaderInput("colortex", colortex)
    
    def __update(self, task: Task.Task):
        frame_time = globalClock.getFrameTime()
        dt = globalClock.getDt()
        self.__core_system.update(frame_time, dt)
        return task.cont


if __name__ == "__main__":
    print(f"Current Directory: {os.getcwd()}")
    print(f"sys.path[0]: {sys.path[0]}")
    print(f"sys.path: {sys.path}")
    print(f"Python Version: {sys.version}")
    print(f"Panda3D Version: {PandaSystem.getVersionString()}")
    windll.winmm.timeBeginPeriod(1)
    globalClock.setMode(ClockObject.M_limited)
    globalClock.setFrameRate(24)
    app = MyApp()
    app.run()
    windll.winmm.timeEndPeriod(1)
    logger.info("終了")