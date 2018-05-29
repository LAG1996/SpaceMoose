import pygame
import math
from BaseClass import BaseClass
from Vector2D import Vector2D
from RectClass import RectClass
from SpriteClass import SpriteClass

class BulletClass(SpriteClass):
    def __init__(self, position, width, height, img, vel, accel = 2, id = "", isTest = True):
        super(BulletClass, self).__init__(position, width, height, img, vel, accel, id, isTest) 
        self.drawn = False     
        self.shot = False
        self.target = Vector2D((self.pos.x + 500, 0))
        
    def HolsterBullet(self, holster):
        self.pos = holster
        self.drawn = False
        self.shot = False
        self.detectedHit = False

    def SetDestination(self, isRight):
        if isRight:
            self.target = Vector2D((self.pos.x + 500, 0))
        else:
            self.target = Vector2D((self.pos.x - 500, 0))
   
    def setTarget(self, t):
        self.target = t

    def moveTo(self,delta):                  
            displacement = self.target.subtract(self.pos)
            direction = displacement.normalize()
            velocity = direction.scale(self.accel)
            #self.velocity = velocity
            step = velocity.scale(delta)

            if step.magnitude() > displacement.magnitude():
                self.pos = self.target

            else:
                self.pos = self.pos.add(step)

        







