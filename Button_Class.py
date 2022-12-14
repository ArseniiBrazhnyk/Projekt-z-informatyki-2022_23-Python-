
import pygame
from pygame.locals import *   
import random      
import time

#klassa przycisk
class Button():  
    # definiowanie i inicjalizacja funkcji  
    def __init__(self, x_coordinate, y_coordinate, image,display_screen):  
        # definicja zmiennych  
        self.image = image  
        self.rect = self.image.get_rect()  
        self.rect.topleft = (x_coordinate, y_coordinate) 
        self.display_screen=display_screen 
    # funkcja do rysowania przycisku na ekranie  
    def draw(self):  
        # zmienna pomocnicza która będzie zwrócona
        action = False  
  
        # otrzymywanie pozycji myszy  
        position = pygame.mouse.get_pos()  
  
        # sprawdzanie czy mysz znajduje się nad przyciskiem  
        if self.rect.collidepoint(position):  
            if pygame.mouse.get_pressed()[0] == 1:  
                action = True  
                  
        # rysowanie przycisku

        self.display_screen.blit(self.image, (self.rect.x, self.rect.y))  
  
        # zwracanie zmiennej  
        return action  