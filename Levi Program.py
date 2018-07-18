#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#I will write all parts of program in one file and 
#I hope that you will put this program into modules and make order

#So i will import Pygame and sys

import pygame, sys
pygame.init()

#I will import my modules
import init_dimensions
import init_drawing

#Drawing screen
init_drawing.drawing()

#Game Loop
while True:
    #Handling event
    for event in pygame.event.get():
        #Exit
        if event.type == pygame.QUIT:
            sys.exit(0)