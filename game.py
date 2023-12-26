import pygame
import sys

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))	# Create the window;
clock = pygame.time.Clock()						# Create the clock;
font = pygame.font.Font(None, 50)				# Create the font;

# Load font, images and convert them;
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/Ground.png").convert()
score_surf = font.render("Score: ", False, (64, 64, 64))
score_rect = score_surf.get_rect(midbottom = (400, 50))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 300))
player_gravity = 0

# Main game loop;
while True:
	for event in pygame.event.get():	# Check player input;
		if event.type == pygame.QUIT:	# Close the window;
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
				player_gravity = -20

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
				player_gravity = -20

	screen.blit(sky_surf, (0, 0))		# Draw sky on the window;
	screen.blit(ground_surf, (0, 300))	# Draw ground on the window;
	
	pygame.draw.rect(screen, "#c0e8ec", score_rect)
	pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
	screen.blit(score_surf, score_rect)	# Draw score on the window;

	snail_rect.x -= 3 					# Increase snail x position;
	if snail_rect.right <= 0:			# Check if snail go out from the window;
		snail_rect.left = 800

	# Snail;
	screen.blit(snail_surf, snail_rect)

	# Player;
	player_gravity += 1
	player_rect.y += player_gravity
	if player_rect.bottom >= 300:
		player_rect.bottom = 300
	screen.blit(player_surf, player_rect)

	pygame.display.update() # Update the window;
	clock.tick(60)			# 60 frames per second;