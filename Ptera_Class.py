import pygame
from pygame.locals import *   
import random      
import time  


#klassa Pteradaktyl
class Ptera(pygame.sprite.Sprite): # klasa bazowa dla widocznych obiektów gry
    def __init__(self, x_coordinate, y_coordinate, speed):  
        pygame.sprite.Sprite.__init__(self)  
        #definiowanie zmiennych
        # tworzenie pustej tablicy 
        self.image_list = []  
        # ustawienie  zmiennych index i counter na o
        self.index = 0  
        
        self.counter = 0
        # iterujemy w przedziale <1,3)  
        for i in range(1, 3):  
            # ładowanie obrazków pteradaktyla wykorzystując load() z modułu pygame.image
            # zamiast {i} jest wstawiana liczba 1 i 2 po kolei   
            image = pygame.image.load(f'images/ptera_{i}.png')  
              
            # dodawanie obrazków do tablicy
            self.image_list.append(image)  
  
        # ustawienie początkowego obrazku pteradaktyla  
        self.image = self.image_list[self.index]  
          
        # tworzenie prostokątu na który jest nakładany obrazek pteradaktyla  
        self.rect = self.image.get_rect()  
  
        # ustawienie pozycji pteradaktyla  
        self.rect.center = [x_coordinate, y_coordinate]  
  
        # definiowanie szybkośći pteradaktyla 
        self.velocity = speed  
        self.movement = [-1*self.velocity,0]
     #metoda do wizualizacji pteradaktyla
     # blit() nakłada obrazek pteradaktyla na prostokąt    
    def draw(self):
        screen.blit(self.image,self.rect)
     #metoda do zmiany obrazków pteradaktyla co powoduje jego animowanie
    def update(self):
        #co jakiś czas self.index zmienia się z 1 na 2 co powoduje zmianę self.image na inny obrazek
        self.counter+=1
        if self.counter % 10 == 0:
            self.index = (self.index+1)%2
        self.image = self.image_list[self.index]
        # move() powoduje ruch pteradaktyla w lewo
        self.rect = self.rect.move(self.movement)
        #jeśli prawa strona prostokąta jest za początkiem osi x (<0) to obiek jest niszczony
        if self.rect.right < 0:
            self.kill()  