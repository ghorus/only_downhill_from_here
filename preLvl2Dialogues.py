import pygame
from setting import *

class preLvl2Dialogues:
    def __init__(self):
        # animation
        self.update_text_time = pygame.time.get_ticks()
        self.anim_cd = 30
        # text
        self.curr_t = 0
        self.currentText = ""
        self.curr_letter = 1
        self.dialogues = ["Hehe..Ain't nobody paying...Hehe...","(He travels to an unknown place)",
                          "(where the IRS won't bother him ever again...)",#3 >>
                          "Month 1","Month 2","Month 3","Month 4",
                          "Month 5","Month 6","Month 7",#10 >>
                          "Pheeee -yew! Oh man, it stinks in here!","......","Oh well.",
                          "Ayyooo! Yo room stinkin' right now!","Take us out to the dumpsters, man!","He's not gonna listen....",
                          "There's only one way to handle this....","We do it ourselves!!!!","An angry trash mob forms..","..even THEY are tired of the smell."]
        # next text
        self.next_text_cd = 0
        self.finish_dialog = False
        #Characters
        self.RedTrashTalkImgs = [pygame.image.load('TrashAnim/RedTrash1.png'),pygame.image.load('TrashAnim/RedTrash2.png')]
        self.RedTrashIdleImgs = [pygame.image.load('TrashAnim/RedTrash3.png'),pygame.image.load('TrashAnim/RedTrash4.png')]
        self.RedBagImgs = [pygame.image.load('TrashAnim/RedTrash5.png'), pygame.image.load('TrashAnim/RedTrash6.png')]
        self.BlueTrashTalkImgs = [pygame.image.load('TrashAnim/BlueTrash3.png'), pygame.image.load('TrashAnim/BlueTrash4.png')]
        self.BlueTrashIdleImgs = [pygame.image.load('TrashAnim/BlueTrash1.png'), pygame.image.load('TrashAnim/BlueTrash2.png')]
        self.BlueBagImgs = [pygame.image.load('TrashAnim/BlueTrash5.png'), pygame.image.load('TrashAnim/BlueTrash6.png')]
        self.mainChar = [pygame.image.load('mainChar_anim/mainChar2.png'),pygame.image.load('mainChar_anim/mainChar3.png')]
        #Character Animation Settings
        self.scalemainCharImgTo = 330
        self.mainCharCurrFrame = 0
        self.mainCharCurrImg = self.mainChar[self.mainCharCurrFrame]
        self.mainCharCurrImg = pygame.transform.scale(self.mainCharCurrImg,(self.scalemainCharImgTo,self.scalemainCharImgTo))
        self.updateMainCharTalkTime = pygame.time.get_ticks()
        self.mainCharTalkAnim_cd = 120
        #Trash Animation Settings
            #red
        self.scaleTrashImgTo = 140
        self.RedTrashCurrFrame = 0
        self.RedTrashCurrImg = self.RedBagImgs[self.RedTrashCurrFrame]
        self.RedTrashCurrImg = pygame.transform.scale(self.RedTrashCurrImg,(self.scaleTrashImgTo,self.scaleTrashImgTo))
        self.RedupdateTrashTime = pygame.time.get_ticks()
        self.RedTrashAnim_cd = 260
            #red talking
        self.RedTalkCurrFrame = 0
        self.RedTalkingCurrImg = self.RedTrashTalkImgs[self.RedTalkCurrFrame]
        self.RedupdateTrashTalkTime = pygame.time.get_ticks()
        self.RedTrashAnim_cd = 130
            #blue
        self.BlueTrashCurrFrame = 0
        self.BlueTrashCurrImg = self.BlueBagImgs[self.BlueTrashCurrFrame]
        self.BlueTrashAnim_cd = 600
        self.BlueupdateTrashTime = pygame.time.get_ticks()
            #blue talking
        self.BlueTalkCurrFrame = 0
        self.BlueTalkingCurrImg = self.BlueTrashTalkImgs[self.BlueTalkCurrFrame]
        self.BlueupdateTrashTalkTime = pygame.time.get_ticks()
        self.BlueTrashAnim_cd = 130
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
            screen.blit(text_render,(screen_width//2-width//2,200))
            #Character Cues
            #main char
            if pygame.time.get_ticks() - self.updateMainCharTalkTime > self.mainCharTalkAnim_cd:
                if self.curr_t == 0 or self.curr_t >10 and self.curr_t<=12:
                    if self.curr_letter >= len(self.dialogues[self.curr_t]):
                        pass
                    else:
                        self.animateMainChar()
                        self.updateMainCharTalkTime = pygame.time.get_ticks()
            screen.blit(self.mainCharCurrImg ,(screen_width//2-self.mainCharCurrImg .get_width()//2,screen_height//2-self.mainCharCurrImg .get_height()//2))
            #Trash bags
            #red bags animation
            if self.curr_t >= 3 and self.curr_t <= 9:
                if pygame.time.get_ticks() - self.RedupdateTrashTime > self.RedTrashAnim_cd:
                    self.animateRedTrashBag()
                    self.RedupdateTrashTime = pygame.time.get_ticks()
                if pygame.time.get_ticks() - self.BlueupdateTrashTime > self.BlueTrashAnim_cd:
                    self.animateBlueTrashBag()
                    self.BlueupdateTrashTime = pygame.time.get_ticks()
                for i in range(1,self.curr_t - 1):
                    if i % 2 == 1:
                        screen.blit(self.RedTrashCurrImg ,(i * 85,screen_height//2+self.mainCharCurrImg.get_height()//2 - self.RedTrashCurrImg.get_height()))
                    if i % 2 == 0:
                        screen.blit(self.BlueTrashCurrImg, (i * 85,
                                                           screen_height // 2 + self.mainCharCurrImg.get_height() // 2 - self.RedTrashCurrImg.get_height()))
            #Talking Bags Come In
            if self.curr_t >= 10:
                #no dialogue bags
                if pygame.time.get_ticks() - self.RedupdateTrashTime > self.RedTrashAnim_cd:
                    self.animateRedTrashBag()
                    self.RedupdateTrashTime = pygame.time.get_ticks()
                if pygame.time.get_ticks() - self.BlueupdateTrashTime > self.BlueTrashAnim_cd:
                    self.animateBlueTrashBag()
                    self.BlueupdateTrashTime = pygame.time.get_ticks()
                for i in range(1,8):
                    if i % 2 == 1:
                        screen.blit(self.RedTrashCurrImg ,(i * 85,screen_height//2+self.mainCharCurrImg.get_height()//2 - self.RedTrashCurrImg.get_height()))
                    if i % 2 == 0:
                        screen.blit(self.BlueTrashCurrImg, (i * 85,
                                                           screen_height // 2 + self.mainCharCurrImg.get_height() // 2 - self.RedTrashCurrImg.get_height()))
                #Talking Red Bag
                if pygame.time.get_ticks() - self.RedupdateTrashTalkTime > self.RedTrashAnim_cd:
                    if self.curr_letter >= len(self.dialogues[self.curr_t]) or self.curr_t >10 and self.curr_t <13 or self.curr_t > 14:
                        pass
                    else:
                        self.animateTalkingRedTrashBag()
                        self.RedupdateTrashTalkTime = pygame.time.get_ticks()
                screen.blit(self.RedTalkingCurrImg, ( 9*85,
                                                    screen_height // 2 + self.mainCharCurrImg.get_height() // 2 - self.RedTrashCurrImg.get_height()))
                # Talking Blue Bag
            if self.curr_t >= 15:
                if pygame.time.get_ticks() - self.BlueupdateTrashTalkTime > self.BlueTrashAnim_cd:
                    if self.curr_letter >= len(self.dialogues[self.curr_t]) or self.curr_t > 17:
                        pass
                    else:
                        self.animateTalkingBlueTrashBag()
                        self.BlueupdateTrashTalkTime = pygame.time.get_ticks()
                screen.blit(self.BlueTalkingCurrImg, (10 * 85,
                                                     screen_height // 2 + self.mainCharCurrImg.get_height() // 2 - self.BlueTrashCurrImg.get_height()))



    def animateMainChar(self):
        if self.mainCharCurrFrame == 0:
            self.mainCharCurrFrame = 1
            self.mainCharCurrImg = self.mainChar[self.mainCharCurrFrame]
            self.mainCharCurrImg = pygame.transform.scale(self.mainCharCurrImg, (self.scalemainCharImgTo,self.scalemainCharImgTo))
        else:
            self.mainCharCurrFrame = 0
            self.mainCharCurrImg  = self.mainChar[self.mainCharCurrFrame]
            self.mainCharCurrImg = pygame.transform.scale(self.mainCharCurrImg, (self.scalemainCharImgTo, self.scalemainCharImgTo))


    def animateRedTrashBag(self):
        if self.RedTrashCurrFrame == 0:
            self.RedTrashCurrFrame = 1
            self.RedTrashCurrImg  = self.RedBagImgs[self.RedTrashCurrFrame]
            self.RedTrashCurrImg  = pygame.transform.scale(self.RedTrashCurrImg, (self.scaleTrashImgTo,self.scaleTrashImgTo))
        elif self.RedTrashCurrFrame == 1:
            self.RedTrashCurrFrame = 0
            self.RedTrashCurrImg  = self.RedBagImgs[self.RedTrashCurrFrame]
            self.RedTrashCurrImg = pygame.transform.scale(self.RedTrashCurrImg, (self.scaleTrashImgTo, self.scaleTrashImgTo))
    def animateTalkingRedTrashBag(self):
        if self.RedTalkCurrFrame == 0:
            self.RedTalkCurrFrame = 1
            self.RedTalkingCurrImg  =  self.RedTrashTalkImgs[self.RedTalkCurrFrame]
            self.RedTalkingCurrImg  = pygame.transform.scale(self.RedTalkingCurrImg, (self.scaleTrashImgTo,self.scaleTrashImgTo))
        elif self.RedTalkCurrFrame == 1:
            self.RedTalkCurrFrame = 0
            self.RedTalkingCurrImg  =  self.RedTrashTalkImgs[self.RedTalkCurrFrame]
            self.RedTalkingCurrImg = pygame.transform.scale(self.RedTalkingCurrImg, (self.scaleTrashImgTo, self.scaleTrashImgTo))

    def animateBlueTrashBag(self):
        if self.BlueTrashCurrFrame == 0:
            self.BlueTrashCurrFrame = 1
            self.BlueTrashCurrImg  = self.BlueBagImgs[self.BlueTrashCurrFrame]
            self.BlueTrashCurrImg   = pygame.transform.scale( self.BlueTrashCurrImg, (self.scaleTrashImgTo,self.scaleTrashImgTo))
        elif self.BlueTrashCurrFrame == 1:
            self.BlueTrashCurrFrame = 0
            self.BlueTrashCurrImg  = self.BlueBagImgs[self.BlueTrashCurrFrame]
            self.BlueTrashCurrImg  = pygame.transform.scale( self.BlueTrashCurrImg, (self.scaleTrashImgTo, self.scaleTrashImgTo))
    def animateTalkingBlueTrashBag(self):
        if self.BlueTalkCurrFrame == 0:
            self.BlueTalkCurrFrame = 1
            self.BlueTalkingCurrImg  = self.BlueTrashTalkImgs[self.BlueTalkCurrFrame]
            self.BlueTalkingCurrImg   = pygame.transform.scale(self.BlueTalkingCurrImg, (self.scaleTrashImgTo,self.scaleTrashImgTo))
        elif self.BlueTalkCurrFrame == 1:
            self.BlueTalkCurrFrame = 0
            self.BlueTalkingCurrImg   = self.BlueTrashTalkImgs[self.BlueTalkCurrFrame]
            self.BlueTalkingCurrImg = pygame.transform.scale(self.BlueTalkingCurrImg, (self.scaleTrashImgTo, self.scaleTrashImgTo))


