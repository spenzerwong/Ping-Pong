#Create your own shooter

from pygame import *
from random import randint
from time import time as timer


win_width = 500
win_height = 700

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100,150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
    
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

window = display.set_mode((win_height,win_width))
display.set_caption('Ping Pong')
background = transform.scale(image.load("background.jpg"),(700,500))

paddle_1 = Player("paddle1.png",600,150,10)
paddle_2 = Player("paddle2.png",5,150,10)

run = True
finish = False
clock = time.Clock()
FPS = 60
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:

        window.blit(background,(0,0))
        paddle_1.update_1()
        paddle_2.update_2()



        paddle_1.reset()
        paddle_2.reset()
        display.update()

    clock.tick(FPS)