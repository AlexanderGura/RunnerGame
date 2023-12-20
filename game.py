import pygame
import sys

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((600, 400))	# Create the window;
clock = pygame.time.Clock()						# Create the clock;
font = pygame.font.Font(None, 50)				# Create the font;

# Load images;
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = font.render("Runner Game", False, "Black")

# Main game loop;
while True:
	for event in pygame.event.get():	# Check player input;
		if event.type == pygame.QUIT:	# Close the window;
			pygame.quit()
			sys.exit()

	screen.blit(sky_surface, (0, 0))		# Draw sky on the window;
	screen.blit(ground_surface, (0, 300))	# Draw ground on the window;
	screen.blit(text_surface, (200, 50))	# Draw text on the window;

	pygame.display.update() # Update the window;
	clock.tick(60)			# 60 frames per second;