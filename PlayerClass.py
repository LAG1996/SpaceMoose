import pygame
import sys
import math
import os
import pygame
from Vector2D import Vector2D
from SpriteClass import SpriteClass
from UltraSpriteClass import UltraSpriteClass
from BulletClass import BulletClass
from pygame.locals import *


ThisDirectory = os.getcwd()
#============================================================================================
class player(UltraSpriteClass):
    def __init__(self, position, width, height, img, vel, accel, id, isTest = True):
        super(player, self).__init__( position, width, height, img, vel, accel, id, isTest) 
        self.health = 100
        self.stamina = 10
        self.BarrelHeat = 0
        self.overheated = False
        self.cooling = True
        self.will = 100 
        self.nextbullet = 0
        self.isRight = True
        self.coolTime = 0
        self.grounded = False
        self.ableToJump = False
        self.w = 30
        self.h = 60
        self.jumpTarget = Vector2D((self.pos.x + 700, self.pos.y -60))
        self.Bullets = (BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(), 1, 1, "BG0001"),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0002",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0003",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0004"),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0005",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0006",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0007",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0008",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0009",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0010",),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0011"),
                        BulletClass((self.pos.x, self.pos.y), 20, 20,pygame.image.load(ThisDirectory +"\\Data\\Textures\\Fireball.png").convert_alpha(),  1, 1, "BG0012",))
#MOVEMENT=========================================================================

    def SetDestination(self):
        if self.isRight:
            self.jumpTarget = Vector2D((self.pos.x + 500, self.pos.y -700))
            
        else:
            self.jumpTarget = Vector2D((self.pos.x - 500, self.pos.y -700))
        

    def jumpTo(self,delta):
        if not self.grounded:
            self.ableToJump = False
        if self.ableToJump:                      
            displacement = self.jumpTarget.subtract(self.pos)
            direction = displacement.normalize()
            velocity = direction.scale(50)
            #self.velocity = velocity
            step = velocity.scale(delta)

            if step.magnitude() > displacement.magnitude():
                self.pos = self.jumpTarget
                
            else:
                if self.detectedHit == False:
                    self.pos = self.pos.add(step)

#STAMINA BAR======================================================================

    def decreaseStamina(self):
        if self.stamina > 0 and self.StateOfAnimation != 0:
            self.stamina -= 1 * 0.001
    def increaseStamina(self):
        if self.stamina < 100 and self.StateOfAnimation == 0:
            self.stamina += 1 * 0.025
    
    def UpdateStats(self):
        self.decreaseStamina()
        self.increaseStamina()

#BARREL HEAT BAR======================================================================
    def decreaseBarrelHeat(self, delta):
            self.BarrelHeat -= 1 * delta *0.02        

    def increaseBearelHeat(self):        
            self.BarrelHeat += 10            
           
    def UpdateCooldown(self, delta):
        if self.overheated:
            self.BarrelHeat -= delta * 0.01
            if self.BarrelHeat <= 0:
                self.overheated = False

    def UpdateBullets(self, other, screen, Delta):

        if self.BarrelHeat < 0:
            self.BarrelHeat = 0
        if self.BarrelHeat >= 100:
            self.overheated = True

        if self.BarrelHeat >= 0 and self.overheated == False:  
           self.decreaseBarrelHeat(Delta)

        self.UpdateCooldown(Delta)   
             
        for b in self.Bullets:
            if b.shot:
                b.moveTo(Delta)
                b.colliDetect(other) 
        
        for b in self.Bullets:
            if b.detectedHit:
                b.drawn = False
                b.shot = False
                b.HolsterBullet(self.pos)
                b.pos = Vector2D((0, 0))

        for b in self.Bullets:
            b.draw(screen)
#BULLET BUTTON ACTIVATION ===============================================
    def BulletButton (self):
         #if self.overheated == False and self.grounded:
        #NOTE FROM LUIS: The above if condition did not allow for bullets to be shot. I'm sure you can see why this was the case by looking at the logic.
        #Below, I changed the condition to be for only when the gun is not overheating.
         if not self.overheated:
                if self.BarrelHeat < 100:
                    self.increaseBearelHeat()
                if self.nextbullet >=12:
                    self.nextbullet = 0   
                self.Bullets[self.nextbullet].pos = self.pos     
                if self.StateOfAnimation == 0:
                    self.Bullets[self.nextbullet].setTarget(self.pos.add(Vector2D((2000, 0))))
                if self.StateOfAnimation == 1:
                    self.Bullets[self.nextbullet].setTarget(self.pos.add(Vector2D((-2000, 0))))
                self.Bullets[self.nextbullet].shot = True
                self.Bullets[self.nextbullet].drawn = True
                self.nextbullet += 1        
#JUMP BUTTON ACTIVATION ================================================
    def JumpButton(self):
        self.StateOfAnimation = 3
        self.SetDestination()
        self.ableToJump = True
     

#STATUS BAR=============================================================
    def DrawStatusBar(self, screen):
        pygame.draw.rect(screen, (200, 0, 0), Rect( 200, 25,  self.health, 20))
        pygame.draw.rect(screen, (0, 120, 100), Rect( 200 , 60,  100 * self.BarrelHeat *0.01, 20))    
        pygame.draw.rect(screen, (0, 0, 100), Rect( 200, 95,  100, 20))
        







        
         
