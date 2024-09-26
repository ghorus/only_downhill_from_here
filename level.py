import pygame.time, pygame
from player import Player
#enemies
from enemy import Spawn_Enemy
from lvl2_enemy import Spawn_lvl2Enemy,trail_group
from lvl3_enemy import Spawn_lvl3Enemy
#bosses
from boss1 import Boss1
from boss2 import Boss2
from boss3 import Boss3
#scenes
from menu import *
from lvl1_scenes import *
from preLvl1Boss_Dialog import *
from preLvl2Dialogues import *
from pre_lvl_2_Boss_Scene import *
from preLvl3_Scene import *
from pre_lvl3_BossScene import *
from game_end import *
from gameOver import *
#scenes, menu,game over
class Intro:
    def __init__(self):
        self.text = Texts()
        self.main_char = main_char()
        self.banker_boss = banker_boss()
        self.mom = Mom()
        self.pressed_Space = False
    def run(self,screen):
        # next screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.pressed_Space == False:
            self.pressed_Space = True
        if self.pressed_Space == True:
            self.text.howToPlay(screen)
        else:
            self.text.display_Title(screen)
            self.text.P2Play(screen)
            # characters
            self.main_char.animate(screen)
            self.banker_boss.animate(screen)
            self.mom.animate(screen)
class GameOver:
    def __init__(self):
        self.gamOverScene = gameOverDialogues()
    def run(self,screen):
        self.gamOverScene.DialogAnim(screen)
class lvl1Scenes:
    def __init__(self):
        self.main_char = Lvl1_main_char()

    def run(self,screen):
        self.main_char.animate(screen)

class preLvl1Boss_Scene:
    def __init__(self):
        self.dialogs = Dialogues()
        self.anims = charAnims()
    def run(self,screen):
        self.dialogs.displayTexts(screen)
        self.anims.animate(screen,self.dialogs)

class prelvl2Scene:
    def __init__(self):
        self.dialogues = preLvl2Dialogues()
    def run(self,screen):
        self.dialogues.DialogAnim(screen)

class prelvl2BossScene():
    def __init__(self):
        self.dialogues = preLvl2BossDialogues()
    def run(self,screen):
        self.dialogues.DialogAnim(screen)

class prelvl3Scene():
    def __init__(self):
        self.dialogues = preLvl3Dialogues()
    def run(self,screen):
        self.dialogues.DialogAnim(screen)
class preLvl3BossScene():
    def __init__(self):
        self.dialogues = preLvl3BossDialogues()
    def run(self,screen):
        self.dialogues.DialogAnim(screen)
class gameEnd_Scene():
    def __init__(self):
        self.dialogues = gameEndDialogues()
    def run(self,screen):
        self.dialogues.DialogAnim(screen)

#playable levels
class Level:
    def __init__(self):
        self.player = Player()
        #enemy
        self.enemy = Spawn_Enemy()

    def run(self,screen):
        self.player.get_input()
        self.player.update(screen,self.enemy)
        self.player.shoot()
        #enemy
        self.enemy.spawn(screen,self.player.player,self.player.bullet_group)

class Level2:
    def __init__(self):
        self.player = Player()
        self.spawn_enemy = Spawn_lvl2Enemy()
        self.trails = trail_group

    def run(self,screen):
        self.player.get_input()
        self.player.updateForLvl2Enemy(screen,self.spawn_enemy,self.trails)
        self.player.shoot()
        self.spawn_enemy.spawn(screen,self.player.player,self.player.bullet_group)

class Level3:
    def __init__(self):
        self.player = Player()
        self.spawn_enemy = Spawn_lvl3Enemy()


    def run(self,screen):
        #enemies & its special atks
        self.spawn_enemy.spawn(screen,self.player.player,self.player.bullet_group)
        self.spawn_enemy.shoot(self.player.player,screen)
        #player
        self.player.get_input()
        self.player.updateForLvl3Enemy(screen, self.spawn_enemy)
        self.player.shoot()

class Boss1Level:
    def __init__(self):
        self.player = Player()
        self.boss = Boss1()
        self.update_time = pygame.time.get_ticks()
        self.special_atk_cd = 1500
    def run(self,screen):
        self.player.get_input()
        self.player.updateForBoss(screen,self.boss)
        self.player.shoot()
        #Boss
        self.boss.update(screen,self.player.player,self.player.bullet_group)
        self.boss.boss_shoot(self.player.player,screen)

class Boss2Level:
    def __init__(self):
        self.player = Player()
        self.boss = Boss2()
        self.trails = Spawn_lvl2Enemy()
    def run(self,screen):
        self.player.get_input()
        self.player.updateForBoss2(screen,self.boss,trail_group)
        self.player.shoot()
        #Boss
        self.boss.update(screen,self.player.player,self.player.bullet_group,trail_group)
        self.trails.spawnTrailsOnly(screen)

class Boss3Level:
    def __init__(self):
        self.player = Player()
        self.boss = Boss3()
    def run(self,screen):
        self.player.get_input()
        self.player.updateForLvl3Boss(screen,self.boss)
        self.player.shoot()
        #Boss
        self.boss.update(screen,self.player.player,self.player.bullet_group)
        self.boss.boss_shoot(self.player.player, screen)
        self.boss.circular_atk(screen)






