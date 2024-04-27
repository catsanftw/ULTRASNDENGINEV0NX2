import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hummer Team Musicdisk")

# Colors
black = (0, 0, 0)
green = (0, 128, 0)
light_green = (0, 255, 0)

# Fonts
font_title = pygame.font.SysFont(None, 32)
font_text = pygame.font.SysFont(None, 24)

# Text elements
title = font_title.render("Hummer Team Musicdisk", True, light_green)
square_a = font_text.render("SQUARE A", True, green)
square_b = font_text.render("SQUARE B", True, green)
triangle = font_text.render("TRIANGLE", True, green)
noise = font_text.render("NOISE", True, green)
instructions = font_text.render("D. PAD LEFT AND RIGHT MOVES TO PREVIOUS AND NEXT SONG", True, light_green)
instructions2 = font_text.render("A STOPS AND B REPLAYS", True, light_green)
current_song = font_text.render("CURRENT SONG: 00", True, light_green)
silence = font_text.render("SILENCE", True, light_green)

# Positions
title_rect = title.get_rect(center=(width // 2, 40))
square_a_rect = square_a.get_rect(topleft=(50, 100))
square_b_rect = square_b.get_rect(topleft=(50, 140))
triangle_rect = triangle.get_rect(topleft=(50, 180))
noise_rect = noise.get_rect(topleft=(50, 220))
instructions_rect = instructions.get_rect(center=(width // 2, 280))
instructions2_rect = instructions2.get_rect(center=(width // 2, 320))
current_song_rect = current_song.get_rect(bottomleft=(50, height - 50))
silence_rect = silence.get_rect(bottomright=(width - 50, height - 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(black)

    # Draw text elements
    screen.blit(title, title_rect)
    screen.blit(square_a, square_a_rect)
    screen.blit(square_b, square_b_rect)
    screen.blit(triangle, triangle_rect)
    screen.blit(noise, noise_rect)
    screen.blit(instructions, instructions_rect)
    screen.blit(instructions2, instructions2_rect)
    screen.blit(current_song, current_song_rect)
    screen.blit(silence, silence_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
