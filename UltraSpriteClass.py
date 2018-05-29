import pygame
import math
from BaseClass import BaseClass
from Vector2D import Vector2D
from RectClass import RectClass
from SpriteClass import SpriteClass


class UltraSpriteClass(SpriteClass):
    def __init__(self, position, width, height, img, vel, accel, id, isTest = True):
        super(UltraSpriteClass, self).__init__(position, width, height, img, vel, accel, id, isTest) 
        self.isRunning = False
        self.row = 0
        self.MARGIN = 2
        self.IMG_W = 28
        self.StateOfAnimation = 0
        self.frame = 0
        self.frame_timer = 0
        self.FRAME_TIME = 100
        self.FRAME_CT = 6
        self.TranslatedImage = pygame.transform.scale(self.img.convert_alpha(), (230, 150))       

    def drawClipped(self, screen, delta):        
        if self.StateOfAnimation == 0:
            self.row = 0
            if self.frame_timer > self.FRAME_TIME:
                self.frame_timer -= self.FRAME_TIME
                self.frame = (self.frame + 1) % self.FRAME_CT
            self.frame_timer += delta                          
            self.clip = pygame.Rect(self.MARGIN + self.IMG_W * self.frame, self.row, self.IMG_W, 75)      
            screen.blit(self.TranslatedImage, (self.pos.x, self.pos.y), self.clip)            
        if self.StateOfAnimation == 1:
            self.row = 75
            if self.frame_timer > self.FRAME_TIME:
                self.frame_timer -= self.FRAME_TIME
                self.frame = (self.frame + 1) % self.FRAME_CT
            self.frame_timer += delta                          
            self.clip = pygame.Rect(self.MARGIN + self.IMG_W * self.frame, self.row, self.IMG_W, 75)      
            screen.blit(self.TranslatedImage, (self.pos.x, self.pos.y), self.clip)


              
            