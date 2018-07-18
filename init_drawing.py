#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
import init_dimensions
pygame.init()

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
#import varbiables
left_x_list = init_dimensions.left_x_list
up_y_list = init_dimensions.up_y_list
widthcard = init_dimensions.widthcard
heightcard = init_dimensions.heightcard
screen = init_dimensions.screen
up_deck_list_left_x = init_dimensions.up_deck_list_left_x
up_deck_up_y = init_dimensions.up_deck_up_y
down_deck_list_left_x = init_dimensions.down_deck_list_left_x
down_deck_up_y = init_dimensions.down_deck_up_y

#Drawing Function
def drawing():
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