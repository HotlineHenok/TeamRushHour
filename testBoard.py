import boardClass
import carClass

board = boardClass.Board(6, 6)
redCar = carClass.Car('A', 1, 2, 2, 'H')
LightBlueCar = carClass.Car('B', 3, 0, 2, 'V')
OrangeCar = carClass.Car('C', 4, 3, 2, 'H')


cars = []
cars.append(redCar)
cars.append(LightBlueCar)
cars.append(OrangeCar)

board.addCar(redCar)
board.addCar(LightBlueCar)
board.addCar(OrangeCar)

board.printBoard()
print (' ')

board.possibleMoves()