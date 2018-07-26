#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from init_dimensions import *
import pygame

class Card:

    def __init__ (self,
                  name ="", 
                  attack = 0, 
                  hp = 0, 
                  frozen_time = 0, 
                  image = 0, 
                  big_image = 0, 
                  reveal = False, 
                  clicked = False, 
                  reveal_turn = False
                  ):
        self.attack = attack
        self.hp = hp
        self.frozen_time = frozen_time
        self.name = name
        self.image = image
        self.big_image = big_image
        self.clicked = clicked
        self.reveal = reveal
        self.reveal_turn = reveal_turn
        pygame.init()
    def __str__(self):
        return self.name

    def get_data(self):
        card_info = {
            "name" : self.name,
            "atk" : self.attack,
            "hp" : self.hp,
            "frozen_time" : self.frozen_time,
            "reveal" : self.reveal
        }

        return card_info

    def double_attack(self):
        self.attack = self.attack*2

    def double_hp(self):
        self.hp = self.hp*2

    def end_turn_minus_frozen(self, barracks):
        for i in range(10):
            if barracks[i] != None:
                barracks[i].frozen_time -= 1

    def return_data(self, data):
        attacks = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        defese = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        barracks = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }

        
        for i in range(10):
            if data["attack_area"][str(i)] == None:
                attacks[i] = None
            else:
                letter = list(data["attack_area"][str(i)]["name"])
                if letter[0] == "2":
                    dot = ".jpg"
                else:
                    dot = ".png"
                attacks[i] = Card(
                    letter[0],
                    data["attack_area"][str(i)]["atk"],
                    data["attack_area"][str(i)]["hp"],
                    data["attack_area"][str(i)]["frozen_time"],
                    pygame.image.load("graphics/" + letter[0] + dot),
                    pygame.image.load("graphics/big_" + letter[0] + dot),
                    data["attack_area"][str(i)]["reveal"]
                )
        
        for i in range(10):
            if data["defense_area"][str(i)] == None:
                defese[i] = None
            else:
                letter = list(data["defense_area"][str(i)]["name"])
                if letter[0] == "2":
                    dot = ".jpg"
                else:
                    dot = ".png"
                defese[i] = Card(
                    letter[0],
                    data["defense_area"][str(i)]["atk"],
                    data["defense_area"][str(i)]["hp"],
                    data["defense_area"][str(i)]["frozen_time"],
                    pygame.image.load("graphics/" + letter[0] + dot),
                    pygame.image.load("graphics/big_" + letter[0] + dot),
                    data["defense_area"][str(i)]["reveal"]
                )

        for i in range(10):
            if data["barracks_area"][str(i)] == None:
                barracks[i] = None
            else:
                letter = list(data["barracks_area"][str(i)]["name"])
                if letter[0] == "2":
                    dot = ".jpg"
                else:
                    dot = ".png"
                barracks[i] = Card(
                    letter[0],
                    data["barracks_area"][str(i)]["atk"],
                    data["barracks_area"][str(i)]["hp"],
                    data["barracks_area"][str(i)]["frozen_time"],
                    pygame.image.load("graphics/" + letter[0] + dot),
                    pygame.image.load("graphics/big_" + letter[0] + dot),
                    data["barracks_area"][str(i)]["reveal"]
                )

        dick = {
            "attacks" : attacks,
            "defense" : defese,
            "barracks" : barracks
        }

        return dick


                


    

    