from visual import *

def ex_17_8():
    scene.range = (256, 256, 256)
    scene.center = (128, 128, 128)

    color = (0.1, 0.1, 0.9)
    sphere(pos=center, radius=128, color=color)
    pass

if __name__ == '__main__':
    ex_17_8()