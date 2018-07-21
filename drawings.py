#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
from init_dimensions import *
from Settings import *
from card import Card
from player import Player
from base_of_card import *

class DrawObjects:
    """Ta klasa służy do ułatwienia rysowania obiektów"""

    def __init__(self, screen, hand_area = 0):
        self.screen = screen
        self.player = Player()
        self.hand_area = hand_area

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
        texture = pygame.Rect(card_viev_left_x, card_view_up_y, 210, 300)    
        pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
        

        self.screen.blit(hero, (up_deck_list_left_x[1], up_deck_up_y))
        self.screen.blit(yhero, (down_deck_list_left_x[1], down_deck_up_y))

    def draw_hand(self):
        #In building - don't move it!
        self.hand_area = WIDTHSCREEN - widthmargin*6

        for i in range(len(self.player.hand)):
            pass

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



