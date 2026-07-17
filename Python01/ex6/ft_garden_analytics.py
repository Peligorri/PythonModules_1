class Plant:
	def __init__(self, name, height, age):
		self._age = 0
		self._height = 0
		self._name = name
		self.set_height(height)
		self.set_age(age)
		self._statistics = Plant.Statistics()
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
		self._statistics.grow_calls()
	def age(self, days):
		self.set_age(self.get_age() + days)
		self._statistics.age_calls()
	def show(self):
		print(f"{self._name}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")
		self._statistics.show_calls()
	@staticmethod
	def check(days):
		if(days <= 365):
			print(f"Is {days} days more than a year? -> False")
		elif(days > 365):
			print(f"Is {days} days more than a year? -> True")
	@classmethod
	def anonymous(cls, name=None, height=0, age=0):
		if name is None:
			name = "Unknown plant"
		return cls(name, height, age)
	class Statistics:
		def __init__(self):
			self._grow_calls = 0
			self._age_calls = 0
			self._show_calls = 0
			self._shade_calls = 0
		def grow_calls(self):
			self._grow_calls = self._grow_calls + 1
		def age_calls(self):
			self._age_calls = self._age_calls + 1
		def show_calls(self):
			self._show_calls =self._show_calls + 1
		def shade_calls(self):
			self._shade_calls =self._shade_calls + 1

def show_statistics(plant):
	print(f"Stats: {plant._statistics._grow_calls} grow, {plant._statistics._age_calls} age, {plant._statistics._show_calls} show")
	if isinstance(plant, Tree):
		print(f"{plant._statistics._shade_calls} shade")

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

class Seed(Flower):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age, color)
		self._seeds = 0
	def set_seeds(self):
		if(self._bloom == False):
			self._seeds = 0
		elif(self._bloom == True):
			self._seeds = self._seeds + 42
	def bloom(self):
		super().bloom()
		self.set_seeds()
	def show(self):
		super().show()
		print(f"Seed: {self._seeds}")

class Tree(Plant):
	def __init__(self, name, height, age, diameter):
		super().__init__(name, height, age)
		self._trunk_diameter = diameter
	def produce_shade(self):
		print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")
		self._statistics.shade_calls()
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
	print("=== Garden statistics ===")
	print("=== Check year-old")
	Plant.check(30)
	Plant.check(400)
	print("")
	print("=== Flower")
	rose = Flower("Rose", 15, 10, "red")
	rose.show()
	show_statistics(rose)
	rose.grow(1)
	rose.bloom()
	rose.show()
	show_statistics(rose)
	print("")
	print("=== Tree")
	oak = Tree("Oak", 200, 365, 5)
	oak.show()
	show_statistics(oak)
	oak.produce_shade()
	show_statistics(oak)
	print("")
	print("=== Seed")
	sunflower = Seed("Sunflower", 80, 45, "yellow")
	sunflower.show()
	sunflower.grow(20)
	sunflower.age(20)
	sunflower.bloom()
	sunflower.show()
	show_statistics(sunflower)
	print("")
	print("=== Anonymous")
	plant = Plant.anonymous()
	plant.show()
	show_statistics(plant)

if __name__ == "__main__":
    main()