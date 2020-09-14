import pygame
import sys
import smbus
import time
import math
import random

# Analog zuweisen
bus = smbus.SMBus(1)
value_X = 0
value_Y = 0
address = 0x48

Ana_Y = 0x41 # A1
Ana_X = 0x42 # A2

x = 129
y = 129

# Pygame var
pygame.init()

WIDTH = 1000
HEIGHT = 700
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
player_color = WHITE

player_pos = [400, 300]
player_size = 10

gegner1_pos = [40, 40]
gegner1_size = 30

geschoss_pos = [500, 700]
geschoss_size = 25

# globale Var Links
kollidiertL = False
iL = 0
geschwL = 0

# globale Var Rechts
kollidiertR = False
iR = 0
geschwR = 0

# globale Var Oben
kollidiertO = False
iO = 0
geschwO = 0

# globale Var Unten
kollidiertU = False
iU = 0
geschwU = 0

#global Var Geschoss
ranGesY = 0
ranGesX = 0
merkeY = 0
merkeX = 0


anzLoop = 0
# Screen einstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))


###################################Wand#########################################
###################################Links########################################
################################################################################

# Pace Berechnung Links
def paceFunL(dif):
    ergebnis = (round(dif/2) * (-1)) + 1
    return ergebnis

# Wall Collision Links
def wallCollL(pace, PosX):
    
    global kollidiertL
    kollidiertL = True
    global iL
    
    # ersterfasste Geschwindigkeit und Spot festlegen
    global geschwL
    if iL == 0:
        geschwL = pace
        iL += 1
        return 50
        

    # Algorithmus
    if iL < geschwL:
        
        if PosX < 15:
            return 15
        
        PosX = PosX + 20     
        iL += 1
        return PosX
    else:
        kollidiertL = False
        iL = 0
        return PosX

####################################Wand########################################
###################################Rechts#######################################
################################################################################

def paceFunR(dif):
    ergebnis = (round(dif/4)) + 1
    return ergebnis

# Wall Collision Rechts
def wallCollR(pace, PosX):
    
    global kollidiertR
    kollidiertR = True
    global iR
    
    # ersterfasste Geschwindigkeit und Spot festlegen
    global geschwR
    if iR == 0:
        geschwR = pace
        iR += 1
        return 950
        

    # Algorithmus
    if iR < geschwR:
        
        if PosX > 985:
            return 985
        
        PosX = PosX - 20     
        iR += 1
        return PosX
    else:
        kollidiertR = False
        iR = 0
        return PosX

##################################Wand##########################################
##################################Oben##########################################
################################################################################

# Pace Berechnung Links
def paceFunO(dif):
    ergebnis = (round(dif/2) * (-1)) + 1
    return ergebnis

# Wall Collision Links
def wallCollO(pace, PosY):
    
    global kollidiertO
    kollidiertO = True
    global iO
    
    # ersterfasste Geschwindigkeit und Spot festlegen
    global geschwO
    if iO == 0:
        geschwO = pace
        iO += 1
        return 50
        

    # Algorithmus
    if iO < geschwO:
        
        if PosY < 15:
            return 15
        
        PosY = PosY + 20     
        iO += 1
        return PosY
    else:
        kollidiertO = False
        iO = 0
        return PosY

###################################Wand#########################################
###################################Unten#########################################
################################################################################

def paceFunU(dif):
    ergebnis = (round(dif/4)) + 1
    return ergebnis

# Wall Collision Rechts
def wallCollU(pace, PosY):
    
    global kollidiertU
    kollidiertU = True
    global iU
    
    # ersterfasste Geschwindigkeit und Spot festlegen
    global geschwU
    if iU == 0:
        geschwU = pace
        iU += 1
        return 650
        

    # Algorithmus
    if iU < geschwU:
        
        if PosY > 685:
            return 685
        
        PosY = PosY - 20     
        iU += 1
        return PosY
    else:
        kollidiertU = False
        iU = 0
        return PosY

################################################################################
###############################Geschoss#########################################
################################################################################

def GeschossY(gesY, rnd):
    global merkeY
    
    if gesY < 0:
        gesY = 700
        return gesX
    else:
        if gesY == 700:
            merkeY = 700
            global ranGesY
            ranGesY = rnd

        merkeY = merkeY - ranGesY
        return merkeY


def GeschossX(gesX, rnd):
    global merkeX
    
    if (gesX < 0) | (gesX > 1000):
        gesX = 500
        return gesX
    else:
        if gesX == 500:
            merkeX = 500
            global ranGesX
            ranGesX = rnd

        merkeX = merkeX - (ranGesX)
        return merkeX
    
# While Var
game_over = False

################################################################################
################################MainFun#########################################
################################################################################

