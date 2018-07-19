#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#I will write all parts of program in one file and 
#I hope that you will put this program into modules and make order

#So i will import Pygame and sys

import pygame, sys

#I will import my modules
import init_dimensions
# import init_drawing
from Settings import *



class Game:  
    def __init__(self):
        # initialize game window etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTHSCREEN, HEIGHTSCREEN))
        pygame.display.set_caption("Neuros")
        self.clock = pygame.time.Clock()
        
        self.running = True
    
    def new(self):
        # start a new game
        pass
        
    def run(self):
        # Gameloop      
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
                  
    def update(self):
        # Gameloop - Update
        pass
    
    def events(self):
        # Gameloop - Events
        for event in pygame.event.get():
        
            #Exit
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def draw(self):
        # Gameloop - Draw
        self.screen.fill(background_color)
        
        for i in range(0,6):
            for ii in range(0,10):
                texture = pygame.Rect(left_x_list[i][ii], up_y_list[i], widthcard, heightcard)
                pygame.draw.rect(self.screen, PLACE_FOR_CARD_COLOR[i], texture)

        for i in range(0,2):
            texture = pygame.Rect(up_deck_list_left_x[i], up_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
            texture = pygame.Rect(down_deck_list_left_x[i], down_deck_up_y, widthcard, heightcard)
            pygame.draw.rect(self.screen, DECK_LINE_COLOR, texture)
        
        pygame.display.flip()
    
    def show_start_screen(self):
        # Loads the start screen
        pass
    
    def game_over_screen(self):
        # Loads the game over screen
        pass
    
    def connect_to_server(self):
        # Connect to server
        pass
    
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over_screen()
    
pygame.quit()

            
         
    
    
    
