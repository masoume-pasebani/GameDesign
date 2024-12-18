import pygame
import sys
from algo import main_algo
from matchstick_puzzel import matchstick
from maze import maze
from ship import ship_game
from hat import hat
from first import firstPuzzle
from dragon import dragon_game
from hat2 import hats_game


mapOfTheMaze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 8, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 5, 0, 1, 0, 0, 0, 1, 0, 0, 0, 5, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 6, 6, 6, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 6, 6, 6, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 5, 1, 1, 6, 6, 6, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 6, 6, 6, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 6, 6, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]


mapOfTheFog = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 8],
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]

]

entrancePoint = [11, 1]
exitPoint = [11, 22]
initialScore = 2000
bonus = 0
numOfEntrances = {}
fogMoves = 0
previousPlace = None
teleports = [(1, 15), (21, 5)]
portals = [(3, 9), (13, 15)]


pygame.init()
w = 500
h = 500


back = 204, 204, 255
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (135, 206, 235)
gray = (169, 169, 169)
purple = (128, 0, 128)
dark_green = (0, 100, 0)
puzzle = (56, 56, 56)
pink = (255, 105, 180)


screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Welcome to the maze")


def moving(direction):
    global entrancePoint, initialScore, fogMoves, previousPlace, puzzle
    x, y = entrancePoint
    done = False
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    if direction in moves:
        dx, dy = moves[direction]
        new_x, new_y = x + dx, y + dy
        num = numOfEntrances.get((new_x, new_y), 0)
        if mapOfTheMaze[new_x][new_y] != 0 and numOfEntrances.get((new_x, new_y), 0) < 3:
            if mapOfTheMaze[new_x][new_y] == 1:
                numOfEntrances[(new_x, new_y)] = numOfEntrances.get((new_x, new_y), 0) + 1
                entrancePoint = [new_x, new_y]

                if num == 0:
                    initialScore -= 10
                elif num == 1:
                    initialScore -= 20
                elif numOfEntrances[(new_x, new_y)] == 3:
                    initialScore -= 40

            if mapOfTheMaze[new_x][new_y] == 5:
                done = open_puzzle(new_x, new_y)
                previousPlace = entrancePoint

                if done:
                    entrancePoint = [new_x, new_y]
                else:
                    entrancePoint = previousPlace
                return

            if mapOfTheMaze[x][y] != 6:
                previousPlace = entrancePoint
                entrancePoint = [new_x, new_y]

            if mapOfTheMaze[new_x][new_y] == 6:

                if fogMoves < 3:
                    f = mapOfTheFog[new_x - 11][new_y - 13]
                    if f == 1:
                        fogMoves += 1
                        entrancePoint = [new_x, new_y]
                    elif f == 8:
                        fogMoves += 1
                        entrancePoint = [3, 9]

                else:
                    entrancePoint = previousPlace
                    initialScore -= 10
                    fogMoves = 0
                    print("Your moves are finished. only 3 moves in the fog!")
                    return

            if (new_x, new_y) in teleports:
                other_teleport = teleports[1] if (new_x, new_y) == teleports[0] else teleports[0]
                entrancePoint = list(other_teleport)
                print(f"You are transmitted to the other teleport")

            if (new_x, new_y) in portals:
                other_portal = portals[1] if (new_x, new_y) == portals[0] else portals[0]
                entrancePoint = list(other_portal)
                print(f"You are transmitted to the other portal!")



font_path = r"fonts\Fruit.ttf"
font = pygame.font.Font(font_path, 8)


