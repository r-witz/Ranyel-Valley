import pygame
from sys import exit
from settings import *
from level import Level

class Game:
	def __init__(self):
		pygame.init()

		
		screen_info = pygame.display.Info()
		screen_width, screen_height = screen_info.current_w, screen_info.current_h

		if FULLSCREEN:
			self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		else:
			self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		
		pygame.display.set_caption('RANYEL VALLEY')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
  
			dt = self.clock.tick(FRAMERATE) / 1000
			self.level.run(dt)
			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
