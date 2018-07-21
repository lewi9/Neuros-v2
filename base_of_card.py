from card import *
import pygame
color_cards = ["_c", "_d", "_s", "_h"]

#Celowo nie użyłem for, ponieważ to baza kart i musi być łatwa zmiana statystyk
#Wiem, że byłoby szybciej, ale potem mogłoby być nieczytelne, a to jest bardzo ważne miejsce

#define nine card

nine = []
for i in range(4):
    nine.append(Card("9" + color_cards[i], 9, 9, 1 , pygame.image.load("graphics/9.png"), pygame.image.load("graphics/big_9.png"))) 

two = []
for i in range(4):
    two.append(Card("2" + color_cards[i], 2, 2, 1 , pygame.image.load("graphics/2.jpg"), pygame.image.load("graphics/big_2.jpg"))) 

three = []
for i in range(4):
    three.append(Card("3" + color_cards[i], 3, 3, 0 , pygame.image.load("graphics/3.png"), pygame.image.load("graphics/big_3.png"))) 

four = []
for i in range(4):
    four.append(Card("4" + color_cards[i], 4, 4, 1 , pygame.image.load("graphics/4.png"), pygame.image.load("graphics/big_4.png"))) 

five = []
for i in range(4):
    five.append(Card("5" + color_cards[i], 5, 5, 0 , pygame.image.load("graphics/5.png"), pygame.image.load("graphics/big_5.png"))) 

six = []
for i in range(4):
    six.append(Card("6" + color_cards[i], 6, 6, 1 , pygame.image.load("graphics/6.png"), pygame.image.load("graphics/big_6.png"))) 

seven = []
for i in range(4):
    seven.append(Card("7" + color_cards[i], 7, 7, 1 , pygame.image.load("graphics/7.png"), pygame.image.load("graphics/big_7.png"))) 

eight = []
for i in range(4):
    eight.append(Card("8" + color_cards[i], 8, 8, 1 , pygame.image.load("graphics/8.png"), pygame.image.load("graphics/big_8.png"))) 

ten = []
for i in range(4):
    ten.append(Card("10" + color_cards[i], 10, 10, 1 , pygame.image.load("graphics/10.png"), pygame.image.load("graphics/big_10.png"))) 

jack = []
for i in range(4):
    jack.append(Card("j" + color_cards[i], 2, 11, 1 , pygame.image.load("graphics/j.png"), pygame.image.load("graphics/big_j.png"))) 

queen = []
for i in range(4):
    queen.append(Card("9" + color_cards[i], 12, 12, 1 , pygame.image.load("graphics/q.png"), pygame.image.load("graphics/big_q.png"))) 

king = []
for i in range(4):
    king.append(Card("9" + color_cards[i], 13, 13, 2 , pygame.image.load("graphics/k.png"), pygame.image.load("graphics/big_k.png"))) 

ace = []
for i in range(4):
    ace.append(Card("9" + color_cards[i], 14, 14, 1 , pygame.image.load("graphics/a.png"), pygame.image.load("graphics/big_a.png"))) 


list_of_card = [
    two, 
    three, 
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten,
    jack,
    queen,
    king,
    ace
    ]
