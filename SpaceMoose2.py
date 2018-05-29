#Libraries=========================================================================================
import pygame
import os
import sys
from BaseClass import BaseClass
from Vector2D import Vector2D
from RectClass import RectClass
from UltraSpriteClass import UltraSpriteClass
from bossMachine import Boss
from SpriteClass import SpriteClass
from PlayerClass import player
from pygame.locals import *
#==================================================================================================

playerDied = False


#=================================================================================================================================
def ScreenText(screen, text = 'Nothing' , x = 100, y = 100, size = 42, color = (200, 0, 0), fontType = 'Miramonte'):
    text = str(text)
    font = pygame.font.SysFont(fontType, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
#=================================================================================================================================


#=================================================================================================================================
def Main():
    SOG = 0
    pygame.init()
    WIDTH = 1024
    HEIGHT = 768

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if SOG == 0:            
            SOG = Splash(screen)

        elif SOG == 1:            
            SOG = Menu(screen)

        elif SOG == 2:
            SOG = Controlls(screen)  
                       
        elif SOG == 3:
            SOG = MainGame()

        elif SOG == 4:
            SOG = LostScreen(screen)

        elif SOG == 5:
            SOG = WinScreen(screen)
#=================================================================================================================================


#=================================================================================================================================
def Splash(screen):
    nextscreen = 0
    inSplash = True
    WIDTH = 1024
    HEIGHT = 768
    ThisDirectory = os.getcwd()
    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\title_screen.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
    down = False
    start = pygame.time.get_ticks()
    startTime = 0
    up = 0
    while inSplash:
        screen.fill((0,0,0))
        delta = pygame.time.get_ticks() - start
        start = pygame.time.get_ticks()
        pygame.event.pump()
        backgroundSprite.draw(screen)
              
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                inSplash = False
                nextscreen = 1       

        #pygame.draw.rect(screen, (200, 0, 0), Rect( 200, 75,  50, 20))
            
        ScreenText(screen, 'SPACE MOOSE',97, 97, 100, (255,	246, 143) )
        ScreenText(screen, 'SPACE MOOSE',100, 100, 100, (255, 255, 0) )
        ScreenText(screen, '10000', 125, 150, 150)
        
        if not down: 
            up += 1 * delta
            if up >= 55:
                up = 55
                down = True
        if  down: 
            up -= 1 * delta
            if up <= 0:
                up = 0
                down = False
        ScreenText(screen, 'Press "Enter" to Start', WIDTH - 400, HEIGHT - 100, 40, (238,	238, up + 10))            
                     
        pygame.display.flip()
    return nextscreen
#=================================================================================================================================


#=================================================================================================================================
def Menu(screen):
    nextscreen = 2
    inMenu = True
    WIDTH = 1024
    HEIGHT = 768
    ThisDirectory = os.getcwd()

    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\title_screen.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
    selectionHover = 3 
    while inMenu:
        screen.fill((0,0,0))
        pygame.event.pump()
        backgroundSprite.draw(screen)

        if selectionHover == 3:
            pygame.draw.rect(screen, (200, 0, 0), Rect( 50, 150,  100, 10))
        elif selectionHover == 2:
            pygame.draw.rect(screen, (200, 0, 0), Rect( 50, 200,  100, 10))
              
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:

                
                if (selectionHover == 2):
                    nextscreen = 2
                if (selectionHover == 3):
                    nextscreen = 3
                inMenu = False

            elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                selectionHover = 3
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                selectionHover = 2
            
        ScreenText(screen, 'Play', 100, 100) 
        ScreenText(screen, 'Controls', 100, 150)          
                     
        pygame.display.flip()
    return nextscreen
#=================================================================================================================================


#=================================================================================================================================
def Controlls(screen):
    nextscreen = 1
    inControlls = True
    WIDTH = 1024
    HEIGHT = 768
    ThisDirectory = os.getcwd()

    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\controlls_menu.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
    down = False
    start = pygame.time.get_ticks()
    startTime = 0
    up = 0

    while inControlls:
        screen.fill((0,0,0))
        delta = pygame.time.get_ticks() - start
        start = pygame.time.get_ticks()
        pygame.event.pump()
        backgroundSprite.draw(screen)
              
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                inControlls = False
                nextscreen = 1
        pygame.draw.rect(screen, (200, 0, 0), Rect( 97, 75,  50, 20))            
        ScreenText(screen, 'Controlls',97, 97, 50, (255,	246, 143) )        
        if not down: 
            up += 1 * delta
            if up >= 200:
                up = 55
                down = True
        if  down: 
            up -= 1 * delta
            if up <= 0:
                up = 0
                down = False
        ScreenText(screen, 'Press "Enter" to Return', WIDTH - 400, HEIGHT - 100, 40, (238,	238, up + 10))              
        pygame.display.flip()
 
    return nextscreen
#=================================================================================================================================

#=================================================================================================================================
def LostScreen(screen):

    nextscreen = 0
    inLost = True
    WIDTH = 1024
    HEIGHT = 768
    ThisDirectory = os.getcwd()
    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\title_screen.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
    down = False
    start = pygame.time.get_ticks()
    startTime = 0
    up = 0
    while inLost:
        screen.fill((0,0,0))
        delta = pygame.time.get_ticks() - start
        start = pygame.time.get_ticks()
        pygame.event.pump()
        backgroundSprite.draw(screen)
              
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                inLost = False
                nextscreen = 0       

        #pygame.draw.rect(screen, (200, 0, 0), Rect( 200, 75,  50, 20))
            
        ScreenText(screen, 'Game Over, Man! Game Over',97, 97, 50, (255,	246, 143) )

        
        if not down: 
            up += 1 * delta
            if up >= 55:
                up = 55
                down = True
        if  down: 
            up -= 1 * delta
            if up <= 0:
                up = 0
                down = False
        ScreenText(screen, 'Press "Enter" to Start', WIDTH - 400, HEIGHT - 100, 40, (238,	238, up + 10))            
                     
        pygame.display.flip()
    return nextscreen
#=================================================================================================================================



#=================================================================================================================================
def WinScreen(screen):
    nextscreen = 0
    inWin = True
    WIDTH = 1024
    HEIGHT = 768
    ThisDirectory = os.getcwd()
    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\title_screen.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
    down = False
    start = pygame.time.get_ticks()
    startTime = 0
    up = 0
    while inWin:
        screen.fill((0,0,0))
        delta = pygame.time.get_ticks() - start
        start = pygame.time.get_ticks()
        pygame.event.pump()
        backgroundSprite.draw(screen)
              
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                inWin = False
                nextscreen = 1       

        #pygame.draw.rect(screen, (200, 0, 0), Rect( 200, 75,  50, 20))
            
        ScreenText(screen, 'VICTORY!!!',97, 97, 100, (255,	246, 143) )

        
        if not down: 
            up += 1 * delta
            if up >= 55:
                up = 55
                down = True
        if  down: 
            up -= 1 * delta
            if up <= 0:
                up = 0
                down = False
        ScreenText(screen, 'Press "Enter" to Start', WIDTH - 400, HEIGHT - 100, 40, (238,	238, up + 10))            
                     
        pygame.display.flip()
    return nextscreen
#=================================================================================================================================

def MainGame():
    #FILES==========================================
    ThisDirectory = os.getcwd()

    #PYGAME=========================================
    pygame.init()
    pygame.mixer.pre_init(22050, -16, 2)
    pygame.mixer.pre_init( 22050, -16, 2 )

    #SCREEN=========================================
    WIDTH = 1024
    HEIGHT = 768
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #MUSIC==========================================
    pygame.mixer.music.load(ThisDirectory +"\\Data\\Sounds\\BossFightTheme1.wav" )
    pygame.mixer.music.play()
    #TIME===========================================
    SPEED = 0.7
    start = pygame.time.get_ticks()
    startTime = 0
    gamePause = False
    shot_delay = 0


    #INITIALIZATION=================================
        #BACKGROUND=================================    
    backgroundSprite = SpriteClass((0, 0), WIDTH, HEIGHT,pygame.image.load(ThisDirectory +"\\Data\\Textures\\background.png").convert_alpha(),  1,  1, "BG0001",)
    backgroundSprite.drawn = True
        #PLAYER=====================================
    #Moose = UltraSpriteClass((WIDTH - 70, 490), 200, 100,pygame.image.load(ThisDirectory +"\\Data\\scott.png").convert_alpha(), "PL", 1, 1)
    Moose = player((WIDTH - 70, 490), 200, 100,pygame.image.load(ThisDirectory +"\\Data\\scott.png").convert_alpha(), "PL", 1, 1)
    Moose.testMode = False
    playerBound = RectClass((Moose.pos.x - 150, Moose.pos.y), Moose.w + 300, Moose.h, "M000", False);
    for o in Moose.Bullets:
        o.testMode = False
    Moose.w = 30
    Moose.h = 70
    invincibilityCount = 0
    gotHit = False
    jumpDelay = 0
    releaseDelay = False

       #BOSS=======================================
    bossSpriteSheet = (pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Idle 1.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 1.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 2.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 10.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 11.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 12.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 14.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 15.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 21.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 22.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 23.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 24.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Claw 25.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Fireball 1b.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Fireball 1c.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Fireball 3.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)),
                       pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Boss Fireball 1.png").convert_alpha(),
                                                                    (HEIGHT,HEIGHT)))

    fireSprite = pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Boss\\Fireball mid.png").convert_alpha(), (50,50))

    bossHealthText = pygame.transform.scale(pygame.image.load("BossHealthText.png").convert_alpha(), (100, 50))

    boss = Boss(Vector2D((10, HEIGHT - 700)), bossSpriteSheet, fireSprite, screen)
    for o in boss.bossBoxes:
        o.testMode = False
    for o in boss.fireBallChain:
        o.testMode = False

        #WALLS======================================
    left = Vector2D((0 + 40,0))
    up = Vector2D((0, 0 + 40))
    right = Vector2D((WIDTH - 40,0))
    down = Vector2D((0,HEIGHT - 40))

    walls = ( RectClass((left.x, left.y), 10, HEIGHT, 3, False), 
              RectClass((up.x, up.y), WIDTH, 10, 4, False),
              RectClass((right.x, right.y), 10, HEIGHT, 5, False))
        #PLATFORMS==================================
    #FOR TESTING
    platImg = pygame.image.load("HitBoxPlaceHolder.png").convert_alpha();
    #FOR TESTING
    #platforms =(SpriteClass((553, 560), 600, 170, pygame.transform.scale(platImg, (600,170)), Vector2D((0,0)), 0, "P0001", True ),
                #SpriteClass((550, 400), 122, 10, pygame.transform.scale(platImg, (122,10)), Vector2D((0,0)), 0, "P0002", True),
                #SpriteClass((785, 450), 50, 10, pygame.transform.scale(platImg, (50,10)), Vector2D((0,0)), 0, "P0003", True))

    platforms =(SpriteClass((553, 560), 600, 600, pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Textures\\Rock Cliff.png").convert_alpha(), (800,600)), Vector2D((0,0)), 0, "P0001", True ),
                SpriteClass((550, 400), 122, 50, pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Textures\\Mushroom platform.png").convert_alpha(), (122,50)), Vector2D((0,0)), 0, "P0002", True),
                SpriteClass((800, 450), 70, 50, pygame.transform.scale(pygame.image.load(ThisDirectory+"\\Data\\Textures\\Branch Platform v1.png").convert_alpha(), (70, 50)), Vector2D((0,0)), 0, "P0003", True))
    for o in platforms:
        o.testMode = False

    time_on_plat = 0
    platform3DimX = 122
    platform3DimY = 10
    plat_gone = False
    plat_shrink = False
    plat_back = 0

    floor = platforms[0]

    #CONTROLS================== 
    inputX = 0
    vel = Vector2D((0, 1))
    grounded = False
    onPlat = False
    facing = 0.9
    #MAIN===========================================
    while True: 
        screen.fill((0,0,0))
        pygame.event.pump()

        #time=======================================
        delta = pygame.time.get_ticks() - start
        start = pygame.time.get_ticks()
        shot_delay = shot_delay - 1
        invincibilityCount = invincibilityCount - 1
        if releaseDelay:
            jumpDelay = jumpDelay - 1

        #QUIT=======================================
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                Moose.testMode = not Moose.testMode
                for o in walls:
                    o.testMode = not o.testMode
                for o in platforms:
                    o.testMode = not o.testMode
                boss.testMode()
                playerBound.testMode = not playerBound.testMode

         #Reading input from keyboard for movement
        if not gamePause:
            inputX = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and (grounded or onPlat) and jumpDelay <=0:
                vel.y = -(SPEED + 0.65)
                grounded = False
                onPlat = False
                jumpDelay = 30
                releaseDelay = False
            elif key[pygame.K_d] and not gotHit:
                if grounded:
                    inputX = 1.1
                else:
                    inputX = .75
                Moose.isRunning = True
                Moose.StateOfAnimation = 0
                Moose.isRight = True
            elif key[pygame.K_a] and not gotHit:
                if grounded:
                    inputX = -1.1
                else:
                    inputX = -.75
                facing = -0.9
                Moose.row = 75
                Moose.StateOfAnimation = 1
                Moose.isRight = False
                
            if key[pygame.K_k] and shot_delay <= 0:
                shot_delay = 50
                Moose.BulletButton()

            if key[pygame.K_1]:
                boss.bossHP = boss.bossHP - 1

            #Manipulate velocity based on input
            if inputX != 0:
                vel.x = inputX * SPEED
            elif vel.x > 0:
                vel.x = vel.x - 0.005
                if vel.x < 0:
                    vel.x = 0
            elif vel.x < 0:
                vel.x = vel.x + 0.005
                if vel.x > 0:
                    vel.x = 0
            #accelerates player downwards when they are not grounded        
            if not grounded:
                onPlat = False
                vel.y = vel.y + 0.002 * delta
                Moose.isRunning = False
                if gotHit:
                    gotHit = False

            #Checks if player is out of bounds (i.e. fell through the floor)
            if Moose.pos.y > HEIGHT:
                playerDied = True
                break;
             #checks for collision with walls==========================================================================
            Moose.pos = Moose.pos.add(vel)
            Moose.colliDetect(walls)
            if Moose.detectedHit:
                #if object collided with left wall
                if Moose.collidedWith.id == 3:
                    vel.x = 0
                    Moose.pos.x = Moose.collidedWith.pos.x + Moose.collidedWith.w
                #if object collided with right wall
                elif Moose.collidedWith.id == 5:
                    vel.x = 0
                    Moose.pos.x = Moose.collidedWith.pos.x - Moose.w
                #if object collided with ceiling
                elif Moose.collidedWith.id == 4:
                    vel.y = 0
                    Moose.pos.y = Moose.collidedWith.pos.y + Moose.collidedWith.h

                #Resetting values for next collision check
                Moose.detectedHit = False

            #Checking for collisions with platforms
            Moose.colliDetect(platforms)
            if Moose.detectedHit:
                #If hitbox detected a hit from the left side
                if Moose.side == 0:
                    vel.x = 0
                    Moose.pos.x = Moose.collidedWith.pos.x + Moose.collidedWith.w
                #If hitbox detected a hit from the top side
                elif Moose.side == 1:
                    vel.y = 0
                    Moose.pos.y = Moose.collidedWith.pos.y + Moose.collidedWith.h
                #If hitbox detected a hit from the right side
                elif Moose.side == 2:
                    vel.x = 0
                    Moose.pos.x = Moose.collidedWith.pos.x - Moose.w
                #If hitbox detected a hit from the bottom side
                elif Moose.side == 3:
                    if Moose.collidedWith.id == "P0002":
                        time_on_plat = time_on_plat + 1
                        if time_on_plat == 800:
                            plat_shrink = True
                    vel.y = 0
                    Moose.pos.y = Moose.collidedWith.pos.y - Moose.h 
                    grounded = True
                    onPlat = True
                    releaseDelay = True
                    

                Moose.side = -1
                Moose.detectedHit = False

            ###########################################
            ##Checking for collisions with boss and attacks
            ###########################################
            ###Don't allow the player to move past the boss
            if Moose.pos.x < boss.boss_hitBox.pos.x + boss.boss_hitBox.w:
                Moose.pos.x = boss.boss_hitBox.pos.x + boss.boss_hitBox.w

            Moose.colliDetect((boss.fireBallSprite,))
            if Moose.detectedHit and invincibilityCount <= 0:
                Moose.health = Moose.health - 15
                invincibilityCount = 250
                Moose.detectedHit = False
                vel.x = 1
                vel.y = -(SPEED + 0.2)
                grounded = False
                gotHit = True

            Moose.colliDetect((boss.fireBallChain))
            if Moose.detectedHit and invincibilityCount <=0:
                Moose.health = Moose.health - 20
                invincibilityCount = 250
                Moose.detectedHit = False
                vel.x = 1
                vel.y = -(SPEED + 0.2)
                grounded = False
                gotHit = True

            Moose.colliDetect((boss.fist_Box,))
            if Moose.detectedHit and invincibilityCount <= 0:
                if boss.animIndex == 2 or boss.animIndex == 3:
                    Moose.health = Moose.health - 10
                    invincibilityCount = 250
                    Moose.detectedHit = False
                    vel.x = 1
                    vel.y = -(SPEED + 0.2)
                    grounded = False
                    gotHit = True

            Moose.colliDetect((boss.fireRain))
            if Moose.detectedHit and invincibilityCount <=0:
                Moose.health = Moose.health - 10
                invincibilityCount = 250
                Moose.detectedHit = False
                vel.x = 1
                vel.y = -(SPEED + 0.2)
                grounded = False
                gotHit = True

            Moose.colliDetect((boss.fireScatter))
            if Moose.detectedHit and invincibilityCount <= 0:
                Moose.health = Moose.health - 5
                invincibilityCount = 250
                Moose.detectedHit = False
                vel.x = 1
                vel.y = -(SPEED + 0.2)
                grounded = False
                gotHit = True

            Moose.colliDetect((boss.fireSpread))
            if Moose.detectedHit and invincibilityCount <= 0:
                Moose.health = Moose.health - 5
                invincibilityCount = 250
                Moose.detectedHit = False
                vel.x = 1
                vel.y = -(SPEED + 0.2)
                grounded = False
                gotHit = True

            if Moose.health <= 0:
                playerDied = True
                break;

            for o in platforms:
                if not((Moose.pos.y + Moose.h == o.pos.y) and (grounded or onPlat)
                       and ((Moose.pos.x > o.pos.x and Moose.pos.x + Moose.w < o.pos.x + o.w)
                       or (Moose.pos.x > o.pos.x and Moose.pos.x < o.pos.x + o.w)
                       or (Moose.pos.x < o.pos.x and Moose.pos.x + Moose.w > o.pos.x))):
                    grounded = False
                else:
                    onPlat = True
                    grounded = True
                    
            #if Moose.pos.y + Moose.h == walls[3].pos.y:
                #grounded = True

            #UPDATE=======================================
            boss.stateMachine(Moose, (platforms), floor, screen, delta)
            boss.detectBullet(Moose.Bullets)
            if boss.bossHP <=0:
                pygame.quit()
                sys.exit()


            #DRAW=========================================
            backgroundSprite.draw(screen)
            for o in platforms:
                o.draw(screen)
                
            Moose.DrawStatusBar(screen)
            Moose.UpdateBullets((playerBound,), screen, delta)
            boss.draw(screen, bossHealthText)

            if (invincibilityCount > 0 and invincibilityCount % 2 != 0) or (invincibilityCount <= 0):
                Moose.drawClipped(screen, delta)

            playerBound.pos.x = Moose.pos.x - 150
            playerBound.pos.y = Moose.pos.y

            if plat_shrink:
                platforms[1].vel.y = 1
                platforms[1].accel = platforms[1].accel + .01
                platforms[1].update(delta)
                if platforms[1].pos.y > 768:
                    platforms[1].pos.y = 768
                    plat_shrink = False
                    plat_gone = True
                    time_on_plat = 0

            if plat_gone:
               plat_back = plat_back + 1
               if plat_back == 10000:
                   plat_gone = False
                   platforms[1].pos.y = 400
                   plat_back = 0
                   
            if Moose.testMode:
                    Moose.drawRect(screen)
            for o in walls:
                if o.testMode:
                    o.drawRect(screen)
            for o in platforms:
                if o.testMode:
                    o.drawRect(screen)
            for o in boss.bossBoxes:
                if o.testMode:
                    o.drawRect(screen)
            for o in boss.fireBallChain:
                if o.testMode:
                    o.drawRect(screen)
            if playerBound.testMode:
                playerBound.drawRect(screen)
            
            pygame.display.flip()

    if playerDied:
        return 4
    else: 
        return 5
Main()
