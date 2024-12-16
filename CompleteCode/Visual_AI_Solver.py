import pygame
import itertools
from collections import Counter

pygame.init()
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Mastermind Solver")

BACKGROUND = (168, 181, 187)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

font = pygame.font.Font(None, 30)

interactive_button_radius = 25
button_positions = [(100, 40), (250, 40), (400, 40), (100, 95), (250, 95), (400, 95)]
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (0, 255, 255)]

selected_circle_index = 0
secret_code = []

circle_radiusSmall = 8
circle_radiusLarge = 20

circle_positionsPrCode = [(195, 160), (265, 160), (335, 160), (405, 160)]
circle_colorsPrCode = [(128, 141, 147)] * 4

circle_positions_large = [
    [(185, 220 + 70 * i), (255, 220 + 70 * i), (325, 220 + 70 * i), (395, 220 + 70 * i)] for i in range(7)
]
circle_colors_large = [[(128, 141, 147)] * 4 for _ in range(7)]

circle_positions_small = [
    [(100 + j * 25, 210 + 70 * i) for j in range(2)] + [(100 + j * 25, 235 + 70 * i) for j in range(2)]
    for i in range(7)
]
circle_colors_small = [[(128, 141, 147)] * 4 for _ in range(7)]

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
    ai_guess = 'R', 'R', 'G', 'G'
    ai_attempts = 0

def ai_step():
    global ai_guess, possible_codes, feedback, ai_attempts, game_started

    if not game_started:
        return

    pygame.time.wait(500)

    # Calculate feedback and display the guess
    feedback = calculate_feedback(ai_guess, tuple(secret_code))
    circle_colors_large[ai_attempts] = [button_colors["RGBYOC".index(color)] for color in ai_guess]
    for i in range(feedback[0]):
        circle_colors_small[ai_attempts][i] = BLACK
    for i in range(feedback[0], feedback[0] + feedback[1]):
        circle_colors_small[ai_attempts][i] = WHITE

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
    pygame.draw.rect(screen, BACKGROUND, (50, 10, 400, 115))
    pygame.draw.rect(screen, BLACK, (50, 10, 400, 115), 2)

    private_code_text = font.render("Private", True, BLACK)
    private_code_text2 = font.render("Code:", True, BLACK)
    screen.blit(private_code_text, (50, 135))
    screen.blit(private_code_text2, (50, 155))
    pygame.draw.rect(screen, BACKGROUND, (155, 135, 290, 50))
    pygame.draw.rect(screen, BLACK, (155, 135, 290, 50), 2)
    for position, color in zip(circle_positionsPrCode, circle_colorsPrCode):
        pygame.draw.circle(screen, color, position, circle_radiusLarge)

    for row, (positions, colors_large, colors_small) in enumerate(
        zip(circle_positions_large, circle_colors_large, circle_colors_small)
    ):
        for position, color in zip(positions, colors_large):
            pygame.draw.circle(screen, color, position, circle_radiusLarge)
        for position, color in zip(circle_positions_small[row], colors_small):
            pygame.draw.circle(screen, color, position, circle_radiusSmall)

    


def draw_game_function_btns():
    # Play button
    pygame.draw.rect(screen, GREEN, (200, 670, 100, 40))
    pygame.draw.rect(screen, BLACK, (200, 670, 100, 40), 2)
    play_text = font.render("Play", True, BLACK)
    text_rect = play_text.get_rect(center=(250, 690))
    screen.blit(play_text, text_rect)
    # Restart button
    pygame.draw.rect(screen, ORANGE, (150, 715, 200, 40))
    pygame.draw.rect(screen, BLACK, (150, 715, 200, 40), 2)
    restart_text = font.render("Restart", True, BLACK)
    text_rect = restart_text.get_rect(center=(250, 735))
    screen.blit(restart_text, text_rect)


    

def reset_game():
    global game_started, ai_attempts, possible_codes, all_codes, ai_guess, feedback
    global selected_circle_index, secret_code, circle_colorsPrCode, circle_colors_large, circle_colors_small

    game_started = False
    ai_attempts = 0
    possible_codes = []
    all_codes = []
    ai_guess = []
    feedback = (0, 0)
    selected_circle_index = 0
    secret_code = []
    circle_colorsPrCode = [(128, 141, 147)] * 4
    circle_colors_large = [[(128, 141, 147)] * 4 for _ in range(7)]
    circle_colors_small = [[(128, 141, 147)] * 4 for _ in range(7)]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for index, position in enumerate(button_positions):
                    if (position[0] - event.pos[0]) ** 2 + (position[1] - event.pos[1]) ** 2 <= interactive_button_radius ** 2:
                        if selected_circle_index < 4:
                            secret_code.append("RGBYOC"[index])
                            circle_colorsPrCode[selected_circle_index] = button_colors[index]
                            selected_circle_index += 1

                
                if (200 <= event.pos[0] <= 300) and (670 <= event.pos[1] <= 710):
                    if len(secret_code) == 4:
                        print("Play btn clicked")
                        knuth_mastermind_start("RGBYOC", 4)
                        game_started = True

                if (150 <= event.pos[0] <= 350) and (715 <= event.pos[1] <= 755):
                    reset_game()

    if game_started:
        ai_step()

    screen.fill((68, 81, 87))
    draw_layout()
    draw_button()
    if not game_started:
        draw_game_function_btns()
    pygame.display.flip()

pygame.quit()
