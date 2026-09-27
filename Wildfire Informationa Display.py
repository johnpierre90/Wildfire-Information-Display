import pygame
import sys

pygame.init()

# Create the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

# Load images
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

wildlife = pygame.image.load("lion.png")
wildlife = pygame.transform.scale(wildlife, (300, 250))

# Fonts
title_font = pygame.font.Font(None, 50)
text_font = pygame.font.Font(None, 30)

# Text
title = title_font.render("African Lion", True, (255, 255, 255))
fact = text_font.render(
    "Lions are social animals that live in groups called prides.",
    True,
    (255, 255, 255)
)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Draw wildlife image
    screen.blit(wildlife, (250, 180))

    # Draw heading and fact
    screen.blit(title, (300, 50))
    screen.blit(fact, (100, 500))

    # Update screen
    pygame.display.flip()

    # 60 frames per second
    clock.tick(60)

pygame.quit()
sys.exit()