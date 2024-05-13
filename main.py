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
    def __init__(self, image, palyer_x, palyer_y, win, move, speed):
        super().__init__( image, palyer_x, palyer_y, win)
        self.keys = [Player.movable[move][0],Player.movable[move][1]]
        self.speed = speed
    def move(self):
        keys = key.get_pressed()
        if keys[self.keys[0]] and self.rect.y>0:
            self.rect.y = self.rect.y- self.speed
        if keys[self.keys[1]] and self.rect.y<420:
            self.rect.y = self.rect.y+ self.speed
    def update(self):
        self.win.blit(self.image,(self.rect.x,self.rect.y))

class Ball(GameSprite):
    def __init__(self,image, palyer_x, palyer_y, win):
        super().__init__(image, palyer_x, palyer_y, win)
        self.speed_x = 2
        self.speed_y = 2
    def move(self,racket1,racket2):
        if self.rect.colliderect(racket1) or self.rect.colliderect(racket2):
            self.speed_x *= -1
        if self.rect.y<0 or self.rect.y>480:
            self.speed_y*= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update(self):
        self.win.blit(self.image,(self.rect.x,self.rect.y))
def update(background):
    win.blit(background,(0,0))
    player_1.move()
    player_1.update()
    player_2.move()
    player_2.update()
    ball_1.move(player_1,player_2)
    ball_1.update()

win = display.set_mode((700, 500))
display.set_caption("Ping_Pong")
clock = time.Clock()
game = True
FPS = 60
finish = False

background = transform.scale(image.load('resources/Background.png'),(700,500))
ball = transform.scale(image.load('resources/Мячь.png'),(20,20))
pong = transform.scale(image.load('resources/Pong.png'),(20,80))


player_1 = Player(pong, 50, 200, win, 'left', 3)
player_2 = Player(pong, 650, 200, win, 'right', 3)
ball_1 = Ball(ball,350,250,win)

while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
            break
    update(background)
    display.update()