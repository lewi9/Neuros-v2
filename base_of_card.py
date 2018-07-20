from card import *



#Celowo nie użyłem for, ponieważ to baza kart i musi być łatwa zmiana statystyk
#Wiem, że byłoby szybciej, ale potem mogłoby być nieczytelne, a to jest bardzo ważne miejsce

#name_of_card.create_card(attack, hp, frozen_time)

#define nine card
nine = Card()
nine.create_card(9,9,1)
#define 2 card
two = Card()
two.create_card(2,2,1)
#define 3 card
three = Card()
three.create_card(3,3,0)
#define 4 card
four= Card()
four.create_card(4,4,1)
#define 5 card
five= Card()
five.create_card(5,5,0)
#define 6 card
six= Card()
six.create_card(6,6,1)
#define 7 card
seven= Card()
seven.create_card(7,7,1)
#define 8 card
eight= Card()
eight.create_card(8,8,1)
#define 10 card
ten= Card()
ten.create_card(10,10,1)
#define jack
jack= Card()
jack.create_card(2,11,1)
#define queen
queen= Card()
queen.create_card(12,12,1)
#define king
king= Card()
king.create_card(13,13,2)
#define ace = card()
ace = Card()
ace.create_card(14,14,1)

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