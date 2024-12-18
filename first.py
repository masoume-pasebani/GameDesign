import pygame
import sys
import arabic_reshaper
from bidi.algorithm import get_display
import textwrap  

pygame.init()

winning = False
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("چیستان - بازی اژدها")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)

font_path = r"fonts\IRANSans.ttf"
font = pygame.font.Font(font_path, 28)

question = "آن چیست که هر چه از آن کم میکنی بیشتر میشود؟"
correct_answer = "حفره"

success_message = "آفرین! پاسخ درست بود. تو برنده شدی!"
failure_message = "پاسخ اشتباه بود! بازی تمام شد."

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def wrap_text(text, line_width=40):
    return textwrap.wrap(text, line_width)

def show_centered_text(text, y_offset=0, color=BLACK):
    lines = wrap_text(text) 
    total_height = len(lines) * font.get_height()
    start_y = (HEIGHT - total_height) // 2 + y_offset

    for i, line in enumerate(lines):
        reshaped_line = reshape_text(line)
        rendered_text = font.render(reshaped_line, True, color)
        text_rect = rendered_text.get_rect(center=(WIDTH // 2, start_y + i * font.get_height()))
        screen.blit(rendered_text, text_rect)

def show_message(message, color):
    screen.fill(color)
    show_centered_text(message)
    pygame.display.update()
    pygame.time.wait(3000)


def firstPuzzle():
    global screen, winning
    answer_input = ""
    input_active = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Solve the riddle!")
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if answer_input.strip() == correct_answer:
                        show_message(success_message, GREEN)
                        winning = True
                        return 60, True
                    else:
                        show_message(failure_message, RED)
                        return -10, False
                elif event.key == pygame.K_BACKSPACE:
                    answer_input = answer_input[:-1]
                else:
                    answer_input += event.unicode

        screen.fill(WHITE)
        show_centered_text(question, y_offset=-30)
        show_centered_text(f"پاسخ: {answer_input}", y_offset=100)
        pygame.display.update()

