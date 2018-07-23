from __future__ import print_function

import copy
import sys

global size_grids, number_grids, all_options, row_index, column_index 
size_grids = 3 #3x3
number_grids = 9 #9 subgrids
row_index = 0 #returned by pos()
column_index = 1 #returned by pos()
all_options = set([1,2,3,4,5,6,7,8,9])

#Returns flatten list
def flatten(lis):
	if(type(lis) == int):
		return(lis)
	else:
		ret = []
		for element in lis:
			if type(element) == int:
				ret.append(element)
			else:
				for i in range(0,len(element)):
					ret.append(element[i])
		return(ret)

#Returns a list of values from column #index
def column(grid,index):
	try:
		if index > (number_grids - 1) or index < 0:
			raise NameError('Invalid Position Index')
		if type(index)!=int:
			raise NameError('Not Integer Index')
	except NameError: 
		print("Invalid Column Access")
		raise
	val = int(index/size_grids)
	mod = int(index%size_grids)
	output = []
	for i in range(0,size_grids):
		for j in range(0,size_grids):
			output.append(grid[val+(i*size_grids)][mod+(j*size_grids)])
	return(output)

#Returns a list of values from row #index
def row(grid,index):
	try:
		if index > (number_grids - 1) or index < 0:
			raise NameError('Invalid Position Index')
		if type(index)!=int:
			raise NameError('Not Integer Index')
	except NameError: 
		print("Invalid Column Access")
		raise
	val = int(index/size_grids)
	mod = int(index%size_grids)
	output = []
	for i in range(0,size_grids):
		for j in range(0,size_grids):
			output.append(grid[(val*size_grids)+i][(mod*size_grids)+j])
	return(output)

#Returns the corresponding position from grid i element j
#Example = grid[3][7] corresponds to row 5 column 1
def pos(i,j):
	try:
		if i > (number_grids - 1) or j >(number_grids - 1) or i < 0 or j < 0:
			raise NameError('Invalid Position Index')
		if type(i)!=int or type(j)!=int:
			raise NameError('Not Integer Index')
	except NameError: 
		print("Invalid Position Access")
		raise
	val = int(i/size_grids)
	mod = int(i%size_grids)
	val2 = int(j/size_grids)
	mod2 = int(j%size_grids)
	row = val*size_grids + val2
	column = mod*size_grids + mod2
	return([row,column])

#Returns the number of missing values (equal to 0)
def missing(grid):
	count = 0
	for i in range(0,number_grids):
		count += grid[i].count(0)
	return(count)

#Returns a list of possible values 
def fullfill(grid):
	fill = copy.deepcopy(grid)
	for i in range(0,number_grids):
		while(fill[i].count(0)>0):
			index = fill[i].index(0)
			position = pos(i,index) 
			result = all_options - set(row(grid,position[row_index]))
			result = result - set(column(grid,position[column_index]))
			fill[i][index] = list(result)
		#if unique option
		for j in range(0,number_grids):
			element = fill[i][j]
			if type(element) != int: #so it is a list of options
				if len(element)==1:
					grid[i][j] = list(element)[0]
					fill[i][j] = list(element)[0]
		#otherwise
		for j in range(0,number_grids):
			element = fill[i][j]
			if type(element) != int: #so it is a list of options
				result = set(element) - set(grid[i])
				if len(result) == 1:
					grid[i][j] = list(result)[0]
					fill[i][j] = list(result)[0]
				else:
					fill[i][j] = list(result)
		#another try
		result = []
		for j in range(0,number_grids):
			result.append(flatten(fill[i][j]))
			result = flatten(result)
		for j in range(0,number_grids):
			element = fill[i][j]
			if type(element) != int:
				for subelement in element:
					if result.count(subelement)==1: #so it is a list of options
						fill[i][j] = subelement
						grid[i][j] = subelement				
	return(grid)

#Solve the Sudoku
def solve_sudoku(grid,iter):
	try: 
		if len(grid)<size_grids or len(grid[0])<size_grids:
			raise NameError('Invalid Size of Grid')
	except NameError: 
		print("Invalid Size of Grid ("+str(size_grids)+")")
		raise
	previous = missing(grid)
	it = 0
	while(previous>0):
		fullfill(grid)
		if iter:
			print("\nIt "+str(it)+":")
			print_grid(grid)
			print("\n\n")
		it += 1
		try:
			if previous == missing(grid):
				raise NameError('Grid not Solvable')
		except NameError: 
			print("It is not possible to solve such Sudoku Grid")
			raise
		previous = missing(grid)
	return(grid)

#Print grid
def print_grid(grid):
	try: 
		if len(grid)<size_grids or len(grid[0])<size_grids:
			raise NameError('Invalid Size of Grid')
	except NameError: 
		print("Invalid Size of Grid ("+str(size_grids)+")")
		raise
	line = "-"*((number_grids*2)+((size_grids-1)*2))
	for i in range(0,number_grids):
		if i%size_grids==0:
			print(line+"\n",end="")
		curr_row = row(grid,i)
		show = ""
		for j in range(0,size_grids):
			val = j*size_grids
			ret = curr_row[val:(val+size_grids)]
			for element in ret:
				print(str(element)+" ",end="")
			if j < size_grids - 1:
				print("| ",end="")
		print("")
	print(line+"\n",end="")
