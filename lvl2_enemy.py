import pygame
from pygame.sprite import Sprite
import random
from setting import *

trail_group = pygame.sprite.Group()
class lvl2Enemy(Sprite):
    def __init__(self):
        super().__init__()
        #special atk
        self.update_time = pygame.time.get_ticks()
        self.atk_cd = 2100
        self.spawn_trail = False
        #Animation Imgs
        self.Blueframe = 0
        self.BlueImgs = [pygame.image.load("TrashAnim/BlueTrash1.png").convert_alpha(),pygame.image.load("TrashAnim/BlueTrash2.png").convert_alpha()]
        self.Redframe = 0
        self.RedImgs = [pygame.image.load("TrashAnim/RedTrash3.png").convert_alpha(), pygame.image.load("TrashAnim/RedTrash4.png").convert_alpha()]
        #Health/DMG
        self.width = 30
        self.height = 30
        self.image = self.BlueImgs[self.Blueframe]
        self.x_pos = random.randint(-self.image.get_width(), screen_width + self.image.get_width())
        self.y_pos = random.choices([-self.image.get_height(), screen_height + self.image.get_height()])
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos[0]))
        self.enemy_speed = 3.2
        self.health = 1

    def update(self,player,bullet_groups,screen):
        player_vec = pygame.math.Vector2(player.center)
        enemy_vec = pygame.math.Vector2(self.rect.center)
        dir = (player_vec - enemy_vec).normalize()
        self.rect.left += dir[0] * self.enemy_speed
        self.rect.top += dir[1] * self.enemy_speed

        if pygame.sprite.spritecollide(self,bullet_groups,True):
            self.health -=1
        if self.health == 0:
            self.kill()

        if pygame.time.get_ticks() - self.update_time > self.atk_cd and self.spawn_trail == False:
            self.spawn_trail = True
            self.update_time = pygame.time.get_ticks()
            turd = Turd_Trail(self.rect)
            trail_group.add(turd)

        if pygame.time.get_ticks() - self.update_time < self.atk_cd:
            self.spawn_trail = False

    def Blueanimate(self):
        if self.Blueframe == 0:
            self.Blueframe = 1
            self.image = self.BlueImgs[self.Blueframe].convert_alpha()
        else:
            self.Blueframe = 0
            self.image = self.BlueImgs[self.Blueframe].convert_alpha()

    def Redanimate(self):
        if self.Redframe == 0:
            self.Redframe = 1
            self.image = self.RedImgs[self.Redframe].convert_alpha()
        else:
            self.Redframe = 0
            self.image = self.RedImgs[self.Redframe].convert_alpha()



class Turd_Trail(Sprite):
    def __init__(self,trash_pos):
        super().__init__()
        self.frame = 0
        self.imgs = [pygame.image.load("TrashAnim/Poop1.png").convert_alpha(),pygame.image.load("TrashAnim/Poop2.png").convert_alpha()]
        self.image = self.imgs[self.frame].convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.trash_pos = trash_pos
        self.rect = self.image.get_rect(midleft=(self.trash_pos.midleft[0],self.trash_pos.midleft[1]))

    def animatePoop(self):
        if self.frame == 0:
            self.frame = 1
            self.image = self.imgs[self.frame].convert_alpha()
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        else:
            self.frame = 0
            self.image = self.imgs[self.frame].convert_alpha()
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()

    def update(self):
        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()

class Spawn_lvl2Enemy():
    def __init__(self):
        self.update_time = pygame.time.get_ticks()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group2 = pygame.sprite.Group()
        self.spawn_cooldown = 755
        self.total_enemies= 1
        #animation
        self.update_animTime = pygame.time.get_ticks()
        self.anim_cd = 200
    def spawn(self,screen,player,bullet_group):
        global trail_group
        if pygame.time.get_ticks() - self.update_time > self.spawn_cooldown:
            self.total_enemies  +=1
            self.update_time = pygame.time.get_ticks()
            if len(self.enemy_group)<10:
                self.enemy_group.add(lvl2Enemy())
                self.enemy_group2.add(lvl2Enemy())

        #animation
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            for e in self.enemy_group:
                e.Blueanimate()
            for e in self.enemy_group2:
                e.Redanimate()
            for p in trail_group:
                p.animatePoop()
        self.enemy_group.update(player,bullet_group,screen)
        self.enemy_group.draw(screen)
        self.enemy_group2.update(player, bullet_group, screen)
        self.enemy_group2.draw(screen)
        trail_group.update()
        trail_group.draw(screen)

    def spawnTrailsOnly(self,screen):
        global trail_group
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            for p in trail_group:
                p.animatePoop()
        trail_group.update()
        trail_group.draw(screen)

