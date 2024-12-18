import pygame
import sys
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()

winning = False
losing = False

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("پازل منطقی کلاه‌ها")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font_path = r"fonts\IRANSans.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)

image_path = r"images\ko.JPG"
image = pygame.image.load(image_path)

player_guess = ""
player_score = 0
input_active = True
answer_checked = False

def draw_text(text, x, y, color=BLACK):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    label = font.render(bidi_text, True, color)
    label_width = label.get_width()
    screen.blit(label, (x - label_width // 2, y))

def draw_button(text, x, y, width, height, color=BLUE):
    pygame.draw.rect(screen, color, (x, y, width, height))
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    label = font.render(bidi_text, True, WHITE)
    label_width = label.get_width()
    screen.blit(label, (x + (width - label_width) // 2, y + 10))

def show_puzzle_page():
    screen.fill(WHITE)
    screen.blit(image, (WIDTH//2 - image.get_width()//2, 80))

    draw_text("چهار مرد در صف ایستاده‌اند و دیواری بین نفر سوم و چهارم وجود دارد.", WIDTH//2, 20)
    draw_text("هر مرد فقط مردهای جلوی خود را می‌بیند و نمی‌تواند سرش را برگرداند.", WIDTH//2, 60)
    draw_text("دو کلاه سفید و دو کلاه سیاه وجود دارد.", WIDTH//2, 100)
    draw_text("کدام مرد می‌تواند رنگ کلاهش را حدس بزند؟", WIDTH//2, 140)
    draw_text("(پاسخ را به صورت یک عدد وارد کنید)", WIDTH//2, 180)

    draw_text("پاسخ: " + player_guess, WIDTH//2, 450, RED)

    draw_button("تایید", WIDTH//2 - 60, 510, 120, 40)

    pygame.display.update()

def show_result(is_correct):
    global winning, losing
    screen.fill(WHITE)
    if is_correct:
        draw_text("پاسخ درست است! سه امتیاز به شما اضافه شد.", WIDTH//2, HEIGHT//2, GREEN)
        winning = True
    else:
        draw_text("پاسخ اشتباه است! سه امتیاز از شما کم شد.", WIDTH//2, HEIGHT//2, RED)
        losing = True

    pygame.display.update()
    pygame.time.delay(5000)
    # pygame.quit()
    # sys.exit()

def get_input():
    global player_guess, player_score, input_active, answer_checked
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not answer_checked:

                    if player_guess == "2":
                        player_score += 3
                        show_result(True)
                    else:
                        player_score -= 3
                        show_result(False)
                    answer_checked = True
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_guess = player_guess[:-1]
                elif event.unicode.isdigit() and len(player_guess) < 1:
                    player_guess += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if WIDTH//2 - 60 <= mouse_x <= WIDTH//2 + 60 and 350 <= mouse_y <= 390:
                    if not answer_checked:
                        if player_guess == "2":
                            player_score += 3
                            show_result(True)
                        else:
                            player_score -= 3
                            show_result(False)
                        answer_checked = True
                        input_active = False

        show_puzzle_page()

def hats_game():
    global player_guess, player_score, screen, winning, losing, input_active, answer_checked
    player_guess = ""
    input_active = True
    answer_checked = False
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Solve the riddle!")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        show_puzzle_page()
        get_input()

        if winning:
            return player_score + 60, True
        elif losing:
            return player_score - 10, False
        pygame.display.update()
        clock.tick(60)

