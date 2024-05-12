from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image, palyer_x, palyer_y, win):
        super().__init__()
        self.image = image
        self.win = win
        self.rect = self.image.get_rect()
        self.rect.x = palyer_x
        self.rect.y = palyer_y
        self.obj_y = palyer_y
        self.obj_x = palyer_x

class Player(GameSprite):
    movable = {"left":{0:K_w,
                       1:K_s},
               'right':{0:K_UP,
                        1:K_DOWN}}
    def __int__(self,image, palyer_x, palyer_y, win,move):
        super().__init__(image, palyer_x, palyer_y, win)
        self.keys = [Player.movable[move][0],Player.movable[move][1]]

class Ball(GameSprite):
    def __init__(self,image, palyer_x, palyer_y, win):
        super().__init__(image, palyer_x, palyer_y, win)
        self.speed_x = 1
        self.speed_y = 1

win = display.set_mode((700, 500))
display.set_caption("Ping_Pong")
clock = time.Clock()
game = True
FPS = 60
finish = False
ball = transform.scale(image.load('resources/Мячь.png'),(55,55))
pong = transform.scale(image.load('resources/Pong.png'),(20,80))

while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
            break
    display.update()