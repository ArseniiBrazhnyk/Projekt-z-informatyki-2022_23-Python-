#importowanie modułów
import pygame 
from pygame.locals import *
import Screen_Class
import test1
import Game_Class
import functions
import data_functions

#inicjacja pygame
pygame.init()


#zmienna z tekstem help
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
Opuszczenie gry będąc w menu - Quit.
Powrót do menu - ESC."""


#tworzenie ekranu z poziomami uzywając klasy Screen
level = Screen_Class.Screen()
#twrozenie listy z opcjami do wyboru
#lambda-funkcja jest anonimową funkcją bez nazwy która po dwukropku ma jedno wyrażenie
level.append_option('Poziom 1', lambda: Game_Class.Game(1400,1))
level.append_option('Poziom 2', lambda: Game_Class.Game(1100,2))
level.append_option('Poziom 3', lambda: Game_Class.Game(800,3))


#tworzenie głównego ekranu uzywając klasy Screen
menu = Screen_Class.Screen()
#twrozymy listę z opcjami do wyboru
menu.append_option('Start', lambda: level.draw_options(level))
menu.append_option('Wyniki', lambda: menu.draw_text(data_functions.output()))
menu.append_option('Help', lambda: menu.draw_text(text))
menu.append_option('Quit',quit)

#rysowanie ekranu głównego z opcjami do wyboru
menu.draw_options(menu)

#zamknięcie ekranu
quit()
