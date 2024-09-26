import pygame
from setting import *

class preLvl3BossDialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 30
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["HUNDREDS...of thousands of dollars unpaid.","Angry IRS agents...","Trash not taken out...","A man in the hospital....","Ignoring mom....",
                          "Oh boy........",".......","...........","..............","She's angry."]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False
        #Characters : IRS agent
        self.updateIRSTime = pygame.time.get_ticks()
        self.IRSAnim_cd = 85
        self.IRSCurrFrame = 0
        self.scaleIRSimgTo = 200
        self.IRSimgs = [pygame.image.load("bankerBoss_anim/BankerBoss2.png"),pygame.image.load("bankerBoss_anim/BankerBoss3.png")]
        self.IRSCurrImg = self.IRSimgs[self.IRSCurrFrame]
        #Trash
        self.BagImgs = [pygame.image.load('TrashAnim/RedTrash5.png'), pygame.image.load('TrashAnim/RedTrash6.png')]
        self.scaleTrashImgTo = 200
        self.TrashCurrFrame = 0
        self.TrashCurrImg = self.BagImgs[self.TrashCurrFrame]
        self.TrashCurrImg = pygame.transform.scale(self.TrashCurrImg,
                                                      (self.scaleTrashImgTo, self.scaleTrashImgTo))
        self.updateTrashTime = pygame.time.get_ticks()
        self.TrashAnim_cd = 260
        # cleaner
        self.cleanerImgs = [pygame.image.load('Boss2Anim/boss26.png'), pygame.image.load('Boss2Anim/boss27.png')]
        self.scaleCleanerImgTo = 200
        self.CleanerCurrFrame = 0
        self.CleanerCurrFrame2 = 2
        self.CleanerCurrImg = self.cleanerImgs[self.CleanerCurrFrame]
        self.CleanerAnim_cd = 300
        self.updateCleanerTime = pygame.time.get_ticks()
        # mom
        self.momImgs = [pygame.image.load('MomAnim/mom0.png'), pygame.image.load('MomAnim/mom1.png'),
                        pygame.image.load('MomAnim/mom2.png')]
        self.scaleMomImgTo = 200
        self.momCurrFrame = 0
        self.momCurrImg = self.momImgs[self.momCurrFrame]
        self.updateMomTime = pygame.time.get_ticks()
        self.momAnim_cd = 130
    def DialogAnim(self,screen):
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
        screen.blit(text_render, (screen_width // 2 - width // 2, screen_height//2 - height//2))

        # Character Cues/ Animations
        # IRS
        if self.curr_t >= 1 and self.curr_t <= 4:
            if pygame.time.get_ticks() - self.updateIRSTime > self.IRSAnim_cd:
                self.updateIRSTime = pygame.time.get_ticks()
                self.animateIRS()
            screen.blit(self.IRSCurrImg, (screen_width // 2 - self.IRSCurrImg.get_width() // 2,
                                         screen_height // 2 + self.IRSCurrImg.get_height() // 2))
        # Trash
        if self.curr_t >= 2 and self.curr_t <= 4:
            if pygame.time.get_ticks() - self.updateTrashTime > self.TrashAnim_cd:
                self.animateTrash()
                self.updateTrashTime = pygame.time.get_ticks()

            screen.blit(self.TrashCurrImg, (screen_width//2 + 200,
                                               screen_height // 2 + self.TrashCurrImg.get_height() // 2))
        # # Cleaner
        if self.curr_t >= 3 and self.curr_t <= 4:
            if pygame.time.get_ticks() - self.updateCleanerTime > self.CleanerAnim_cd:
                self.CleanerCurrImg = self.cleanerImgs[self.CleanerCurrFrame]
                self.animateCleaner()
                self.updateCleanerTime = pygame.time.get_ticks()
            screen.blit(self.CleanerCurrImg, (screen_width // 2 -400,
                                              screen_height // 2 + self.CleanerCurrImg.get_height() // 2))
            # mom
        if self.curr_t ==4:
            if pygame.time.get_ticks() - self.updateMomTime > self.momAnim_cd:
                self.momCurrImg = self.momImgs[self.momCurrFrame]
                self.animateMom()
                self.updateMomTime = pygame.time.get_ticks()
            screen.blit(self.momCurrImg, (screen_width // 2 - 700,
                                          screen_height // 2 + self.CleanerCurrImg.get_height() // 2))

    def animateIRS(self):
        if self.IRSCurrFrame == 0:
            self.IRSCurrFrame = 1
            self.IRSCurrImg  = self.IRSimgs[self.IRSCurrFrame]
            self.IRSCurrImg   = pygame.transform.scale(self.IRSCurrImg , (self.scaleIRSimgTo,self.scaleIRSimgTo))
        elif self.IRSCurrFrame == 1:
            self.IRSCurrFrame = 0
            self.IRSCurrImg  = self.IRSimgs[self.IRSCurrFrame]
            self.IRSCurrImg = pygame.transform.scale(self.IRSCurrImg, (self.scaleIRSimgTo, self.scaleIRSimgTo))

    def animateTrash(self):
        if self.TrashCurrFrame == 0:
            self.TrashCurrFrame = 1
            self.TrashCurrImg = self.BagImgs[self.TrashCurrFrame]
            self.TrashCurrImg = pygame.transform.scale(self.TrashCurrImg,
                                                          (self.scaleTrashImgTo, self.scaleTrashImgTo))
        elif self.TrashCurrFrame == 1:
            self.TrashCurrFrame = 0
            self.TrashCurrImg = self.BagImgs[self.TrashCurrFrame]
            self.TrashCurrImg = pygame.transform.scale(self.TrashCurrImg,
                                                          (self.scaleTrashImgTo, self.scaleTrashImgTo))

    def animateCleaner(self):
        if self.CleanerCurrFrame == 0:
            self.CleanerCurrFrame = 1
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame]
            self.CleanerCurrImg   = pygame.transform.scale(self.CleanerCurrImg, (self.scaleCleanerImgTo, self.scaleCleanerImgTo))
        elif self.CleanerCurrFrame == 1:
            self.CleanerCurrFrame = 0
            self.CleanerCurrImg  = self.cleanerImgs[self.CleanerCurrFrame]
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


