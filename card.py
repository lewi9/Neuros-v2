class Card:

    def __init__ (self, attack = 0, hp = 0, frozen_time = 0):
        self.attack = attack
        self.hp = hp
        self.frozen_time = frozen_time

    def create_card (self, a, b, c):
        self.attack = a
        self.hp = b
        self.frozen_time = c