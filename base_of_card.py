from card import *



#Celowo nie użyłem for, ponieważ to baza kart i musi być łatwa zmiana statystyk
#Wiem, że byłoby szybciej, ale potem mogłoby być nieczytelne, a to jest bardzo ważne miejsce

#define nine card
nine = Card(9,9,1)

#define 2 card
two = Card(2,2,1)

#define 3 card
three = Card(3,3,0)

#define 4 card
four= Card(4,4,1)

#define 5 card
five= Card(5,5,0)

#define 6 card
six= Card(6,6,1)

#define 7 card
seven= Card(7,7,1)

#define 8 card
eight= Card(8,8,1)

#define 10 card
ten= Card(10,10,1)

#define jack
jack= Card(2,11,1)

#define queen
queen= Card(12,12,1)

#define king
king= Card(13,13,2)

#define ace = card()
ace = Card(14,14,1)

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