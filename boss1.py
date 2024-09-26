import pygame
from pygame.sprite import Sprite
import random
import math
from setting import *

class Boss1(Sprite):
    def __init__(self):
        super().__init__()
        self.width = 150
        self.height = 150
        self.img = [pygame.image.load("bankerBoss_anim/BankerBoss2.png"),pygame.image.load("bankerBoss_anim/BankerBoss3.png")]
        self.frame = 0
        self.image = self.img[self.frame]
        self.x_pos= random.randint(-self.width,screen_width+ self.width)
        self.y_pos = random.choices([-self.height,screen_height+self.height])
        self.y_pos = self.y_pos[0]
        self.rect = self.image.get_rect(topleft= (self.x_pos,self.y_pos))
        self.enemy_speed = 3.28
        self.health = 140
        self.died = False
        self.boss_bullet = pygame.sprite.Group()
        #special atk
        self.boss_shooting = False
        self.atk_cd = 400
        self.update_time = pygame.time.get_ticks()
        #animation, dmg anim
        self.dmgAnim = False
        self.dmgAnimCD = 0
        self.anim_cd = 100
        self.update_animTime = pygame.time.get_ticks()
        self.bulletFrame = 0
        #bullet anim
        self.anim_BulletCD = 500
        self.update_BulletanimTime = pygame.time.get_ticks()

    def update(self,screen,player,bullet_group):
        player_vec = pygame.math.Vector2(player.center)
        boss_vec = pygame.math.Vector2(self.rect.center)
        dir = (player_vec - boss_vec).normalize()
        self.rect.left += dir[0] * self.enemy_speed
        self.rect.top += dir[1] * self.enemy_speed
        #collision/dmg animation
        if pygame.sprite.spritecollide(self,bullet_group,True):
            self.health -=1
            self.dmgAnim = True
        if self.health == 0:
            self.died = True
        if self.dmgAnim == True:
            imgCopy = self.image.copy()
            imgCopy.fill("Red",special_flags=pygame.BLEND_RGBA_MULT)
            if self.dmgAnimCD <= 50:
                screen.blit(imgCopy,self.rect)
                self.dmgAnimCD +=1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                self.dmgAnimCD = 0
                screen.blit(self.image, self.rect)
        elif self.dmgAnim == False:
            screen.blit(self.image, self.rect)

        #animation
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate()
        #bullet animation
        if pygame.time.get_ticks() - self.update_BulletanimTime > self.anim_BulletCD:
            self.update_BulletanimTime = pygame.time.get_ticks()
            for e in self.boss_bullet:
                e.animateBullet()
        # boss name
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        text = "IRS Agent"
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render, (screen_width // 2 - (width // 2), screen_height - 200))
        # health
        for i in range(1, self.health + 1):
            health_surf = pygame.Surface((10, 15))
            screen.blit(health_surf, (screen_width // 2 - 750+(i*health_surf.get_width()), screen_height -130))

    def boss_shoot(self,player,screen):
        if pygame.time.get_ticks() - self.update_time > self.atk_cd and self.boss_shooting == False:
            self.boss_shooting = True
            self.update_time = pygame.time.get_ticks()
            s = Boss_Bullet(self.rect, player)
            self.boss_bullet.add(s)
        self.boss_bullet.update()
        self.boss_bullet.draw(screen)

        if pygame.time.get_ticks() - self.update_time < self.atk_cd:
            self.boss_shooting = False

    def animate(self):
        if self.frame == 0:
            self.frame =1
            self.image = self.img[self.frame]
        else:
            self.frame = 0
            self.image = self.img[self.frame]

class Boss_Bullet(Sprite):
    def __init__(self,boss_pos,player_pos):
        super().__init__()
        self.img = [pygame.image.load('BossWeaponAnim/Boss1Weapon0.png'),pygame.image.load('BossWeaponAnim/Boss1Weapon1.png'),
                    pygame.image.load('BossWeaponAnim/Boss1Weapon2.png'),pygame.image.load('BossWeaponAnim/Boss1Weapon3.png')]
        self.bulletFrame = 0
        self.image = self.img[self.bulletFrame]
        self.boss_pos = boss_pos
        self.rect = self.image.get_rect(midleft=(self.boss_pos.midleft[0],self.boss_pos.midleft[1]))
        self.player_pos = player_pos
        self.x_dist = self.player_pos.midleft[0] - self.boss_pos.midleft[0]+ 0.000001
        self.y_dist = self.player_pos.midleft[1] - self.boss_pos.midleft[1] + 0.000001
        self.rad = math.atan2(self.y_dist, self.x_dist)
        self.dx = math.cos(self.rad)
        self.dy = math.sin(self.rad)
        self.bullet_speed = 16.8

    def update(self):
        self.rect.left += self.dx * self.bullet_speed
        self.rect.top += self.dy * self.bullet_speed

        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()

    def animateBullet(self):
        if self.bulletFrame == len(self.img)-1:
            self.bulletFrame =0
            self.image = self.img[self.bulletFrame]
        else:
            self.bulletFrame +=1
            self.image = self.img[self.bulletFrame]
