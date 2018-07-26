import pygame

FPS = 30

PORT = 12345

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
GREEN = (0, 250, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

WIDTHSCREEN = 810
HEIGHTSCREEN = 690

BACKGROUND_COLOR = (39, 117, 112)
DECK_LINE_COLOR = (221, 220, 186)
PLACE_FOR_CARD_COLOR = [
    (168, 135, 126),
    (181, 254, 249),
    (227, 156, 113),
    (227, 156, 113),
    (181, 254, 249),
    (168, 135, 126)
]

hero = pygame.image.load("graphics/hero.jpg")
yhero = pygame.image.load("graphics/yhero.jpg")
big_hero = pygame.image.load("graphics/big_hero.jpg")
big_yhero = pygame.image.load("graphics/big_yhero.jpg")
deck_image = pygame.image.load("graphics/deck.png")
big_deck = pygame.image.load("graphics/big_deck.png")

