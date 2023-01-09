# importowanie niezbędnych modułów  
import pygame                
from pygame.locals import * 
import random      
import time
import Bird_Class
import Button_Class 
import Ptera_Class
import data_functions
import functions
 
#klasa gra
class Game:
    #inicjowanie zmiennych 
    def __init__(self,freq,level):
        pygame.init()
        #tworzenie obiektu Clock() do śledzenia ilości czasu
        self.game_clock = pygame.time.Clock()
        #fps gry
        self.game_fps = 60
        #zmienna częstotliwości pojawienia się pteradaktylów w milisec
        self.pteraFrequency = freq
        #poziom gry
        self.level = level
        #ustawienie ekranu i jego rozmiaru
        self.SCREEN_HEIGHT = 720 
        self.SCREEN_WIDTH = 600
        self.display_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        #czcionka
        self.fontStyle = pygame.font.SysFont('arial black', 55) 
        #czarny kolor
        self.black = (0,0,0)

        self.baseScroll = 0  
        self.scrollSpeed = 4  

          
        #self.pteraFrequency = freq   
        #zmienna 
        self.lastPtera = pygame.time.get_ticks() - self.pteraFrequency 
        #rachunek - pukty 
        self.playerScore = 0
        #zmienne pomocnicze
        self.passPtera = False  
        self.check = True
        self.check1 = True  
        self.game_run = True  
        self.birdFlying = False   
        self.gameOver = False  
        # ładowanie zdjęć  
        self.background = pygame.image.load('images/background.png')  
        self.base = pygame.image.load('images/base.png')  
        self.button = pygame.image.load('images/restart.png')
        self.button_menu = pygame.image.load('images/menu.png')   
       
        # tworzenie klas dla dwóch przycisków  
        self.startButton = Button_Class.Button(175, 350, self.button,self.display_screen)
        self.menuButton = Button_Class.Button(325,350,self.button_menu,self.display_screen)
    
        # tworzenie grupy obiektów za pomocą modułu pygame.sprite   
        self.birdGroup = pygame.sprite.Group()  
        self.pteraGroup = pygame.sprite.Group()  
              
        #tworzenie obiektu ptak
        self.bird = Bird_Class.FlappyBird(50, int(self.SCREEN_HEIGHT / 2))  
              
        #dodawanie obiektu ptak do grupy  
        self.birdGroup.add(self.bird)  
              
    
        #start gry
        Game.run(self)
        


    def drawText(self,text, textColor, x_coordinate, y_coordinate): 
        # funkcja render() rysuje tekst jak zdjęcie  
        image = self.fontStyle.render(text, True, textColor)  
      
        # funkcja blit() wyświetla tekst(zdjęcie) na ekranie
        self.display_screen.blit(image, (x_coordinate, y_coordinate))  
      
    # funkcja do resetowania gry  
    def resetGame(self):  
        # funkcja empty() usuwa wszystkie obiekty z grupy ptera  
        self.pteraGroup.empty()
        self.gameOver = False 
        # współrzędne opisujące pozycje ptaka po restarcie  
        self.bird.rect.x = 50  
        self.bird.rect.y = int(self.SCREEN_HEIGHT / 2)  
        # ustawienie rachunku na 0
        self.check1 = True
        # zwracanie rachunku  
        return 0

     # funkcja resetująca czas i zwracająca nowe ustawienie zmiennej pomocniczej (True)
    def resetVariables():
        return time.time(), True

    #funkcja w której zawarta jest logika gry 
    def run(self):
        #cała gra jest iterowana w pętli while(True)
        while self.game_run: 
            
            #ustawienie fps gry
            self.game_clock.tick(self.game_fps)
 
                  
             #rysowanie tła 
            self.display_screen.blit(self.background, (0, 0))  
                  
            #rysowanie ptaka
            self.birdGroup.draw(self.display_screen)  
                  
                    # calling the update() function  
            self.birdGroup.update(self.birdFlying,self.gameOver)  
                  
            #rysowanie pteradaktylu
            self.pteraGroup.draw(self.display_screen)  
                  
            #rysowanie ziemi  
            self.display_screen.blit(self.base, (self.baseScroll, 576))  
                  
            # self.checking the score  
            if len(self.pteraGroup) > 0:  
                        # sprawdzenie jeśli ptak  minął lewą stronę pteradaktyla ale nie prawą  
                if self.birdGroup.sprites()[0].rect.left > self.pteraGroup.sprites()[0].rect.left \
                    and self.birdGroup.sprites()[0].rect.left < self.pteraGroup.sprites()[0].rect.right \
                        and self.passPtera == False:
                          
                                # setting the boolean value to true  
                            self.passPtera = True  
            
            #sprawdzenie czy pteradaktyl został ominięty   
            if self.passPtera == True: 

                #ten moduł odpowiada za wyłapywanie błedu w przypadku gdy ptak minał lewą stronę pteradaktyla ale nie prawą i zmarł
                #bez tego modułu wyrzuci błąd list out of range i gra się zamnki
                try: 
                    #sprawdzamy czy lewa krawędź prostokąta ptaka omineła prawą krawędź prostokąta pteradaktyla
                    if self.birdGroup.sprites()[0].rect.left > self.pteraGroup.sprites()[0].rect.right:
                        # dodajemy do rachunku 1
                        self.playerScore += 1
                        #zmieniamy zmienną pomocniczą 
                        self.passPtera=False   
                          
                #wyłapywania błędu który może spowodować kraszowanie gry
                except IndexError  :
                    #dodajemy do rachunku 1
                    self.playerScore+=1
                    #resetujemy grę
                    self.playerScore=Game.resetGame(self)

                        
                  
            # funkcja drawText() rysuje bieżącą ilość puktów na ekranie  
            Game.drawText(self,str(self.playerScore), self.black, int(self.SCREEN_WIDTH / 2), 15)  
                  
            # sprawdzenie kolizji pomiędzy ptakiem i pterodaktylem  
            if pygame.sprite.groupcollide(self.birdGroup, self.pteraGroup, False, False) or self.bird.rect.top < 0:  
                self.gameOver = True  
                  
            #sprawdzenie czy ptak udzerzył się w dolną część ekranu  
            if self.bird.rect.bottom >= 576:  
                self.gameOver = True  
                self.birdFlying = False  
            #sprawdzenie czy ptak udzerzył się w górną część ekranu    
            if self.bird.rect.top <= 0:  
                self.gameOver = True  
                self.birdFlying = False     





                  
            # sprawdzenie czy gra się nie zakończyła  
            if self.gameOver == False and self.birdFlying == True:  
                    
                #generacja nowych pteradaktylów  
                timeNow = pygame.time.get_ticks() 
                if timeNow - self.lastPtera > self.pteraFrequency: 
                    #ustawienie randomowej pozycji pteradaktyla 
                    ptera_x = random.randint(650,700)
                    ptera_y = random.randint(40, 500)  
                    
                    #tworzenie obiektu ptera za pomocą klasy Ptera_Class
                    ptera = Ptera_Class.Ptera(ptera_x, ptera_y,10)
                    #dodanie nowego obiektu do grupy ptera
                    self.pteraGroup.add(ptera)  
                    #zapisywanie do zmiennej bieżącego czasu
                    self.lastPtera = timeNow  
                    
                        # scrolling the base  
                self.baseScroll -= self.scrollSpeed  
                if abs(self.baseScroll) > 70:  
                    self.baseScroll = 0  
                              
                # update pteradaktyla
                self.pteraGroup.update()  
                  
            # sprawdzenie czy gra się zakończyła  
            if self.gameOver == True:
                #sprawdzenie czy zmienn pomocnicza True
                if self.check == True:

                    #print(time.time()-self.timer)
                    #uzyskania czasu trwania gry za pomocą odejmowania zmiennej timer od bieżącego czasu
                    self.timer=time.time()-self.timer
                    #zapis dannych gry do plika tekstowego
                    data_functions.input(self.playerScore, round(self.timer,2),self.level)
                    
                    #zmiana zmiennej pomocniczej na False żeby zapis do pliku odbyłał się tylko 1 raz po zakończeniu gry
                    self.check = False
                
                #sprawdzenie czy pzycisk restart został naciśnięty  
                if self.startButton.draw() == True:
                    #resetowanie rachunku
                    self.playerScore = Game.resetGame(self)  
                    #resetowanie tajmera i zmiennej pomocniczej
                    self.timer, self.check = Game.resetVariables() 
                    
                    
                #jeśli zostaje naciśnięty klawisz menu, pętla jest przytywana - powrót do menu
                if self.menuButton.draw() == True:
                    break  
                  
            # za pomocą pętli zostają wyłapywane dzieje z klawiatury  
            for event in pygame.event.get():  
                        
                #naciśnięcie krzyżyka powoduje zamknięcie gry       
                if event.type == QUIT:  
                    self.game_run = False
                #naciśnięcie ESC powoduje zatrzymanie gry i wyświetlenie pomocy
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.birdFlying = False
                    functions.help()
                    
                        
                        

                
                # jeśli został naciśnięty lewy przycisk myszy i gra nie jest zakończona i ptach nie leci - zmienna birdflying ustawia się na True
                #co powoduje że ptach leci
                if event.type == MOUSEBUTTONDOWN and self.birdFlying == False and self.gameOver == False:  
                    self.birdFlying = True
                if event.type == MOUSEBUTTONDOWN and self.gameOver == False and self.check1 == True:
                    self.timer = time.time()
                    self.check1 = False
                  
            # używanie funkcji update() modułu pygame.display aktualizuje wydarzenia w grze  
            pygame.display.update()  
                  
                
        return 0



