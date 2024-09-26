import pygame
from setting import *


class lvl1_Texts:
    def __init__(self,padding):
        #animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 45
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.mainChar_Texts = ["Another day to be lazy..." , "Hehe...", "(Looks at bank account)" ,
                               "THOUSANDS of dollars due today,", "but still not gonna pay for it!" , "Hehehehe..." ,
                               "You have so much money due today,","and you're not gonna pay it??????","What are you, nuts?????",
                               "Nahhh....No paying today." , "All this responsibility is makin' me sleepy...","Zzzzzzzzzzzzzzzzzzzzzzzz",
                               "Hey!!!!..........","The credit card desperately urges him to pay.","Looks like it's taking matters to its own hands!",
                               "This man ain't tryna pay though. He tryna sleep!!!"]
        self.dialog_box = pygame.Surface((screen_width - padding,250))
        self.dialog_box.fill("white")
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False

    def mainChar_dialogue(self, screen):
        self.keys = pygame.key.get_pressed()
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        #text
        text = self.mainChar_Texts[self.curr_t]
        self.currentText = text
        text = text[:self.curr_letter]
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        screen.blit(text_render, (screen_width // 2 - (width // 2), screen_height - 200))
        # text anim
        if pygame.time.get_ticks() - self.update_text_time > self.anim_cd:
            self.update_text_time = pygame.time.get_ticks()
            self.curr_letter += 1
        # next text
        if self.keys[pygame.K_SPACE]:
            if self.curr_t == len(self.mainChar_Texts)-1:
                self.curr_letter = 1
                if self.next_text_cd > 300:
                    self.finish_dialog = True
            elif self.next_text_cd > 300:
                self.curr_letter = 1
                self.curr_t += 1
                self.next_text_cd = 0
        self.next_text_cd += 10

class Lvl1_main_char:
    def __init__(self):
        #load img
        self.spriteSheet_img = pygame.image.load('main char.png')
        self.imgScaleTo = 500
        self.totalFrames = 4
        self.spriteSheet_img = pygame.transform.scale(self.spriteSheet_img,(self.imgScaleTo,self.imgScaleTo//2 * self.totalFrames))
        #animation
        self.update_time = pygame.time.get_ticks()
        self.frame_size = self.imgScaleTo/2
        self.curr_y = self.frame_size
        self.anim_cd = 100
        self.frame = 0
        #load on screen
        self.x_pos = screen_width // 2 - (self.frame_size // 2)
        self.y_pos = screen_height // 2 - (self.frame_size // 2)
        #dialogue
        self.padding_dialog_box = 50
        self.text = lvl1_Texts(self.padding_dialog_box)
        self.dialogue_box = self.text.dialog_box
        self.lvl1_txts = lvl1_Texts(0)
        self.card = card()

    def animate(self, screen):
        if self.lvl1_txts.curr_t >= 11:
            self.anim_cd = 150
            self.curr_y = self.frame_size * 2
        screen.blit(self.spriteSheet_img, (self.x_pos, self.y_pos),
                    (self.frame, self.curr_y, self.frame_size, self.frame_size))
        screen.blit(self.dialogue_box,(screen_width-self.dialogue_box.get_width()-self.padding_dialog_box//2,
                                       screen_height-self.dialogue_box.get_height()-self.padding_dialog_box))
        if pygame.time.get_ticks() - self.update_time > self.anim_cd:
            self.update_time = pygame.time.get_ticks()
            if self.lvl1_txts.curr_t < 6 or self.lvl1_txts.curr_t > 8 and self.lvl1_txts.curr_t < 12:
                if self.lvl1_txts.curr_letter >= len(self.lvl1_txts.currentText):
                    self.frame = 0
                elif self.frame == 0:
                    self.frame = self.frame_size
                elif self.frame == self.frame_size:
                    self.frame = 0
        self.lvl1_txts.mainChar_dialogue(screen)
        self.card.animate(screen,self.lvl1_txts)

class card():
    def __init__(self):
        self.spriteSheet_img = pygame.image.load('card.png')
        self.imgScaleTo = 500
        self.spriteSheet_img = pygame.transform.scale(self.spriteSheet_img,(self.imgScaleTo,self.imgScaleTo))
        self.update_CardTime = pygame.time.get_ticks()
        self.frame_size = self.imgScaleTo/2
        self.anim_cd = 120
        self.frame = 0
        self.x_pos = screen_width // 2 - (self.frame_size // 2) - 300
        self.y_pos = screen_height // 2 - (self.frame_size // 2)
        self.curr_y = 0

    def animate(self, screen,curr_dialog):
        if curr_dialog.curr_t >=6:
            if curr_dialog.curr_t == 12:
                self.curr_y = self.frame_size
            screen.blit(self.spriteSheet_img, (self.x_pos, self.y_pos), (self.frame, self.curr_y, self.frame_size, self.frame_size))
        if pygame.time.get_ticks() - self.update_CardTime > self.anim_cd:
            self.update_CardTime = pygame.time.get_ticks()
            if curr_dialog.curr_t >=6 and curr_dialog.curr_t <=8 or curr_dialog.curr_t ==12:
                if curr_dialog.curr_letter >= len(curr_dialog.currentText):
                    self.frame = 0
                elif self.frame == 0:
                    self.frame = self.frame_size
                elif self.frame == self.frame_size:
                    self.frame = 0






