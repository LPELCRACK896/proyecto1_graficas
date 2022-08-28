from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend, grayScale, greenScale, redScale, blueScale
import lpmath as lpm 
width = 1913
height = 735

rend = Renderer(width, height)

#rend.active_texture = Texture('models/dkt-copy.bmp')
rend.background = Texture('models/ascent_fondo.bmp')
#rend.dirLight = V3(1, 0, 0)

rend.active_shader = textureBlend

rend.glClearBackground()

""" rend.glLoadModel("models/wall.obj",
                 translate = V3(-15, -5.5, -22),
                 scale = V3(0.5,0.5,0.5),
                 rotate = V3(10,-40,-20)) """
""" rend.glLoadModel("models/SigSauerP250.obj",
                 translate = V3(-12, -5.5, -22),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,0)) """
rend.active_texture = Texture('models/sage_wall_texture.bmp')

rend.glLoadModel("models/wall.obj",
                 translate = V3(-25, -9, -40),
                 scale = V3(1,1,1),
                 rotate = V3(0,60,-5))
rend.active_texture = Texture('models/gun_BC.bmp')

rend.glLoadModel("models/SigSauerP250.obj",
                 translate = V3(-13, -5.5, -18),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,80))
                 
rend.active_texture = Texture('models/Sword01_BaseColor.bmp')

rend.glLoadModel("models/sword2.obj",
                 translate = V3(30, -5, -22),
                 scale = V3(.1,.1,.1),
                 rotate = V3(-120,-30,120))

rend.active_texture = None#Texture('models/Sword01_BaseColor.bmp')

rend.glLoadModel("models/MK2.obj",
                 translate = V3(1, 1, 1),
                 scale = V3(10,10,10),
                 rotate = V3(-120,-30,120))

""" rend.active_shader = redScale

rend.glLoadModel("models/model.obj",
                 translate = V3(-4, 3, -10)
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = blueScale

rend.glLoadModel("models/model.obj",
                 translate = V3(0, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = grayScale """

""" rend.glLoadModel("models/model.obj",
                 translate = V3(4, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0)) """

#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))



rend.glFinish("output.bmp")

