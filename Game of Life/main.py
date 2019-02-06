#!/usr/bin/python
# from __future__ import unicode_literals
# coding:utf-8

import pygame, sys
from pygame.locals import *

def main():
	class Cell(pygame.sprite.Sprite):
		def __init__(self, pos_x, pos_y):
			super(Cell, self).__init__()
		
			self.image = pygame.image.load("Resources/cell.png").convert_alpha()
		
			self.rect = self.image.get_rect()
			self.rect.x = pos_x
			self.rect.y = pos_y

			self.state = 0
			self.time_alive = 0
			self.adjacent_alive = 0
		
			cells.append(self)

	pygame.init()

	fenetre = pygame.display.set_mode((960, 620))

	clock = pygame.time.Clock()

	pygame.display.set_caption("Game Of Life")

	icone = pygame.image.load("Resources/logo_cell.png").convert_alpha()
	pygame.display.set_icon(icone)

	home = pygame.image.load("Resources/menu.png").convert_alpha()
	bright = pygame.image.load("Resources/bright.png").convert_alpha()

	background = pygame.image.load("Resources/grey_background.png").convert_alpha()

	rect_menu = home.get_rect()
	rect_menu.center = fenetre.get_rect().center

	menu = True
	pos_menu = False
	pos_bright = False

	keydown = True

	lines = 10 # int(input("lignes : "))
	columns = 10 # int(input("colonnes : "))
	var = ""

	cells = []
	check = []

	for L in range(lines):
		for C in range(columns):
			var += "X" # X, une cellule
	
		check.append(var)
		var = ""

	check_surface = pygame.Surface((columns * 17, lines * 17))
	rect_check_surface = check_surface.get_rect()
	rect_check_surface.center = fenetre.get_rect().center

	x, y = 0, 0
	for L in check:
		for C in L:
			Cell(x, y)
			x += 17

		y += 17
		x = 0

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
			if event.type == MOUSEMOTION and menu:
				if 507 <= event.pos[0] <= 701 and 274 <= event.pos[1] <= 474:
					pos_bright = True

				else :
					pos_bright = False

				if 214 <= event.pos[0] <= 746 and 111 <= event.pos[1] <= 510:
					pos_menu = True

				else :
					pos_menu = False

			if event.type == MOUSEBUTTONUP and pos_menu:
				menu = False

		fenetre.blit(background, (0, 0))

		if menu:
			if not pos_bright:
				fenetre.blit(home, rect_menu)

			else :
				fenetre.blit(bright, rect_menu)

		else :
			for C in cells:
				if event.type == MOUSEBUTTONDOWN:
					init_x = rect_check_surface.left
					init_y = rect_check_surface.top

					if C.rect.x + init_x <= pygame.mouse.get_pos()[0] <= C.rect.x + 17 + init_x and C.rect.y + init_y <= pygame.mouse.get_pos()[1] <= C.rect.y + 17 + init_y:
						if C.state == 0:
							C.state = 1
							C.image = pygame.image.load("Resources/cell2.png").convert_alpha()

						elif C.state == 1:
							C.state = 0
							C.image = pygame.image.load("Resources/cell.png").convert_alpha()
							
						break
				
				check_surface.blit(C.image, (C.rect.x, C.rect.y))
				
				if event.type == KEYDOWN and event.key == K_SPACE and keydown:
					print("space")
					keydown = False
					index = cells.index(C)
					
					try :
						if cells[index - columns].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass
					
					try :
						if cells[index - columns - 1].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass
							
					try :	
						if cells[index - columns + 1].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass
						
					try :
						if cells[index - 1].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass

					try :
						
						if cells[index + 1].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass
					
					try :	
						if cells[index + columns].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass	
						
					try :	
						if cells[index + columns - 1].state == 1:
							C.adjacent_alive += 1
					except IndexError:

						pass	
					
					try :
						if cells[index + columns + 1].state == 1:
							C.adjacent_alive += 1

					except IndexError:
						pass
					
					if C.adjacent_alive == 3 and C.state == 0:
						C.state = 1
						C.image = pygame.image.load("Resources/cell2.png").convert_alpha()

					elif (C.adjacent_alive == 2 or C.adjacent_alive == 3) and C.state == 1:
						C.state = 1
						C.image = pygame.image.load("Resources/cell2.png").convert_alpha()

					else :
						C.state = 0
						C.image = pygame.image.load("Resources/cell.png").convert_alpha()
					
					C.adjacent_alive = 0
			
			fenetre.blit(check_surface, rect_check_surface)
	
		keydown = True		
		pygame.display.flip()
		
		clock.tick(60)

if __name__ == "__main__":
	main()
