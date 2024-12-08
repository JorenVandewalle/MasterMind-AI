import pygame
import itertools
from collections import Counter

pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Mastermind Solver")

# Define colors
BACKGROUND = (168, 181, 187)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Define the font
font = pygame.font.Font(None, 30)

# Button positions and colors
interactive_button_radius = 30
button_positions = [(100, 60), (250, 60), (400, 60), (100, 125), (250, 125), (400, 125)]
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

# Secret Code Input
selected_circle_index = 0
secret_code = []

# Circle Positions and Colors
circle_radiusSmall = 8
circle_radiusLarge = 20

circle_positionsPrCode = [(195, 205), (265, 205), (335, 205), (405, 205)]
circle_colorsPrCode = [(128, 141, 147)] * 4  # Placeholder

circle_positions_large = [
    [(145, 275 + 70 * i), (215, 275 + 70 * i), (285, 275 + 70 * i), (355, 275 + 70 * i)] for i in range(7)
]
circle_colors_large = [[(128, 141, 147)] * 4 for _ in range(7)]

circle_positions_small = [
    [(62 + j * 25, 262 + 70 * i) for j in range(2)] + [(62 + j * 25, 287 + 70 * i) for j in range(2)]
    for i in range(7)
]
circle_colors_small = [[(128, 141, 147)] * 4 for _ in range(7)]  # Black and white feedback

# Game State
game_started = False
ai_attempts = 0
possible_codes = []
all_codes = []
ai_guess = []
feedback = (0, 0)


def calculate_feedback(guess, code):
    black_pins = sum(g == c for g, c in zip(guess, code))
    white_pins = sum((Counter(code) & Counter(guess)).values()) - black_pins
    return black_pins, white_pins


def filter_possible_codes(possible_codes, guess, feedback):
    return [
        code
        for code in possible_codes
        if calculate_feedback(guess, code) == feedback
    ]


def choose_next_guess(possible_codes):
    best_guess = None
    smallest_worst_case = float("inf")

    for guess in possible_codes:
        feedback_counts = Counter(calculate_feedback(guess, code) for code in possible_codes)
        worst_case = max(feedback_counts.values())

        if worst_case < smallest_worst_case:
            smallest_worst_case = worst_case
            best_guess = guess

    return best_guess


def knuth_mastermind_start(colors, positions):
    global possible_codes, all_codes, ai_guess, ai_attempts
    all_codes = list(itertools.product(colors, repeat=positions))
    possible_codes = all_codes[:]
    ai_guess = tuple(colors[:2] * (positions // 2))
    ai_attempts = 0


def ai_step():
    global ai_guess, possible_codes, feedback, ai_attempts, game_started

    if not game_started:
        return

    # Add a small delay before displaying the next guess
    pygame.time.wait(500)  # Wait for 500 milliseconds (0.5 seconds)

    # Calculate feedback and display the guess
    feedback = calculate_feedback(ai_guess, tuple(secret_code))
    circle_colors_large[ai_attempts] = [button_colors["RGBYOP".index(color)] for color in ai_guess]
    for i in range(feedback[0]):
        circle_colors_small[ai_attempts][i] = BLACK
    for i in range(feedback[0], feedback[0] + feedback[1]):
        circle_colors_small[ai_attempts][i] = WHITE

    # Check if AI solved it
    if feedback == (4, 0):
        game_started = False
        print(f"AI solved the code in {ai_attempts + 1} attempts!")
        return

    # Filter possibilities and choose next guess
    possible_codes = filter_possible_codes(possible_codes, ai_guess, feedback)
    ai_guess = choose_next_guess(possible_codes)
    ai_attempts += 1



def draw_button():
    for position, color in zip(button_positions, button_colors):
        pygame.draw.circle(screen, BLACK, position, interactive_button_radius)
        pygame.draw.circle(screen, color, position, interactive_button_radius - 2)


def draw_layout():
    # Main layout and secret code circles
    pygame.draw.rect(screen, BACKGROUND, (50, 25, 400, 135))
    pygame.draw.rect(screen, BLACK, (50, 25, 400, 135), 2)

    private_code_text = font.render("Private Code:", True, BLACK)
    screen.blit(private_code_text, (50, 180))
    pygame.draw.rect(screen, BACKGROUND, (155, 180, 290, 50))
    pygame.draw.rect(screen, BLACK, (155, 180, 290, 50), 2)
    for position, color in zip(circle_positionsPrCode, circle_colorsPrCode):
        pygame.draw.circle(screen, color, position, circle_radiusLarge)

    # Draw guesses and feedback
    for row, (positions, colors_large, colors_small) in enumerate(
        zip(circle_positions_large, circle_colors_large, circle_colors_small)
    ):
        for position, color in zip(positions, colors_large):
            pygame.draw.circle(screen, color, position, circle_radiusLarge)
        for position, color in zip(circle_positions_small[row], colors_small):
            pygame.draw.circle(screen, color, position, circle_radiusSmall)

    # Draw the play button
    pygame.draw.rect(screen, GREEN, (200, 730, 100, 40))
    pygame.draw.rect(screen, BLACK, (200, 730, 100, 40), 2)
    play_text = font.render("Play", True, BLACK)
    text_rect = play_text.get_rect(center=(250, 750))
    screen.blit(play_text, text_rect)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for index, position in enumerate(button_positions):
                    if (position[0] - event.pos[0]) ** 2 + (position[1] - event.pos[1]) ** 2 <= interactive_button_radius ** 2:
                        if selected_circle_index < 4:
                            secret_code.append("RGBYOP"[index])
                            circle_colorsPrCode[selected_circle_index] = button_colors[index]
                            selected_circle_index += 1

                if (200 <= event.pos[0] <= 300) and (730 <= event.pos[1] <= 770):
                    if len(secret_code) == 4:
                        knuth_mastermind_start("RGBYOP", 4)
                        game_started = True

    if game_started:
        ai_step()

    screen.fill((68, 81, 87))
    draw_layout()
    draw_button()
    pygame.display.flip()

pygame.quit()
