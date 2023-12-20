import pygame
import sys

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 600)) # Create the window;
clock = pygame.time.Clock()

# Main game loop;
while True:
	for event in pygame.event.get():	# Check player input;
		if event.type == pygame.QUIT:	# Close the window;
			pygame.quit()
			sys.exit()

	pygame.display.update() # Update the window;
	clock.tick(60)