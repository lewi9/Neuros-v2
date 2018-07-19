import pygame
from drawings import DrawObjects
from Settings import *
from MakeButton import Button


class IpInput:
    """Nie ma pole na input tekstowy w pygame. To jest 
    klasa która właśnie tworzy input tekstowy w pygame'ie"""

    def __init__(self, screen):
        self.ip = ""
        self.screen = screen
        self.drawer = DrawObjects(self.screen)
        self.input_box_cords = (100, 200)
        self.buttons = []

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

    def createButtons(self):
        """This is going to create all the buttons"""
        third_of_screen = WIDTHSCREEN / 3
        button_width = third_of_screen / 3


        # self.button1 = Button(self.screen, 270, )
        # self.button2 = Button(self.screen, 360,)
        # self.button3 = Button(self.screen, 450,)
        # self.button4 = Button(self.screen, 270,)
        # self.button5 = Button(self.screen, 360,)
        # self.button6 = Button(self.screen, 450,)
        # self.button7 = Button(self.screen, 270,)
        # self.button8 = Button(self.screen, 360,)
        # self.button9 = Button(self.screen, 450,)
        # self.buttondot = Button(self.screen, 270,)
        # self.button0 = Button(self.screen, 360,)
        # self.buttonEnter = Button(self.screen, 450,)

