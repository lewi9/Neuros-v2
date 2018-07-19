#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
import init_dimensions
from Settings import DECK_LINE_COLOR, PLACE_FOR_CARD_COLOR


#import varbiables
left_x_list = init_dimensions.left_x_list
up_y_list = init_dimensions.up_y_list
widthcard = init_dimensions.widthcard
heightcard = init_dimensions.heightcard
up_deck_list_left_x = init_dimensions.up_deck_list_left_x
up_deck_up_y = init_dimensions.up_deck_up_y
down_deck_list_left_x = init_dimensions.down_deck_list_left_x
down_deck_up_y = init_dimensions.down_deck_up_y


class DrawObjects:
    """Ta klasa służy do ułatwienia rysowania obiektów"""

    def __init__(self, screen):
        self.screen = screen

    def draw_board(self):
        for i in range(6):
            for ii in range(10):
                texture = pygame.Rect(left_x_list[i][ii], up_y_list[i], widthcard, heightcard)
                pygame.draw.rect(self.screen, PLACE_FOR_CARD_COLOR[i], texture)

        for i in range(2):
            texture = pygame.Rect(up_deck_list_left_x[i], up_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
            texture = pygame.Rect(down_deck_list_left_x[i], down_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)



