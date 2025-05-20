import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen setup (increased size for better visibility)
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Toss")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 60)

# Load coin images
heads_img = pygame.image.load("images/head.png")
tails_img = pygame.image.load("images/tail.png")

# Scale images (make coins bigger)
heads_img = pygame.transform.scale(heads_img, (300, 300))
tails_img = pygame.transform.scale(tails_img, (300, 300))

def draw_text(text, x, y):
    """Helper function to render text."""
    rendered_text = font.render(text, True, BLACK)
    screen.blit(rendered_text, (x, y))

def toss_coin():
    """Simulates the coin toss animation and returns the result."""
    options = ["Heads", "Tails"]
    result = random.choice(options)
    animation_frames = [heads_img, tails_img] * 10  # Flipping animation

    # Animation loop
    for frame in animation_frames:
        screen.fill(WHITE)
        screen.blit(frame, (WIDTH//2 - 150, HEIGHT//2 - 150))  # Center the coin
        pygame.display.flip()
        time.sleep(0.1)  # Delay for animation

    return result

# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_text("Press SPACE to toss", WIDTH//2 - 220, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            result = toss_coin()
            # Display result
            screen.fill(WHITE)
            draw_text(f"The result is: {result}", WIDTH//2 - 200, 50)
            # Show the coin result in the center
            if result == "Heads":
                screen.blit(heads_img, (WIDTH//2 - 150, HEIGHT//2 - 150))
            else:
                screen.blit(tails_img, (WIDTH//2 - 150, HEIGHT//2 - 150))
            pygame.display.flip()
            time.sleep(2)

    pygame.display.flip()

# Quit pygame
pygame.quit()
