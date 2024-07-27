import pygame
import sys
from array import array

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong with Sound FX")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# Paddle and ball properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 10
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create paddles and ball
left_paddle = pygame.Rect(20, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Define functions to generate sound effects
def generate_beep_sound(frequency=440, duration=0.1):
    sample_rate = pygame.mixer.get_init()[0]
    max_amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
    samples = int(sample_rate * duration)
    wave = [int(max_amplitude * ((i // (sample_rate // frequency)) % 2)) for i in range(samples)]
    sound = pygame.mixer.Sound(buffer=array('h', wave))
    sound.set_volume(0.1)
    return sound

# Create sound effects
hit_paddle_sound = generate_beep_sound(440, 0.1)  # Frequency for hitting paddle
hit_wall_sound = generate_beep_sound(523.25, 0.1)  # Frequency for hitting wall

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

def draw_loading_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    loading_text = font.render("Loading...", True, WHITE)
    text_rect = loading_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(loading_text, text_rect)
    
    # Draw a loading bar
    pygame.draw.rect(screen, GREY, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 20), 2)
    pygame.draw.rect(screen, WHITE, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 0, 20))
    
    pygame.display.flip()

def main():
    global BALL_SPEED_X, BALL_SPEED_Y
    clock = pygame.time.Clock()

    # Show the loading screen
    loading_time = 2000  # Time in milliseconds (2 seconds)
    start_time = pygame.time.get_ticks()
    
    while pygame.time.get_ticks() - start_time < loading_time:
        draw_loading_screen()
        pygame.time.delay(50)  # Delay to slow down the loop slightly
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
            left_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += BALL_SPEED_X
        ball.y += BALL_SPEED_Y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            BALL_SPEED_Y = -BALL_SPEED_Y
            hit_wall_sound.play()  # Play wall hit sound

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            BALL_SPEED_X = -BALL_SPEED_X
            hit_paddle_sound.play()  # Play paddle hit sound

        # Ball out of bounds
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            BALL_SPEED_X = -BALL_SPEED_X  # Reset direction

        draw_objects()
        pygame.display.flip()
        clock.tick(60)  # Ensure the game runs at 60 FPS

if __name__ == "__main__":
    main()
