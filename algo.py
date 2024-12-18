import pygame
import sys
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()

WIDTH, HEIGHT = 800, 400
FPS = 60

FONT_PERSIAN = pygame.font.Font(r"fonts\IRANSans.ttf", 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

attempts = 0
max_attempts = 4
score = 5
hints = [
    "راهنمای 1: به ترتیب حروف دقت کنید.",
    "راهنمای 2: ممکن است کلمه خروجی تغییر نکرده باشد."
]
current_word = "\u062f\u0627\u0648\u0631"  # 'داور'
correct_output = "\u062f\u0627\u0648\u0631"  # 'داور'
user_input = ""
message = "کلمه \"داور\" را به فرم جدید تبدیل کنید."
winning = False

# Pygame Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("پازل تبدیل کلمات")
clock = pygame.time.Clock()
image = pygame.image.load(r"images\davar.PNG")
image = pygame.transform.scale(image, (200, 100))


# Functions
def render_persian_text(text, color):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return FONT_PERSIAN.render(bidi_text, True, color)


def draw_screen():
    screen.fill(WHITE)

    score_text = render_persian_text(f"امتیاز: {score}", BLACK)
    attempts_text = render_persian_text(f"تعداد تلاش‌ها: {attempts}/{max_attempts}", BLACK)
    message_text = render_persian_text(message, BLUE if attempts < max_attempts else RED)
    user_input_text = render_persian_text(f"ورودی شما: {user_input}", BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    attempts_rect = attempts_text.get_rect(center=(WIDTH // 2, 100))
    image_rect = image.get_rect(center=(WIDTH // 2, 175))
    message_rect = message_text.get_rect(center=(WIDTH // 2, 250))
    user_input_rect = user_input_text.get_rect(center=(WIDTH // 2, 300))
    screen.blit(score_text, score_rect)
    screen.blit(attempts_text, attempts_rect)
    screen.blit(image, image_rect)
    screen.blit(message_text, message_rect)
    screen.blit(user_input_text, user_input_rect)
    pygame.display.flip()

def show_try_again():
    screen.fill(ORANGE)
    try_again_text = render_persian_text("دوباره تلاش کن!", BLACK)
    try_again_rect = try_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(try_again_text, try_again_rect)
    pygame.display.flip()
    pygame.time.wait(1500)


def game_over(won):
    screen.fill(WHITE)
    end_message = "شما برنده شدید!" if won else f"بازی تمام شد! پاسخ درست: {correct_output}"
    end_text = render_persian_text(end_message, GREEN if won else RED)
    screen.blit(end_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


def input_box():
    global user_input, attempts, message, score, winning
    user_text = ""
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    attempts += 1
                    if user_text == correct_output:
                        score += 5
                        winning = True
                        game_over(True)
                    else:
                        show_try_again()
                        score -= 1
                        if attempts == 2:
                            message = hints[0]
                        elif attempts == 4:
                            message = hints[1]
                        if attempts >= max_attempts:
                            game_over(False)
                    user_input = user_text
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        screen.fill(WHITE)
        input_text = render_persian_text("پاسخ خود را وارد کنید: " + user_text, BLACK)
        input_rect = input_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(input_text, input_rect)
        pygame.display.flip()


# Main Loop
def main_algo():
    global winning, score, attempts
    puzzle_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("پازل تبدیل کلمات")
    global score
    score = 0
    attempts = 0
    winning = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_box()

        draw_screen()
        clock.tick(FPS)

        if winning:
            return score, True
        elif attempts >= max_attempts:
            return score, False
