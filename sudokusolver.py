from __future__ import print_function

import copy
import sys

global size_grids, number_grids, all_options, row_index, column_index 
size_grids = 3 #3x3
number_grids = 9 #9 grids
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
def column(board,index):
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
			output.append(board[val+(i*size_grids)][mod+(j*size_grids)])
	return(output)

#Returns a list of values from row #index
def row(board,index):
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
			output.append(board[(val*size_grids)+i][(mod*size_grids)+j])
	return(output)

#Returns the corresponding position from board i element j
#Example = board[3][7] corresponds to row 5 column 1
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

#Get Row Neighbors
def get_row_neighbors(board,i,j):
	position = pos(i,j)
	ret = copy.deepcopy(row(board,position[row_index]))
	del ret[position[column_index]]
	return(ret)

#Get Column Neighbors
def get_column_neighbors(board,i,j):
	position = pos(i,j)
	ret = copy.deepcopy(column(board,position[column_index]))
	del ret[position[row_index]]
	return(ret)

#Get board Neighbors
def get_board_neighbors(board,i,j):
	ret =copy.deepcopy(board[i])
	del ret[j]
	return(ret)

#Get Neighbors
def get_neighbors(board,i,j):
	ret = [get_row_neighbors(board,i,j),get_column_neighbors(board,i,j),get_board_neighbors(board,i,j)]
	ret = flatten(ret)
	return ret

#Returns the number of missing values (equal to 0)
def missing(board):
	count = 0
	for i in range(0,number_grids):
		count += board[i].count(0)
	return(count)

#Returns if is a fixed value or list of options
def is_options(board,i,j):
	if type(board[i,j])!=int:
		return True
	else:
		return False

#Returns a list of possible values 
def fullfill(board):
	fill = copy.deepcopy(board)
	for i in range(0,number_grids):
		while(fill[i].count(0)>0):
			index = fill[i].index(0)
			position = pos(i,index) 
			result = all_options - set(get_neighbors(board,i,index))
			fill[i][index] = list(result)
		#if unique option
		for j in range(0,number_grids):
			element = fill[i][j]
			if type(element) != int: #so it is a list of options
				if len(element)==1:
					board[i][j] = list(element)[0]
					fill[i][j] = list(element)[0]
		#otherwise
		for j in range(0,number_grids):
			element = fill[i][j]
			if type(element) != int: #so it is a list of options
				result = set(element) - set(get_board_neighbors(board,i,j))
				if len(result) == 1:
					board[i][j] = list(result)[0]
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
						board[i][j] = subelement				
	return(board)


#Solve the Sudoku
def solve_sudoku(board,iter):
	try: 
		if len(board)<size_grids or len(board[0])<size_grids:
			raise NameError('Invalid Size of board')
	except NameError: 
		print("Invalid Size of board ("+str(size_grids)+")")
		raise
	previous = missing(board)
	it = 0
	while(previous>0):
		fullfill(board)
		if iter:
			print("\nIt "+str(it)+":")
			print_board(board)
			print("\n\n")
		it += 1
		try:
			if previous == missing(board):
				raise NameError('board not Solvable')
		except NameError: 
			print("It is not possible to solve such Sudoku board")
			raise
		previous = missing(board)
	return(board,it)

#Print board
def print_board(board):
	try: 
		if len(board)<size_grids or len(board[0])<size_grids:
			raise NameError('Invalid Size of board')
	except NameError: 
		print("Invalid Size of board ("+str(size_grids)+")")
		raise
	line = "-"*((number_grids*2)+((size_grids-1)*2))
	for i in range(0,number_grids):
		if i%size_grids==0:
			print(line+"\n",end="")
		curr_row = row(board,i)
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

