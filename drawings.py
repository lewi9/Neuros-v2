#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
import init_dimensions
from Settings import *


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
        """Draw the playing arena"""
        for i in range(6):
            for ii in range(10):
                texture = pygame.Rect(left_x_list[i][ii], up_y_list[i], widthcard, heightcard)
                pygame.draw.rect(self.screen, PLACE_FOR_CARD_COLOR[i], texture)

        for i in range(3):
            texture = pygame.Rect(up_deck_list_left_x[i], up_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
            texture = pygame.Rect(down_deck_list_left_x[i], down_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
        texture = pygame.Rect(init_dimensions.card_viev_left_x, init_dimensions.card_view_up_y, 210, 300)    
        pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
        
        self.draw_square((0,0,0), init_dimensions.card_viev_left_x, 600, 210, 50)
        self.draw_text("END TURN", 30, CYAN, 690, 625 )



    def draw_text(self, text, size, color, x, y):
        """This draws a text in pygame. The x and y is the center of the text"""
        font = pygame.font.SysFont("monospace", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_square(self, color, x, y, length, height):
        """This draws a square"""
        button = pygame.Rect(x, y, length, height)
        pygame.draw.rect(self.screen, color, button)



