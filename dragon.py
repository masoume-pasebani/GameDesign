import pygame
import sys
import arabic_reshaper
from bidi.algorithm import get_display
import textwrap
pygame.init()

WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("بازی اژدها")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)

font_path = r"fonts\IRANSans.ttf"
font = pygame.font.Font(font_path, 28)

questions = [
    {"question": "آن چیست که در روسیه، کره جنوبی، کره شمالی، عربستان، عراق و ترکمنستان دوم شده است اما در روسیه اول؟",
     "answer": "ر",
     "success_message": "اکنون آماده سوال دوم باش..."},
    {"question": "وقتی از قطب، دشت کویر و لب ساحل برمیگردم، او می ماند.",
     "answer": "رد پا",
     "success_message": "خوب کار کردی، اما سوال آخر دشوارتر خواهد بود."},
    {"question": "عمر مرا با ساعت اندازه می گیرند و با پایان یافتنم به تو خدمت میکنم. وقتی لاغر باشم سریعم و وقتی چاق باشم کند. باد دشمن من است.",
     "answer": "شمع",
     "success_message": "تو توانستی از هر سه چیستان عبور کنی. دکمه Enter را بفشار و از آزادی خود لذت ببر!"}
]

current_question = 0

intro_text = """ای مسافر، تو که بی پروا به قلمرو من و برادرانم وارد شده‌ای، اکنون در دام ما افتاده‌ای.
اما خوش شانس هستی، چرا که امروز روز مهربانی ماست. فرصتی به تو می‌دهیم که از این مهلکه بگریزی،
اما به شرط آنکه شایستگی‌ات را ثابت کنی.
هر یک از سرهای ما معمایی برایت دارد؛ سه چیستان که هریک از دیگری سخت‌تر است.
اگر با علم خود بتوانی هر سه را پاسخ دهی، ما این دیوار را در آتش می‌سوزانیم و راهت را باز می‌کنیم.
اما اگر حتی در یکی شکست بخوری، در شعله‌های ما خواهی سوخت."""

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

def draw_button(text, rect, hover=False):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=10)
    button_text = font.render(reshape_text(text), True, WHITE)
    button_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, button_rect)

def show_intro():
    intro_running = True
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)

    while intro_running:
        screen.fill(WHITE)
        show_centered_text(intro_text)
        mouse_pos = pygame.mouse.get_pos()

        hover = button_rect.collidepoint(mouse_pos)
        draw_button("ادامه", button_rect, hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and hover:
                intro_running = False

        pygame.display.update()

def show_success_message(message):
    screen.fill(GREEN)
    show_centered_text(message)
    pygame.display.update()
    pygame.time.wait(3000)

def dragon_game():
    global current_question, screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Solve the riddles!")
    show_intro()

    while current_question < len(questions):  # بررسی محدوده‌ی سوالات
        screen.fill(WHITE)

        # مطمئن شوید که سوال موجود در محدوده است
        if current_question < len(questions):
            show_centered_text(f"چیستان {current_question + 1}:\n{questions[current_question]['question']}")

        answer_input = ""
        input_active = True

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # چک کنید که سوال وجود دارد
                        if current_question < len(questions) and answer_input.strip() == questions[current_question]["answer"]:
                            show_success_message(questions[current_question]["success_message"])
                            current_question += 1
                            input_active = False
                        else:
                            screen.fill(RED)
                            show_centered_text("پاسخ اشتباه بود! بازی تمام شد.")
                            pygame.display.update()
                            pygame.time.wait(3000)
                            return -10, False
                    elif event.key == pygame.K_BACKSPACE:
                        answer_input = answer_input[:-1]
                    else:
                        answer_input += event.unicode

            screen.fill(WHITE)
            # بررسی دوباره برای جلوگیری از دسترسی به سوال خارج از محدوده
            if current_question < len(questions):
                show_centered_text(f"چیستان {current_question + 1}:\n{questions[current_question]['question']}")
                show_centered_text(f"پاسخ: {answer_input}", y_offset=100)
            pygame.display.update()

    screen.fill(GREEN)
    show_centered_text("تبریک! تو توانستی از هر سه چیستان عبور کنی و آزاد شوی!")
    pygame.display.update()
    pygame.time.wait(5000)
    return 60, True
