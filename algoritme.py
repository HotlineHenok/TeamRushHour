import boardClass
import carClass
import random

board = boardClass.Board(6, 6)
redCar = carClass.Car('A', 3, 2, 2, 'H')
LightBlueCar = carClass.Car('B', 3, 0, 2, 'H')
OrangeCar = carClass.Car('C', 4, 3, 2, 'H')
BlueCar = carClass.Car('D', 4, 5, 2, 'H')
LightBlueCar2 = carClass.Car('E', 1, 4, 2, 'H')
OrangeCar2 = carClass.Car('F', 0, 4, 2, 'V')
Purplebus = carClass.Car('G', 2, 0, 3, 'V')
Yellowbus = carClass.Car('H', 5, 0, 3, 'V')
Orangebus = carClass.Car('I', 3, 3, 3, 'V')

board.addCar(redCar)
board.addCar(LightBlueCar)
board.addCar(LightBlueCar2)
board.addCar(OrangeCar)
board.addCar(OrangeCar2)
board.addCar(Orangebus)
board.addCar(BlueCar)
board.addCar(Purplebus)
board.addCar(Yellowbus)

print(board.cars)

print(' ')
board.printBoard()



						