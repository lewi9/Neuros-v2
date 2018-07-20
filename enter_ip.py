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

        self.button1 = Button(self.screen, 270, 280, 90, 90)
        self.button2 = Button(self.screen, 361, 280, 90, 90)
        self.button3 = Button(self.screen, 452, 280, 90, 90)
        self.button4 = Button(self.screen, 270, 371, 90, 90)
        self.button5 = Button(self.screen, 361, 371, 90, 90)
        self.button6 = Button(self.screen, 452, 371, 90, 90)
        self.button7 = Button(self.screen, 270, 462, 90, 90)
        self.button8 = Button(self.screen, 361, 462, 90, 90)
        self.button9 = Button(self.screen, 452, 462, 90, 90)
        self.buttondot = Button(self.screen, 270, 553, 90, 90)
        self.button0 = Button(self.screen, 361, 553, 90, 90)
        self.buttonEnter = Button(self.screen, 452, 553, 90, 90)

        self.button0.set_text("0")
        self.button1.set_text("1")
        self.button2.set_text("2")
        self.button3.set_text("3")
        self.button4.set_text("4")
        self.button5.set_text("5")
        self.button6.set_text("6")
        self.button7.set_text("7")
        self.button8.set_text("8")
        self.button9.set_text("9")
        self.buttondot.set_text(".")
        self.buttonEnter.set_text("Enter")

        self.buttons_list = [
                    self.button0,
                    self.button1,
                    self.button2,
                    self.button3,
                    self.button4,
                    self.button5,
                    self.button6,
                    self.button7,
                    self.button8,
                    self.button9,
                    self.buttondot,
                    self.buttonEnter
                    ]

        for button in self.buttons_list:
            button.set_button_color(CYAN)
            button.set_text_color(BLACK)
            button.set_text_size(25)
            button.create()

        self.buttonBackSpace = Button(self.screen, 543, 280, 190, 90)
        self.buttonBackSpace.set_button_color(CYAN)
        self.buttonBackSpace.set_text("BACK SPACE")
        self.buttonBackSpace.set_text_color(BLACK)
        self.buttonBackSpace.set_text_size(30)
        self.buttonBackSpace.create()

    def check_if_pressed(self, cords):
        """This function will check if any button is pressed and modify the IP"""

        if self.button1.wasclicked(cords):
            self.ip += "1"
            self.button1.set_button_color(RED)
            self.button1.create()

        if self.button2.wasclicked(cords):
            self.ip += "2"
            self.button2.set_button_color(RED)
            self.button2.create()

        if self.button3.wasclicked(cords):
            self.ip += "3"
            self.button3.set_button_color(RED)
            self.button3.create()

        if self.button4.wasclicked(cords):
            self.ip += "4"
            self.button4.set_button_color(RED)
            self.button4.create()

        if self.button5.wasclicked(cords):
            self.ip += "5"
            self.button5.set_button_color(RED)
            self.button5.create()

        if self.button6.wasclicked(cords):
            self.ip += "6"
            self.button6.set_button_color(RED)
            self.button6.create()

        if self.button7.wasclicked(cords):
            self.ip += "7"
            self.button7.set_button_color(RED)
            self.button7.create()

        if self.button8.wasclicked(cords):
            self.ip += "8"
            self.button8.set_button_color(RED)
            self.button8.create()

        if self.button9.wasclicked(cords):
            self.ip += "9"
            self.button9.set_button_color(RED)
            self.button9.create()

        if self.button0.wasclicked(cords):
            self.ip += "0"
            self.button0.set_button_color(RED)
            self.button0.create()

        if self.buttondot.wasclicked(cords):
            self.ip += "."
            self.buttondot.set_button_color(RED)
            self.buttondot.create()

        if self.buttonBackSpace.wasclicked(cords):
            self.ip = self.ip[:-1]
            self.buttonBackSpace.set_button_color(RED)
            self.buttonBackSpace.create()

    def enter_button_pressed(self, cords):
        if self.buttonEnter.wasclicked(cords):
            return self.ip




