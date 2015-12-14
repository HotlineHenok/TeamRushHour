
class Board(object):
	
	def __init__(self, rows, columns):
		self.grid = []
		self.cars = []
		self.rows = rows
		self.columns = columns
		for row in range(rows):
			# Add an empty array that will hold each cell
			# in this row
			self.grid.append([])
			for column in range(columns):
				self.grid[row].append(0)  # Append a cell

	def addCar(self, car):
		self.grid[car.y][car.x] = car.id
		if car.orientation == 'H':
			if car.length == 2:
				self.grid[car.y][car.x + 1] = car.id
				self.cars.append(car)
			else:
				self.grid[car.y][car.x + 2] = car.id
				self.cars.append(car)
		if car.orientation == 'V':
			if car.length == 2:
				self.grid[car.y + 1][car.x] = car.id
				self.cars.append(car)
			if car.length == 3:
				self.grid[car.y + 2][car.x] = car.id
				self.cars.append(car)


	def moveCarUp(self, car):
		self.grid[car.y - 1][car.x] = car.id
		self.grid[car.y + 1][car.x] = 0
		if car.length == 3:
			self.grid[car.y + 1][car.x] = car.id
			self.grid[car.y + 2][car.x] = 0
		car.y = car.y - 1 

	def moveCarDown(self, car):
		self.grid[car.y + 2][car.x] = car.id
		self.grid[car.y][car.x] = 0
		if car.length == 3:
			self.grid[car.y + 3][car.x] = car.id
		car.y = car.y + 1	

	def moveCarLeft(self, car):
		self.grid[car.y][car.x - 1] = car.id
		self.grid[car.y][car.x + 1] = 0
		if car.length == 3:
			self.grid[car.y][car.x + 1] = car.id
			self.grid[car.y][car.x + 2] = 0
		car.x = car.x - 1

	def moveCarRight(self, car):
		self.grid[car.y][car.x + 2] = car.id
		self.grid[car.y][car.x] = 0
		if car.length == 3:
			self.grid[car.y][car.x + 3] = car.id
		car.x = car.x + 1

	def printBoard(self):
		for elem in self.grid:
			print(elem)

	def possibleMoves(self):
		moves = []
		for car in self.cars:
			if car.orientation == 'H':
				if car.length == 2:
					if car.x >= 0 | car.x <= 4: 
						if self.grid[car.y][car.x - 1] == 0:
							moves.append((car, 'LEFT'))
					if car.x >= 0 | car.x <= 3:
						if self.grid[car.y][car.x + 2] == 0:
							moves.append((car, 'RIGHT'))
				else:
					if car.x >= 0 | car.x <= 4:
						if self.grid[car.y][car.x - 1] == 0:
							moves.append((car, 'LEFT'))
					if car.x >= 0 | car.x <= 2:
						if self.grid[car.y][car.x + 3] == 0:
							moves.append((car, 'RIGHT'))
			if car.orientation == 'V':
				if car.length == 2:	
					if car.y > 0: 	
						if self.grid[car.y - 1][car.x] == 0:
							moves.append[(car, 'UP')]
					if car.y <= 3:	
						if self.grid[car.y + 3][car.x] == 0:
							moves.append((car, 'DOWN'))
				else:
					if car.y > 0:
						if self.grid[car.y - 1][car.x] == 0:
							moves.append((car, 'UP'))
					if car.y <=2:
						if self.grid[car.y + 3][car.x] == 0:
							moves.append((car, 'DOWN'))
		return moves

