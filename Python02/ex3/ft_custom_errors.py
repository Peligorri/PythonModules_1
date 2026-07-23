class GardenError(Exception):
	def __init__(self, message="Unkwon garden error"):
		super().__init__(message)
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def try_errors(error_num):
	if error_num == 1:
		try:
			try_errors(2)
		except GardenError as error:
			print(f"Caught GardenError: {error}")
		try:
			try_errors(3)
		except GardenError as error:
			print(f"Caught GardenError: {error}")
	elif error_num == 2:
		raise PlantError("The tomato plant is wilting!")
	elif error_num == 3:
		raise WaterError("Not enough water in the tank!")
	else:
		raise GardenError()

def garden_operations(error):
	try:
		try_errors(error)
	except PlantError as error:
		print(f"Caught PlantError: {error}")
	except WaterError as error:
		print(f"Caught WaterError: {error}")
	except GardenError as error:
		print(f"Caught GardenError: {error}")
	print("")

def main():
	print("=== Custom Garden Errors Demo ===")
	print("")
	print("Testing PlantError...")
	garden_operations(2)
	print("Testing WaterError...")
	garden_operations(3)
	print("Testing catching all garden errors...")
	garden_operations(1)
	print("All custom error types work correctly!")

	

if __name__ == "__main__":
    main()