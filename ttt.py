def mark_cell(grid, shape, pos):
    # Shape -> -1:Circle 0:Empty 1:X
    # Pos -> 1-9 left to right, bottom to top
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
    i, j = pos_index[pos]
    grid[i][j] = shape

    return grid


def check_for_win(grid):
    n = []
    for i in grid:
        for j in i:
            n.append(j)

    sum = 0
    # Horizontal
    for i in range(len(n)):
        if (i+1) % 3 == 0:
            if sum == 3 or sum == -3:
                return n[i]
            sum = 0
        else:
            sum += n[i]
    # Vertical
    for i in range(3):
        for j in range(0, 7, 3):
            sum += n[j]
        if sum == 3 or sum == -3:
            return n[i]
        else:
            sum = 0
    # Diagonal l-r
    for j in range(0, 9, 4):
        sum += n[j]
    if sum == 3 or sum == -3:
        return n[0]
    else:
        sum = 0
    # Diagonal r-l
    for j in range(2, 7, 2):
        sum += n[j]
    if sum == 3 or sum == -3:
        return n[2]
    else:
        sum = 0


def show_game(grid):
    s = {
        -1 : "O",
        0 : "-",
        1 : "X"
    }
    print("-"*13)
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(s[grid[i][j]], end=" | ")
        print()
        print("-"*13)


def_grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
grid = def_grid.copy()
run = True
turn = 1
step = 1
while run:
    show_game(grid)
    player = int(input())
    grid = mark_cell(grid, turn, player)
    winner = check_for_win(grid)
    if winner != None:
        run = False
        show_game(grid)
        print("X" if winner == 1 else "O", "is the winner!")
    if step < 9:
        turn = 1 if turn == -1 else -1
        step += 1
    else:
        grid = def_grid.copy()
        step = 1
            

print("Program End")
