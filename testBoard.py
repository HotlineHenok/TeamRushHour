import boardClass
import carClass
import random

board = boardClass.Board(6, 6)
redCar = carClass.Car('A', 1, 1, 2, 'H')
LightBlueCar = carClass.Car('B', 3, 0, 2, 'V')
OrangeCar = carClass.Car('C', 4, 3, 2, 'H')

board.addCar(redCar)
board.addCar(OrangeCar)
board.addCar(LightBlueCar)

board.printBoard()

while board.grid[4][2] != 'A':
	moves = board.possibleMoves()
	for car in moves:
		for LEFT in (moves):
			board.moveCarLeft(car)
		for RIGHT in random.choice(moves):
			board.moveCarRight(car)
		for UP in random.choice(moves):
			board.moveCarUp(car)
		for DOWN in random.choice(moves):
			board.moveCarDown(car)
		board.printBoard()