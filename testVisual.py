import pygame
import sys

pygame.init()

SCREEN_SIZE = (1000, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mastermind")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define button positions and colors for the color buttons
button_radius = 40
button_positions = [
    (112 - 45 + button_radius, 75),  # Red
    (224 - 45 + button_radius, 75),  # Green
    (336 - 45 + button_radius, 75),  # Blue
    (448 - 45 + button_radius, 75),  # Yellow
    (560 - 45 + button_radius, 75),  # Orange
    (672 - 45 + button_radius, 75),  # Purple
    (784 - 45 + button_radius, 75),  # White
    (896 - 45 + button_radius, 75)   # Cyan
]
button_colors = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 255, 255),  # White
    (0, 255, 255)     # Cyan
]

def draw_button():
    # Draw color buttons as circles with black borders
    for position, color in zip(button_positions, button_colors):
        # Draw the border (black)
        pygame.draw.circle(screen, BLACK, position, button_radius)
        # Draw the filled circle
        pygame.draw.circle(screen, color, position, button_radius - 2)

def draw_layout():
    # Draw the code pegs area (hidden from player)
    pygame.draw.rect(screen, WHITE, (50, 25, 900, 100))  # Code area
    pygame.draw.rect(screen, BLACK, (50, 25, 900, 100), 2)  # Border for code area

    # Draw the guess pegs area
    for i in range(8):  # 8 guesses
        pygame.draw.rect(screen, WHITE, (50, 175 + i * 70, 900, 50))  # Guess area
        pygame.draw.rect(screen, BLACK, (50, 175 + i * 70, 900, 50), 2)  # Border for guess area

    # Draw the feedback area
    for i in range(8):  # 8 guesses
        pygame.draw.rect(screen, WHITE, (950, 175 + i * 70, 50, 50))  # Feedback area
        pygame.draw.rect(screen, BLACK, (950, 175 + i * 70, 50, 50), 2)  # Border for feedback area

    # Draw the play button
    pygame.draw.rect(screen, GREEN, (450, 800, 100, 50))  # Play button
    pygame.draw.rect(screen, BLACK, (450, 800, 100, 50), 2)  # Border for play button
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    screen.blit(text, (475, 660))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if any color button was clicked
                for position in button_positions:
                    if pygame.math.Vector2(position).distance_to(event.pos) <= button_radius:
                        print("Color button clicked!")

                # Check if play button was clicked
                if pygame.Rect(450, 650, 100, 50).collidepoint(event.pos):
                    print("Play button clicked!")

    # Fill the screen with a background color
    screen.fill((68, 81, 87))

    # Draw the layout and buttons
    draw_layout()
    draw_button()

    # Update the display
    pygame.display.flip ()

pygame.quit()