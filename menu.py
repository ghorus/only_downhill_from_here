import pygame
from setting import *

class Texts():
    def __init__(self):
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 10
        self.curr_letter = 1
        self.howToPlayTexts = ["How to Play","A young man wants to stay true to himself,", "but is constantly pressured by society",
                "to change and conform.","A,W,S,D keys: to move", "Mouse Left-Click: to shoot","Your only weapon? Sheer willpower.", "Good luck!"]
        #next screen
        self.next_screen_cd = 0
        self.next_screen = False

    def display_Title(self,screen):
        text_size = 60
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        t = "Only DownHill From Here"
        text = font.render(t, False, "White")
        width, height = font.size(t)
        screen.blit(text, (screen_width//2 - (width//2), screen_height//6))

    def P2Play(self,screen):
        text_size = 52
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        t = "Press Space to Navigate"
        text = font.render(t, False, "White")
        width, height = font.size(t)
        screen.blit(text, (screen_width // 2 - (width // 2), screen_height - height - 50))

    def howToPlay(self,screen):
        screen.fill("white")
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        keys = pygame.key.get_pressed()
        for i,t in enumerate(self.howToPlayTexts):
            padding = 30
            if i == len(self.howToPlayTexts)-1:
                padding = 50
            text = self.howToPlayTexts[i]
            text = text[:self.curr_letter]
            text_render = font.render(text, False, "Black")
            screen.blit(text_render, (250,screen_height//4 - (-(text_size + padding) * i)))
        #text anim
        if pygame.time.get_ticks() - self.update_text_time > self.anim_cd:
            self.update_text_time = pygame.time.get_ticks()
            self.curr_letter += 1
        #next screen
        if keys[pygame.K_SPACE]:
            if self.next_screen_cd > 600:
                self.next_screen = True
        self.next_screen_cd += 10

class main_char():
    def __init__(self):
        self.spriteSheet_img = pygame.image.load('main char.png')
        self.update_time = pygame.time.get_ticks()
        self.frame_size = 180
        self.anim_cd = 700
        self.frame = 0
        self.x_pos = screen_width//2 -(self.frame_size//2)
        self.y_pos = screen_height//2 - (self.frame_size//2)

    def animate(self,screen):
        screen.blit(self.spriteSheet_img,(self.x_pos,self.y_pos),(self.frame,0,self.frame_size,self.frame_size))
        if pygame.time.get_ticks() - self.update_time > self.anim_cd:
            self.update_time = pygame.time.get_ticks()
            if self.frame == 0:
                self.frame = self.frame_size
            elif self.frame == self.frame_size:
                self.frame =0

class banker_boss():
    def __init__(self):
        self.spriteSheet_img = pygame.image.load('Banker Boss.png')
        self.update_time = pygame.time.get_ticks()
        self.anim_cd = 600
        self.frame = 0
        self.frame_size = 190
        self.x_pos = screen_width//2 + 300
        self.y_pos = screen_height // 2 - (self.frame_size//2)
    def animate(self,screen):
        screen.blit(self.spriteSheet_img,(self.x_pos,self.y_pos),(self.frame,0,self.frame_size,self.frame_size))
        if pygame.time.get_ticks() - self.update_time > self.anim_cd:
            self.update_time = pygame.time.get_ticks()
            if self.frame == 0:
                self.frame = self.frame_size
            elif self.frame == self.frame_size:
                self.frame =0


class Mom():
    def __init__(self):
        self.spriteSheet_img = pygame.image.load('mom_crying.png')
        self.update_time = pygame.time.get_ticks()
        self.frame_size = 180
        self.anim_cd = 200
        self.frame = 0
        self.x_pos = screen_width // 2 - (300 + self.frame_size)
        self.y_pos = screen_height // 2 - (self.frame_size // 2)

    def animate(self, screen):
        screen.blit(self.spriteSheet_img, (self.x_pos, self.y_pos), (self.frame, 0, self.frame_size, self.frame_size))
        if pygame.time.get_ticks() - self.update_time > self.anim_cd:
            self.update_time = pygame.time.get_ticks()
            if self.frame == 0:
                self.frame = self.frame_size
            elif self.frame == self.frame_size:
                self.frame = 0

