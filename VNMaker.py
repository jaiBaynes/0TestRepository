#makes visual novels from any inputted book

# Imports all the things needed to make the program run
import time
import pygame
import math 
from math import sqrt
import random
from pygame.locals import*
import os
import pyttsx3
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25) # makes appear consistantly in the top left corner of the screen

# initialize the gane DO NOT EDIT
pygame.init()
readAloud = False
autoplay = False
screen = pygame.display.set_mode()
xval, yval = screen.get_size();
win = pygame.display.set_mode ((xval,int(yval)),HWSURFACE|DOUBLEBUF|RESIZABLE)
FPS = 60
clock = pygame.time.Clock()

class VNCharacter:
    def __init__ (self,name, image, size, width, voice):
        self.name = name
        if size == "small":
            self.imagey = yval//4
        if size == "medium":
            self.imagey = yval//3.5
        if size == "middle":
            self.imagey = yval//3            
        if size == "large":
            self.imagey = yval//2.5
        if size == "giant":
            self.imagey = yval//2   
        self.imagex = int(self.imagey*float(width))
        
        self.image = image
        self.appeared = -1
    def appear(self,spot):
        surf = pygame.transform.scale (pygame.image.load(self.image), (int(self.imagex*2), int(self.imagey*2)))
        win.blit(surf, (xval//7*spot, yval - int(self.imagey*2)))
        self.appeared += 1
    def remove(self,spot):
        onScreen.pop(spot)
        self.appeared = -1