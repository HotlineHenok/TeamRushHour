import boardClass
import carClass

board = boardClass.Board(6, 6)
redCar = carClass.Car('A', 1, 1, 2, 'H')
LightBlueCar = carClass.Car('B', 3, 0, 2, 'V')
OrangeCar = carClass.Car('C', 4, 3, 2, 'H')

cars = []
board.addCar(redCar)
board.addCar(OrangeCar)

board.printBoard()
print (' ')

board.possibleMoves()
