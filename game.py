from time import sleep
from random import *
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,speed,x,y,w,h):
        super().__init__()
        self.image = Surface((w,h))
        self.image.fill((165,67,34)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y  > 5:
            self.rect.y -= 10
        elif keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += 10

    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        elif keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += 10

class Ball(GameSprite):
    def __init__(self,speedx,speedy,x,y,sizex,sizey):
        super().__init__(speedx,x,y,sizex,sizey)
        self.speed2 = speedy
    def update(self,stena1,stena2):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if sprite.collide_rect(self,stena1) or sprite.collide_rect(self,stena2):
            self.speed *= -1
        if self.rect.y < 0 or self.rect.bottom > 500:
            self.speed2 *= -1
        







font.init()
font1 = font.Font(None,50)
sharik = Ball(5,5,100,300,30,30)
clock = time.Clock()
finish = False
game = True
FPS = 40
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
stena1 = Player(10,80,200,20,50)
stena2 = Player(10,600 ,200,20,50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_r:
            sharik.rect.x = 350
            sharik.rect.y = 250
            finish = False

                
    if finish != True:
        window.fill((34,212,189))
        stena1.reset()
        stena2.reset()
        stena2.update1()
        stena1.update2()
        sharik.reset()
        sharik.update(stena1, stena2)
        if sharik.rect.x < 0:
            finish = True
            text1 = font1.render(('Левый игрок проиграл, нажми на R, чтобы начать игру заново!',1,(180, 0, 0)))
        display.update()
        clock.tick(FPS)
