from gameclient import GameClient
import pygame
import random
import string

def draw_test_button(screen):
	button = pygame.Rect(700, 300, 50, 50)
	pygame.draw.rect(screen, (0, 0, 0), button)

def wasclicked(cords):
	if cords[0] >= 700 and cords[1] >= 300 and cords[0] <= 750 and cords[1] <= 350:
		return True

def create_random_text():
	list_range = random.choice(list(range(30)))
	alphabet = list(string.ascii_lowercase)
	randomchars = []
	random_string = ""

	for i in range(list_range):
		randomchars.append(random.choice(alphabet))

	for char in randomchars:
		random_string += char

	return random_string



