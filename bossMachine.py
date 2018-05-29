import pygame
from RectClass import RectClass
import math
from Vector2D import Vector2D
from SpriteClass import SpriteClass

class Boss:

    ##########################################################
    #
    #   CONSTRUCTOR
    #   PARAMETER LIST:
    #   
    #   Boss self - explicit call for in-instance operation. Does not need to be
    #           passed by programmer.
    #
    #   vector2 pos - vector2 object holding position of boss
    #
    #   string img - tuple of images for img. The order inserted NEEDS to be as follows:
    #           -boss idle sprite
    #           -boss fistslam sprites (INDIVIDUAL; NOT IN A TUPLE)
    #           -DIFFERENT SPRITES MAY COME LATER
    ###########################################################
    def __init__(self, pos, img = None, fire = None, screen = None):
        self.bossHP = 300.0
        self.MAXHP = 300.0
        self.bossHP_Bar_WIDTH = 650.0
        self.enraged = False
        self.pos = pos
        self.animIndex = 0
        self.windUpTimer = 50
        self.screen = screen
        self.pass1 = False
        self.pass2 = False

                #Boolean holding whether boss is in idle pose or not. Boss will
        #only be able to take new actions during idle pose.
        self.idle = True

        #Boolean variables holding whether boss is during certain attack
        #states. Each attack state will have its own cooldown time, so
        #the boss will return to idle state accordingly.
        if not fire == None:
            self.fire = fire
            self.FB_WIDTH = 50
            self.FB_HEIGHT = 50
            self.noFireImage = False
        else:
            self.noFireImage = True
            self.FB_WIDTH = 50
            self.FB_HEIGHT = 50

        self.fireBall = False
        self.fireScatterActive = False
        self.fireBreath = False
        self.fistSlam = False
        self.fireRainActive = False
        self.fireSpreadActive = False
        self.windUpActive = False

        self.fireBallActive = False
        self.fireBreathActive = False
        self.fireBallSprite = SpriteClass((-300, -300), 50, 50 ,fire, Vector2D((0,0)), .15)
        self.distPlayer = 0

        self.time_on_floor = 0

        #Int that keeps count of "cooldown" time, incrementing each tick of
        #the game loop
        self.coolDown = 0
        self.fireBallAgain = 600
        self.fistSlamAgain = 300
        self.fireBreathAgain = 600
        self.fireRainAgain = 800
        self.fireScatterTime = 500
        self.actAgain = 0
        self.flicker = 0

        #The following ints hold the amount of cooldown each boss attack will
        #require.
        self.FBALL_CD = 100
        self.FBREA_CD = 300
        self.FSLAM_CD = 400

        self.bossID = "A000"
        self.fireBallID = "A001"

        self.lastBulletHitID = "nan"



        ####################################################################
        #
        #   HITBOXES AND STUFF
        #
        ####################################################################
        
        self.boss_hitBox = RectClass((self.pos.x + 75, self.pos.y + 100), 400, 500, self.bossID, False)
        self.fireBall_hitBox = RectClass((self.fireBallSprite.pos.x, self.fireBallSprite.pos.y), 50, 50, self.fireBallID, False)

        self.fist_Box = RectClass((-1000, -1000), 200, self.boss_hitBox.h/5, "0", False)

        self.fireBallChain = (SpriteClass((-300, -300), 70, 40, pygame.transform.scale(fire, (70, 40)), Vector2D((0,0)), .7),
                              SpriteClass((-300, -300), 70, 40, pygame.transform.scale(fire, (70, 40)), Vector2D((0,0)), .7),
                              SpriteClass((-300, -300), 70, 40, pygame.transform.scale(fire, (70, 40)), Vector2D((0,0)), .7))

        self.fireRain = (SpriteClass((553, -300), 40, 40, pygame.transform.rotate(pygame.transform.scale(fire, (40, 40)), -90.0), Vector2D((0,0)), .6),
                         SpriteClass((753, -300), 40, 40, pygame.transform.rotate(pygame.transform.scale(fire, (40, 40)), -90.0), Vector2D((0,0)), .6),
                         SpriteClass((953, -300), 40, 40, pygame.transform.rotate(pygame.transform.scale(fire, (40, 40)), -90.0), Vector2D((0,0)), .6))

        self.fireScatter = (SpriteClass((-300,-300), 50, 50, self.fireBallSprite.img, Vector2D((0,0)), .6),
                            SpriteClass((-300,-300), 50, 50, self.fireBallSprite.img, Vector2D((0,0)), .6),
                            SpriteClass((-300,-300), 50, 50, self.fireBallSprite.img, Vector2D((0,0)), .6),
                            SpriteClass((-300,-300), 50, 50, self.fireBallSprite.img, Vector2D((0,0)), .6))

        self.fireSpread = (SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2),
                           SpriteClass((-300,-300), 50, 50, self.fireRain[0].img, Vector2D((0,0)), .2))

        self.bossBoxes = (self.boss_hitBox, self.fireBall_hitBox, self.fist_Box)

        self.isTest = False


        #SPRITE########################################################################################################

        if not img == None:
            self.bossSprite = SpriteClass((self.pos.x, self.pos.y), self.boss_hitBox.w, self.boss_hitBox.h, img[0], (0,0), 0)
            self.bossHurtSprite = SpriteClass((self.pos.x, self.pos.y), self.boss_hitBox.w, self.boss_hitBox.h, img[13], (0,0), 0)

            self.fistSlamSprite = (SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[1],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[2],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[3],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[4],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[5],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[6],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[7],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[9],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[10],Vector2D((0,0)), 0),
                                   SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[11],Vector2D((0,0)), 0))

            self.fireWindUp = ( SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[12],Vector2D((0,0)), 0),
                                SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[13],Vector2D((0,0)), 0),
                                SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[14],Vector2D((0,0)), 0),
                                SpriteClass( (self.pos.x, self.pos.y), 100, 100,img[15],Vector2D((0,0)), 0))
            
            self.activeFrame = self.bossSprite
            self.noImage = False
        else:
            self.noImage = True
        


    ############################################################################
    #The following function is the state machine for the boss.
    #Structurally, it's just a switch-board that checks what "state"
    #the boss is in, and then has the boss act accordingly in that state.
    #For example, if the boss is idle, then it will make an action.
    #Another example is if the boss is in fire ball state, then there's a
    #certain cooldown time that the boss must wait for before it can act again.
    #############################################################################
    def stateMachine(self, player, world, floor, screen, delta):
        if self.bossHP < self.MAXHP/2:
                    self.enraged = True
        if self.fireBallAgain > 0 and not self.fireBall:
            self.fireBallAgain = self.fireBallAgain - 1

        if self.fistSlamAgain > 0 and not self.fistSlam:
            self.fistSlamAgain = self.fistSlamAgain - 1

        if self.fireBreathAgain > 0 and not self.fireBreath:
            self.fireBreathAgain = self.fireBreathAgain - 1

        if self.fireRainAgain > 0 and not self.fireRainActive:
            self.fireRainAgain = self.fireRainAgain - 1

        if self.actAgain > 0 and not self.fireBall and not self.fistSlam and not self.fireBallActive:
            self.actAgain = self.actAgain - 1

        if self.flicker > 0:
            self.flicker = self.flicker - 1
        
        #Checks if the player is on the floor. If the player is, increment the counter
        #for the player's time on the ground.
        if player.pos.y + player.h == floor.pos.y and not (self.fireBreath or self.fireBall or self.fistSlam):
                self.time_on_floor = self.time_on_floor + 1

        #Checks if boss is in idle state (i.e. not in the middle of attack animation)
        #Also checks if the boss's fireball is still on screen.
        #If the boss is idle and the fireball is offscreen, the boss may act.      
        if self.idle and not self.fireBallActive and self.actAgain <= 0:
            #If the boss senses that the player is too close and is on the floor,
            #it will attack with a fist slam.
            self.actAgain = 300
            if math.fabs(player.pos.x - (self.boss_hitBox.pos.x + self.boss_hitBox.w)) < 250 and self.fistSlamAgain <= 0 and player.pos.y + player.h == floor.y:
                self.fistSlamAgain = 600
                self.fistSlam = True
                self.idle = False
                self.swingDown = True
                self.fist_Box.pos = Vector2D((((self.boss_hitBox.pos.x + self.boss_hitBox.w), self.boss_hitBox.pos.y + 50)))
                self.fistSlamAtk()

            #If the boss sees that the player has been on the ground for too long,
            #it will attack with a fire breath.
            elif self.time_on_floor >= 600 and self.fireBreathAgain <= 0 and not self.fireBreathActive:
                self.fireBreathAgain = 600
                self.fireBreath = True
                self.idle = False
                self.time_on_floor = 0
                self.windUpActive = True
                self.windUpAnim(delta, floor, screen)

            #If the boss does not do either of the attacks above,
            #it will attack with a fire ball attack.
            elif self.fireBallAgain <= 0:
                self.fireBallAgain = 600
                self.fireBall = True
                self.idle = False
                self.windUpActive = True
                self.windUpAnim(delta, floor, screen)

        elif self.fireBall and not self.windUpActive:
            if self.coolDown == self.FBALL_CD:
                self.coolDown = 0
                self.fireBall = False
                self.idle = True
            else:
                self.coolDown = self.coolDown + 1
                self.fireBallAtk(delta, player.pos, world, screen)

        elif self.fistSlam:
            if self.coolDown == self.FSLAM_CD:
                self.fistSlamAgain = 600
                self.coolDown = 0
                self.animIndex = 0
                self.fistSlam = False
                self.idle = True
                self.activeFrame = self.bossSprite

            else:
                self.coolDown = self.coolDown + 1
                self.fistSlamAtk()
                    
        if self.fireBallActive and not self.fireBall:
               self.fireBallAtk(delta, player.pos, world, screen)
               
        if self.fireBreathActive:
            self.fireBreathAtk(delta, floor, screen)

        if self.fireRainAgain <= 0 and self.enraged and not self.fireSpreadActive:
            self.fireRainAtk(delta, floor)
        elif self.fireSpreadActive:
            self.fireBallSpread(delta)

        if self.fireScatterActive:
            self.fireBallScatter(delta)

        if self.windUpActive:
            if self.animIndex >= 4:
                self.animIndex = 0
                self.windUpActive = False
                self.activeFrame = self.bossSprite
                if self.fireBreath:
                    self.fireBreath = False
                    self.fireBreathAtk(delta, floor, screen)
                else:
                    self.fireBallAtk(delta, player.pos, world, screen)
            else:
                self.windUpAnim(delta, floor, screen)
        
    #The following function is for the fireball's tracking.
    #The fireball's trajectory is set outside the function.
    #If the fireball detected that it hit something, it will disappear from the game map.
    #Otherwise, it will continue moving towards its trajectory.
    def fireBallAtk(self, delta, player_pos, world, screen):
        if not self.fireBallActive:
               self.fireBallActive = True
               self.fireBallSprite.pos.x = self.boss_hitBox.pos.x + 200
               self.fireBallSprite.pos.y = self.boss_hitBox.pos.y + 50
               self.fireBallSprite.vel = player_pos.subtract(self.fireBallSprite.pos)
               
        self.fireBallSprite.colliDetect(world)
        if self.fireBallSprite.detectedHit or self.fireBallSprite.pos.x > 1024 or self.fireBallSprite.pos.y > 768:
            if self.enraged:
                self.fireScatterActive = True
                for o in self.fireScatter:
                    o.pos = self.fireBallSprite.pos
                self.fireScatter[0].vel = Vector2D((-1,0))
                self.fireScatter[1].vel = Vector2D((0, -1))
                self.fireScatter[2].vel = Vector2D((1,0))
                self.fireScatter[3].vel = Vector2D((0,1))
                self.fireBallScatter(delta)
            else:
                self.fireBallActive = False
                
            self.fireBallSprite.pos.x = -300
            self.fireBallSprite.pos.y = -300
            self.fireBallSprite.vel = Vector2D((0,0))
            
            self.fireBallSprite.detectedHit = False
            self.fireBallAgain = 600
            self.fireBallSprite.accel = .1               
                   
        else:
            if self.fireBallSprite.accel < .75:
                self.fireBallSprite.accel = self.fireBallSprite.accel + .01
            self.fireBallSprite.update(delta)

    def fireBallScatter(self, delta):
        for o in self.fireScatter:
            o.update(delta)
        self.fireScatterTime = self.fireScatterTime - 1
        if self.fireScatterTime <= 0:
            self.fireScatterActive = False
            self.fireBallActive = False
            for o in self.fireScatter:
                self.fireScatterTime = 500
                o.vel = Vector2D((0,0))
                o.pos = Vector2D((-1000,-1000))

    def fireBreathAtk(self, delta, floor, screen):
        if not self.fireBreathActive:
            self.fireBreathActive = True
            self.fireBallChain[0].pos = Vector2D(((self.boss_hitBox.pos.x + self.boss_hitBox.w) - 50, self.boss_hitBox.pos.y + 50))
            self.fireBallChain[1].pos = Vector2D((self.fireBallChain[0].pos.x, self.fireBallChain[0].pos.y + 40))
            self.fireBallChain[2].pos = Vector2D((self.fireBallChain[0].pos.x, self.fireBallChain[0].pos.y - 40))

            for o in self.fireBallChain:
                o.vel.x = 1

            self.fireBallChain[0].accel = .1
            self.fireBallChain[1].accel = .1
            self.fireBallChain[2].accel = .1
            
        elif self.fireBallChain[0].pos.x > 1024:
            if self.enraged and not self.pass2:
                self.pass1 = True
                for o in self.fireBallChain:
                    o.vel.x = -1
                    o.accel = .15
                    o.pos.x = 1024 - o.w
                    o.update(delta)
            else:
                self.pass2 = False
                for o in self.fireBallChain:
                    o.pos = Vector2D((-1000,-1000))
                    o.vel = Vector2D((0,0))
                    o.accel = 0
                self.fireBreathActive = False
                self.idle = True

        elif self.fireBallChain[0].pos.x < floor.x and self.pass1:
            self.pass1 = False
            self.pass2 = True
            for o in self.fireBallChain:
                o.vel.x = 1
                o.accel = .15
                o.update(delta)

        elif self.fireBallChain[1].pos.y + self.fireBallChain[1].h < floor.y:
                for o in self.fireBallChain:
                    o.vel.y = 1

                for o in self.fireBallChain:
                    o.update(delta)
                
                if self.fireBallChain[1].pos.y + self.fireBallChain[1].h > floor.pos.y:
                    for o in self.fireBallChain:
                        o.vel.y = 0
                    self.fireBallChain[1].pos.y = floor.pos.y - self.fireBallChain[1].h
                    self.fireBallChain[0].pos.y = self.fireBallChain[1].pos.y - 40
                    self.fireBallChain[2].pos.y = self.fireBallChain[0].pos.y - 40

        else:
            for o in self.fireBallChain:
                if o.accel < .9:
                    o.accel = o.accel + .01
                o.update(delta)

    def fistSlamAtk(self):
        #Animating the fist coming down
        if self.coolDown % (self.FSLAM_CD / 10) == 0 and self.animIndex < 10:
            self.fist_Box.pos.y = self.fist_Box.pos.y + 30
            self.activeFrame = self.fistSlamSprite[self.animIndex]
            self.animIndex = self.animIndex + 1
            if self.animIndex == 10:
                self.fist_Box.pos = Vector2D((-1000,-1000))
                

    def fireRainAtk(self, delta, floor):
        if not self.fireRainActive:
            for o in self.fireRain:
                o.pos.y = 0
                o.vel.y = 1
            self.fireRainActive = True     
        elif self.fireRain[0].pos.y > floor.x:
            if self.bossHP < self.MAXHP*.25:
                self.fireSpreadActive = True
                self.spreadTimer = 200
                self.fireSpread[0].pos = self.fireRain[0].pos
                self.fireSpread[1].pos = self.fireRain[0].pos.add(Vector2D((self.fireSpread[0].w, 0)))
                self.fireSpread[1].vel = self.fireSpread[0].vel = Vector2D((1,0))

                self.fireSpread[2].pos = self.fireRain[1].pos
                self.fireSpread[3].pos = self.fireRain[1].pos
                self.fireSpread[4].pos = self.fireRain[1].pos
                self.fireSpread[2].vel = Vector2D((-1,0))
                self.fireSpread[4].vel = Vector2D((1,0))

                self.fireSpread[5].pos = self.fireRain[2].pos.subtract(Vector2D((self.fireRain[2].w, 0)))
                self.fireSpread[6].pos = self.fireRain[2].pos
                self.fireSpread[5].vel = self.fireSpread[5].vel = Vector2D((-1,0))

                for o in self.fireSpread:
                    o.pos.y = floor.y - o.h
                
                self.fireBallSpread(delta)
                
            for o in self.fireRain:
                o.pos.y = -300
                self.fireRainActive = False
                self.fireRainAgain = 800
        else:
            for o in self.fireRain:
                if o.accel < .7:
                    o.accel = o.accel + .001
                o.update(delta)

    def fireBallSpread(self, delta):
        for o in self.fireSpread:
            o.update(delta)
        self.spreadTimer = self.spreadTimer - 1

        if self.spreadTimer <= 0:
            for o in self.fireSpread:
                o.pos = Vector2D((0,0))
            self.fireSpreadActive = False

    def windUpAnim(self, delta, floor, screen):
        self.windUpTimer = self.windUpTimer - 1
        if self.windUpTimer <= 0:
            self.activeFrame = self.fireWindUp[self.animIndex]
            self.windUpTimer = 50
            self.animIndex = self.animIndex + 1

    def detectBullet(self, bullet):
        for o in bullet:
            if o.pos.x <= self.boss_hitBox.pos.x + self.boss_hitBox.w and o.pos.x > 0 and o.pos.y > self.boss_hitBox.pos.y and o.id != self.lastBulletHitID:
                self.bossHP = self.bossHP - 6
                self.lastBulletHitID = o.id
                self.flicker = 200
                
    def testMode(self):
        for o in self.bossBoxes:
               o.testMode = not o.testMode
        for o in self.fireBallChain:
            o.testMode = not o.testMode

    def draw(self, screen, text):
        if self.flicker <= 0 or (self.flicker %2 == 0):
            self.activeFrame.draw(screen)

        if self.fireSpreadActive:
            for o in self.fireSpread:
                o.draw(screen)
        if self.fireBreathActive:
            for o in self.fireBallChain:
                o.draw(screen)
        if self.fireScatterActive:
            for o in self.fireScatter:
                o.draw(screen)
        if self.fireBallActive:
            self.fireBallSprite.draw(screen)
        if self.fireRainActive:
            for o in self.fireRain:
                o.draw(screen)
        screen.blit(text, (150, 600))
         
        pygame.draw.rect(screen, (255,0,0), (150, 650, self.bossHP_Bar_WIDTH * (self.bossHP/self.MAXHP), 20), 0)
        
