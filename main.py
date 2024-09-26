import sys, asyncio
from level import *
from pygame import mixer
#game setup
pygame.mixer.pre_init(32000,16,2,3800)
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
#scenes
MainMenu = Intro()
gameover = GameOver()
lvl1Scenes = lvl1Scenes()
prelvl1BossScene = preLvl1Boss_Scene()
prelvl2Scene = prelvl2Scene()
prelvl2BossScene = prelvl2BossScene()
prelvl3 = prelvl3Scene()
prelvl3BossScene = preLvl3BossScene()
gameEndScene = gameEnd_Scene()
#levels
level = Level()
level2 = Level2()
level3 = Level3()
#bosses
boss1 = Boss1Level()
boss2 = Boss2Level()
boss3 = Boss3Level()

class GameState():
    def __init__(self):
        self.state = "intro"
        self.pressed = False
        self.last_state = ""
        self.keys = pygame.key.get_pressed()
        #background music
        self.sound = pygame.mixer.Sound("soundtracks/Sweet Crazy.WAV")
        self.sound.set_volume(1)
        self.last_song = ""
        self.last_volume = 0

    #Scenes
    def intro(self):
        screen.fill((140,2,239))
        MainMenu.run(screen)
        self.sound.play(-1)
        if MainMenu.text.next_screen == True:
            self.state = "lvl1_scenes"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def game_over(self):
        self.sound.play(-1)
        screen.fill((230,230,0))
        gameover.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        #load last game
        if gameover.gamOverScene.finish_dialog == True:
            self.state = self.last_state
            self.sound.stop()
            self.sound = pygame.mixer.Sound(self.last_song)
            self.sound.set_volume(self.last_volume)


    def gameEnd(self):
        self.sound.play(-1)
        screen.fill((125,200,220))
        gameEndScene.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    def lvl1_scenes(self):
        screen.fill((102,0,204))
        lvl1Scenes.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        if lvl1Scenes.main_char.lvl1_txts.finish_dialog ==True:
            self.state = "lvl_1"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Fire in the Hole.mp3")
            self.sound.set_volume(0.1)

    def prelvl1_bossScene(self):
        self.sound.play(-1)
        screen.fill("orange")
        prelvl1BossScene.run(screen)
        if prelvl1BossScene.dialogs.finish_dialog == True:
            self.state = "lvl_1_boss"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/The Apparition.mp3")
            self.sound.set_volume(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def preLvl2Scene(self):
        self.sound.play(-1)
        screen.fill((164,238,255))
        prelvl2Scene.run(screen)
        if prelvl2Scene.dialogues.finish_dialog == True:
            self.state = "lvl2"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Rivaling Force.mp3")
            self.sound.set_volume(0.06)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    def preLvl2BossScene(self):
        self.sound.play(-1)
        screen.fill("pink")
        prelvl2BossScene.run(screen)
        if prelvl2BossScene.dialogues.finish_dialog == True:
            self.state = "lvl2_boss"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    def prelvl3Scene(self):
        self.sound.play(-1)
        screen.fill("gray")
        prelvl3.run(screen)
        if prelvl3.dialogues.finish_dialog == True:
            self.state = "lvl3"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Coffee Break.mp3")
            self.sound.set_volume(0.06)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def prelvl3Boss(self):
        screen.fill((120,220,240))
        prelvl3BossScene.run(screen)
        if prelvl3BossScene.dialogues.finish_dialog == True:
            self.state = 'lvl3_boss'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    #Playable levels
    def lvl_1(self):
        self.sound.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("white")
        level.run(screen)
        pygame.display.update()

        if level.enemy.total_enemies == 195:
            self.state ='prelvl1_bossScene'
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Sure Forever.WAV")
            self.sound.set_volume(0.6)
        elif level.player.dues <= 0:
            self.state = "gameOver"
            self.last_state = "lvl_1"
            level.enemy.total_enemies = 0
            level.player.dues = 10000
            #sound
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_volume = 0.1
            self.last_song = "soundtracks/Fire in the Hole.mp3"

    def lvl_2(self):
        self.sound.play(-1)
        screen.fill("white")
        level2.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        if level2.spawn_enemy.total_enemies == 95:
            for remaining_enemies in level2.spawn_enemy.enemy_group:
                remaining_enemies.kill()
            self.state = "preLvl2Boss"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Against All Odds.mp3")
            self.sound.set_volume(0.06)
        elif level2.player.health == 0 or level2.player.TrashTakenOut == 0:
            self.last_state = "lvl2"
            level2.spawn_enemy.total_enemies = 0
            level2.player.health = 10
            level2.player.TrashTakenOut = 10
            for remaining_enemies in level2.spawn_enemy.enemy_group:
                remaining_enemies.kill()
            for remaining_enemies in level2.spawn_enemy.enemy_group2:
                remaining_enemies.kill()
            for t in trail_group:
                t.kill()
            self.state = "gameOver"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_volume = 0.06
            self.last_song = "soundtracks/Rivaling Force.mp3"

    def lvl3(self):
        self.sound.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        screen.fill("white")
        level3.run(screen)
        if level3.spawn_enemy.total_enemies == 115:
            for remaining_enemies in level3.spawn_enemy.enemy_group:
                remaining_enemies.kill()
            self.state = "prelvl3Boss"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Ex Machina.mp3")
            self.sound.set_volume(0.06)
        elif level3.player.hearts == 32:
            level3.spawn_enemy.total_enemies = 0
            level3.player.hearts = 0
            for remaining in level3.spawn_enemy.enemy_group:
                remaining.kill()
            for remaining in level3.spawn_enemy.enemy_bullet_group:
                remaining.kill()
            self.last_state = "lvl3"
            self.state = "gameOver"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_volume = 0.06
            self.last_song = "soundtracks/Coffee Break.mp3"
    #Bosses
    def lvl_1_boss(self):
        self.sound.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("white")
        boss1.run(screen)
        if boss1.boss.died == True:
            self.state = "preLvl2Scene"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Bounty Hunter.mp3")
            self.sound.set_volume(0.06)
        elif boss1.player.IRSdues <= 0:
            self.state = "gameOver"
            self.last_state = "lvl_1_boss"
            boss1.player.IRSdues = 100000
            boss1.boss.health = 100
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_volume = 0.1
            self.last_song = "soundtracks/The Apparition.mp3"
        pygame.display.update()

    def lvl2_boss(self):
        self.sound.play(-1)
        global trail_group
        screen.fill("white")
        boss2.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if boss2.boss.died == True:
            self.state = "prelvl3Scene"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Stray Cat.mp3")
            self.sound.set_volume(0.06)
        elif boss2.player.lvl2_hearts == 0:
            boss2.player.lvl2_hearts = 10
            boss2.boss.health = 120
            self.last_state = "lvl2_boss"
            self.state = "gameOver"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_volume = 0.06
            self.last_song = "soundtracks/Against All Odds.mp3"
        pygame.display.update()

    def lvl3_boss(self):
        self.sound.play(-1)
        screen.fill("white")
        boss3.run(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if boss3.boss.died == True:
            self.state = "gameEnd"
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Thought Soup.mp3")
            self.sound.set_volume(0.06)
        elif boss3.player.life == 0:
            self.sound.stop()
            self.sound = pygame.mixer.Sound("soundtracks/Null and Void.mp3")
            self.sound.set_volume(0.1)
            self.last_state = "lvl3_boss"
            self.state = "gameOver"
            self.last_song ="soundtracks/Ex Machina.mp3"
            self.last_volume = 0.06
            boss3.boss.health = 100
            boss3.player.life = 10
        pygame.display.update()

    def state_manager(self):
        #scenes
        if self.state == 'intro':
            self.intro()
        if self.state =='lvl1_scenes':
            self.lvl1_scenes()
        if self.state =='prelvl1_bossScene':
            self.prelvl1_bossScene()
        if self.state =="preLvl2Scene":
            self.preLvl2Scene()
        if self.state == "preLvl2Boss":
            self.preLvl2BossScene()
        if self.state == "prelvl3Scene":
            self.prelvl3Scene()
        if self.state == "prelvl3Boss":
            self.prelvl3Boss()
        if self.state == "gameEnd":
            self.gameEnd()
        #playable levels
        if self.state =='lvl_1':
            self.lvl_1()
        if self.state == 'lvl2':
            self.lvl_2()
        if self.state == 'lvl3':
            self.lvl3()
        #bosses
        if self.state == 'lvl_1_boss':
            self.lvl_1_boss()
        if self.state =='lvl2_boss':
            self.lvl2_boss()
        if self.state =='lvl3_boss':
            self.lvl3_boss()
        if self.state =='gameOver':
            self.game_over()

game_state = GameState()
# async def main():
while True:
    game_state.state_manager()
    clock.tick(200)
        # await asyncio.sleep(0)

#
# app = main()
# asyncio.run(app)
