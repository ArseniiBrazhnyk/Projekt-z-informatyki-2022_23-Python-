import pygame 
from pygame.locals import *
import Screen_Class
#biblioteka do wyświetlania tekstu
import ptext

#fukcja help() zawiera w sobie tekst do wyświetlania
def help():
	text="""Celem gry jest ominięcie ptyrodaktyle,
po zetknięciu z ptyrodaktylem lub 
górną/dolną granicą ekranu gra 
się zakonczy. Sterowanie ptachiem
odbywa się poprzez lewy przycisk myszy. 
Przesuwanie się	po menu odbywa się
poprzez użycie klawiszy W/S, wybór 
opcji - Space. Zatrzymanie gry - ESC.
Opuszczenie gry - krżyżyk lub Space 
podczas zatrzymania gry.
Powrót do menu - ESC."""

	draw(text)
	return

#funkcja do wyświetlania tekstu
def draw(data):
	pygame.init()

	#rozmiar ekranu
	size=(600,720)
	screen = pygame.display.set_mode(size)
	#ładujemy obrazki
	background = pygame.image.load('images/background.png')
	ground = pygame.image.load('images/base.png')
	#kolor czcionki
	white = (230,97,29)

	run = True
	while run:
		#wyłapujemy action z klawiatury
		for event in pygame.event.get():
			#zamknięcie okna
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				run = False
		#rysujemy tło i ziemie
		screen.blit(background, (0, 0))
		screen.blit(ground, (0, 576))
		#wyświetlanie tekstu(text,pozycja,kolor)
		ptext.draw(data, (10, 100), color=white)
		
		#rysujemy listę z opcjami do wyboru
		#odświeżamy ekran
		pygame.display.flip()

	#zamknięcie ekranu
	return


#def read():


#def write():
