import boardClass
import carClass
import random
import sys
import queueClass
import copy

board = boardClass.Board(6, 6)
redCar = carClass.Car('A', 1, 1, 2, 'H')
LightBlueCar = carClass.Car('B', 3, 0, 2, 'V')
OrangeCar = carClass.Car('C', 4, 3, 2, 'H')

board.addCar(redCar)
board.printBoard()


queue = queueClass.Queue()
oldStates = [board]
queue.enqueue(board)
nextStates = []
while queue.isEmpty() != True:
	while board.grid[4][2] != 'A':	
		boardNow = queue.dequeue()		
		moves = boardNow.possibleMoves()
		for elem in moves:
			boardCopy = copy.deepcopy(boardNow)			
			if elem[1] == 'LEFT':	
				boardCopy.moveCarLeft(elem[0])
				if boardCopy not in oldStates:
					nextStates.append(boardCopy)
					queue.enqueue(boardCopy)
				if boardCopy.checkFinish(boardCopy, redCar) == True:
					sys.exit(0)
				boardCopy.moveCarRight(elem[0])
			elif elem[1] == 'RIGHT':
				boardCopy.moveCarRight(elem[0])
				if boardCopy not in oldStates:
					nextStates.append(boardCopy)
					queue.enqueue(boardCopy)
					boardCopy.printBoard()
				if boardCopy.checkFinish(boardCopy, redCar) == True:
					sys.exit(0)
				boardCopy.moveCarLeft(elem[0])
			elif elem[1] == 'UP':
				boardCopy.moveCarUp(elem[0])	
				if boardCopy not in oldStates:
					nextStates.append(boardCopy)
					queue.enqueue(boardCopy)
					boardCopy.printBoard()
				if boardCopy.checkFinish(boardCopy, redCar) == True:
					sys.exit(0)
				boardCopy.moveCarDown(elem[0])
			elif elem[1] == 'DOWN':
				boardCopy.moveCarDown(elem[0])
				if boardCopy not in oldStates:
					nextStates.append(boardCopy)
					queue.enqueue(boardCopy)
					boardCopy.printBoard()
				if boardCopy.checkFinish(boardCopy, redCar) == True:
					sys.exit(0)
				boardCopy.moveCarUp(elem[0])
		oldStates = nextStates
print(queue.size())

