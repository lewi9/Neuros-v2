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

#color of screen
background_color = (39, 117, 112)

#Screen set
screen = pygame.display.set_mode((widthscreen, heightscreen))
screen.fill(background_color)

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

#set parameters
left_x_of_card = []

for i in range(0,10):
    left_x = x + widthmargin * (i+1) + widthcard * i
    left_x_of_card.append(left_x)

right_x_of_card = []

for i in range(1,11):
    right_x = x + widthmargin*1 + widthcard*1
    right_x_of_card.append(right_x)

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
up_barrack_list_left_x = left_x_of_card
up_barrack_down_y = y + (heightmargin*3) + (heightcard*3)
up_barrack_list_right_x = right_x_of_card
up_barrack_up_y = y + (heightmargin*3) + (heightcard*2)

#Up Defense
up_defense_list_left_x = left_x_of_card
up_defense_down_y = y + (heightmargin*4) + (heightcard*4)
up_defense_list_right_x = right_x_of_card
up_defense_up_y = y + (heightmargin*4) + (heightcard*3)

#Up Attack
up_attack_list_left_x = left_x_of_card
up_attack_down_y = y + (heightmargin*5) + (heightcard*5)
up_attack_list_right_x = right_x_of_card
up_attack_up_y = y + (heightmargin*5) + (heightcard*4)

#Down Attack
down_attack_list_left_x = left_x_of_card
down_attack_down_y = y + (heightmargin*5) + (heightcard*6) + bigheightmargin
down_attack_list_right_x = right_x_of_card
down_attack_up_y = y + (heightmargin*5) + (heightcard*5) + bigheightmargin

#Down Defense
down_defense_list_left_x = left_x_of_card
down_defense_down_y = y + (heightmargin*6) + (heightcard*7) + bigheightmargin
down_defense_list_right_x = right_x_of_card
down_defense_up_y = y + (heightmargin*6) + (heightcard*6) + bigheightmargin

#Down Barrack
down_barrack_list_left_x = left_x_of_card
down_barrack_down_y = y + (heightmargin*7) + (heightcard*8) + bigheightmargin
down_barrack_list_right_x = right_x_of_card
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

#Colord of place for cards
deck_line_color = (221, 220, 186)
place_for_card_color = [
    (168, 135, 126),
    (181, 254, 249),
    (227, 156, 113),
    (227, 156, 113),
    (181, 254, 249),
    (168, 135, 126)
]
#Lists of dimensions lists
left_x_list = [
    up_barrack_list_left_x,
    up_defense_list_left_x,
    up_attack_list_left_x,
    down_attack_list_left_x,
    down_defense_list_left_x,
    down_barrack_list_left_x
    ]
down_y_list = [
    up_barrack_down_y,
    up_defense_down_y,
    up_attack_down_y,
    down_attack_down_y,
    down_defense_down_y,
    down_barrack_down_y
]
right_x_list = [
    up_barrack_list_right_x,
    up_defense_list_right_x,
    up_attack_list_right_x,
    down_attack_list_right_x,
    down_defense_list_right_x,
    down_barrack_list_right_x
]
up_y_list = [
    up_barrack_up_y,
    up_defense_up_y,
    up_attack_up_y,
    down_attack_up_y,
    down_defense_up_y,
    down_barrack_up_y
]

#Drawing Commands
for i in range(0,6):
    for ii in range(0,10):
        texture = pygame.Rect(left_x_list[i][ii], up_y_list[i], widthcard, heightcard)
        pygame.draw.rect(screen, place_for_card_color[i], texture)

for i in range(0,2):
        texture = pygame.Rect(up_deck_list_left_x[i], up_deck_up_y, widthcard, heightcard)
        pygame.draw.rect(screen, deck_line_color, texture)
        texture = pygame.Rect(down_deck_list_left_x[i], down_deck_up_y, widthcard, heightcard)
        pygame.draw.rect(screen, deck_line_color, texture)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)