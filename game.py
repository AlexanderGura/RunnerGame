import pygame
import sys

def display_score():
	# Draw score on the window;
	current_time = pygame.time.get_ticks() // 1000 - start_time
	score_surf = font.render(f"Score: {current_time}", False, (64, 64, 64))
	score_rect = score_surf.get_rect(midbottom = (400, 50))
	screen.blit(score_surf, score_rect)
	return current_time

pygame.init()
pygame.display.set_caption("Runner")
screen = pygame.display.set_mode((800, 400))		# Create the window;
clock = pygame.time.Clock()							# Create the clock;
font = pygame.font.Font("font/Pixeltype.ttf", 50)	# Create the font;
game_active = False									# Game statement;
start_time = 0

# Load font, images and convert them;
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/Ground.png").convert()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800, 300))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 300))
player_gravity = 0
score = 0

# Intro screen;
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Intsructions on the intro screen;
game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))
instruction = font.render("Press 'SPACE' to run", False, (111, 196, 169))
instruction_rect = instruction.get_rect(center = (400, 330))


# Main game loop;
while True:
	# Check player input;
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	# Close the window;
			pygame.quit()
			sys.exit()

		if game_active:
			# Check mouse input;
			if event.type == pygame.MOUSEBUTTONDOWN:
				if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
					player_gravity = -20

			# Check keyboard input;
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				snail_rect.left = 800
				start_time = pygame.time.get_ticks() // 1000

	if game_active:
		screen.blit(sky_surf, (0, 0))		# Draw sky on the window;
		screen.blit(ground_surf, (0, 300))	# Draw ground on the window;
		
		# Score;
		score = display_score()

		# Snail;
		snail_rect.x -= 4			# Increase snail x position;
		if snail_rect.right <= 0:	# Check if snail go out from the window;
			snail_rect.left = 800
		screen.blit(snail_surf, snail_rect)

		# Player;
		player_gravity += 1
		player_rect.y += player_gravity
		if player_rect.bottom >= 300:
			player_rect.bottom = 300
		screen.blit(player_surf, player_rect)

		if snail_rect.colliderect(player_rect):
			game_active = False
	else:
		screen.fill((94, 129, 162))
		screen.blit(player_stand, player_stand_rect)

		screen.blit(game_name, game_name_rect)
		score_message = font.render(f"Your score: {score}", False, (111, 196, 169))
		score_message_rect = score_message.get_rect(center = (400, 330))

		if score == 0:
			screen.blit(instruction, instruction_rect)
		else:
			screen.blit(score_message, score_message_rect)

	pygame.display.update() # Update the window;
	clock.tick(60)			# 60 frames per second;