from copy import deepcopy
from collections import defaultdict
from pygame.locals import *
import os.path as path
import numpy as np
import pygame
import sys


def reset_game():
    global grid
    grid = deepcopy(def_grid)
    return grid


def take_action(action):
    global grid, turn
    grid, success = mark_cell(grid, turn, action+1)
    reward = 0
    winner = None
    if not success:
        reward -= 10
    else:
        winner = check_for_win(grid)
        if not winner and not (0 in grid[0] or 0 in grid[1] or 0 in grid[2]):
            reward -= 5
            winner = "Draw"
        elif winner:
            reward += 10
        turn = 1 if turn == -1 else -1
    return grid, turn, winner, reward


def mark_cell(grid, shape, pos):
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
        for j in range(0+i, 7+i, 3):
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


def show_game(grid, msgs=["Use numpads to play"]):
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

    for i in range(len(msgs)):
        text2 = font2.render(msgs[i] , 1, (0, 0, 0))
        screen.blit(text2, (20, 300 + (i+1) * 20))

    pygame.display.update()
    # Legacy
    # print("-"*13)
    # for i in range(3):
    #     print("|", end=" ")
    #     for j in range(3):
    #         print(s[grid[i][j]], end=" | ")
    #     print()
    #     print("-"*13)


def input_read():
    global run, player
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
                show_game(grid, ["Invalid Key"])


def player_turn():
    global grid, success, player
    while not (player in range(1, 10)):
        input_read()
    grid, success = mark_cell(grid, turn, player)
    if not success:
        player = 0
        show_game(grid, ["Cell Marked"])
    while not success:
        player_turn()


def ai_turn():
    global grid, success, player
    player = np.argmax(Q[str(grid)]) + 1
    grid, success = mark_cell(grid, turn, player)
    if not success:
        player = 0
    while not success:
        player += 1
        grid, success = mark_cell(grid, turn, player)


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
def_grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
grid = deepcopy(def_grid)
turn = 1

if __name__ == '__main__':
    # Pygame components
    pygame.font.init()
    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("TIC TAC TOE With AI")
    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)
    dif = 100

    # Base components
    run = True
    mode = 0

    # Choose play mode
    show_game(grid, ["Choose mode:", "1 : Normal", "2 : AI"])
    while not mode:
        for event in pygame.event.get():
            if event.type == QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_KP1:
                    mode = 1
                elif event.key == K_KP2:
                    fileName = "q1.npy"
                    pathToFile = "Q_Tables/"+fileName
                    if path.exists(pathToFile):
                        Q = defaultdict(lambda:np.zeros(9), np.load(pathToFile, allow_pickle=True).item())
                        print("Q-Table loaded")
                        mode = 2
                    else:
                        show_game(grid, ["No AI available"])

    # Game loop
    while run:
        show_game(grid)
        player = 0
        if mode == 1:
            player_turn()
        elif mode == 2:
            if turn == 1:
                player_turn()
            else:
                ai_turn()

        match_end = False
        winner = check_for_win(grid)
        if winner != None:
            show_game(grid, [("X" if winner == 1 else "O") + " is the winner!"])
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