import pygame 
from pygame.locals import *
import Screen_Class
import main



#inicjacja pygame
pygame.init()

#rozmiar ekranu
size=(600,720)
screen = pygame.display.set_mode(size)
#ładujemy obrazki
background = pygame.image.load('images/background.png')
ground = pygame.image.load('images/base.png')
#ustawiamy czcionke
fontStyle = pygame.font.SysFont('arial black', 55) 



#tworzymy ekran menu uzywając klasy Screen
menu = Screen_Class.Screen()

#twrozymy listę z opcjami do wyboru
#lambda-funkcja jest anonimową funkcją bez nazwy która po dwukropku na jedno wyrażenie
menu.append_option('Start', lambda: main.main())
menu.append_option('Wyniki', lambda: print('Hello world'))
menu.append_option('Help', lambda: print('Hello world'))
menu.append_option('Quit',quit)


run = True
while run:
	#wyłapujemy action z klawiatury
	for event in pygame.event.get():
		#zamknięcie okna
		if event.type == QUIT:
			run = False
		if event.type == KEYDOWN:
			#do góry W
			if  event.key == K_w:
				#switch metoda klasy Screen
				menu.switch(-1)
			#do dołu S
			elif event.key == K_s:
				menu.switch(1)
			#Wybór SPACE
			elif event.key == K_SPACE:
				#select metoda klasy Screen
				menu.select()
	#rysujemy tło i ziemie
	screen.blit(background, (0, 0))
	screen.blit(ground, (0, 576)) 
	
	#rysujemy listę z opcjami do wyboru
	menu.draw(screen, 220, 110, 75)
	#odświeżamy ekran
	pygame.display.flip()

#zamknięcie ekranu
quit()
