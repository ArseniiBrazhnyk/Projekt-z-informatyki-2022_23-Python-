import pygame 
from pygame.locals import *
import main





class Screen:
	#inicjacja zmiennych pomocniczcyh
	def __init__(self):
		#przechowuje listę z opcjami wyboru
		self.option_surfaces = []
		#przechowuje metody które wyłowywane prz wyborze opcji z listy self.option_surfaces
		self.callbacks = []
		#zmienna current_option_index pomaga ustalić na jakim punkcie z listy opcji jesteśmy w tym momencie
		self.current_option_index = 0
		#czcionka
		self.fontStyle = pygame.font.SysFont('arial black', 55)
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
	# option_y_padding dustans pomiędzy punktami listy
	def draw(self, screen, x, y, option_y_padding):
		# enumerate() zwraca numer(i=0,1,2...) i obiekt z listy self.option_surfaces
		for i, option in enumerate(self.option_surfaces):
			option_rect = option.get_rect()
			option_rect.topleft = (x, y + i * option_y_padding)
			#jeśli i jest równe self.current_option_index to rysujemy prostokąt nad punktem z listy
			if i == self.current_option_index:
				pygame.draw.rect(screen, (230,97,29), option_rect)
			screen.blit(option, option_rect)


