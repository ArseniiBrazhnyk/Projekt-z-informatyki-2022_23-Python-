import math
import os
from random import randit
from collections import deque
import pygame
from pygame.locals import *


#ustawienia
FPS=60
Animation_Speed=0.18
Win_Width=560
Win_Height=512


'''

ta klasa definuje zachowanie ptaszka
ptaszek może lecić w góre lub spadać na dół
zadaniem ptaszka jest omijanie latających dynozauwrów z góry lub z dołu

zmienne:
x = kordynata x ptaszka
y = kordynata y ptaszka
width=długość ptaszka
height=szerokość ptaszka
up_speed=prędkość polotu ptaszka w góre. wyrażana w pikseli/msec
down_speed=prędkość polotu ptaszka w dół. wyrażana w pikseli/msec
msec_to_climb=długość polotu ptaszka w góre, ile milisekund potrzebuje ptaszek
żeby wzlecić do góry'''
class Bird(pygame.sprite.Sprite):

	width=30
	height=30
	up_speed=0.3
	down_speed=0.17
	climb_duration=333.3

	def __init__(self,x,y,msec_to_climb,images):


		super(Bird,self).__init__()
		self.x=x
		self.y=y
		self.msec_to_climb=msec_to_climb
		self._image_wingup,self._image_wingdown=images
		self._mask_wingup=pygame.mask.from_surface(self._image_wingup)
		self._mask_wingdown=pygame.mask.from_surface(self._image_wingdown)

	def mask(self):
		if pygame.time.get_ticks()%100>=250:
			return self._mask_wingup
		else:
			return self._mask_wingdown
#funkcja pobierająca obrazy i zwracająca dict z nimi
def load_image():
	def load_image(img_name):
		file_name=os.path.join('.','images',img_name)
		img=pygame.image.load(file_name)

		img.convert()
		return {
			'background':load_image('background.png').
			'dinosaur':load_image('dinosaur.png').
			'bird_wingup':load_image('bird_wingup.png').
			'bird_wingdown':load_image('bird_wingdown.png').
		}

#konwertujemy kadry w milisekundy z ustalonym fps
def frames_to_mseconds(frame,fps=FPS):
	return 1000.0*frame/fps

#konwertujemy milisekundy w kadry z istalonym fps
def mseconds_to_frames(millisec,fps=FPS):
	return fps*millisec/1000.0

#główna funkcja z której startuje program
def main():

	pygame.init()
	display_surface=pygame.display.set_mode((Win_Width,Win_Height))

	pygame.display.set_caption("Ptaszek z dynozaurami")

	clock=pygame.time.Clock()

	score=pygame.font.SysFont(None,32,bold=True)

	images=pobierz_obrazy()
