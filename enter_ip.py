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
        """This draws the box where the ip will be displayed"""
        self.drawer.draw_square(CYAN, 
                                self.input_box_cords[0],
                                self.input_box_cords[1], 
                                WIDTHSCREEN - (100 * 2), 
                                50
                                )

    def draw_ip_text(self):
        """This draws the ip"""
        self.drawer.draw_text(self.ip, 
                              32, 
                              BLACK,
                              WIDTHSCREEN / 2,
                              self.input_box_cords[1] + 25
                              )

