import pygame
from array import array

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Screen setup - fixed size window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NX2 Augmenter SND Test 0.1 Infdev")

# Define a function to generate beep sounds with varying frequencies
def generate_beep_sound(frequency=440, duration=0.1):
    sample_rate = pygame.mixer.get_init()[0]
    max_amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
    samples = int(sample_rate * duration)
    wave = [int(max_amplitude * ((i // (sample_rate // frequency)) % 2)) for i in range(samples)]
    sound = pygame.mixer.Sound(buffer=array('h', wave))
    sound.set_volume(0.1)
    return sound

# Create a list of sound tuples (name, sound object)
sounds = [
    ("SND_1", generate_beep_sound(440, 0.1)),  # A4
    ("SND_2", generate_beep_sound(523.25, 0.1)),  # C5
    ("SND_3", generate_beep_sound(587.33, 0.1)),  # D5
    ("SND_4", generate_beep_sound(659.25, 0.1)),  # E5
]
current_sound_index = 0  # Index of the currently selected sound

# Font setup for displaying sound names
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Play the current sound
                sounds[current_sound_index][1].play()
            elif event.key == pygame.K_RIGHT:
                # Cycle to the next sound
                current_sound_index = (current_sound_index + 1) % len(sounds)
            elif event.key == pygame.K_LEFT:
                # Cycle to the previous sound
                current_sound_index = (current_sound_index - 1) % len(sounds)

    # Clear screen and render the name of the current sound
    screen.fill((0, 0, 0))
    sound_name_text = font.render(sounds[current_sound_index][0], True, (255, 255, 255))
    text_rect = sound_name_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(sound_name_text, text_rect)

    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()
