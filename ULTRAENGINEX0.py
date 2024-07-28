import pygame
import sys
from array import array

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ULTRA NX [ALPHA] 0.X.X.X")

# Define a function to generate beep sounds with varying frequencies
def generate_beep_sound(frequency=440, duration=0.1):
    sample_rate = pygame.mixer.get_init()[0]
    max_amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
    samples = int(sample_rate * duration)
    wave = [int(max_amplitude * ((i // (sample_rate // frequency)) % 2)) for i in range(samples)]
    sound = pygame.mixer.Sound(buffer=array('h', wave))
    sound.set_volume(0.1)
    return sound

# Create sound effects
sounds = [
    ("Sound 1", generate_beep_sound(440, 0.5)),  # A4
    ("Sound 2", generate_beep_sound(523.25, 0.5)),  # C5
    ("Sound 3", generate_beep_sound(587.33, 0.5)),  # D5
    ("Sound 4", generate_beep_sound(659.25, 0.5))   # E5
]
current_sound_index = 0

# Font setup for displaying sound names and controls
font = pygame.font.Font(None, 36)

# Create a function to draw the HUD
def draw_hud():
    screen.fill((0, 0, 0))
    
    sound_name_text = font.render(f"Current Sound: {sounds[current_sound_index][0]}", True, (255, 255, 255))
    screen.blit(sound_name_text, (20, 20))
    
    control_text = font.render("Press SPACE to play, LEFT/RIGHT to change sound", True, (255, 255, 255))
    screen.blit(control_text, (20, 60))

# Main game loop
def main():
    global current_sound_index
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        
        draw_hud()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
