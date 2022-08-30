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


rend.glClearBackground()

rend.active_shader = grayScale

rend.active_texture = Texture('models/wall/sage_wall_texture.bmp')
rend.glLoadModel("models/wall/wall.obj",
                 translate = V3(-25, -9, -40),
                 scale = V3(1,1,1),
                 rotate = V3(0,60,-5))


rend.active_shader = textureBlend
rend.active_texture = Texture('models/gun/gun_BC.bmp')

rend.glLoadModel("models/gun/SigSauerP250.obj",
                 translate = V3(-13, -5.5, -18),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,80))
                
rend.active_texture = Texture('models/sword/Sword01_BaseColor.bmp')

rend.glLoadModel("models/sword/sword2.obj",
                 translate = V3(32, -2, -30),
                 scale = V3(.1,.1,.1),
                 rotate = V3(-50,-60,120))
""" rend.active_texture =   None #Texture('models/barrel/poison_barrel_text.bmp')

rend.glLoadModel("models/barrel/barrel.obj",
                 translate = V3(0, 0, 0),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,0)) """

""" rend.active_texture =   Texture('models/tree/tree.bmp')

rend.glLoadModel("models/tree/tree.obj",
                 translate = V3(0, 0, 0),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,0)) """

    
""" rend.active_texture = None

rend.glLoadModel("models/Gun.obj",
                 translate =V3(1, 1, 1),
                 scale = V3(4,4,4),
                 rotate = V3(-120,-30,120))  """

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
