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

    def __init__(
                self, 
                screen, 
                hand_area = 0,
                hand_list_of_left_x = [],
                hand_list_of_right_x = [], 
                hand_up_y = 0,
                hand_down_y = 0,
                beetwen_card = 0):
    
        self.screen = screen
        self.player = Player()
        self.hand_area = hand_area
        self.hand_list_of_left_x = hand_list_of_left_x
        self.hand_list_of_right_x = hand_list_of_right_x
        self.hand_up_y = hand_up_y
        self.hand_down_y = hand_down_y
        self.beetwen_card = beetwen_card

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
        self.screen.blit(deck_image, (up_deck_list_left_x[0], up_deck_up_y))
        self.screen.blit(deck_image, (down_deck_list_left_x[0], down_deck_up_y))

    def draw_hand(self):
        self.hand_list_of_left_x = []
        self.hand_list_of_right_x = []
        self.hand_area = WIDTHSCREEN - widthmargin*6
        self.beetwen_card = self.hand_area / len(self.player.hand)
        self.hand_up_y = y + (heightmargin*9) + (heightcard*9) + bigheightmargin
        self.hand_down_y = y + (heightmargin*9) + (heightcard*10) + bigheightmargin
        for i in range(len(self.player.hand)-1):
            self.hand_list_of_left_x.append(widthmargin*3 + self.beetwen_card * i)
            self.hand_list_of_right_x.append(self.hand_list_of_left_x[i] + widthcard)
            self.screen.blit(self.player.hand[i].image, (self.hand_list_of_left_x[i], self.hand_up_y))

    def draw_right_from_hand(self):
        position = pygame.mouse.get_pos()
        if self.hand_list_of_left_x[2] > self.hand_list_of_right_x[1]:
            for i in range(len(self.player.hand)-2):
                if position[0] > self.hand_list_of_left_x[i] and position[0] < self.hand_list_of_left_x[i+1]:
                    if position[1] < self.hand_down_y and position[1] > self.hand_up_y:
                        self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))
            last = len(self.player.hand-1)
            if position[0] > self.hand_list_of_left_x[last] and position[0] < self.hand_list_of_right_x[last]:
                 if position[1] < self.hand_down_y and position[1] > self.hand_up_y:   
                       self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))         
        else:
            for i in range(len(self.player.hand)-1):
                if position[0] > self.hand_list_of_left_x[i] and position[0] < self.hand_list_of_right_x[i]:
                    if position[1] < self.hand_down_y and position[1] > self.hand_up_y:
                        self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))

            

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



