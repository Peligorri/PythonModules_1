class Plant:
	def __init__(self, name, height, age):
		self._age = 0
		self._height = 0
		self._name = name
		self.set_height(height)
		self.set_age(age)
		self.show()
	def set_height(self, height):
		if (height >= 0):
			self._height = height
		else:
			print()
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")
			print()
	def set_age(self, age):
		if (age >= 0):
			self._age = age
		else:
			print()
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")
			print()
	def get_height(self):
		return self._height
	def get_age(self):
		return self._age
	def grow(self):
		self.set_height(self.get_height() + 0.8)
	def show(self):
		print(f"Created: {self._name}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")

class Flower(Plant):
	super().__init__(name, height, age)
	self._color = color
	def bloom(self):
		print(f"{self._name} is blooming beautifully!")

class Tree(Plant):
	super().__init__(name, height, age)
	self._trunk_diameter = diameter
	def produce_shade(self):
		print(f"{self._name} is producing shade")

class Vegetable(Plant):
	super().__init__(name, height, age)
	self._harvest_season = harvest_season
	self._nutritional_value = 0

def main():

if __name__ == "__main__":
    main()