# Schleife
while not game_over:

    # Zuweisungen
    value_X = bus.read_byte_data(address, Ana_X)
    value_Y = bus.read_byte_data(address, Ana_Y)

    PosX = player_pos[0]
    PosY = player_pos[1]

    # Algorithmus
    if x != value_X:
        dif = value_X - x
        PosX = PosX + dif
        player_color = WHITE
        
        # Wand Kollision Links
        if (PosX < 15) | (kollidiertL == True):
            # Farbänderung
            if anzLoop % 2 == 0:
                player_color = RED
            else:
                player_color = WHITE

            # Funktionsaufrufe
            pace = paceFunL(dif)
            PosX = wallCollL(pace, PosX)

        # Wand Kollision Rechts
        elif (PosX > 985) | (kollidiertR == True):
            # Farbänderung
            if anzLoop % 2 == 0:
                player_color = RED
            else:
                player_color = WHITE

            # Funktionsaufrufe
            pace = paceFunR(dif)
            PosX = wallCollR(pace, PosX)

    if y != value_Y:
        dif = (y - value_Y) * (-1)
        PosY = PosY + dif
        player_color = WHITE

        # Wand Kollision Oben
        if (PosY < 15) | (kollidiertO == True):
            # Farbänderung
            if anzLoop % 2 == 0:
                player_color = RED
            else:
                player_color = WHITE

            # Funktionsaufrufe
            pace = paceFunO(dif)
            PosY = wallCollO(pace, PosY)

        # Wand Kollision Unten
        elif (PosY > 685) | (kollidiertU == True):

            # Farbänderung
            if anzLoop % 2 == 0:
                player_color = RED
            else:
                player_color = WHITE

            # Funktionsaufrufe
            pace = paceFunU(dif)
            PosY = wallCollU(pace, PosY)

    player_pos = [PosX, PosY]
################################################################################
###################################Gegner 1#####################################
################################################################################
            
    G1_X = gegner1_pos[0]
    G1_Y = gegner1_pos[1]

    if PosX < G1_X:
        G1_X = G1_X - 10
    elif PosX > G1_X:
        G1_X = G1_X + 10
    if PosY < G1_Y:
        G1_Y = G1_Y - 10
    if PosY > G1_Y:
        G1_Y = G1_Y + 10

    gegner1_pos = [G1_X, G1_Y]

################################################################################
##############################Gegner1 Kollision#################################
################################################################################

    DisX = PosX - G1_X
    if DisX < 0:
        DisX = DisX * (-1)

    DisY = PosY - G1_Y
    if DisY < 0:
        DisY = DisY * (-1)

    Dis = math.sqrt((DisX * DisX) + (DisY * DisY))

    if Dis < 30:
        print("GAME OVER")
        #quit()
        game_over = True

################################################################################
##############################Geschoss##########################################
################################################################################

    valuesX = [2, 4, 6, 8, 10]
    valuesY = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    rnd1 = (random.choice(valuesY)) * 2
    rnd2 = (random.choice(valuesX)) * 2
    
    gesX = geschoss_pos[0]
    gesY = geschoss_pos[1]

    gesX = GeschossX(gesX, rnd1)
    if gesX == 500:
        gesY = 700
        
    gesY = GeschossY(gesY, rnd2)
    if gesY == 700:
        gesX = 500

    geschoss_pos = [gesX, gesY]

################################################################################
###########################Geschoss Kollision###################################
################################################################################
    
    GeX = PosX - gesX
    if GeX < 0:
        GeX = GeX * (-1)
    
    GeY = PosY - gesY
    if GeY < 0:
        GeY = GeY * (-1)

    Dis = math.sqrt((GeX * GeX) + (GeY * GeY))

    if Dis < 30:
        print("GAME OVER")
        #quit()
        game_over = True
            
################################################################################
################################################################################
################################################################################
    
    # Formen
    screen.fill((0, 0, 0))
    
    # Bälle
    pygame.draw.circle(screen, player_color, (player_pos[0], player_pos[1]), player_size) # Player
    pygame.draw.circle(screen, RED, (gegner1_pos[0], gegner1_pos[1]), gegner1_size) # Gegner1
    pygame.draw.circle(screen, GREEN, (geschoss_pos[0], geschoss_pos[1]), geschoss_size) # Geschoss
    pygame.draw.ellipse(screen, BLUE, [450, 670, 100, 80]) # Atellerie
    
    # Wände
    pygame.draw.line(screen, WHITE, [0, 0], [1000,0], 10) # oben
    pygame.draw.line(screen, WHITE, [0, 0], [0,700], 10) # links
    pygame.draw.line(screen, WHITE, [1000, 0], [1000,700], 10) # rechts
    pygame.draw.line(screen, WHITE, [0, 700], [1000,700], 10) # unten
    
    pygame.display.update()

    anzLoop += 1
    
    time.sleep(0.04)


