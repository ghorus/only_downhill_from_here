import pygame
from setting import *

class gameOverDialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 30
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["Whatchu tryna do..?","Be responsible???"]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False

    def DialogAnim(self, screen):
        # key press
        self.keys = pygame.key.get_pressed()
        # text
        text_size = 30
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
        screen.blit(text_render, (screen_width // 2 - width // 2, screen_height // 2 - height // 2))


