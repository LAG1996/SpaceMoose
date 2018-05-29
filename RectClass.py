import pygame
import math
from BaseClass import BaseClass
from Vector2D import Vector2D

class RectClass(Vector2D):    
    def __init__(self, position, width, height, id , isTest = True):
        super(RectClass, self).__init__(position, id)
        self.w = width       
        self.h = height
        self.pos = Vector2D((self.x, self.y))
        self.center = Vector2D((self.pos.x + (width/2), (self.pos.y+ (height/2))))
        
        
        #======================================================
        #   THE FOLLOWING VARIABLES ARE FOR DEBUGGING PURPOSES
        #======================================================
        
        self.testMode = isTest
        #default color for when the box isn't hitting something
        self.defColor = (0,0,255)
        #default color for when the box is hitting something
        self.colliColor = (255,0,0)
        self.actColor = self.defColor
        #thickness of rectangle for easier viewing while debugging
        self.thick = 1

        #IMPORTANT!!! THIS IS A "TYPE" CODE FOR HITBOX!!!
        #TYPE 1 MEANS THIS IS A RECTANGULAR HITBOX!!!
        self.TYPE = 1

        #Boolean value which detects collision.
        self.detectedHit = False

        #number for checking direction of collision.
        #0 = left
        #1 = up
        #2 = right
        #3 = down
        self.side = -1

        #(Should be) unique ID for object
        self.collidedWith = -1

    #The following method detects other hitboxes to prevent overlap
    def colliDetect(self, other):
        for o in other:
            #Makes sure that the hitbox does not check itself
            if self.id != o.id:
                #if the other hitbox is of circle type...
                if o.TYPE == 0:
                    #checking rightmost side of hitbox
                    if (self.pos.x + self.w) > (o.pos.x - o.rad) and self.pos.x < o.pos.x:
                        if self.testMode:
                            print "Hit circle from right!"
                        self.detectedHit = True
                        self.side = 2
                        self.collidedWith = o

                    #checking leftmost side of hitbox
                    if self.pos.x < (o.pos.x + o.rad) and self.pos.x > o.pos.x:
                        if self.testMode:
                            print "Hit circle from left!"
                        self.detectedHit = True
                        self.side = 0
                        self.collidedWith = o

                    #checking bottommost side of hitbox    
                    if (self.pos.y + self.h) > o.pos.y - o.rad and self.pos.y < o.pos.y:
                        if self.testMode:
                            print "Hit circle from bottom!"
                        self.detectedHit = True
                        self.side = 3
                        self.collidedWith = o

                    #checking topmost side of hitbox
                    if self.pos.y < (o.pos.y + o.rad) and self.pos.y > o.pos.y:
                        if self.testMode:
                            print "Hit circle from top!"
                        self.detectedHit = True
                        self.side = 1
                        self.collidedWith = o


                #if the other hitbox is of rectangle type...
                elif o.TYPE == 1:
                    #checking rightmost side of hitbox
                    if (self.pos.x + self.w > o.pos.x and self.pos.x + (self.w/2) < o.pos.x
                        and ((self.pos.y > o.pos.y and self.pos.y < o.pos.y + o.h)
                             or (self.pos.y + self.h > o.pos.y and self.pos.y + self.h < o.pos.y + o.h)
                             or (self.pos.y > o.pos.y and self.pos.y + self.h < o.pos.y + o.h))):
                        if self.testMode:
                               print "Hit rect from right!"
                        self.detectedHit = True
                        self.side = 2
                        self.collidedWith = o
                    #checking leftmost side of hitbox
                    elif (self.pos.x < (o.pos.x + o.w) and self.pos.x + (self.w/2) > (o.pos.x + o.w)
                        and ((self.pos.y > o.pos.y and self.pos.y < o.pos.y + o.h)
                             or (self.pos.y + self.h > o.pos.y and self.pos.y + self.h < o.pos.y + o.h)
                             or (self.pos.y > o.pos.y and self.pos.y + self.h < o.pos.y + o.h))):
                            if self.testMode:
                                print "Hit rect from left!"
                            self.detectedHit = True
                            self.side = 0
                            self.collidedWith = o 
                    #checking bottommost side of hitbox
                    if (self.pos.y + self.h > o.pos.y and self.pos.y + (self.h/2) < o.pos.y
                        and ((self.pos.x > o.pos.x and self.pos.x < o.pos.x + o.w)
                              or (self.pos.x + self.w > o.pos.x and self.pos.x + self.w < o.pos.x + o.w)
                              or (self.pos.x > o.pos.x and self.pos.x + self.w < o.pos.x + o.w))):
                            if self.testMode:
                                print "Hit rect from bottom!"
                            self.detectedHit = True
                            self.side = 3
                            self.collidedWith = o
                    #checking topmost side of hitbox
                    elif (self.pos.y < (o.pos.y + o.h) and self.pos.y + (self.h/2) > o.pos.y + o.h
                         and ((self.pos.x > o.pos.x and self.pos.x < o.pos.x + o.w)
                              or (self.pos.x + self.w > o.pos.x and self.pos.x + self.w < o.pos.x + o.w)
                              or (self.pos.x > o.pos.x and self.pos.x + self.w < o.pos.x + o.w))):
                            if self.testMode:
                                print "Hit rect from top!"
                            self.detectedHit = True
                            self.side = 1
                            self.collidedWith = o
    

    def drawRect(self, screen):

        pygame.draw.rect(screen, self.actColor, (self.pos.x,self.pos.y,self.w,self.h),self.thick)



