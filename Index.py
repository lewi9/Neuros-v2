#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#I will write all parts of program in one file and 
#I hope that you will put this program into modules and make order

#Dziękujemy Czajce, że pomógł mi odkryć błąd w idei tworzenia obiektów klasy Card oraz zasugerował inne miniaturki

#So i will import Pygame and sys

import pygame, sys
import pprint
import threading
import socket

#I will import my modules
from init_dimensions import *
from drawings import DrawObjects
from client_test_button import *
from Settings import *
from enter_ip import IpInput
from MakeButton import Button 
from card import Card
from base_of_card import *
from player import Player
from gameclient import GameClient


class Game:  
    def __init__(self):
        # initialize game window etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTHSCREEN, HEIGHTSCREEN)) # tworzymy wielkość ekranu
        pygame.display.set_caption("Neuros") # nadajemy nazwe ekranu
        self.clock = pygame.time.Clock() # nie wiem jak to działa ale pozwala na fps
        
        self.running = True 
        self.player = Player()
        self.card = Card()

        self.player1_data = {}
        self.player2_data = {}

        self.player1_data_for_sending = {}
        self.player2_data_for_sending = {}

        self.game_data = {}
        self.enemy_name = ""

        self.drawer = DrawObjects(self.screen) 
        self.ipscreen = IpInput(self.screen)

        self.mouse_position = None
        self.hovered_hero = False
        self.hovered_yhero = False

        self.end_turn = Button(self.screen, card_viev_left_x, down_deck_up_y, 210, heightcard)
        self.end_turn.set_text("END TURN")
        self.end_turn.set_text_color(CYAN)
        self.end_turn.set_button_color(BLACK)
        self.end_turn.set_text_size(30)
            
    def new(self):
        # start a new game
        self.connect_to_server(ip = self.ip) 
        self.barracks_put = 0
        self.player.fill_deck()
        self.player.shuffle_deck()
        self.player.prepare_hand()
        self.run()
        
    def run(self):
        # Gameloop      
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)

            self.update()
            # print(self.game_data[self.player.player_name]["myTurn"])
            self.events()
            self.draw()

            try:
                # updates client-side data and waits for it to be sent (delay 0.5 sec)
                if self.player.player_name == "Player_1":
                    self.connection.update_player1_data_to_be_sent(self.player1_data_for_sending) 
                    self.connection.update_player2_data_to_be_sent(self.player2_data_for_sending) 
                elif self.player.player_name == "Player_2":
                    self.connection.update_player2_data_to_be_sent(self.player2_data_for_sending) 
                    self.connection.update_player1_data_to_be_sent(self.player1_data_for_sending) 

            except BrokenPipeError:
                pass
            
        try: # kiedy gameloop się skończył, ten kod jest do odłaćzenia się z serwer'em
            self.connection.listening = False
            self.connection.sending = False
            self.connection.shutdown(socket.SHUT_WR)
            self.connection.close()
        except OSError: # jak mi ten error wywali to ma iść dalej
            pass

    def update(self):
        # Gameloop - Update

        # update game data

        # This block checks if there is a connection. If there is a conection then
        # It updates the game data with the connection
        if self.connection.recv_player1_data != None:
            self.player1_data["Player_1"] = self.connection.recv_player1_data
            if self.player1_data:
                self.game_data.update(self.player1_data)		

        # This block checks if there is a connection. If there is a conection then
        # It updates the game data with the connection
        if self.connection.recv_player2_data != None:
            self.player2_data["Player_2"] = self.connection.recv_player2_data
            if self.player2_data: # checks if enemy data exists
                self.game_data.update(self.player2_data)


        # this checks the player name and makes changes to the game data based on game events and updates
        if self.player.player_name == "Player_1":
            data = self.player.player_data()
            self.player1_data_for_sending = data
            self.game_data[self.player.player_name] = data
 
        # this checks the player name and makes changes to the game data based on game events and updates
        elif self.player.player_name == "Player_2":
            data = self.player.player_data()
            self.player2_data_for_sending = data
            self.game_data[self.player.player_name] = data

        if self.player2_data and self.player1_data:
            self.enemy_areas = self.card.return_data(self.game_data[self.enemy_name])

        # This updates the opponent/enemies' game data
        if self.game_data:
            if self.player.player_name == "Player_1":
                try: # produces keyerror if hasn't recieved data from opponent
                    self.player2_data_for_sending = self.game_data[self.enemy_name]
                except KeyError:
                    pass

            elif self.player.player_name == "Player_2":
                try: # produces keyerror if hasn't recieved data from opponent
                    self.player1_data_for_sending = self.game_data[self.enemy_name]
                except KeyError:
                    pass


        # pp = pprint.PrettyPrinter()
        # pp.pprint(self.game_data)
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def events(self):
        # Gameloop - Events
        for event in pygame.event.get():
        
            #Exit
            if event.type == pygame.QUIT:
                print(self.enemy_name)
                if self.playing:
                    self.playing = False
                self.running = False

            # event który sprawdza czy test button był naciśnięty
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                clicked = wasclicked(mouse)
                self.player.reveal_defense(mouse)
                self.player.move_from_barracks_to_attacks(mouse, self.player)
                self.barracks_put = self.player.place_card(mouse, self.player, self.barracks_put )
                self.player.was_clicked_in_hand(mouse,
                                                self.drawer.hand_list_of_left_x,
                                                self.drawer.hand_list_of_right_x,
                                                self.drawer.hand_up_y,
                                                self.drawer.hand_down_y,
                                                self.player
                                                )
                self.player.was_clicked_in_barracks(mouse, self.player)

                if clicked:
                    self.player.draw_card()
                    print(len(self.player.deck))

                if self.end_turn.wasclicked(mouse):
                    print("Now is your enemies turn")
                    self.player.end_turn()
                    self.player.draw_card()
                    self.barracks_put = 0
                    data = self.player.player_data()
                    #print(data)


    def draw(self):
        # Gameloop - Draw

        self.screen.fill(BACKGROUND_COLOR)
        self.drawer.draw_board()
        self.drawer.draw_hand()
        self.drawer.draw_player_area_cards(self.player.attacks,
                                           self.player.defense,
                                           self.player.barracks)
        if self.player2_data and self.player1_data:
            self.drawer.draw_enemy_area_cards(self.enemy_areas["attacks"],
                                              self.enemy_areas["defense"],
                                              self.enemy_areas["barracks"])
            self.drawer.draw_right_from_enemy_areas(self.enemy_areas["attacks"],
                                                    self.enemy_areas["defense"],
                                                    self.enemy_areas["barracks"])
        self.drawer.draw_right_from_hand()
        self.drawer.draw_right_from_areas(self.player)
        self.drawer.blit_hero()
        #jest tylko testowy jeżeli przeszkadza to ta funkcja jest w client_test_button.py
        draw_test_button(self.screen, self.player.player_name)
        
        #This is End Turn Button
        self.end_turn.create()
           
        pygame.display.flip()

    def show_start_screen(self):
        # Loads the start screen        
        self.screen.fill(WHITE)

        self.drawer.draw_text("WELCOME TO NEUROS", 48, RED, WIDTHSCREEN / 2, 100)
        self.drawer.draw_text("PLEASE ENTER IP", 25, BLACK, 215, 180)

        self.ipscreen.draw_input_box()
        self.ipscreen.draw_ip_text()
        
        self.dev = Button(self.screen, 600, 600, 170, 50)
        self.dev.set_text("Dev: Wejdz do gry")
        self.dev.set_text_size(15)
        self.dev.create()

        self.ipscreen.createButtons()

        pygame.display.flip()
        self.wait_for_user()


    def game_over_screen(self):
        # Loads the game over screen
        pass

    def wait_for_user(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    clicked_dev = self.dev.wasclicked(mouse)

                    self.ipscreen.check_if_pressed(mouse)
                    self.ip = self.ipscreen.enter_button_pressed(mouse)

                    if clicked_dev or self.ip:
                        waiting = False
                
                if event.type == pygame.MOUSEBUTTONUP:
                    self.ipscreen.createButtons()

            self.ipscreen.draw_input_box()
            self.ipscreen.draw_ip_text()
            pygame.display.flip()
                        
    def connect_to_server(self, ip = "localhost", port = PORT):
        # Connect to server
        if not ip:
            ip = "localhost"

        self.connection = GameClient(ip, port)
        self.player.player_name = self.connection.get_received_name()

        if self.player.player_name == "Player_1":
            self.enemy_name = "Player_2"
        elif self.player.player_name == "Player_2":
            self.enemy_name = "Player_1"

g = Game()

while g.running:
    g.show_start_screen()
    g.new()
    g.game_over_screen()
    
pygame.quit()


    
    
    
