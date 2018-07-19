#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#I will write all parts of program in one file and 
#I hope that you will put this program into modules and make order

#So i will import Pygame and sys

import pygame, sys

#I will import my modules
from init_dimensions import *
from drawings import DrawObjects
from client_test_button import *
from Settings import *
from enter_ip import IpInput
from MakeButton import Button 


class Game:  
    def __init__(self):
        # initialize game window etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTHSCREEN, HEIGHTSCREEN)) # tworzymy wielkość ekranu
        pygame.display.set_caption("Neuros") # nadajemy nazwe ekranu
        self.clock = pygame.time.Clock() # nie wiem jak to działa ale pozwala na fps

        self.running = True 

        self.drawer = DrawObjects(self.screen) 
        self.ipscreen = IpInput(self.screen)
            
    def new(self):
        # start a new game
        self.run()

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

            # event który sprawdza czy test button był naciśnięty
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                clicked = wasclicked(mouse)
                if clicked:
                    print("yay it works :D")


    def draw(self):
        # Gameloop - Draw

        self.screen.fill(BACKGROUND_COLOR)

        self.drawer.draw_board()

        #jest tylko testowy jeżeli przeszkadza to ta funkcja jest w client_test_button.py
        draw_test_button(self.screen)
           
        pygame.display.flip()
    
    def show_start_screen(self):
        # Loads the start screen        
        self.screen.fill(WHITE)
        self.drawer.draw_text("WELCOME TO NEUROS", 48, RED, WIDTHSCREEN / 2, 100)
        self.ipscreen.draw_input_box()
        self.ipscreen.draw_ip_text()
        self.dev = Button(self.screen, 600, 600, 170, 50)
        self.dev.set_text("Dev: Wejdz do gry")
        self.dev.set_text_size(15)
        self.dev.create()

        pygame.display.flip()
        self.wait_for_user()
    
    def game_over_screen(self):
        # Loads the game over screen
        pass

    def wait_for_user(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    clicked = self.dev.wasclicked(mouse)
                    if clicked:
                        waiting = False
                        
    def connect_to_server(self):
        # Connect to server
        pass
    
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over_screen()
    
pygame.quit()

            
         
    
    
    
