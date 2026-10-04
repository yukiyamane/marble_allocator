from logging import getLogger, StreamHandler, DEBUG

#pyrefly: ignore [missing-import]
from panda3d.core import (PandaNode, Vec2, Vec3, Vec4, VBase3, Quat, Material, TransparencyAttrib,
                        TextureStage, TexGenAttrib, LightRampAttrib, Texture, Shader, MaterialAttrib,
                        LineSegs, NodePath, AntialiasAttrib, TextNode,
                        WindowProperties, PandaSystem, ClockObject,
                        AmbientLight, DirectionalLight, PointLight, Spotlight, BitMask32,
                        DepthWriteAttrib, ColorBlendAttrib,
                        GeomNode, TextNode, Point3, Point2,

                        TransformState,

                        CollisionRay, CollisionHandlerQueue, CollisionTraverser, CollisionNode, 
                        CardMaker, GeomVertexRewriter, GeomVertexWriter,GeomVertexFormat, GeomVertexData, GeomTriangles, Geom, GeomNode, InternalName, GeomVertexArrayFormat, GeomEnums,
                        TextNode, MeshDrawer, Camera, OrthographicLens, PerspectiveLens
                        )
from direct.gui.OnscreenImage import OnscreenImage
# pyrefly: ignore [missing-import]
from panda3d.bullet import BulletWorld, BulletRigidBodyNode, BulletSphereShape, BulletPlaneShape, BulletBoxShape, BulletCylinderShape, BulletTriangleMesh, BulletTriangleMeshShape, BulletContactCallbackData, BulletGhostNode, ZUp
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.task import Task

globalClock = ClockObject.getGlobalClock()

#from panda3d_tools import pstats
#pstats()
#from panda3d.core import loadPrcFile
#loadPrcFile("conf.prc")
#from direct.directbase.DirectStart import *
#run()
#from panda3d.core import PStatClient
#PStatClient.connect()



logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
#logger.disabled = True

#os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

#path = os.getcwd()
#logger.info(path)
