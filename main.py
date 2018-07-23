from __future__ import print_function

### GRID ### 
# SQUARE 0 | SQUARE 1 | SQUARE 2
# SQUARE 3 | SQUARE 4 | SQUARE 5
# SQUARE 6 | SQUARE 7 | SQUARE 8

### SQUARE N ###
# X0 X1 X2
# X3 X4 X5
# X6 X7 X8

import time
import sudokusolver as ss
import dictsudoku as ds

print("\n")
print("WELCOME TO SUDOKU SOLVER!")
print("PLEASE, ENTER THE OPTION DESIRED: EASY, MEDIUM, HARD OR EXPERT => ",end="")
level = raw_input()
while(not(level.upper()=="EASY" or level.upper()=="MEDIUM" or level.upper()=="HARD" or level.upper()=="EXPERT")):
	print("Invalid option, try again => ",end="")
	level = raw_input()
print("\n\n")
grid = ds.get_grid(level)
if len(grid)>0:
	print("INPUT GRID: ")
	ss.print_grid(grid)
	print("\n")
	print("GET SOLUTION? (Y)/N) => ",end="")
	solve = raw_input()
	while(solve.upper()=="N"):
		print("WAITING.... (Y)/N => ",end="")
		solve = raw_input()
	print("\n\n")
	print("OUTPUT GRID: ")
	start = time.time()
	result = ss.solve_sudoku(grid)
	ss.print_grid(result)
	end = time.time()
	print("\n")
	print("Elapsed time: "+str(end-start)+"s")
	print("\n")