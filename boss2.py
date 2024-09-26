import pygame
from pygame.sprite import Sprite
import random
import math
from setting import *

class Boss2(Sprite):
    def __init__(self):
        super().__init__()
        self.CurrFrame = 0
        self.imgs = [pygame.image.load("Boss2Anim/boss22.png"), pygame.image.load("Boss2Anim/boss23.png"),
                     pygame.image.load("Boss2Anim/boss24.png"), pygame.image.load("Boss2Anim/boss25.png")]
        self.image = self.imgs[self.CurrFrame]
        #spawn
        self.x_pos= random.randint(-self.image.get_width(),screen_width+ self.image.get_width())
        self.y_pos = random.choices([-self.image.get_height(),screen_height+self.image.get_height()])
        self.y_pos = self.y_pos[0]
        self.rect = self.image.get_rect(topleft= (self.x_pos,self.y_pos))
        #settings
        self.enemy_speed = 2.1
        self.health = 125
        self.died = False
        self.closest = []
        self.updateTime = pygame.time.get_ticks()
        self.Anim_cd = 200
        #dmg
        self.dmgAnim = False
        self.dmgAnimCD = 0

    def update(self,screen,player,bullet_group,trail):
        trail_vec = pygame.math.Vector2(player.center)
        closest = 0
        for i,t in enumerate(trail):
            x_dist = self.rect.center[0] - t.rect.center[0] + 0.000001
            y_dist = t.rect.center[1] - self.rect.center[1] + 0.000001
            dist = ((x_dist) ** 2 + (y_dist) ** 2) ** (1 / 2)
            if closest == 0:
                closest = dist
            if dist < closest:
                closest = dist
                trail_vec = pygame.math.Vector2(t.rect.center)
            if len(trail)==1:
                trail_vec = pygame.math.Vector2(t.rect.center)
        if len(trail) == 0:
            self.enemy_speed = 5.2

        boss_vec = pygame.math.Vector2(self.rect.center)
        dir = (trail_vec - boss_vec).normalize()
        self.rect.left += dir[0] * self.enemy_speed
        self.rect.top += dir[1] * self.enemy_speed
        #Clean up mechanics
        trail.draw(screen)
        pygame.sprite.spritecollide(self,trail,True)
        #animate boss
        if pygame.time.get_ticks() - self.updateTime > self.Anim_cd:
            self.animate()
            self.updateTime = pygame.time.get_ticks()
        # Boss hit animation
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.health -= 1
            self.dmgAnim = True
        if self.health == 0:
            self.died = True
        if self.dmgAnim == True:
            imgCopy = self.image.copy()
            imgCopy.fill("Red", special_flags=pygame.BLEND_RGBA_MULT)
            if self.dmgAnimCD <= 50:
                screen.blit(imgCopy, self.rect)
                self.dmgAnimCD += 1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                self.dmgAnimCD = 0
                screen.blit(self.image, self.rect)
        elif self.dmgAnim == False or self.died == False:
            screen.blit(self.image, self.rect)
        # boss name
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        text = "\"The Cleaner\""
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render, (screen_width // 2 - (width // 2), 20))
        # health
        for i in range(1, self.health + 1):
            health_surf = pygame.Surface((10, 15))
            screen.blit(health_surf, (screen_width // 2 - 650 + (i * health_surf.get_width()), height + 40))

    def animate(self):
        if self.CurrFrame == len(self.imgs)-1:
            self.CurrFrame = 0
            self.image = self.imgs[self.CurrFrame].convert_alpha()
        else:
            self.CurrFrame += 1
            self.image  = self.imgs[self.CurrFrame].convert_alpha()






