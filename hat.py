import pygame
import sys
import arabic_reshaper
from bidi.algorithm import get_display

pygame.init()
winning = False
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('پازل منطقی کلاه‌ها')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

font_path = r"fonts/IRANSans.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)

image_path = r"images/kolah.jpg"
image = pygame.image.load(image_path)

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
    label = font.render(bidi_text, True, BLACK)
    label_width = label.get_width()
    label_height = label.get_height()

    text_x = x + (width - label_width) // 2
    text_y = y + (height - label_height) // 2
    
    screen.blit(label, (text_x, text_y))

def show_intro_page():
    screen.fill(WHITE)
    
    screen.blit(image, (WIDTH//2 - image.get_width()//2, HEIGHT//2 - image.get_height()//2))  

    draw_text("پازل منطقی کلاه‌ها", WIDTH//2, 50, BLUE)
    draw_text("سه نفر در جزیره‌ی آدم خواران منطقی گیر افتاده‌اند.", WIDTH//2, 150)
    draw_text("آن‌ها پنج کلاه مشابه دارند. 3 کلاه سفید و 2 کلاه سیاه.", WIDTH//2, 200)
    draw_text("هر زندانی کلاه‌های دو نفر دیگر را می‌بیند، اما کلاه خودش را نمی‌تواند ببیند.", WIDTH//2, 250)
    draw_text("آیا نفر اول می‌تواند رنگ کلاه خود را درست حدس بزند؟", WIDTH//2, 300)

    draw_button("ادامه", WIDTH//2 - 75, HEIGHT - 100, 150, 50)

    pygame.display.update()

def show_puzzle_page(answer_text):
    screen.fill(WHITE)
    
    screen.blit(image, (WIDTH//2 - image.get_width()//2, HEIGHT//2 - image.get_height()//2))  

    draw_text("نفر آخر و نفر دوم رنگ کلاه خود را نمیدانند.", WIDTH//2, 150)
    draw_text("اما نفر اول ادعا میکند رنگ کلاه خود را میداند.", WIDTH//2, 200)
    draw_text("شما باید رنگ کلاه نفر اول را حدس بزنید.", WIDTH//2, 250)
    draw_text("جواب خود را وارد کنید:", WIDTH//2, 300)

    draw_text(answer_text, WIDTH//2, 350, RED)

    pygame.display.update()


def get_input():
    input_text = ""
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    return input_text  
                else:
                    input_text += event.unicode

        show_puzzle_page(input_text)  
        pygame.display.update()

def show_result(is_winner):
    global winning
    screen.fill(WHITE)
    if is_winner:
        draw_text("برنده شدی!", WIDTH//2, HEIGHT//2, GREEN)
        winning = True
    else:
        draw_text("باختی!", WIDTH//2, HEIGHT//2, RED)  

    pygame.display.update()
    pygame.time.delay(2000)  


def hat():
    global screen
    clock = pygame.time.Clock()
    running = True
    intro_page = True
    answer_text = ""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # تغییر اندازه صفحه
    pygame.display.set_caption("Hats Game")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if intro_page and WIDTH//2 - 75 <= mouse_x <= WIDTH//2 + 75 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    intro_page = False
                    show_puzzle_page(answer_text)
                    answer_text = get_input()  

                    if answer_text == "سفید":
                        show_result(True) 
                    else:
                        show_result(False)  

                    running = False 

        if intro_page:
            show_intro_page()
        else:
            show_puzzle_page(answer_text)

        pygame.display.update()
        clock.tick(60)
    if winning:
        return 60, True
    else:
        return -10, False
