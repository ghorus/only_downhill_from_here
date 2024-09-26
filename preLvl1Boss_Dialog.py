import pygame
from setting import *
class Dialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 45
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["1 Year Later...","(Wakes up.....)","HOLY -. I've been asleep for a whole year???",
                          "I slept GOOD!","Like a teddy bear in hibernation..","(Knock knock knock)","This is the IRS!!",
                          "You're past overdue for $100,000!!!","Pay up!!!","(no response......)",
                          "The IRS agent is impatient and kicks down the door."]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False

    def displayTexts(self,screen):
        #key press
        self.keys = pygame.key.get_pressed()
        #text
        text_size = 30
        font = pygame.font.Font("PressStart2P.ttf", text_size)
        text = self.dialogues[self.curr_t]
        self.currentText = text
        text = text[:self.curr_letter]
        text_render = font.render(text, False, "Black")
        width, height = font.size(text)
        textHeight = screen_height//2 - height//2
        #animation
        if pygame.time.get_ticks() - self.update_text_time > self.anim_cd:
            self.update_text_time = pygame.time.get_ticks()
            self.curr_letter += 1
        # next text
        if self.keys[pygame.K_SPACE]:
            if self.curr_t == len(self.dialogues)-1:
                self.curr_letter = 1
                if self.next_text_cd > 300:
                    self.finish_dialog = True
            elif self.next_text_cd > 300:
                self.curr_letter = 1
                self.curr_t += 1
                self.next_text_cd = 0
        self.next_text_cd += 10
        if self.curr_t ==0:
            screen.blit(text_render,(screen_width//2 - width//2,textHeight))
        elif self.curr_t > 0:
            screen.blit(text_render, (screen_width // 2 - width // 2, screen_height - height - 100))

class charAnims():
    def __init__(self):
        # main char
        self.imgScaleTo = 500
        self.frame_size = self.imgScaleTo//2
        self.selected_anim = 2
        self.curr_anims = (self.imgScaleTo//2) * 4
        self.spriteSheet_img2 = pygame.image.load('main char.png')
        self.spriteSheet_img2 = pygame.transform.scale(self.spriteSheet_img2,
                                                       (self.imgScaleTo, self.curr_anims))
        # main char anim
        self.update_time = pygame.time.get_ticks()
        self.frame_size = self.imgScaleTo / 2
        self.curr_x = 0
        self.anim_cd = 500
        self.talk_animCD = 100
        self.chosen_cd = self.anim_cd
        self.frame = 0
        self.x_pos = screen_width // 2 - (self.frame_size // 2)
        self.y_pos = screen_height // 2 - (self.frame_size // 2)

        #BOSS
        self.selected_anim2 = 0
        self.imgScaleTo2 = 700
        self.curr_anims2 = (self.imgScaleTo2 // 2) * 2
        self.spriteSheet_img = pygame.image.load('Banker Boss.png')
        self.spriteSheet_img = pygame.transform.scale(self.spriteSheet_img,(self.imgScaleTo2, self.curr_anims2))
        # boss animation
        self.frame_size2 = self.imgScaleTo2 / 2
        self.curr_x2 = 0
        self.frame = 0
        # boss load on screen
        self.x_pos2 = screen_width // 2 - (self.frame_size // 2) - 400
        self.y_pos2 = screen_height // 2 - (self.frame_size // 2)

    def animate(self,screen,curr_dial):
        #MAIN CHAR
        if curr_dial.curr_t ==1:
            screen.blit(self.spriteSheet_img2, (self.x_pos, self.y_pos),
                        (self.curr_x,self.frame_size * self.selected_anim, self.frame_size,self.frame_size))
        if curr_dial.curr_t >1 and curr_dial.curr_t < 5:
            self.chosen_cd = self.talk_animCD
            self.selected_anim = 1
            screen.blit(self.spriteSheet_img2, (self.x_pos, self.y_pos),
                        (self.curr_x, self.frame_size * self.selected_anim, self.frame_size, self.frame_size))
            if pygame.time.get_ticks() - self.update_time > self.chosen_cd:
                if curr_dial.curr_letter >= len(curr_dial.currentText):
                    self.curr_x = 0
                elif self.curr_x == 0:
                    self.curr_x = self.frame_size
                elif self.curr_x == self.frame_size:
                    self.curr_x = 0
                self.update_time = pygame.time.get_ticks()
        elif  curr_dial.curr_t >= 5 and curr_dial.curr_t <= 8:
            self.curr_x = 0
            screen.blit(self.spriteSheet_img2, (self.x_pos, self.y_pos),
                        (self.curr_x, self.frame_size * self.selected_anim, self.frame_size, self.frame_size))
            # BOSS
            screen.blit(self.spriteSheet_img, (self.x_pos2, self.y_pos2),
                        (self.curr_x2, self.frame_size2 * self.selected_anim2, self.frame_size2, self.frame_size2))
            if pygame.time.get_ticks() - self.update_time > self.chosen_cd:
                if curr_dial.curr_letter >= len(curr_dial.currentText):
                    self.curr_x2 = 0
                elif self.curr_x2 == 0:
                    self.curr_x2 = self.frame_size2
                elif self.curr_x2 == self.frame_size2:
                    self.curr_x2 = 0
                self.update_time = pygame.time.get_ticks()
        elif curr_dial.curr_t > 8:
            self.curr_x = 0
            self.curr_x2 = 0
            screen.blit(self.spriteSheet_img2, (self.x_pos, self.y_pos),
                        (self.curr_x, self.frame_size * self.selected_anim, self.frame_size, self.frame_size))
            # BOSS
            screen.blit(self.spriteSheet_img, (self.x_pos2, self.y_pos2),
                        (self.curr_x2, self.frame_size2 * self.selected_anim2, self.frame_size2, self.frame_size2))

