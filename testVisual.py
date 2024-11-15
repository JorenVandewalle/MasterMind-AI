import pygame
import sys
from solver import knuth_mastermind

pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Mastermind")

# Define colors
BACKGROUND = (168, 181, 187)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Button positions and colors
button_radius = 30
button_positions = [(100, 60), (250, 60), (400, 60), (100, 125), (250, 125), (400, 125)]
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

# Circles for position preset
circle_radius = 8
circle_positions = [(62, 262), (87, 262), (62, 287), (87, 287)]
circle_colors = [(0, 0, 0), (0, 255, 255), (255, 0, 0), (0, 255, 0)]



def draw_button():
    for position, color in zip(button_positions, button_colors):
        pygame.draw.circle(screen, BLACK, position, button_radius)
        pygame.draw.circle(screen, color, position, button_radius - 2)

def draw_layout():
    # Draw the main area
    pygame.draw.rect(screen, BACKGROUND, (50, 25, 400, 135))
    pygame.draw.rect(screen, BLACK, (50, 25, 400, 135), 2)

    # Draw the rows for guesses
    for i in range(7):
        pygame.draw.rect(screen, BACKGROUND, (50, 250 + i * 70, 50, 50))
        pygame.draw.rect(screen, BLACK, (50, 250 + i * 70, 50, 50), 2)
        pygame.draw.rect(screen, BACKGROUND, (105, 250 + i * 70, 290, 50))
        pygame.draw.rect(screen, BLACK, (105, 250 + i * 70, 290, 50), 2)
        pygame.draw.rect(screen, BACKGROUND, (400, 250 + i * 70, 50, 50))
        pygame.draw.rect(screen, BLACK, (400, 250 + i * 70, 50, 50), 2)

    # Draw the circles for position preset
    for position, color in zip(circle_positions, circle_colors):
        pygame.draw.circle(screen, BLACK, position, circle_radius)
        pygame.draw.circle(screen, color, position, circle_radius)

    # Draw the play button
    pygame.draw.rect(screen, GREEN, (200, 730, 100, 40))
    pygame.draw.rect(screen, BLACK, (200, 730, 100, 40), 2)

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
                if (200 <= event.pos[0] <= 300) and (750 <= event.pos[1] <= 790):
                    print("Play button clicked!")
                    button_colors[0] = ((214, 0, 221))

    screen.fill((68, 81, 87))
    draw_layout()
    draw_button()
    pygame.display.flip()

pygame.quit()