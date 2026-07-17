class Plant:
	def __init__(self, name, height, age):
		self._age = 0
		self._height = 0
		self._name = name
		self.set_height(height)
		self.set_age(age)
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
	def grow(self, days):
		self.set_height(self.get_height() + (0.8 * days))
	def age(self, days):
		self.set_age(self.get_age() + days)
	def show(self):
		print(f"Created: {self._name}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self._color = color
		self._bloom = False
	def get_bloom(self):
		if(self._bloom == False):
			print(f"{self._name} has not bloomed yet")
		else:
			print(f"{self._name} is blooming beautifully!")
	def bloom(self):
		if(self._bloom == False):
			self._bloom = True
	def show(self):
		super().show()
		print(f"Color: {self._color}")
		self.get_bloom()

class Tree(Plant):
	def __init__(self, name, height, age, diameter):
		super().__init__(name, height, age)
		self._trunk_diameter = diameter
	def produce_shade(self):
		print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")
	def show(self):
		super().show()
		print(f"Trunk diameter: {self._trunk_diameter}cm")

class Vegetable(Plant):
	def __init__(self, name, height, age, harvest_season):
		super().__init__(name, height, age)
		self._harvest_season = harvest_season
		self._nutritional_value = 0
	def show(self):
		super().show()
		print(f"Nutritional value: {self._nutritional_value}, harvest season: {self._harvest_season}")
	def grow(self, days):
		super().grow(days)
		super().age(days)
		self._nutritional_value = self._nutritional_value + (1.5 * days)

def main():
	print("=== Garden Plant Types")
	print("=== Flower")
	rose = Flower("Rose", 15, 10, "red")
	rose.show()
	rose.bloom()
	rose.show()
	print("")
	print("=== Tree")
	oak = Tree("Oak", 200, 365, 5.0)
	oak.show()
	oak.produce_shade()
	print("")
	print("=== Vegetable")
	tomato = Vegetable("Tomato", 5, 10, "April")
	tomato.show()
	tomato.grow(20)
	tomato.show()

if __name__ == "__main__":
    main()