import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1200, 600
FPS = 60
MATCH_WIDTH = 10
MATCH_LENGTH = 60
FONT = pygame.font.Font(None, 36)


WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matchstick Puzzle")
clock = pygame.time.Clock()

matchsticks = [
    pygame.Rect(100, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(100, 200 + MATCH_LENGTH + 5, MATCH_WIDTH, MATCH_LENGTH),

    pygame.Rect(220, 240, MATCH_LENGTH, MATCH_WIDTH),  
    pygame.Rect(250, 200, MATCH_WIDTH, MATCH_LENGTH),  

    pygame.Rect(350, 200, MATCH_LENGTH, MATCH_WIDTH),  
    pygame.Rect(410, 200, MATCH_WIDTH, MATCH_LENGTH),  
    pygame.Rect(350, 260, MATCH_LENGTH, MATCH_WIDTH),  
    pygame.Rect(350, 320, MATCH_LENGTH, MATCH_WIDTH), 
    pygame.Rect(350, 260, MATCH_WIDTH, MATCH_LENGTH),  

    pygame.Rect(470, 260, MATCH_LENGTH, MATCH_WIDTH),


    pygame.Rect(550, 200, MATCH_LENGTH, MATCH_WIDTH),  
    pygame.Rect(610, 200, MATCH_WIDTH, MATCH_LENGTH),  
    pygame.Rect(550, 260, MATCH_LENGTH, MATCH_WIDTH),  
    pygame.Rect(610, 260, MATCH_WIDTH, MATCH_LENGTH),  
    pygame.Rect(550, 320, MATCH_LENGTH, MATCH_WIDTH),  

    pygame.Rect(690, 240, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(690, 300, MATCH_LENGTH, MATCH_WIDTH),


    pygame.Rect(800, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(800, 200 + MATCH_LENGTH + 5, MATCH_WIDTH, MATCH_LENGTH),

    pygame.Rect(880, 200, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(880, 260, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(940, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(880, 320, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(880, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(940, 260, MATCH_WIDTH, MATCH_LENGTH),

    pygame.Rect(980, 200, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(980, 260, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(1040, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(980, 320, MATCH_LENGTH, MATCH_WIDTH),
    pygame.Rect(980, 200, MATCH_WIDTH, MATCH_LENGTH),
    pygame.Rect(1040, 260, MATCH_WIDTH, MATCH_LENGTH),
]

TARGET_X = 220  
TARGET_Y = 200  

attempts = 3
message = "Move one matchstick to make it correct!"
selected_match = None
game_over_time = None


def draw_screen():
    screen.fill(BLACK)
    for match in matchsticks:
        pygame.draw.rect(screen, YELLOW, match, border_radius=5)
    message_text = FONT.render(message, True, RED if message == "Game Over!" else GREEN if message == "You Win!" else WHITE)
    screen.blit(message_text, (50, 50))
    pygame.display.flip()


def handle_matchstick_selection(pos):
    global selected_match
    for i, match in enumerate(matchsticks):
        if match.collidepoint(pos):
            selected_match = i
            return
    selected_match = None

def move_matchstick(pos):
    global selected_match
    if selected_match is not None:
        matchsticks[selected_match].x = pos[0] - MATCH_WIDTH // 2
        matchsticks[selected_match].y = pos[1] - MATCH_WIDTH // 2

def check_win():
    global message
    target_rect = pygame.Rect(TARGET_X, TARGET_Y, MATCH_WIDTH, MATCH_LENGTH)
    left_match_of_9 = matchsticks[23]  
    
    if left_match_of_9.colliderect(target_rect):
        message = "You Win!"
        return True
    return False


def matchstick():
    global attempts, game_over_time, message, selected_match, WIDTH, HEIGHT, screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # تغییر اندازه صفحه
    pygame.display.set_caption("Matchstick Puzzle")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_matchstick_selection(event.pos)
            elif event.type == pygame.MOUSEMOTION and selected_match is not None:
                move_matchstick(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP and selected_match is not None:
                selected_match = None
                attempts -= 1
                if check_win():
                    message = "You Win!"
                    game_over_time = time.time()
                    draw_screen()
                    pygame.time.delay(1000)
                    clock.tick(FPS)
                    return 60, True
                elif attempts == 0:
                    message = "Game Over!"
                    game_over_time = time.time()
                    draw_screen()
                    clock.tick(FPS)
                    return -10, False

        if game_over_time and time.time() - game_over_time > 5:
            pygame.quit()
            sys.exit()

        draw_screen()
        clock.tick(FPS)

