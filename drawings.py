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

        "Draw Cards on hand"
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

        "Draw Cards, on right part of screen, from hand"
        position = pygame.mouse.get_pos()
        if len(self.hand_list_of_left_x) > 3:
            if self.hand_list_of_left_x[2] < self.hand_list_of_right_x[1]:
                for i in range(len(self.player.hand)-2):
                    if position[0] > self.hand_list_of_left_x[i] and position[0] < self.hand_list_of_left_x[i+1]:
                        if position[1] < self.hand_down_y and position[1] > self.hand_up_y:
                            self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))
                last = len(self.player.hand) - 2 
                if position[0] > self.hand_list_of_left_x[last] and position[0] < self.hand_list_of_right_x[last]:
                     if position[1] < self.hand_down_y and position[1] > self.hand_up_y:   
                           self.screen.blit(self.player.hand[i+1].big_image, (card_viev_left_x, card_view_up_y))         
        
            else:
                for i in range(len(self.player.hand)-1):
                    if position[0] > self.hand_list_of_left_x[i] and position[0] < self.hand_list_of_right_x[i]:
                        if position[1] < self.hand_down_y and position[1] > self.hand_up_y:
                            self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))
    
        else:
            for i in range(len(self.player.hand)-1):
                if position[0] > self.hand_list_of_left_x[i] and position[0] < self.hand_list_of_right_x[i]:
                    if position[1] < self.hand_down_y and position[1] > self.hand_up_y:
                        self.screen.blit(self.player.hand[i].big_image, (card_viev_left_x, card_view_up_y))
    
    def draw_right_from_areas(self, player):
        position = pygame.mouse.get_pos()
        for i in range(10):
            if position[0] > left_x_of_card[i] and position[0] < right_x_of_card[i]:
                if position[1] < down_attack_down_y and position[1] > down_attack_up_y:
                    if player.attacks[i] != None:
                        self.screen.blit(player.attacks[i].big_image, (card_viev_left_x, card_view_up_y))
                elif position[1] < down_defense_down_y and position[1] > down_defense_up_y:
                    if player.defense[i] != None:
                        self.screen.blit(player.defense[i].big_image, (card_viev_left_x, card_view_up_y))
                elif position[1] < down_barrack_down_y and position[1] > down_barrack_up_y:
                    if player.barracks[i] != None:    
                        self.screen.blit(player.barracks[i].big_image, (card_viev_left_x, card_view_up_y))

    def draw_right_from_enemy_areas(self, attacks, defense, barracks):
        position = pygame.mouse.get_pos()
        for i in range(10):
            if position[0] > left_x_of_card[i] and position[0] < right_x_of_card[i]:
                if position[1] < up_attack_down_y and position[1] > up_attack_up_y:
                    if attacks[i] != None:
                        if attacks[i].reveal != True:
                            self.screen.blit(big_deck, (card_viev_left_x, card_view_up_y))
                        else:
                            self.screen.blit(attacks[i].big_image, (card_viev_left_x, card_view_up_y))
                if position[1] < up_defense_down_y and position[1] > up_defense_up_y:
                    if defense[i] != None:
                        if defense[i].reveal != True:
                            self.screen.blit(big_deck, (card_viev_left_x, card_view_up_y))
                        else:
                            self.screen.blit(defense[i].big_image, (card_viev_left_x, card_view_up_y))
                if position[1] < up_barrack_down_y and position[1] > up_barrack_up_y:
                    if barracks[i] != None:
                        if barracks[i].reveal != True:
                            self.screen.blit(big_deck, (card_viev_left_x, card_view_up_y))
                        else:
                            self.screen.blit(barracks[i].big_image, (card_viev_left_x, card_view_up_y))
            


    def blit_hero(self):
        mouse_position = pygame.mouse.get_pos()

            
        if mouse_position[0] > up_deck_list_left_x[1] and mouse_position[0] < up_deck_list_right_x[1]:
            if mouse_position[1] < up_deck_down_y and mouse_position[1] > up_deck_up_y:
                self.screen.blit(big_hero, (card_viev_left_x, card_view_up_y))
                
            elif mouse_position[1] < down_deck_down_y and mouse_position[1] > down_deck_up_y:
                self.screen.blit(big_yhero, (card_viev_left_x, card_view_up_y))

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

    def draw_player_area_cards(self, attacks, defense, barracks):
        "This Draw a player areas cards"
        for i in range(10):
            if attacks[i] != None:
                if attacks[i].reveal:
                    self.screen.blit(attacks[i].image, (left_x_of_card[i], down_attack_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], down_attack_up_y))
            if defense[i] != None:
                if defense[i].reveal:
                    self.screen.blit(defense[i].image, (left_x_of_card[i], down_defense_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], down_defense_up_y))
            if barracks[i] != None:
                if barracks[i].reveal:
                    self.screen.blit(barracks[i].image, (left_x_of_card[i], down_barrack_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], down_barrack_up_y))
    

    #Tu taka funckja jak u góry, tylko inne parametry
    def draw_enemy_area_cards(self, attacks, defense, barracks):
        
        for i in range(10):
            if attacks[i] != None:
                
                if attacks[i].reveal:
                    self.screen.blit(attacks[i].image, (left_x_of_card[i], up_attack_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], up_attack_up_y))
            if defense[i] != None:
                if defense[i].reveal:
                    self.screen.blit(defense[i].image, (left_x_of_card[i], up_defense_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], up_defense_up_y))
            if barracks[i] != None:
                if barracks[i].reveal:
                    self.screen.blit(barracks[i].image, (left_x_of_card[i], up_barrack_up_y))
                else:
                    self.screen.blit(deck_image, (left_x_of_card[i], up_barrack_up_y))
        


