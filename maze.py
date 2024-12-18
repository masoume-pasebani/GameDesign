import pygame
import sys
import time

status = False
def draw_maze(screen, color):
    pygame.draw.rect(screen, color, (50, 50, 500, 500), 10) 
    
    walls = [
        ((50, 150), (400, 150)),
        ((200, 250), (550, 250)),
        ((50, 350), (400, 350)),
        ((200, 450), (550, 450)),

        ((150, 50), (150, 400)),
        ((250, 200), (250, 550)),
        ((350, 50), (350, 400)),
        ((450, 200), (450, 550)),
    ]

    for wall in walls:
        pygame.draw.line(screen, color, wall[0], wall[1], 10)  

    
    pygame.draw.line(screen, (255, 255, 255), (50, 105), (50, 125), 10)  
    pygame.draw.line(screen, (255, 255, 255), (550, 475), (550, 495), 10)  

def maze():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Maze Challenge")
    clock = pygame.time.Clock()

    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0) 


    start_point = (50, 115)
    end_point = (550, 485)
    
    drawing = False
    path = []
    game_won = False
    show_hit_message = False
    hit_time = 0  

    def reset_game():
        nonlocal path, drawing, game_won, show_hit_message, hit_time
        path = []
        drawing = False
        game_won = False
        show_hit_message = False
        hit_time = 0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if not drawing and abs(event.pos[0] - start_point[0]) <= 10 and abs(event.pos[1] - start_point[1]) <= 10:
                        drawing = True
                        path = [event.pos]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    
                    if abs(path[-1][0] - end_point[0]) <= 10 and abs(path[-1][1] - end_point[1]) <= 10:
                        game_won = True
                        pygame.time.set_timer(pygame.USEREVENT, 5000)  
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    path.append(event.pos)

                    
                    if 50 <= event.pos[0] <= 550 and 50 <= event.pos[1] <= 550:
                        
                        if screen.get_at(event.pos)[:3] == ORANGE:
                            print("Hit the wall! Start over.")
                            show_hit_message = True
                            hit_time = pygame.time.get_ticks()  
                            reset_game()

    
        screen.fill(BLACK)  
        draw_maze(screen, ORANGE)  
        pygame.draw.circle(screen, GREEN, start_point, 14)  
        pygame.draw.circle(screen, RED, end_point, 14) 

    
        if len(path) > 1:
            pygame.draw.lines(screen, RED, False, path, 3)

    
        if game_won:
            font = pygame.font.Font(None, 74)
            text = font.render("You win!", True, GREEN)
            screen.blit(text, (200, 250))
            pygame.time.wait(3000)
            return 60, True


    
        if show_hit_message and pygame.time.get_ticks() - hit_time < 1000: 
            font = pygame.font.Font(None, 50)
            text = font.render("Hit the wall!", True, RED)
            screen.blit(text, (150, 250))
            pygame.time.wait(1000)
        pygame.display.flip()
