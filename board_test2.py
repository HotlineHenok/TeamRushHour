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
    

