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
def main():
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 25, 30)
	rose.set_height(-2)
	rose.show()
	rose.grow()
	rose.grow()
	rose.show()
	oak = Plant("Oak", 200, 365)
	cactus = Plant("Cactus", 5, 90)
	sunflower = Plant("Sunflower", 80, 45)
	fern = Plant("Fern", 15, 120)
if __name__ == "__main__":
    main()