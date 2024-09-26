import pygame
import math
from pygame.sprite import Sprite
from setting import *
class Player(Sprite):
    def __init__(self):
        super().__init__()
        #load img
        self.img = [pygame.image.load('mainChar_anim/mainChar4.png').convert_alpha(), pygame.image.load('mainChar_anim/mainChar5.png').convert_alpha(),
                    pygame.image.load('mainChar_anim/mainChar6.png').convert_alpha(), pygame.image.load('mainChar_anim/mainChar7.png').convert_alpha()]
        self.frame = 0
        self.frame2 = 2
        self.image = self.img[self.frame]
        #load on screen
        self.x_pos = screen_width//2
        self.y_pos = screen_height//2
        self.player = self.image.get_rect(topleft = (self.x_pos,self.y_pos))
        self.rect = self.player
        self.speed = 5
        self.fired = False
        self.bullet_group= pygame.sprite.Group()
        #animation
        self.update_animTime = pygame.time.get_ticks()
        self.anim_cd = 200
        self.run_anim_cd = 100
        self.gotHit_CD = 0
        self.invincible = False
        #dmg anim
        self.imgCopy = self.image.copy()
        self.imgCopy.fill("red",special_flags=pygame.BLEND_RGBA_MULT)
        self.dmgAnim = False
        self.dmgAnimCD = 0
        #"health" for Lvl 1
        self.dmg = 600
        self.bossDmg = 7850
        self.dues = 10000
        self.IRSdues = 100000
        # "health" for Lvl 2
        self.lvl2_dmg = 1
        self.health = 10
        self.TrashTakenOut = 10
        #"health" for lvl 3
        self.scaleHeartsTo = 200
        self.hearts = 0
        self.heartImg = pygame.image.load("heart0.png").convert_alpha()
        self.heartImg = pygame.transform.scale(self.heartImg,(self.scaleHeartsTo,self.scaleHeartsTo)).convert_alpha()
        self.heartRows = screen_width/self.scaleHeartsTo
        #health for lvl2 Boss
        self.lvl2_hearts = 10
        #health for lvl3 Boss
        self.life = 10

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.player.right += self.speed
        if keys[pygame.K_a]:
            self.player.left -=self.speed
        if keys[pygame.K_w]:
            self.player.bottom -=self.speed
        if keys[pygame.K_s]:
            self.player.top +=self.speed

    def shoot(self):
        if pygame.mouse.get_pressed()[0] and self.fired == False:
            self.fired= True
            bullet = Bullet(self.player)
            self.bullet_group.add(bullet)
        if pygame.mouse.get_pressed()[0] == False:
            self.fired= False

    def update(self, screen,enemy):
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        #animate
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate()
        #collisions, health,dmg anim
        gets_hit = pygame.sprite.spritecollide(self, enemy.enemy_group,True)
        if gets_hit and self.dmgAnim == False:
            self.dues -=self.dmg
            self.dmgAnim = True
        if self.dmgAnim == True:
            if self.dmgAnimCD <= 50:
                screen.blit(self.imgCopy,self.player)
                self.dmgAnimCD +=1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                screen.blit(self.image, self.player)
        else:
            self.dmgAnimCD = 0
            screen.blit(self.image, self.player)
        #boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

        #display health
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        text = "$" + str(self.dues)
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render,(screen_width//2-width//2,20))
    #LVL 2 ENEMY
    def updateForLvl2Enemy(self, screen,enemy,trails):
        self.image = self.img[self.frame2].convert_alpha()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        #animate
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate2()
        #collisions, health,dmg anim
        gets_hit = pygame.sprite.spritecollide(self, enemy.enemy_group,True)
        gets_hit_OtherEnemy = pygame.sprite.spritecollide(self, enemy.enemy_group2,True)
        gets_hitByTrail = pygame.sprite.spritecollide(self, trails, True)
        if gets_hit and self.dmgAnim == False or gets_hit_OtherEnemy and self.dmgAnim == False:
            self.TrashTakenOut -=self.lvl2_dmg
            self.dmgAnim = True
        if gets_hitByTrail and self.dmgAnim == False:
            self.health -=1
            self.dmgAnim = True
        if self.dmgAnim == True:
            imgCopy = self.image.copy().convert_alpha()
            imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
            if self.dmgAnimCD <= 50:
                screen.blit(imgCopy,self.player)
                self.dmgAnimCD +=1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                self.dmgAnimCD = 0
                screen.blit(self.image, self.player)
        elif self.dmgAnim ==False:
            screen.blit(self.image, self.player)
        #display health & stats
        for i in range(1,self.TrashTakenOut):
            self.TrashImg = pygame.transform.scale(pygame.image.load("TrashAnim/RedTrash5.png"), (30, 30)).convert_alpha()
            screen.blit(self.TrashImg, (30 * i, 30))
        for i in range(1,self.health + 1):
            self.heartImg = pygame.transform.scale(self.heartImg,(30,30)).convert_alpha()
            screen.blit(self.heartImg,(30 * i,65))
        #boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def updateForLvl3Enemy(self, screen,enemy):
        self.image = self.img[self.frame2].convert_alpha()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        # boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        #animate
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate2()
        #collisions, health,dmg anim
        gets_hit = pygame.sprite.spritecollide(self, enemy.enemy_group,True)
        gets_hitBy_Bullet = pygame.sprite.spritecollide(self, enemy.enemy_bullet_group,True)
        # gets_hitByTrail = pygame.sprite.spritecollide(self, trails, True)
        if gets_hit and self.dmgAnim == False or gets_hitBy_Bullet and self.dmgAnim == False:
            self.hearts += 1
            self.dmgAnim = True
        if self.dmgAnim == True:
            imgCopy = self.image.copy().convert_alpha()
            imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
            if self.dmgAnimCD <= 50:
                screen.blit(imgCopy,self.player)
                self.dmgAnimCD +=1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                self.dmgAnimCD = 0
                screen.blit(self.image, self.player)
        elif self.dmgAnim ==False:
            screen.blit(self.image, self.player)
        # #display hearts
        if self.hearts > 0:
            for h in range(self.hearts):
                screen.blit(self.heartImg,(self.heartImg.get_width() * (h%self.heartRows),(h//self.heartRows) * self.heartImg.get_height()))

    #BOSS
    def updateForBoss(self, screen,enemy):
        # boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        self.image = self.img[self.frame2].convert_alpha()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        #animate player
        if pygame.time.get_ticks() - self.update_animTime > self.run_anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate2()
        #collisions, health, damage animation
        gets_hit = pygame.Rect.colliderect(self.rect, enemy.rect)
        hitByBullet = pygame.sprite.spritecollide(self,enemy.boss_bullet,True)
        if hitByBullet and self.invincible == False:
            self.invincible = True
            self.IRSdues -=self.bossDmg
            if self.invincible == True:
                imgCopy = self.image.copy().convert_alpha()
                imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
                if self.gotHit_CD >= 100:
                    self.gotHit_CD = 0
                    self.invincible = False
                else:
                    screen.blit(imgCopy, self.player)

        else:
            screen.blit(self.image, self.player)
        if gets_hit and self.invincible == False:
            self.IRSdues -= self.bossDmg
            self.invincible = True
        if self.invincible == True:
            imgCopy = self.image.copy().convert_alpha()
            imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
            if self.gotHit_CD >= 100:
                self.gotHit_CD = 0
                self.invincible = False
            else:
                screen.blit(imgCopy, self.player)
            self.gotHit_CD += 1
        #display health
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        text = "$" + str(self.IRSdues)
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render,(screen_width//2-width//2,20))
    #BOSS 2:
    def updateForBoss2(self, screen,enemy,trails):
        self.image = self.img[self.frame2].convert_alpha()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        # boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        #animate player
        if pygame.time.get_ticks() - self.update_animTime > self.run_anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate2()
        #collisions, health, damage animation
        gets_hit = pygame.Rect.colliderect(self.rect, enemy.rect)
        if gets_hit:
            imgCopy = self.image.copy().convert_alpha()
            imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(imgCopy, self.player)
        else:
            screen.blit(self.image, self.player)
        if gets_hit and self.invincible == False:
            self.lvl2_hearts -= 1
            self.invincible = True
        if self.invincible == True:
            if self.gotHit_CD >= 100:
                self.gotHit_CD = 0
                self.invincible = False
            self.gotHit_CD +=1
        if len(trails) == 0:
            for i in range(1,self.lvl2_hearts + 1):
                heartImg = pygame.transform.scale(pygame.image.load("heart0.png").convert_alpha(), (40, 40))
                screen.blit(heartImg,(heartImg.get_width()* i,20))

    def updateForLvl3Boss(self, screen,enemy):
        self.image = self.img[self.frame2].convert_alpha()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        # boundaries
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        #animate
        if pygame.time.get_ticks() - self.update_animTime > self.anim_cd:
            self.update_animTime = pygame.time.get_ticks()
            self.animate2()
        #collisions, health,dmg anim
        gets_hitBy_Bullet = pygame.sprite.spritecollide(self, enemy.boss_bullet,True)
        gets_hitBy_SecondBullet = pygame.sprite.spritecollide(self, enemy.second_bullet,True)
        gets_hitBy_projectiles = pygame.sprite.spritecollide(self,enemy.projectile_group,True)
        if gets_hitBy_Bullet and self.dmgAnim == False or gets_hitBy_SecondBullet and self.dmgAnim == False or gets_hitBy_projectiles and self.dmgAnim == False:
            self.life -= 1
            self.dmgAnim = True
        if self.dmgAnim == True:
            imgCopy = self.image.copy().convert_alpha()
            imgCopy.fill("red", special_flags=pygame.BLEND_RGBA_MULT)
            if self.dmgAnimCD <= 50:
                screen.blit(imgCopy,self.player)
                self.dmgAnimCD +=1
            elif self.dmgAnimCD > 50:
                self.dmgAnim = False
                self.dmgAnimCD = 0
                screen.blit(self.image, self.player)
        elif self.dmgAnim ==False:
            screen.blit(self.image, self.player)
        # #display hearts
        for h in range(1,self.life+1):
            self.heartImg = pygame.transform.scale(self.heartImg,(30,30))
            screen.blit(self.heartImg,(self.heartImg.get_width() * h,10))

    #Main Character frames for certain scenes
    def animate(self):
        if self.frame == 0:
            self.frame = 1
            self.image = self.img[self.frame].convert_alpha()
        else:
            self.frame = 0
            self.image = self.img[self.frame].convert_alpha()
    def animate2(self):
        if self.frame2 == 2:
            self.frame2 = 3
            self.image = self.img[self.frame2].convert_alpha()
        else:
            self.frame2 = 2
            self.image = self.img[self.frame2].convert_alpha()

class Bullet(Sprite):
    def __init__(self,player_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.player_pos = player_pos
        self.rect = self.image.get_rect(midleft=(self.player_pos.midleft[0],self.player_pos.midleft[1]))
        self.pos = pygame.mouse.get_pos()
        self.x_dist = self.pos[0] - self.player_pos.midleft[0]
        self.y_dist = self.pos[1] - self.player_pos.midleft[1]
        self.rad = math.atan2(self.y_dist, self.x_dist)
        self.dx = math.cos(self.rad)
        self.dy = math.sin(self.rad)
        self.bullet_speed = 12

    def update(self):
        self.rect.left += self.dx * self.bullet_speed
        self.rect.top += self.dy * self.bullet_speed
        if self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0 or self.rect.left > screen_width:
            self.kill()
