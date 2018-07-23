import random

easy = {'grid0': [[4,2,7,0,0,5,6,0,3],[1,0,0,0,0,6,0,0,0],[0,6,8,3,0,0,1,0,0],[2,0,0,3,4,0,8,0,1],[0,1,0,0,6,7,0,5,0],[4,0,0,0,5,1,0,2,0],[0,9,0,7,0,4,0,3,2],[0,0,0,3,0,0,0,9,4],[7,3,0,2,0,9,6,0,0]],
'grid1': [[5,0,0,0,4,0,8,0,0],[6,7,0,8,0,0,5,0,0],[9,0,0,0,0,0,6,1,3],[0,6,2,1,0,0,3,7,4],[4,0,0,0,0,3,9,0,8],[0,7,0,0,2,0,0,0,0],[0,9,6,2,1,8,0,5,0],[1,0,7,0,0,6,0,8,0],[8,0,2,0,4,5,0,9,0]]}

medium = {'grid0':[[0,0,0,0,0,2,5,0,6],[4,0,0,0,0,0,9,0,0],[2,0,0,0,1,8,0,3,0],[0,6,9,0,5,0,8,0,0],[0,0,0,0,0,0,1,5,7],[3,0,0,0,2,1,6,0,9],[0,0,0,9,0,0,0,0,0],[0,3,0,6,0,2,0,0,0],[9,6,0,0,5,0,7,0,2]]}


def get_grid(level):
	try:
		if(level.upper()=='EASY'):
			return(easy[str("grid"+str(random.randint(0, (len(easy)-1))))]) 
		if(level.upper()=='MEDIUM'):
			return(medium[str("grid"+str(random.randint(0, (len(medium)-1))))]) 
		if(level.upper()=='MEDIUM'):
			raise NameError('Level '+level.upper()+' Not Implemented Yet')
		if(level.upper()=='HARD'):
			raise NameError('Level '+level.upper()+' Not Implemented Yet')
		if(level.upper()=='EXPERT'):
			raise NameError('Level '+level.upper()+' Not Implemented Yet')
		else:
			raise NameError('Unknown Level: '+level.upper())
	except NameError:
		print("No grid found")
		raise
	return('')