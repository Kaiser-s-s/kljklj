#Створи власний Шутер!

from typing import Any
from pygame import*
window = display.set_mode((700,500))
display.set_caption(("шутер"))
dackground = transform.scale(image.load("galaxy.jpg"),(700,500))
mixer.init()
font.init()
mixer.music.set_volume(0.02)
mixer.music.load("space.ogg")

mixer.music.play()
clock = time.Clock()
FPS = 60
scene = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

blyts =sprite.Group()
class Play(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x +=self.speed
    def fier(self):
        panda = bylt("bullet.png", self.rect.centerx,self.rect.top,5)
        blyts.add(panda)
        
font1 = font.Font(None, 36)
lost = 0
class anemi (GameSprite):
    def update(self):
        global lost
        self.rect.y +=self.speed
        if self.rect.y > 600:
            self.rect.y = 0
            lost =lost + 1


class bylt (GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y < 0:
            self.kill()

monsters = sprite.Group()
text_lost = font1.render("пропущено:"  + str(lost), 1, (255, 255, 255))


lotos = Play("rocket.png",325,200,5)
panda = bylt("bullet.png", lotos.rect.centerx,lotos.rect.top,-15)
arrivals1 = anemi("ufo.png",100,56,2)
arrivals2 = anemi("ufo.png",200,59,1)
arrivals3 = anemi("ufo.png",300,70,2)
arrivals4 = anemi("ufo.png",400,20,1)
arrivals5 = anemi("ufo.png",500,40,2)

while scene:
    text_lost = font1.render("пропущено:"  + str(lost), 1, (255, 255, 255))
    window.blit(dackground,(0,0))
    panda.reset()
    panda.update()
    arrivals5.reset()
    arrivals5.update()
    arrivals4.reset()
    arrivals4.update()
    arrivals3.reset()
    arrivals3.update()
    arrivals2.reset()
    arrivals2.update()
    arrivals1.reset()
    arrivals1.update()
    lotos.reset()
    lotos.update()
    clock.tick(FPS)
    window.blit(text_lost,(70,100))



    blyts.update()
    blyts.draw(window)
    for e in event.get():
        if e.type ==QUIT:
            scene =False
        if e.type == KEYDOWN and e.key == K_SPACE:
       
            lotos.fier()
    display.update()

