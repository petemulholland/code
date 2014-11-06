from visual import * 
from color_list import *

def ex_17_8():
    scene.range = (256, 256, 256) 
    scene.center = (128, 128, 128) 
    color = (0.1, 0.1, 0.9) # mostly blue 
    sphere(pos = scene.center, radius = 128, color = color)

def ex_17_8_2():
    scene.range = (256, 256, 256) 
    scene.center = (128, 128, 128) 
    #color = (0.1, 0.1, 0.9) # mostly blue 
    t = range( 0, 256, 51) 
    for x in t: 
        for y in t: 
            for z in t: 
                pos = x, y, z 
                color = (x / 255.0, y / 255.0, z / 255.0)
                sphere( pos = pos, radius = 10, color = color)

def ex_17_8_3():
    base_range = 256
    base_center = base_range / 2

    space_multiplier = 5
    use_radius = 10

    use_range = base_range * space_multiplier
    use_center = base_center * space_multiplier

    scene.range = (use_range, use_range, use_range) 
    scene.center = (use_center, use_center, use_center) 

    dict, rgbs = read_colors()

    for color in rgbs:
        rgb = color[0]
        red = int(rgb[1:3], 16)
        green = int(rgb[3:5], 16)
        blue = int(rgb[5:7], 16)

        
        pos = (red * space_multiplier, green * space_multiplier, blue * space_multiplier)
        col = (red / 255.0, green / 255.0, blue / 255.0)
        #print 'pos:', pos, 'color:', col
        sphere(pos=pos, radius = use_radius, color=col)


if __name__ == '__main__':

    ex_17_8_3()