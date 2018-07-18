#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#I will write all parts of program in one file and 
#I hope that you will put this program into modules and make order

#So i will import Pygame and sys

import pygame, sys

pygame.init()


#I will set screen

#Screen size
widthscreen = 810
heightscreen = 690

#Screen set
screen = pygame.display.set_mode((widthscreen, heightscreen))
screen.fill((30,0,0))

#Sizes
onewidhtunit = widthscreen/130
oneheightunit = heightscreen/115

widthmargin = onewidhtunit * 2
heightmargin = oneheightunit
bigheightmargin = oneheightunit * 5
 
widthcard =  onewidhtunit * 7
heightcard =  oneheightunit * 10


x=0
y=0

#Lists will all screen parameters


#Up Deck
up_deck_list_left_x = [
    x + widthmargin,
    x + (widthmargin*10) + (widthcard*9) 
]

up_deck_down_y = y + (heightmargin*2) + (heightcard*2)



up_deck_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*10) + (widthcard*10)

]

up_deck_up_y = y + (heightmargin*2) + heightcard
 

#Up Barrack
up_barrack_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)
]

up_barrack_down_y = y + (heightmargin*3) + (heightcard*3)

up_barrack_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

up_barrack_up_y = y + (heightmargin*3) + (heightcard*2)

#Up Defense
up_defense_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)

]

up_defense_down_y = y + (heightmargin*4) + (heightcard*4)

up_defense_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

up_defense_up_y = y + (heightmargin*4) + (heightcard*3)

#Up Attack
up_attack_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)
]

up_attack_down_y = y + (heightmargin*5) + (heightcard*5)

up_attack_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

up_attack_up_y = y + (heightmargin*5) + (heightcard*4)

#Down Attack
down_attack_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)
]

down_attack_down_y = y + (heightmargin*5) + (heightcard*6) + bigheightmargin

down_attack_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

down_attack_up_y = y + (heightmargin*5) + (heightcard*5) + bigheightmargin

#Down Defense
down_defense_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)
]

down_defense_down_y = y + (heightmargin*6) + (heightcard*7) + bigheightmargin

down_defense_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

down_defense_up_y = y + (heightmargin*6) + (heightcard*6) + bigheightmargin

#Down Barrack
down_barrack_list_left_x = [
    x+widthmargin,
    x+(widthmargin*2) + widthcard,
    x+(widthmargin*3) + (widthcard*2),
    x+(widthmargin*4) + (widthcard*3),
    x+(widthmargin*5) + (widthcard*4),
    x+(widthmargin*6) + (widthcard*5),
    x+(widthmargin*7) + (widthcard*6),
    x+(widthmargin*8) + (widthcard*7),
    x+(widthmargin*9) + (widthcard*8),
    x+(widthmargin*10) + (widthcard*9)
]

down_barrack_down_y = y + (heightmargin*7) + (heightcard*8) + bigheightmargin

down_barrack_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*2) + (widthcard*2),
    x + (widthmargin*3) + (widthcard*3),
    x + (widthmargin*4) + (widthcard*4),
    x + (widthmargin*5) + (widthcard*5),
    x + (widthmargin*6) + (widthcard*6),
    x + (widthmargin*7) + (widthcard*7),
    x + (widthmargin*8) + (widthcard*8),
    x + (widthmargin*9) + (widthcard*9),
    x + (widthmargin*10) + (widthcard*10)
]

down_barrack_up_y = y + (heightmargin*7) + (heightcard*7) + bigheightmargin

#Down Deck
down_deck_list_left_x = [
    x + widthmargin,
    x + (widthmargin*10) + (widthcard*9)
]

down_deck_down_y = y + (heightmargin*8) + (heightcard*9) + bigheightmargin


down_deck_list_right_x = [
    x + widthmargin + widthcard,
    x + (widthmargin*10) + (widthcard*10)
]

down_deck_up_y = y + (heightmargin*8) + (heightcard*8) + bigheightmargin 



#Drawing Commands
for i in range(0,10):

    if i < 2:
        texture = pygame.Rect(up_deck_list_left_x[i], up_deck_up_y, widthcard, heightcard)
        pygame.draw.rect(screen, (0, 0, 0), texture)
        texture = pygame.Rect(down_deck_list_left_x[i], down_deck_up_y, widthcard, heightcard)
        pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(up_barrack_list_left_x[i], up_barrack_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(up_defense_list_left_x[i], up_defense_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(up_attack_list_left_x[i], up_attack_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(down_attack_list_left_x[i], down_attack_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(down_defense_list_left_x[i], down_defense_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    texture = pygame.Rect(down_barrack_list_left_x[i], down_barrack_up_y,widthcard,heightcard)
    pygame.draw.rect(screen, (0, 0, 0), texture)
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)