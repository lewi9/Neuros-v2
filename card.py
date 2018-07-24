from init_dimensions import *

class Card:

    def __init__ (self, name ="", attack = 0, hp = 0, frozen_time = 0, image = 0, big_image = 0, clicked = False):
        self.attack = attack
        self.hp = hp
        self.frozen_time = frozen_time
        self.name = name
        self.image = image
        self.big_image = big_image
        self.clicked = clicked
    def __str__(self):
        return self.name

    def get_data(self):
        card_info = {
            "name" : self.name,
            "atk" : self.attack,
            "hp" : self.hp,
            "frozen_time" : self.frozen_time,
        }

        return card_info

    def double_attack(self):
        self.attack = self.attack*2

    def double_hp(self):
        self.hp = self.hp*2

    