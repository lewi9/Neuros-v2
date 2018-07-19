from card import *



#Celowo nie użyłem for, ponieważ to baza kart i musi być łatwa zmiana statystyk
#Wiem, że byłoby szybciej, ale potem mogłoby być nieczytelne, a to jest bardzo ważne miejsce

#define nine card
nine = Card()
nine.attack = 9
nine.defense = 9
nine.frozen_time = 1
#define 2 card
two = Card()
two.attack = 2
two.defense = 2
two.frozen_time = 1
#define 3 card
three = Card()
three.attack = 3
three.defense = 3
three.frozen_time = 0
#define 4 card
four= Card()
four.attack = 4
four.defense = 4
four.frozen_time = 1
#define 5 card
five= Card()
five.attack = 5
five.defense = 5
five.frozen_time = 0
#define 6 card
six= Card()
six.attack = 6
six.defense = 6
six.frozen_time = 1
#define 7 card
seven= Card()
seven.attack = 7
seven.defense = 7
seven.frozen_time = 1
#define 8 card
eight= Card()
eight.attack = 8
eight.defense = 8
eight.frozen_time = 1
#define 10 card
ten= Card()
ten.attack = 10
ten.defense = 10
ten.frozen_time = 1
#define jack
jack= Card()
jack.attack = 2
jack.defense = 11
jack.frozen_time = 1
#define queen
queen= Card()
queen.attack = 12
queen.defense = 12
queen.frozen_time = 1
#define king
king= Card()
king.attack = 13
king.defense = 13
king.frozen_time = 2
#define ace = card()
ace = Card()
ace.attack = 14
ace.defense = 14
ace.frozen_time = 1

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