import pygame
from pygame.sprite import Sprite
import random
import math
from setting import *

class Boss3(Sprite):
    def __init__(self):
        super().__init__()
        self.scaleImgTo = 75
        # imgs
        self.frame = 0
        self.imgs = [pygame.image.load("MomAnim/mom3.png").convert_alpha(),pygame.image.load("MomAnim/mom4.png").convert_alpha(), pygame.image.load("MomAnim/mom5.png").convert_alpha()]
        self.image = self.imgs[self.frame]
        self.image = pygame.transform.scale(self.image, (self.scaleImgTo, self.scaleImgTo))
        # spawn
        self.x_pos = random.randint(-self.image.get_width(), screen_width + self.image.get_width())
        self.y_pos = random.choices([-self.image.get_height(), screen_height + self.image.get_height()])
        self.y_pos = self.y_pos[0]
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.enemy_speed = 3
        self.health = 100
        self.died = False
        self.boss_bullet = pygame.sprite.Group()
        self.second_bullet = pygame.sprite.Group()
        #special atk
        self.boss_shooting = False
        self.atk_cd = 1000
        self.update_time = pygame.time.get_ticks()
        #2nd special atk
        self.projectile_group = pygame.sprite.Group()
        #stop cooldown
        self.walk_cd = 2000
        self.update_stop_time = pygame.time.get_ticks()
        self.stopping_cd = 0
        #dmg animation
        self.updateTime = pygame.time.get_ticks()
        self.dmgAnim = False
        self.dmgAnimCD = 0
        self.Anim_cd = 90

    def update(self,screen,player,bullet_group):
        player_vec = pygame.math.Vector2(player.center)
        boss_vec = pygame.math.Vector2(self.rect.center)
        dir = (player_vec - boss_vec).normalize()
        if pygame.time.get_ticks() - self.update_stop_time < self.walk_cd:
            self.rect.left += dir[0] * self.enemy_speed
            self.rect.top += dir[1] * self.enemy_speed
        if pygame.time.get_ticks() - self.update_stop_time > self.walk_cd:
            self.stopping_cd += 15
            if self.stopping_cd == 900:
                self.update_stop_time = pygame.time.get_ticks()
                self.stopping_cd = 0
                for x in range(-4, 5, 4):
                    if x ==-4 or x == 4:
                        for y in range(-4, 5, 4):
                            p = Projectiles(self.rect,x,y)
                            self.projectile_group.add(p)
        # animate boss
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
        text = "One Angry Mom"
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render, (screen_width // 2 - (width // 2), 20))
        # health
        for i in range(1, self.health + 1):
            health_surf = pygame.Surface((10, 15))
            screen.blit(health_surf, (screen_width // 2 - 550 + (i * health_surf.get_width()), height + 40))

    def boss_shoot(self,player,screen):
        if pygame.time.get_ticks() - self.update_time > self.atk_cd and self.boss_shooting == False:
            self.boss_shooting = True
            self.update_time = pygame.time.get_ticks()
            for i in range(1,3):
                s = Boss_Bullet(self.rect, player,i)
                self.boss_bullet.add(s)
        self.boss_bullet.update()
        self.boss_bullet.draw(screen)
        if pygame.time.get_ticks() - self.update_time < self.atk_cd:
            self.boss_shooting = False

    def circular_atk(self,screen):
        self.projectile_group.update()
        self.projectile_group.draw(screen)

    def animate(self):
        if self.frame == len(self.imgs)-1:
            self.frame = 0
            self.image = self.imgs[self.frame].convert_alpha()
        else:
            self.frame += 1
            self.image  = self.imgs[self.frame].convert_alpha()

class Boss_Bullet(Sprite):
    def __init__(self,boss_pos,player_pos,dir):
        super().__init__()
        self.image = pygame.image.load("heart0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(20,20))
        self.boss_pos = boss_pos
        self.rect = self.image.get_rect(midleft=(self.boss_pos.midleft[0],self.boss_pos.midleft[1]))
        self.player_pos = player_pos
        self.x_dist = self.player_pos.midleft[0] - self.boss_pos.midleft[0] + 0.000001
        self.y_dist = self.player_pos.midleft[1] - self.boss_pos.midleft[1] + 0.000001
        self.rad = math.atan2(self.y_dist, self.x_dist)
        self.dx = math.cos(self.rad)
        self.dy = math.sin(self.rad)
        self.bullet_speed = 11
        self.dir = dir

    def update(self):
        self.rect.left += self.dx * self.bullet_speed + self.dir
        self.rect.top += self.dy * self.bullet_speed
        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()

class Projectiles(Sprite):
    def __init__(self,boss_pos,dirx,diry):
        super().__init__()
        self.image = pygame.image.load("heart0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(90, 90))
        self.boss_pos = boss_pos
        self.rect = self.image.get_rect(midleft=(self.boss_pos.midleft[0],self.boss_pos.midleft[1]))
        self.dirx = dirx
        self.diry =diry

    def update(self):
        self.rect.left += self.dirx * 1.6
        self.rect.top += self.diry * 1.6
        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()