def show_score():
    score_text = font.render(f"Score: {initialScore}", True, white)
    screen.blit(score_text, (w // 2 - score_text.get_width() // 2, h - 40))


def draw_maze():
    screen.fill(back)
    wall_img = pygame.image.load("images/wall.jpg")
    maze_width = len(mapOfTheMaze[0]) * 20
    maze_height = len(mapOfTheMaze) * 20
    offset_x = (w - maze_width) // 2
    offset_y = (h - maze_height) // 2
    for i, row in enumerate(mapOfTheMaze):
        for j, cell in enumerate(row):
            color = white if cell == 1 else black
            if (i, j) == tuple(entrancePoint):
                color = blue
            elif [i,j] == [11,22] or [i,j] == [11,1]:
                color = pink
            elif cell == 6:
                color = gray
            elif cell == 7:
                color = purple
            elif cell == 8:
                color = dark_green
            elif cell == 5:
                color = puzzle
            elif (i, j) in numOfEntrances:
                visits = numOfEntrances[(i, j)]
                if visits == 2:
                    color = yellow
                elif visits >= 3:
                    color = red
            pygame.draw.rect(screen, color, (j * 20 + offset_x, i * 20 + offset_y, 20, 20))
    show_score()


def open_puzzle(dx, dy):
    global initialScore, bonus, screen

    if dx == 8 and dy == 5:
        original_screen = pygame.display.get_surface()
        puzzle_score, winning = main_algo()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += puzzle_score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 4 and dy == 9:
        original_screen = pygame.display.get_surface()
        score, winning = firstPuzzle()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 8 and dy == 15:
        original_screen = pygame.display.get_surface()
        score, winning = ship_game()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 9 and dy == 12:
        original_screen = pygame.display.get_surface()
        score, winning = hat()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 10 and dy == 9:
        original_screen = pygame.display.get_surface()
        score, winning = dragon_game()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 13 and dy == 10:
        original_screen = pygame.display.get_surface()
        score, winning = hats_game()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 18 and dy == 7:
        original_screen = pygame.display.get_surface()
        score, winning = maze()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False

    elif dx == 19 and dy == 6:
        original_screen = pygame.display.get_surface()
        score, winning = matchstick()
        screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Welcome to the maze")
        initialScore += score
        if initialScore > 2000:
            bonus += (initialScore - 2000)
            initialScore = 2000
        if winning:
            mapOfTheMaze[dx][dy] = 1
            return True
        else:
            mapOfTheMaze[dx][dy] = 5
            return False


def intro_page(scr, w, h):
    global font, font_path
    scr = pygame.display.set_mode((w, h))
    pygame.font.init()

    font_path = r"fonts\Fruit.ttf"
    title_font = pygame.font.Font(font_path, 30)
    text_font = pygame.font.Font(font_path, 20)
    countdown_font = pygame.font.Font(font_path, 10)

    bg_color = (8, 24, 168)
    text_color = (224, 224, 224)
    border_color = (0, 0, 0)
    line_color = (173, 216, 230)

    title_text = "Welcome to the Maze Game!"
    description_text = "Solve funny puzzles and finish the Maze!"

    clock = pygame.time.Clock()
    intro_duration = 5 * 1000
    start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        scr.fill(bg_color)

        title_surface = title_font.render(title_text, True, text_color)
        desc_surface = text_font.render(description_text, True, text_color)

        title_x = (w - title_surface.get_width()) // 2
        title_y = (h // 2) - 80
        desc_x = (w - desc_surface.get_width()) // 2
        desc_y = (h // 2) + 20

        border_padding = 10

        pygame.draw.line(scr, line_color, (0, 10), (w, 10), 5)
        pygame.draw.line(scr, line_color, (0, h - 10), (w, h - 10), 5)

        pygame.draw.rect(scr, border_color,
                         (title_x - border_padding, title_y - border_padding,
                          title_surface.get_width() + 2 * border_padding,
                          title_surface.get_height() + 2 * border_padding), 2)
        pygame.draw.rect(scr, border_color,
                         (desc_x - border_padding, desc_y - border_padding,
                          desc_surface.get_width() + 2 * border_padding,
                          desc_surface.get_height() + 2 * border_padding), 2)

        scr.blit(title_surface, (title_x, title_y))
        scr.blit(desc_surface, (desc_x, desc_y))

        elapsed_time = pygame.time.get_ticks() - start_time
        countdown_value = max(0, 5 - elapsed_time // 1000)

        countdown_surface = countdown_font.render(f"Be ready in: {countdown_value}", True, text_color)
        countdown_x = (w - countdown_surface.get_width()) // 2
        countdown_y = h - 50
        scr.blit(countdown_surface, (countdown_x, countdown_y))

        pygame.display.flip()

        if countdown_value <= 0:
            break

        clock.tick(60)





def show_end_screen(player_rank, final_score):
    def draw_gradient_background(surface, top_color, bottom_color):
        for y in range(h):
            blended_color = (
                top_color[0] + (bottom_color[0] - top_color[0]) * y // h,
                top_color[1] + (bottom_color[1] - top_color[1]) * y // h,
                top_color[2] + (bottom_color[2] - top_color[2]) * y // h,
            )
            pygame.draw.line(surface, blended_color, (0, y), (w, y))

    def draw_divider_lines(surface, line_color, thickness=5):
        pygame.draw.line(surface, line_color, (0, 20), (w, 20), thickness)
        pygame.draw.line(
            surface, line_color, (0, h - 20), (w, h - 20), thickness
        )

    pygame.font.init()
    font_path = r"fonts\Fruit.ttf"
    header_font = pygame.font.Font(font_path, 40)
    info_font = pygame.font.Font(font_path, 30)
    footer_font = pygame.font.Font(font_path, 20)

    if player_rank == "S":
        gradient_start, gradient_end = (252, 211, 77), (245, 93, 66)
    elif player_rank == "A":
        gradient_start, gradient_end = (180, 180, 255), (100, 149, 237)
    elif player_rank == "B":
        gradient_start, gradient_end = (255, 182, 77), (210, 105, 30)
    else:
        gradient_start, gradient_end = (85, 85, 85), (50, 50, 50)

    line_color = (200, 200, 200)

    title_text = header_font.render("Game Over!", True, (0, 0, 0))
    rank_text = info_font.render(f"Rank: {player_rank}", True, (0, 0, 0))
    score_text = info_font.render(f"Score: {final_score}", True, (0, 0, 0))
    thanks_text = footer_font.render("Thanks for playing!", True, (0, 0, 0))

    animation_offset = 0
    animation_direction = 1

    for frame in range(150):
        animation_offset += 0.5 * animation_direction
        if animation_offset > 20 or animation_offset < -20:
            animation_direction *= -1

        draw_gradient_background(screen, gradient_start, gradient_end)
        draw_divider_lines(screen, line_color)

        screen.blit(
            title_text,
            (w // 2 - title_text.get_width() // 2, h // 4 + animation_offset),
        )
        screen.blit(
            rank_text,
            (w // 2 - rank_text.get_width() // 2, h // 2 - 50 + animation_offset),
        )
        screen.blit(
            score_text, (w // 2 - score_text.get_width() // 2, h // 2 + 60)
        )
        screen.blit(
            thanks_text,
            (w // 2 - thanks_text.get_width() // 2, h - 80),
        )
        pygame.display.flip()
        pygame.time.delay(40)

    pygame.time.delay(2000)
    draw_gradient_background(screen, gradient_start, gradient_end)
    draw_divider_lines(screen, line_color)
    screen.blit(title_text, (w // 2 - title_text.get_width() // 2, h // 4))
    screen.blit(rank_text, (w // 2 - rank_text.get_width() // 2, h // 2 - 50))
    screen.blit(score_text, (w // 2 - score_text.get_width() // 2, h // 2 + 60))
    screen.blit(thanks_text, (w // 2 - thanks_text.get_width() // 2, h - 80))
    pygame.display.flip()
    pygame.time.delay(2000)



def main():
    global initialScore, bonus, screen, w, h, fogMoves

    fogMoves = 0
    players_rank = ""
    running = True
    intro_page(screen, w, h)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moving("up")
                elif event.key == pygame.K_DOWN:
                    moving("down")
                elif event.key == pygame.K_LEFT:
                    moving("left")
                elif event.key == pygame.K_RIGHT:
                    moving("right")

        draw_maze()
        pygame.display.flip()

        if entrancePoint == [11,21]:
            initialScore += 2000
            initialScore += bonus
            initialScore = min(initialScore, 4000)
            if initialScore >= 3750:
                players_rank = "S"
            elif 3650 <= initialScore <= 3749:
                players_rank = "A"
            elif 3400 <= initialScore <= 3649:
                players_rank = "B"
            elif 0 <= initialScore < 3400:
                players_rank = "C"

            print(players_rank)
            show_end_screen(players_rank, initialScore)

            running = False


if __name__ == "__main__":
    main()
