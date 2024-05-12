from pygame import *

win = display.set_mode((700, 500))
display.set_caption("Ping_Pong")
clock = time.Clock()
game = True
FPS = 60
finish = False

while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
            break
    display.update()