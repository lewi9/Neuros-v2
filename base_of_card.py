from card import *
import pygame


#Celowo nie użyłem for, ponieważ to baza kart i musi być łatwa zmiana statystyk
#Wiem, że byłoby szybciej, ale potem mogłoby być nieczytelne, a to jest bardzo ważne miejsce

#define nine card
nine = Card("9",9,9,1)
nine.image = pygame.image.load("graphics/9.png")
nine.big_image = pygame.image.load("graphics/big_9.png")

#define 2 card
two = Card("2",2,2,1)
two.image = pygame.image.load("graphics/2.jpg")
two.big_image = pygame.image.load("graphics/big_2.jpg")
#define 3 card
three = Card("3",3,3,0)
three.image = pygame.image.load("graphics/3.png")
three.big_image = pygame.image.load("graphics/big_3.png")
#define 4 card
four= Card("4",4,4,1)
four.image = pygame.image.load("graphics/4.png")
four.big_image = pygame.image.load("graphics/big_4.png")
#define 5 card
five= Card("5",5,5,0)
five.image = pygame.image.load("graphics/5.png")
five.big_image = pygame.image.load("graphics/big_5.png")
#define 6 card
six= Card("6",6,6,1)
six.image = pygame.image.load("graphics/6.png")
six.big_image = pygame.image.load("graphics/big_6.png")
#define 7 card
seven= Card("7",7,7,1)
seven.image = pygame.image.load("graphics/7.png")
seven.big_image = pygame.image.load("graphics/big_7.png")
#define 8 card
eight= Card("8",8,8,1)
eight.image = pygame.image.load("graphics/8.png")
eight.big_image = pygame.image.load("graphics/big_8.png")
#define 10 card
ten= Card("10",10,10,1)
ten.image = pygame.image.load("graphics/10.png")
ten.big_image = pygame.image.load("graphics/big_10.png")
#define jack
jack= Card("J",2,11,1)
jack.image = pygame.image.load("graphics/j.png")
jack.big_image = pygame.image.load("graphics/big_j.png")
#define queen
queen= Card("Q",12,12,1)
queen.image = pygame.image.load("graphics/q.png")
queen.big_image = pygame.image.load("graphics/big_q.png")
#define king
king= Card("K",13,13,2)
king.image = pygame.image.load("graphics/k.png")
king.big_image = pygame.image.load("graphics/big_k.png")
#define ace = card()
ace = Card("A",14,14,1)
ace.image = pygame.image.load("graphics/a.png")
ace.big_image = pygame.image.load("graphics/big_a.png")

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