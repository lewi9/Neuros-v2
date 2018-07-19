from drawings import DrawObjects
from Settings import *

class Button:
    """This class allows for the creation of buttons in pygame"""

    def __init__(self, 
                 screen, 
                 x, 
                 y, 
                 length, 
                 height, 
                 text = "", 
                 color = BLACK, 
                 text_color = GREEN, 
                 text_size = 10
                 ):

        self.x = x
        self.y = y 
        self.text = text
        self.color = color
        self.text_color = text_color
        self.text_size = text_size
        self.length = length
        self.height = height
        self.drawer = DrawObjects(screen)

    def draw_button(self):
        """this button draws the square that represents the button"""
        self.drawer.draw_square(color = self.color, 
                                x = self.x, 
                                y = self.y, 
                                length = self.length, 
                                height = self.height
                                )

    def draw_button_text(self):
        """This draws text on the button"""
        self.drawer.draw_text(self.text, 
                              self.text_size, 
                              self.text_color,
                              self.x + (self.length / 2), 
                              self.y + (self.height / 2)
                              )
    def create(self):
        """This creates the button, button can be recreated if values are changed"""
        self.draw_button()
        self.draw_button_text()

    def set_text(self, text):
        """Set the text of the button"""
        self.text = text

    def set_text_color(self, color):
        """Set the color of the text in the button"""
        self.text_color = color

    def set_text_size(self, size):
        """Set the size of the text"""
        self.text_size = size

    def set_button_color(self, color):
        """Set color of button"""
        self.color = color

    def wasclicked(self, cords):
        """This function returns true if the button is clicked"""
        if cords[0] > self.x and cords[0] < self.x + self.length:
            if cords[1] > self.y and cords[1] < self.y + self.height:
                return True
