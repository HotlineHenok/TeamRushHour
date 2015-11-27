
class Board(object):
	
	def __init__(self, rows, columns):
		self.grid = []
		self.cars = []
		for row in range(rows):
			# Add an empty array that will hold each cell
			# in this row
			self.grid.append([])
			for column in range(columns):
				self.grid[row].append(0)  # Append a cell

	def addCar(self, car):
		self.grid[car.y][car.x] = car.id
		if car.orientation == 'H':
			self.grid[car.y][car.x + 1] = car.id
			if car.length == 3:
				self.grid[car.y][car.x + 2] = car.id
		if car.orientation == 'V':
			self.grid[car.y + 1][car.x] = car.id
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
					if car.x + car.length < self.rows | car.x - car.length >= 0:
						if self.grid[car.y][car.x - 1] == 0:
							moves.append((car, 'LEFT'))
						if self.grid[car.y][car.x + 2] == 0:
							moves.append((car, 'RIGHT'))
					else:
						return false	
				else:
					if car.x + car.length < self.rows | car.x - car.length >= 0:
						if self.grid[car.y][car.x - 1] == 0:
							moves.append((car, 'LEFT'))
						if self.grid[car.y][car.x + 3] == 0:
							moves.append((car, 'RIGHT'))
					else:
						return false		
			else:
				if car.length == 2:
					if car.y + car.length < self.columns | car.y - car.length >= 0:
						if self.grid[car.y - 1][car.x] == 0:
							moves.append((car, 'UP'))
						if self.grid[car.y + 2][car.x] == 0:
							moves.append((car, 'DOWN'))
					else:
						return false		
				else:
					if car.y + car.length < self.columns | car.y - car.length >= 0:
						if self.grid[car.y - 1][car.x] == 0:
							moves.append((car, 'UP'))
						if self.grid[car.y + 3][car.x] == 0:
							moves.append((car, 'DOWN'))
					else:
						return false			
		for elem in moves:
			print(elem)
		return moves
