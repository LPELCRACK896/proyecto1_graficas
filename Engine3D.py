from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend, grayScale, greenScale, redScale, blueScale
 
width = 960
height = 540

rend = Renderer(width, height)

#rend.active_texture = Texture('models/body.bmp')

rend.dirLight = V3(1, 0, 0)

rend.active_shader = flat

rend.glLoadModel("models/ufo.obj",
                 translate = V3(-8, 3, -10),
                 scale = V3(1,1,1),
                 rotate = V3(0,0,0))
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

rend.glLoadModel("models/model.obj",
                 translate = V3(4, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

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

