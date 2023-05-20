import numpy as np

grid = [[0,0,0,0,0,0,0,0,0], # the zeros are blank spaces
        [0,0,0,0,0,0,0,0,0], # you can change the numbers based the format of sodoku
        [0,0,0,0,8,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,6,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

def possible(row, column, number):
    global grid #turns the variable 'grid' from a local to a global variable
    for i in range(0, 9):# for 8 times 
        if grid[row][i] == number:#check if the grid's row match the number in the grid
            return False # if it does, return False
    for i in range(0, 9):# for 8 times
        if grid[i][column] == number:#check if the grid's colmun match the number in the grid
            return False# if it does, return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid [row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
        
    print(np.matrix(grid))
    input('More possible solutions')

solve()
