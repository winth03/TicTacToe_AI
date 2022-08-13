from copy import deepcopy
import re
from pygame.locals import *
import pygame
import sys

def marK_KPcell(grid, shape, pos):
    # Shape -> -1:Circle 0:Empty 1:X
    # Pos -> 1-9 left to right, bottom to top
    i, j = pos_index[pos]
    if grid[i][j] == 0:
        grid[i][j] = shape
    else:
        return grid, False

    return grid, True


def check_for_win(grid):
    n = []
    for i in grid:
        for j in i:
            n.append(j)

    res = 0
    # Horizontal
    for i in grid:
        if sum(i) == 3 or sum(i) == -3:
            return i[0]
    # Vertical
    for i in range(3):
        for j in range(0, 7, 3):
            res += n[j]
        if res == 3 or res == -3:
            return n[i]
        else:
            res = 0
    # Diagonal l-r
    for j in range(0, 9, 4):
        res += n[j]
    if res == 3 or res == -3:
        return n[0]
    else:
        res = 0
    # Diagonal r-l
    for j in range(2, 7, 2):
        res += n[j]
    if res == 3 or res == -3:
        return n[2]
    else:
        res = 0


def show_game(grid, msg=''):
    s = {
        -1 : "O",
        0 : "-",
        1 : "X"
    }
    screen.fill((255, 255, 255))

    for i in range (3):
        for j in range (3):

            if grid[i][j]!= 0:
 
                # Fill color in marked cell
                pygame.draw.rect(screen, (235, 235, 228), (j * dif, i * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(s[grid[i][j]], 1, (0, 0, 0))
                screen.blit(text1, (j * dif + 35, i * dif + 15))
    # Draw lines horizontally and vertically to form grid          
    for i in range(4):
        thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (300, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 300), thick)

    text2 = font1.render(msg, 1, (0, 0, 0))
    screen.blit(text2, (0, 320))

    pygame.display.update()
    # Legacy
    # print("-"*13)
    # for i in range(3):
    #     print("|", end=" ")
    #     for j in range(3):
    #         print(s[grid[i][j]], end=" | ")
    #     print()
    #     print("-"*13)


if __name__ == '__main__':
    # Pygame components
    pygame.font.init()
    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("TIC TAC TOE With AI")
    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)
    dif = 100

    # Base components
    def_grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    pos_index = {
        1 : (2, 0),
        2 : (2, 1),
        3 : (2, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (0, 0),
        8 : (0, 1),
        9 : (0, 2),
    }
    grid = deepcopy(def_grid)
    run = True
    turn = 1

    # Game loop
    while run:
        show_game(grid)
        player = 0
        # Check for keyboard input
        while not (player in range(1, 10)):
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_KP1:
                        player = 1
                    elif event.key == K_KP2:
                        player = 2
                    elif event.key == K_KP3:
                        player = 3
                    elif event.key == K_KP4:
                        player = 4
                    elif event.key == K_KP5:
                        player = 5
                    elif event.key == K_KP6:
                        player = 6
                    elif event.key == K_KP7:
                        player = 7
                    elif event.key == K_KP8:
                        player = 8
                    elif event.key == K_KP9:
                        player = 9
                    else:
                        show_game(grid, "Invalid Key")
        grid, success = marK_KPcell(grid, turn, player)
        if not success:
            player = 0
            show_game(grid, "Cell Marked")
        while not success:
            # Check for keyboard input
            while not (player in range(1, 10)):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_KP1:
                            player = 1
                        elif event.key == K_KP2:
                            player = 2
                        elif event.key == K_KP3:
                            player = 3
                        elif event.key == K_KP4:
                            player = 4
                        elif event.key == K_KP5:
                            player = 5
                        elif event.key == K_KP6:
                            player = 6
                        elif event.key == K_KP7:
                            player = 7
                        elif event.key == K_KP8:
                            player = 8
                        elif event.key == K_KP9:
                            player = 9
                        else:
                            show_game(grid, "Invalid Key")
            grid, success = marK_KPcell(grid, turn, player)
            if not success:
                player = 0
                show_game(grid, "Cell Marked")

        match_end = False
        winner = check_for_win(grid)
        if winner != None:
            show_game(grid, ("X" if winner == 1 else "O") + " is the winner!")
            # Wait for restart
            ready = False
            while not ready:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        ready = True
            match_end = True
        if not (0 in grid[0] or 0 in grid[1] or 0 in grid[2]):
            match_end = True
        
        # Check if the game ends
        if match_end:
            grid = deepcopy(def_grid)
            turn = 1
        else:
            turn = 1 if turn == -1 else -1
            
    print("Program End")
