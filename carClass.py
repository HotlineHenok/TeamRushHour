# carId = {"a", "b", "c", "d", "e", "f", "g"}
# busId = {"q", "r", "s", "t"}
# if id in carId:
		# 	 self.length = 2
		# else:
		#	 self.length = 3

class Car(object):
	def __init__(self, id, x, y, length, orientation):
		self.id = id
		self.x = x
		self.y = y
		self.length = length
		self.orientation = orientation

	 
