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
        #Robię słownik, który będzie zwracany
        dicti = {
            "barracks" : None,
            "defense" : None,
            "attacks" : None
        }
        #Robię 3 lokalne słowniki
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
        defense = {
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
        #Robię przegląd danych
        print("XDDDDD")
        for i in range(10):
            #Jeśli None to zapisz tam none
            if data["barracks_area"][i] == None:
                barracks[i] = None
            else:
                #To jest pobranie pierwszej litery, czyli wartość karty np. "9" albo "2"
                letter = list(data["barracks_area"][i][name])
                #"2" ma inne rozszerzenie obrazka
                if letter[0] == "2":
                    rozszerzenie = ".jpg"
                else:
                    rozszerzenie = ".png"
                #Tutaj tworzę obiekt
                barracks[i] =      Card(data["barracks_area"][i][name],
                                        data["barracks_area"][i][atk], 
                                        data["barracks_area"][i][hp], 
                                        data["barracks_area"][i][frozen_time], 
                                        pygame.image.load("graphics/" + letter[0] + rozszerzenie), 
                                        pygame.image.load("graphics/big_" + letter[0] + rozszerzenie), 
                                        data["barracks_area"][i][reveal])
            #Powtarzam kod dla innych stref
            if data["defense_area"][i] == None:
                defense[i] = None
            else:
                letter = list(data["defense_area"][i][name])
                if letter[0] == "2":
                    rozszerzenie = ".jpg"
                else:
                    rozszerzenie = ".png"
                defense[i] =       Card(data["defense_area"][i][name],
                                        data["defense_area"][i][atk], 
                                        data["defense_area"][i][hp], 
                                        data["defense_area"][i][frozen_time], 
                                        pygame.image.load("graphics/" + letter[0] + rozszerzenie), 
                                        pygame.image.load("graphics/big_" + letter[0] + rozszerzenie), 
                                        data["defense_area"][i][reveal])
            if data["attack_area"][i] == None:
                attacks[i] = None
            else:
                letter = list(data["attack_area"][i][name])
                if letter[0] == "2":
                    rozszerzenie = ".jpg"
                else:
                    rozszerzenie = ".png"
                attacks[i] =       Card(data["attack_area"][i][name],
                                        data["attack_area"][i][atk], 
                                        data["attack_area"][i][hp], 
                                        data["attack_area"][i][frozen_time], 
                                        pygame.image.load("graphics/" + letter[0] + rozszerzenie), 
                                        pygame.image.load("graphics/big_" + letter[0] + rozszerzenie), 
                                        data["attack_area"][i][reveal])
        #Teraz uzupełniam słownik, który da mi odpowiednie dane                                
        dicti["barracks"] = barracks
        dicti["defense"] = defense
        dicti["attacks"] = attacks
        return dicti



                


    

    