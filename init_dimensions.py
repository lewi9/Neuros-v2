#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Settings import WIDTHSCREEN, HEIGHTSCREEN

#Sizes
onewidhtunit = WIDTHSCREEN/130
oneheightunit = HEIGHTSCREEN/115

widthmargin = onewidhtunit * 2
heightmargin = oneheightunit
bigheightmargin = oneheightunit * 5
 
#44
widthcard =  onewidhtunit * 7
#60
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
    right_x = x + widthmargin*i + widthcard*i
    right_x_of_card.append(right_x)

#Lists will all screen parameters

#Up Deck
up_deck_list_left_x = [
    x + widthmargin,
    x + widthmargin*2 + widthcard,
    x + (widthmargin*10) + (widthcard*9) 
]
up_deck_down_y = y + (heightmargin*2) + (heightcard*2)
up_deck_list_right_x = [
    x + widthmargin + widthcard,
    x + widthmargin*2 + widthcard*2,
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
    x + widthmargin*2 + widthcard,
    x + (widthmargin*10) + (widthcard*9)
]
down_deck_down_y = y + (heightmargin*8) + (heightcard*9) + bigheightmargin
down_deck_list_right_x = [
    x + widthmargin + widthcard,
    x + widthmargin*2 + widthcard*2,
    x + (widthmargin*10) + (widthcard*10)
]
down_deck_up_y = y + (heightmargin*8) + (heightcard*8) + bigheightmargin 

#Card Viev
card_viev_left_x = x + widthmargin*12 + widthcard*10 
card_view_up_y = 185
card_viev_right_x = 785
card_viev_down_y =  515

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