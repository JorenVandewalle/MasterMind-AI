import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Mastermind")

# Define colors
BACKGROUND = (168, 181, 187)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define the font
font = pygame.font.Font(None, 30)

# Track which private code circle to fill
selected_circle_index = 0

# Button positions and colors
interactive_button_radius = 30
button_positions = [(100, 60), (250, 60), (400, 60), (100, 125), (250, 125), (400, 125)]
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

# Circles for position preset
circle_radiusSmall = 8
circle_radiusLarge = 20

circle_positionsPrCode = [(195, 205), (265, 205), (335, 205), (405, 205)]
circle_colorsPrCode = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions1L = [(62, 262), (87, 262), (62, 287), (87, 287)]
circle_colors1L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions1R = [(412, 262), (437, 262), (412, 287), (437, 287)]
circle_colors1R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions1 = [(145, 275), (215, 275), (285, 275), (355, 275)]
circle_colors1 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions2L = [(62, 332), (87, 332), (62, 357), (87, 357)]
circle_colors2L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions2R = [(412, 332), (437, 332), (412, 357), (437, 357)]
circle_colors2R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions2 = [(145, 345), (215, 345), (285, 345), (355, 345)]
circle_colors2 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions3L = [(62, 402), (87, 402), (62, 427), (87, 427)]
circle_colors3L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions3R = [(412, 402), (437, 402), (412, 427), (437, 427)]
circle_colors3R =[(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions3 = [(145, 415), (215, 415), (285, 415), (355, 415)]
circle_colors3 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions4L = [(62, 472), (87, 472), (62, 497), (87, 497)]
circle_colors4L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions4R = [(412, 472), (437, 472), (412, 497), (437, 497)]
circle_colors4R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions4 = [(145, 485), (215, 485), (285, 485), (355, 485)]
circle_colors4 = [(128 , 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions5L = [(62, 542), (87, 542), (62, 567), (87, 567)]
circle_colors5L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions5R = [(412, 542), (437, 542), (412, 567), (437, 567)]
circle_colors5R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions5 = [(145, 555), (215, 555), (285, 555), (355, 555)]
circle_colors5 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions6L = [(62, 612), (87, 612), (62, 637), (87, 637)]
circle_colors6L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions6R = [(412, 612), (437, 612), (412, 637), (437, 637)]
circle_colors6R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions6 = [(145, 625), (215, 625), (285, 625), (355, 625)]
circle_colors6 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions7L = [(62, 682), (87, 682), (62, 707), (87, 707)]
circle_colors7L = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]
circle_positions7R = [(412, 682), (437, 682), (412, 707), (437, 707)]
circle_colors7R = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

circle_positions7 = [(145, 695), (215, 695), (285, 695), (355, 695)]
circle_colors7 = [(128, 141, 147), (128, 141, 147), (128, 141, 147), (128, 141, 147)]

def draw_button():
    for position, color in zip(button_positions, button_colors):
        pygame.draw.circle(screen, BLACK, position, interactive_button_radius)
        pygame.draw.circle(screen, color, position, interactive_button_radius - 2)

def draw_layout():
    # Draw the main area
    pygame.draw.rect(screen, BACKGROUND, (50, 25, 400, 135))
    pygame.draw.rect(screen, BLACK, (50, 25, 400, 135), 2)

    # Private code
    private_code_text = font.render("Private Code:", True, BLACK)
    text_rect = private_code_text.get_rect(center=(85, 205))
    screen.blit(private_code_text, text_rect)
    pygame.draw.rect(screen, BACKGROUND, (155, 180, 290, 50))
    pygame.draw.rect(screen, BLACK, (155, 180, 290, 50),2)
    for position, color in zip(circle_positionsPrCode, circle_colorsPrCode):
        pygame.draw.circle(screen, color, position, circle_radiusLarge)

    # Draw the rows for guesses
    for i in range(7):
        pygame.draw.rect(screen, BACKGROUND, (50, 250 + i * 70, 50, 50))
        pygame.draw.rect(screen, BLACK, (50, 250 + i * 70, 50, 50), 2)
        pygame.draw.rect(screen, BACKGROUND, (105, 250 + i * 70, 290, 50))
        pygame.draw.rect(screen, BLACK, (105, 250 + i * 70, 290, 50), 2)
        pygame.draw.rect(screen, BACKGROUND, (400, 250 + i * 70, 50, 50))
        pygame.draw.rect(screen, BLACK, (400, 250 + i * 70, 50, 50), 2)

    # Draw the small circles for the positions preset
    circle_groupsSmall = [
        (circle_positions1L, circle_colors1L),
        (circle_positions1R, circle_colors1R),
        (circle_positions2L, circle_colors2L),
        (circle_positions2R, circle_colors2R),
        (circle_positions3L, circle_colors3L),
        (circle_positions3R, circle_colors3R),
        (circle_positions4L, circle_colors4L),
        (circle_positions4R, circle_colors4R),
        (circle_positions5L, circle_colors5L),
        (circle_positions5R, circle_colors5R),
        (circle_positions6L, circle_colors6L),
        (circle_positions6R, circle_colors6R),
        (circle_positions7L, circle_colors7L),
        (circle_positions7R, circle_colors7R),
    ]
    
    for positions, colors in circle_groupsSmall:
        for position, color in zip(positions, colors):
            pygame.draw.circle(screen, color, position, circle_radiusSmall)

    # Draw the large circles for the guesses
    circle_groupsLarge = [
        (circle_positions1, circle_colors1),
        (circle_positions2, circle_colors2),
        (circle_positions3, circle_colors3),
        (circle_positions4, circle_colors4),
        (circle_positions5, circle_colors5),
        (circle_positions6, circle_colors6),
        (circle_positions7, circle_colors7),
    ]

    for positions, colors in circle_groupsLarge:
        for position, color in zip(positions, colors):
            pygame.draw.circle(screen, color, position, circle_radiusLarge)

    # Draw the play button
    pygame.draw.rect(screen, GREEN, (200, 730, 100, 40))
    pygame.draw.rect(screen, BLACK, (200, 730, 100, 40), 2)

    # Render the text "Play"
    play_text = font.render("Play", True, BLACK)  # True for anti-aliasing
    text_rect = play_text.get_rect(center=(250, 750))  # Center the text on the button
    screen.blit(play_text, text_rect)  # Draw the text onto the screen

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if a button is clicked
                for index, position in enumerate(button_positions):
                    if (position[0] - event.pos[0]) ** 2 + (position[1] - event.pos[1]) ** 2 <= interactive_button_radius ** 2:
                        print(f"Color {index} button clicked!")
                        
                        # Update the private code circle color if not all are filled
                        if selected_circle_index < len(circle_positionsPrCode):
                            circle_colorsPrCode[selected_circle_index] = button_colors[index]
                            selected_circle_index += 1  # Move to the next circle

                # Check if "Play" button is clicked
                if (200 <= event.pos[0] <= 300) and (730 <= event.pos[1] <= 770):
                    print("Play button clicked!")

    screen.fill((68, 81, 87))
    draw_layout()
    draw_button()
    pygame.display.flip()

pygame.quit()