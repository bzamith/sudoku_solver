### GRID ### 
# SQUARE 0 | SQUARE 1 | SQUARE 2
# SQUARE 3 | SQUARE 4 | SQUARE 5
# SQUARE 6 | SQUARE 7 | SQUARE 8

### SQUARE N ###
# X0 X1 X2
# X3 X4 X5
# X6 X7 X8


import sudokusolver as ss

grid = [[4,2,7,0,0,5,6,0,3],[1,0,0,0,0,6,0,0,0],[0,6,8,3,0,0,1,0,0],[2,0,0,3,4,0,8,0,1],[0,1,0,0,6,7,0,5,0],[4,0,0,0,5,1,0,2,0],[0,9,0,7,0,4,0,3,2],[0,0,0,3,0,0,0,9,4],[7,3,0,2,0,9,6,0,0]]
result = ss.solve_sudoku(grid)
print(result)