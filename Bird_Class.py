
#dodawanie modułów i bibliotek
import pygame
from pygame.locals import *   
import random      
import time




#klassa Ptak
class Bird(pygame.sprite.Sprite):  
    # definiowanie zmiennych pomocniczych  
    def __init__(self, x_coordinate, y_coordinate):  
        pygame.sprite.Sprite.__init__(self)  
        
        # tworzenie listy dla obrazów  
        self.image_list = []  
        # ustawienie zmiennych index i counter na 0  
        self.index = 0  
        self.counter = 0
        # zmienna pomocnicza  
        self.chek = 5    
        # iteracja w pętli w celu dodania obrazków do listy  
        for i in range(1, 4):  
            # ładujemy za pomocą funkcji load()  obrazki 
            image = pygame.image.load(f'images/bird_{i}.png')  
              
            # dodajemy obrazki za pomocą funkcji append() do listy 
            self.image_list.append(image)  
  
        # ustawiamy bieżący obrazek  
        self.image = self.image_list[self.index]  
          
        # tworzymy prostokąt w którym będzie obrazek  
        self.rect = self.image.get_rect()  
  
        # ustawienie pozycji ptaka  
        self.rect.center = [x_coordinate, y_coordinate]  
        
        # szybkość początkowa ptaka  
        self.speed = 0  
        self.pressed = False  
      
    # metoda animująca ptaka   
    def update(self,birdFlying,gameOver):  

        #zmienne pomocnicze
        self.birdFlying = birdFlying  
        self.gameOver = gameOver  
        # sprawdzenie czy ptak leci  
        if self.birdFlying == True:    
            # zwiększenie szybkości ptaka  
            self.speed += 0.5  
  
            #ustalenie szybkośći na 8.5 jeśli szybkość jest powyżej 8.5
            if self.speed > 8.5:  
                self.speed = 8.5  
            # if the rectangle's bottom is less than 576  
            # then increment its y-axis value by speed's integer value   
            if self.rect.bottom < 576:  
                self.rect.y += int(self.speed)  
  
        # sprawdzenie czy gra się nie zakończyła  
        if self.gameOver == False:  
            # sprawdzenie czy został nasiśnięta przycik myszy  
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:  
                # ustawienie zmiennej na True  
                self.pressed = True  
                # zmiana szybkośći  
                self.speed = -10  
  
            # sprawdzenie czy przycisk myszy został zwolniony  
            if pygame.mouse.get_pressed()[0] == 0:  
                # ustawienie zmiennej z powrotem na Falsem  
                self.pressed = False  
  
            # zwiększenie zmiennej counter o 1  
            self.counter += 1  
            
  
            # sprawdzenie czy  zmienna counter większa od chek
            #jest to potrzebne żeby animacja ptaka (zmiana zdjęć) była płynna
            #bez tego sprawdzenia, zdjęcia będą zmieniali się co kilka milisekund 
            if self.counter > self.chek:
            #zerowanie licznika  
                self.counter = 0  
                  
                # zwiększenie zmiennej index o 1  
                self.index += 1  
  
                #sprawdzenie czy zmienna index jest większa od długości listy z obrazkami 
                if self.index >= len(self.image_list):  
                    #zerowanie indexa
                    self.index = 0  
  
            # zmiana obrazka ptaka  
            self.image = self.image_list[self.index]  
              
            # obrót obrazka ptaka o kąt speed * (-2) stopni
            self.image = pygame.transform.rotate(self.image_list[self.index], self.speed * -2)  
        # jeśli gra się zakończyła  
        else:  
            # zmiana kąta obrazka ptaka o -90 stopni  
            self.image = pygame.transform.rotate(self.image_list[self.index], -90)
