import pygame
from pygame.sprite import Sprite
import random
import math
from setting import *
class lvl3Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.scaleImgTo = 75
        #imgs
        self.frame = 0
        self.imgs = [pygame.image.load("MomAnim/mom5.png"),pygame.image.load("MomAnim/mom6.png"),pygame.image.load("MomAnim/mom7.png")]
        self.image = self.imgs[self.frame]
        self.image = pygame.transform.scale(self.image,(self.scaleImgTo,self.scaleImgTo))
        #spawn
        self.x_pos = random.randint(-self.image.get_width(), screen_width + self.image.get_width())
        self.y_pos = random.choices([-self.image.get_height(), screen_height + self.image.get_height()])
        self.y_pos = self.y_pos[0]
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.enemy_speed = 2
        self.health = 1

    def update(self, player, player_bullet_group):
        player_vec = pygame.math.Vector2(player.center)
        enemy_vec = pygame.math.Vector2(self.rect.center)
        dir = (player_vec - enemy_vec).normalize()
        self.rect.left += dir[0] * self.enemy_speed
        self.rect.top += dir[1] * self.enemy_speed
        if pygame.sprite.spritecollide(self, player_bullet_group, True):
            self.health -= 1
        if self.health == 0:
            self.kill()

    def animate(self):
        if self.frame == len(self.imgs)-1:
            self.frame = 0
            self.image = self.imgs[self.frame].convert_alpha()
            self.image = pygame.transform.scale(self.image,(self.scaleImgTo,self.scaleImgTo))
        else:
            self.frame += 1
            self.image = self.imgs[self.frame].convert_alpha()
            self.image = pygame.transform.scale(self.image,(self.scaleImgTo,self.scaleImgTo))

#Spawn Enemies
class Spawn_lvl3Enemy():
    def __init__(self):
        self.update_time = pygame.time.get_ticks()
        self.enemy_group = pygame.sprite.Group()
        self.spawn_cooldown = 740
        self.total_enemies= 0
        # special atk
        self.enemy_shooting = False
        self.enemy_bullet_group = pygame.sprite.Group()
        self.update_shoot_time = pygame.time.get_ticks()
        self.atk_cd = 540
        #animation
        self.update_animTime = pygame.time.get_ticks()
        self.anim_cd = 100

    def spawn(self,screen,player,bullet_group):
        if pygame.time.get_ticks() - self.update_time > self.spawn_cooldown:
            self.total_enemies  +=1
            self.update_time = pygame.time.get_ticks()
            if len(self.enemy_group)<30:
                self.enemy_group.add(lvl3Enemy())
        self.enemy_group.update(player,bullet_group)
        self.enemy_group.draw(screen)
        #animations for enemies
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            for e in (self.enemy_group):
                e.animate()

    def shoot(self,player,screen):
        if pygame.time.get_ticks() - self.update_shoot_time > self.atk_cd and self.enemy_shooting == False:
            self.enemy_shooting = True
            self.update_shoot_time = pygame.time.get_ticks()
            for e in self.enemy_group:
                self.enemy_bullet_group.add(Lvl3Enemy_Bullet(e.rect, player))
        self.enemy_bullet_group.update()
        self.enemy_bullet_group.draw(screen)

        if pygame.time.get_ticks() - self.update_shoot_time < self.atk_cd:
            self.enemy_shooting = False

#Enemy special atk
class Lvl3Enemy_Bullet(Sprite):
    def __init__(self,enemy_pos,player_pos):
        super().__init__()
        self.image = pygame.image.load("heart0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20,20))
        self.enemy_pos = enemy_pos
        self.rect = self.image.get_rect(midleft=(self.enemy_pos.midleft[0],self.enemy_pos.midleft[1]))
        self.player_pos = player_pos
        self.x_dist = self.player_pos.midleft[0] - self.enemy_pos.midleft[0]
        self.y_dist = self.player_pos.midleft[1] - self.enemy_pos.midleft[1]
        self.rad = math.atan2(self.y_dist, self.x_dist)
        self.dx = math.cos(self.rad)
        self.dy = math.sin(self.rad)
        self.bullet_speed = 8.3

    def update(self):
        self.rect.left += self.dx * self.bullet_speed
        self.rect.top += self.dy * self.bullet_speed
        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()




