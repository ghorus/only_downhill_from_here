import pygame
from setting import *

class preLvl2BossDialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 30
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["From months of trash, the room is airy of rot,","The stench is now so foul that it travels outside,","and the neighbors hire \"The Cleaner,\" ",
                          "the city's #1 cleaner for the worst of smells.","\"GodDANG it smells like ass in here!\"","\"Welp...at least I'm getting paid good for this..\"",
                          "\"I'm cleaning you up after I clean all this mess, buddy!\""]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False
        #Character Animation Settings
        self.scaleImgTo = 330
        self.CurrFrame = 0
        self.imgs =[pygame.image.load("Boss2Anim/boss20.png"),pygame.image.load("Boss2Anim/boss21.png")]
        self.CurrImg = self.imgs[self.CurrFrame]
        self.CurrImg = pygame.transform.scale(self.CurrImg,(self.scaleImgTo,self.scaleImgTo))
        self.updateTime = pygame.time.get_ticks()
        self.Anim_cd = 150

    def DialogAnim(self,screen):
            # key press
            self.keys = pygame.key.get_pressed()
            # text
            text_size = 25
            font = pygame.font.Font("PressStart2P.ttf", text_size)
            text = self.dialogues[self.curr_t]
            self.currentText = text
            text = text[:self.curr_letter]
            text_render = font.render(text, False, "Black")
            width, height = font.size(text)
            # animation
            if pygame.time.get_ticks() - self.update_text_time > self.anim_cd:
                self.update_text_time = pygame.time.get_ticks()
                self.curr_letter += 1
            # next text
            if self.keys[pygame.K_SPACE]:
                if self.curr_t == len(self.dialogues) - 1:
                    if self.next_text_cd > 300:
                        self.finish_dialog = True
                elif self.next_text_cd > 300:
                    self.curr_letter = 1
                    self.curr_t += 1
                    self.next_text_cd = 0
            self.next_text_cd += 10
            screen.blit(text_render,(screen_width//2-width//2,200))
            #Character Cue
            if pygame.time.get_ticks() - self.updateTime > self.Anim_cd:
                self.animate()
                self.updateTime = pygame.time.get_ticks()
            screen.blit(self.CurrImg ,(screen_width//2-self.CurrImg .get_width()//2,screen_height//2-self.CurrImg .get_height()//2))

    def animate(self):
        if self.CurrFrame == 0:
            self.CurrFrame = 1
            self.CurrImg = self.imgs[self.CurrFrame].convert_alpha()
            self.CurrImg = pygame.transform.scale(self.CurrImg, (self.scaleImgTo,self.scaleImgTo))
        else:
            self.CurrFrame = 0
            self.CurrImg  = self.imgs[self.CurrFrame].convert_alpha()
            self.CurrImg = pygame.transform.scale(self.CurrImg, (self.scaleImgTo, self.scaleImgTo))

