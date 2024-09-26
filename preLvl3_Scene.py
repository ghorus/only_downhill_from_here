import pygame
from setting import *

class preLvl3Dialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 30
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["Breaking News!","....","A man's room smells so bad,",#2 - 3
                          "\"The Cleaner\" was called in, but","he is now in the","hospital after altercations", # 5- 7
                          "with the man...","Who can stop him??", #8 -10
                          "We have report that,","the man's mom is","now at the scene!","\"Honey! Why are you doing","this to yourself??\"",
                          "\"I'm coming in there","to save you from yourself!!\"","\"It's for your own good!!\"","\"I don't need your love!!\""]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False
        #Characters
        self.momImgs = [pygame.image.load('MomAnim/mom0.png'),pygame.image.load('MomAnim/mom1.png'),pygame.image.load('MomAnim/mom2.png')]
        self.cleanerImgs = [pygame.image.load('Boss2Anim/boss20.png'),pygame.image.load('Boss2Anim/boss21.png'), pygame.image.load('Boss2Anim/boss26.png'),
                            pygame.image.load('Boss2Anim/boss27.png')]
        self.tvImgs = [pygame.image.load('tvAnim/tv0.png'), pygame.image.load('tvAnim/tv1.png')]
        self.scalemainCharImgTo = 150
        self.mainCharCurrFrame = 0
        self.mainCharImgs = [pygame.image.load('mainChar_anim/mainChar2.png'),pygame.image.load('mainChar_anim/mainChar6.png')]
        self.mainChar = self.mainCharImgs[self.mainCharCurrFrame]
        self.mainChar = pygame.transform.scale(self.mainChar, (self.scalemainCharImgTo, self.scalemainCharImgTo))
        #Character Animation Settings
        self.updateMainCharTalkTime = pygame.time.get_ticks()
        self.mainCharTalkAnim_cd = 120
            #tv
        self.scaleTVImgTo = 950
        self.TVCurrFrame = 0
        self.TVCurrImg = self.tvImgs[self.TVCurrFrame]
        self.TVCurrImg = pygame.transform.scale(self.TVCurrImg,(self.scaleTVImgTo,self.scaleTVImgTo))
        self.updateTVTime = pygame.time.get_ticks()
        self.TVAnim_cd = 1780
            #mom
        self.scaleMomImgTo = 160
        self.momCurrFrame = 0
        self.momCurrImg = self.momImgs[self.momCurrFrame]
        self.updateMomTime = pygame.time.get_ticks()
        self.momAnim_cd = 130
            #cleaner
        self.scaleCleanerImgTo = 150
        self.CleanerCurrFrame = 0
        self.CleanerCurrFrame2 = 2
        self.CleanerCurrImg = self.cleanerImgs[self.CleanerCurrFrame]
        self.CleanerAnim_cd = 300
        self.updateCleanerTime = pygame.time.get_ticks()

    def DialogAnim(self,screen):
        # key press
        self.keys = pygame.key.get_pressed()
        # text
        text_size = 15
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
        #Character Cues/ Animations
            #TV
        if pygame.time.get_ticks() - self.updateTVTime > self.TVAnim_cd:
            self.updateTVTime = pygame.time.get_ticks()
            self.animateTV()
        screen.blit(self.TVCurrImg ,(screen_width//2-self.TVCurrImg.get_width()//2 + 70,screen_height//2-self.TVCurrImg.get_height()//2))
            #Cleaner
        if self.curr_t ==2:
            screen.blit(self.mainChar,(screen_width//2-self.mainChar.get_width()//2,screen_height//2-self.mainChar.get_height()//2))
        if self.curr_t >= 3 and self.curr_t <= 4:
            if pygame.time.get_ticks() - self.updateCleanerTime > self.CleanerAnim_cd:
                self.animateCleaner()
                self.updateCleanerTime = pygame.time.get_ticks()
            screen.blit(self.CleanerCurrImg,(screen_width//2 - self.CleanerCurrImg.get_width()//2,screen_height//2-self.CleanerCurrImg.get_height()//2))
        if self.curr_t >=5 and self.curr_t <=8:
            if pygame.time.get_ticks() - self.updateCleanerTime > self.CleanerAnim_cd:
                self.CleanerCurrImg = self.cleanerImgs[self.CleanerCurrFrame]
                self.animateXXCleaner()
                self.updateCleanerTime = pygame.time.get_ticks()
            screen.blit(self.CleanerCurrImg,(screen_width//2 - self.CleanerCurrImg.get_width()//2,screen_height//2-self.CleanerCurrImg.get_height()//2))
            #mom
        if self.curr_t >= 9 and self.curr_t <= 10:
            screen.blit(self.momCurrImg,(screen_width//2-self.momCurrImg.get_width()//2,screen_height//2-self.momCurrImg.get_height()//2))
        if self.curr_t >= 11 and self.curr_t <= 15:
            if pygame.time.get_ticks() - self.updateMomTime > self.momAnim_cd:
                self.momCurrImg = self.momImgs[self.momCurrFrame]
                self.animateMom()
                self.updateMomTime = pygame.time.get_ticks()
            screen.blit(self.momCurrImg, (screen_width // 2 - self.CleanerCurrImg.get_width() // 2,
                                              screen_height // 2 - self.CleanerCurrImg.get_height() // 2))
            #text
        if self.curr_t == 16:
            self.mainChar = self.mainCharImgs[1]
            self.mainChar = pygame.transform.scale(self.mainChar,(self.scalemainCharImgTo,self.scalemainCharImgTo))
            screen.blit(self.mainChar,(screen_width//2-self.mainChar.get_width()//2,screen_height//2-self.mainChar.get_height()//2))
        screen.blit(text_render, (screen_width // 2 - width // 2, 300))

    def animateTV(self):
        if self.TVCurrFrame == 0:
            self.TVCurrFrame = 1
            self.TVCurrImg  = self.tvImgs[self.TVCurrFrame]
            self.TVCurrImg   = pygame.transform.scale(self.TVCurrImg , (self.scaleTVImgTo,self.scaleTVImgTo))
        elif self.TVCurrFrame == 1:
            self.TVCurrFrame = 0
            self.TVCurrImg  = self.tvImgs[self.TVCurrFrame]
            self.TVCurrImg = pygame.transform.scale(self.TVCurrImg, (self.scaleTVImgTo, self.scaleTVImgTo))

    def animateCleaner(self):
        if self.CleanerCurrFrame == 0:
            self.CleanerCurrFrame = 1
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame]
            self.CleanerCurrImg   = pygame.transform.scale(self.CleanerCurrImg, (self.scaleCleanerImgTo, self.scaleCleanerImgTo))
        elif self.CleanerCurrFrame == 1:
            self.CleanerCurrFrame = 0
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame]
            self.CleanerCurrImg  = pygame.transform.scale(self.CleanerCurrImg, (self.scaleCleanerImgTo, self.scaleCleanerImgTo))
    def animateXXCleaner(self):
        if self.CleanerCurrFrame2 == 2:
            self.CleanerCurrFrame2 = 3
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame2]
            self.CleanerCurrImg  = pygame.transform.scale(self.CleanerCurrImg, (self.scaleCleanerImgTo, self.scaleCleanerImgTo))
        elif self.CleanerCurrFrame2 == 3:
            self.CleanerCurrFrame2 = 2
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame2]
            self.CleanerCurrImg  = pygame.transform.scale(self.CleanerCurrImg, (self.scaleCleanerImgTo, self.scaleCleanerImgTo))

    def animateMom(self):
        if self.momCurrFrame == len(self.momImgs)-1:
            self.momCurrFrame = 0
            self.momCurrImg  = self.momImgs[self.momCurrFrame]
            self.momCurrImg   = pygame.transform.scale(self.momCurrImg, (self.scaleMomImgTo, self.scaleMomImgTo))
        else:
            self.momCurrFrame += 1
            self.momCurrImg  = self.momImgs[self.momCurrFrame]
            self.momCurrImg  = pygame.transform.scale(self.momCurrImg, (self.scaleMomImgTo, self.scaleMomImgTo))
