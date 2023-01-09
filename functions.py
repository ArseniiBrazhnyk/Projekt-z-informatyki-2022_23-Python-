import pygame 
from pygame.locals import *
import Screen_Class
#biblioteka do wyświetlania tekstu




#fukcja help() zawiera w sobie tekst do wyświetlania
def help():
	window = Screen_Class.Screen()
	text="""Celem gry jest ominięcie ptyrodaktyle,
po zetknięciu z ptyrodaktylem lub 
górną/dolną granicą ekranu gra 
się zakonczy. Gra ma 3 poziomy:
czym wyższy poziom tym większa
prędkośc ptyrodaktylów.
Sterowanie ptachiem odbywa się 
poprzez lewy przycisk myszy. 
Przesuwanie się	po menu odbywa się
poprzez użycie klawiszy W/S, wybór 
opcji - Space. Zatrzymanie gry - ESC.
Opuszczenie gry - krżyżyk lub Fn+F4 
podczas zatrzymania gry.
Powrót do gry - ESC.
Wznowienie gry - lewy przycisk myszy. """

	window.draw_text(text)
	return
