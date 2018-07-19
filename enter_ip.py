import pygame
from drawings import DrawObjects
from Settings import *


class IpInput:
    """Nie ma pole na input tekstowy w pygame. To jest 
    klasa która właśnie tworzy input tekstowy w pygame'ie"""

    def __init__(self, screen):
        self.ip = "127.0.0.1"
        self.screen = screen
        self.drawer = DrawObjects(self.screen)
        self.input_box_cords = (100, 200)

    def draw_input_box(self):
        self.drawer.draw_square(CYAN, 
                                self.input_box_cords[0],
                                self.input_box_cords[1], 
                                WIDTHSCREEN - (100 * 2), 
                                50
                                )

    def draw_ip_text(self):
        self.drawer.draw_text(self.ip, 
                              32, 
                              BLACK,
                              WIDTHSCREEN / 2,
                              self.input_box_cords[1] + 25
                              )

    def wasclicked(self, cords, box_cords):
        if cords[0] > box_cords[0] and cords[0] < box_cords[0] + self.length:
            if cords[1] < box_cords[1] and cords[1] > box_cords[1] - self.height:
                return True

    def write_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("haha yes")