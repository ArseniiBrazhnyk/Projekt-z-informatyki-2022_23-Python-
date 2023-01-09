import pygame 
from pygame.locals import *
import ptext



#klassa Screen
class Screen:
	#inicjacja zmiennych 
	def __init__(self):
		#przechowuje listę z opcjami wyboru
		self.option_surfaces = []
		#przechowuje metody które wyłowywane prz wyborze opcji z listy self.option_surfaces
		self.callbacks = []
		#zmienna current_option_index pomaga ustalić na jakim punkcie z listy opcji jesteśmy w tym momencie
		self.current_option_index = 0
		#czcionka
		self.fontStyle = pygame.font.SysFont('arial black', 45)
		#rozmiar ekranu
		self.screen = pygame.display.set_mode((600,720))
		#tło
		self.background = pygame.image.load('images/background.png')
		#ziemia
		self.ground = pygame.image.load('images/base.png')
	
	#dodanie opcji wyboru i funkcji która jest przywiązana do tej opcji 	
	def append_option(self, option, callback):
		self.option_surfaces.append(self.fontStyle.render(option, True, (255,255,255)))
		self.callbacks.append(callback)
	#metoda switch służy do zmiany current_option_index który jest odpowiedzialny za przesuwanie w góre i do dołu wyboru
	def switch(self,direction):
		self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_surfaces)-1))
	#metoda zwracająca funkcje która jest przywiązana do wybranej opcji z listy
	def select(self):
		self.callbacks[self.current_option_index]()
	#metoda do rysowania prostokąta który przesuwa się po liście wyboru.
	# option_y_padding dystans pomiędzy punktami listy
	def draw(self, screen, x, y, option_y_padding):
		# enumerate() zwraca numer(i=0,1,2...) i obiekt z listy self.option_surfaces
		for i, option in enumerate(self.option_surfaces):
			option_rect = option.get_rect()
			option_rect.topleft = (x, y + i * option_y_padding)
			#jeśli i jest równe self.current_option_index to rysujemy prostokąt nad punktem z listy
			if i == self.current_option_index:
				pygame.draw.rect(screen, (230,97,29), option_rect)
			screen.blit(option, option_rect)

	#metoda do wyświetlania tekstu
	def draw_text(self,data):
		self.data = data
		#pygame.init()


		#kolor czcionki
		orange = (230,97,29)

		run = True
		while run:
			#wyłapujemy action z klawiatury
			for event in pygame.event.get():
				#zamknięcie okna
				if event.type == QUIT  :
					quit()
				if event.type == KEYDOWN: 
					if event.key == K_ESCAPE:
						run = False
					if event.key == K_F4:
						quit()
			#rysujemy tło i ziemie
			self.screen.blit(self.background, (0, 0))
			self.screen.blit(self.ground, (0, 576))
			#wyświetlanie tekstu(text,pozycja,kolor)
			ptext.draw(self.data, (10, 10), color=orange)
			
			#rysujemy listę z opcjami do wyboru
			#odświeżamy ekran
			pygame.display.flip()

		#zamknięcie ekranu
		return
		#metoda do wyświetlania opcji wyboru
	def draw_options(self,list_options):
		self.list_options = list_options
		run = True
		while run:
			#wyłapujemy action z klawiatury
			for event in pygame.event.get():
				#zamknięcie okna
				if  event.type == QUIT:
					quit()
				if event.type == KEYDOWN:
					#do góry W
					if  event.key == K_w:
						#switch metoda klasy Screen
						list_options.switch(-1)
					#do dołu S
					elif event.key == K_s:
						list_options.switch(1)
					#Wybór SPACE
					elif event.key == K_SPACE:
						#select metoda klasy Screen
						list_options.select()
					elif event.key == K_ESCAPE:
						run = False
			#rysujemy tło i ziemie
			self.screen.blit(self.background, (0, 0))
			self.screen.blit(self.ground, (0, 576)) 
			
			#rysujemy listę z opcjami do wyboru
			self.list_options.draw(self.screen, 220, 110, 75)
			#odświeżamy ekran
			pygame.display.flip()

		#metoda help() zawiera w sobie tekst do wyświetlenia tłumaczący zasady gry
		def help(self):
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
			#rysowanie tekstu
			draw_options(text)
			return





