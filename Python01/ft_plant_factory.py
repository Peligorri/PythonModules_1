class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	def grow(self):
		self.height = round((float(self.height) + 0.8), 1)
	def show(self):
		print(f"Created: {self.name}: {round(float(self.height), 1)}cm, {self.age} days old")
def main():
	print("=== Plant Factory Output ===")
	rose = Plant("Rose", 25, 30)
	oak = Plant("Oak", 200, 365)
	cactus = Plant("Cactus", 5, 90)
	sunflower = Plant("Sunflower", 80, 45)
	fern = Plant("Fern", 15, 120)
	rose.show()
	oak.show()
	cactus.show()
	sunflower.show()
	fern.show()
if __name__ == "__main__":
    main()
