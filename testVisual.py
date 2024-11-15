import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mastermind")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Button positions and colors
button_radius = 40
button_positions = [(140, 75), (280, 75), (420, 75), (560, 75), (700, 75), (840, 75)]
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

def draw_button():
    for position, color in zip(button_positions, button_colors):
        pygame.draw.circle(screen, BLACK, position, button_radius)
        pygame.draw.circle(screen, color, position, button_radius - 2)

def draw_layout():
    pygame.draw.rect(screen, WHITE, (50, 25, 900, 100))
    pygame.draw.rect(screen, BLACK, (50, 25, 900, 100), 2)

    for i in range(8):
        pygame.draw.rect(screen, WHITE, (50, 175 + i * 70, 900, 50))
        pygame.draw.rect(screen, BLACK, (50, 175 + i * 70, 900, 50), 2)

    pygame.draw.rect(screen, WHITE, (950, 175, 50, 560))
    pygame.draw.rect(screen, BLACK, (950, 175, 50, 560), 2)

    pygame.draw.rect(screen, GREEN, (450, 800, 100, 50))
    pygame.draw.rect(screen, BLACK, (450, 800, 100, 50), 2)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for index, position in enumerate(button_positions):
                    if (position[0] - event.pos[0]) ** 2 + (position[1] - event.pos[1]) ** 2 <= button_radius ** 2:
                        print(f"Color {index} button clicked!")
                if (450, 800) == (event.pos[0], event.pos[1]) or (450, 650) == (event.pos[0], event.pos[1]):
                    print("Play button clicked!")

    screen.fill((68, 81, 87))
    draw_layout()
    draw_button()
    pygame.display.flip()

pygame.quit()