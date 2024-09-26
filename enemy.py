import pygame
from pygame.sprite import Sprite
import random
from setting import *

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        #load img
        self.imgScaleTo = 60
        self.img = [pygame.image.load('card_anim/card2.png'),pygame.image.load('card_anim/card3.png')]
        self.frame = 0
        self.image = pygame.transform.scale(self.img[self.frame],(self.imgScaleTo,self.imgScaleTo))
        #enemy spawn
        self.x_pos = random.randint(-self.imgScaleTo, screen_width + self.imgScaleTo//2)
        self.y_pos = random.choices([-self.imgScaleTo,screen_height+self.imgScaleTo//2])
        self.y_pos = self.y_pos[0]
        self.rect = self.image.get_rect(topleft= (self.x_pos,self.y_pos))
        self.enemy_speed = 2.8
        self.health = 1

    def update(self,player,bullet_group):
        player_vec = pygame.math.Vector2(player.center)
        enemy_vec = pygame.math.Vector2(self.rect.center)
        dir = (player_vec - enemy_vec).normalize()
        self.rect.left += dir[0] * self.enemy_speed
        self.rect.top += dir[1] * self.enemy_speed
        #collision
        if pygame.sprite.spritecollide(self,bullet_group,True):
            self.health -=1
        if self.health == 0:
            self.kill()

    def animate(self):
        if self.frame == 0:
            self.frame = 1
            self.image = self.img[self.frame]
        else:
            self.frame = 0
            self.image = self.img[self.frame]
class Spawn_Enemy():
    def __init__(self):
        self.update_time = pygame.time.get_ticks()
        self.enemy_group = pygame.sprite.Group()
        self.spawn_cooldown = 300
        self.total_enemies = 0
        # animation
        self.update_animTime = pygame.time.get_ticks()
        self.anim_cd = 200

    def spawn(self,screen,player,bullet_group):
        if pygame.time.get_ticks() - self.update_time > self.spawn_cooldown:
            self.total_enemies  +=1
            self.update_time = pygame.time.get_ticks()
            if len(self.enemy_group)<30:
                self.enemy_group.add(Enemy())
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            for e in self.enemy_group:
                e.animate()
        self.enemy_group.update(player,bullet_group)
        self.enemy_group.draw(screen)
