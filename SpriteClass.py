import pygame
import math
from BaseClass import BaseClass
from Vector2D import Vector2D
from RectClass import RectClass

class SpriteClass(RectClass): 
    def __init__(self, position, width, height, img, vel, accel, id = "", isTest = True):
        super(SpriteClass, self).__init__(position, width, height, id, isTest)             
        self.vel = vel       
        self.img = img       
        self.accel = accel 
        self.drawn = isTest

    def update(self, delta):
            step = self.vel.normalize()
            self.pos = self.pos.add(step.scale(delta*self.accel))
            
    def draw(self, screen):
        if self.drawn== True:
            screen.blit(self.img, (self.pos.x, self.pos.y))
       
        
