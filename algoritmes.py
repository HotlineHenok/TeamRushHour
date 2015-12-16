
BRUTE FORCE ALGORITHM
oldMoves = board.possibleMoves()
while board.grid[4][2] != 'A':
	for elem in oldMoves:
		if elem[1] == 'LEFT':
			board.moveCarLeft(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'RIGHT':
			board.moveCarRight(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'UP':
			board.moveCarUp(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'DOWN':
			board.moveCarDown(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
	newMoves = board.possibleMoves()
	oldMoves = newMoves


RANDOM ALGORITHM
oldMoves = board.possibleMoves()
while board.grid[4][2] != 'A':
	for elem in random.choice(oldMoves):
		if elem[1] == 'LEFT':
			board.moveCarLeft(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'RIGHT':
			board.moveCarRight(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'UP':
			board.moveCarUp(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
		elif elem[1] == 'DOWN':
			board.moveCarDown(elem[0])
			if checkFinish(boardNow, redCar) == True:
				sys.exit(0)
	newMoves = board.possibleMoves()
	oldMoves = newMoves



BREADTH FIRST ALGORITHM
oldStates = [board]
while board.grid[4][2] != 'A':
	nextStates = []
	for boardNow in oldStates:
		moves = boardNow.possibleMoves()
		for elem in moves:
			if elem[1] == 'LEFT':
				boardNow.moveCarLeft(elem[0])
				if boardNow.grid not in nextStates:
					nextStates.append(boardNow)
				if checkFinish(boardNow, redCar) == True:
					sys.exit(0)
				boardNow.moveCarRight(elem[0])
			elif elem[1] == 'RIGHT':
				boardNow.moveCarRight(elem[0])
				if boardNow.grid not in nextStates:
					nextStates.append(boardNow)
				if checkFinish(boardNow, redCar) == True:
					sys.exit(0)
				boardNow.moveCarLeft(elem[0])
			elif elem[1] == 'UP':
				boardNow.moveCarUp(elem[0])
				if boardNow.grid not in nextStates:
					nextStates.append(boardNow)
				if checkFinish(boardNow, redCar) == True:
					sys.exit(0)
					return oldStates
				boardNow.moveCarDown(elem[0])
			elif elem[1] == 'DOWN':
				boardNow.moveCarDown(elem[0])
				if boardNow.grid not in nextStates:
					nextStates.append(boardNow)
				if checkFinish(boardNow, redCar) == True:
					sys.exit(0)
				boardNow.moveCarUp(elem[0])
	oldStates = nextStates


