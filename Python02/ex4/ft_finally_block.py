class PlantError(Exception):
	pass

def test_watering_system1():
	print("Opening watering system")
	try:
		water_plant("Tomato")
		water_plant("Lettuce")
		water_plant("Carrots")
	except PlantError as error:
		print(f"Caught PlantError: {error}")
		print("... ending test and returning to main")
	finally:
		print("Closing watering system")

def test_watering_system2():
	print("Opening watering system")
	try:
		water_plant("Tomato")
		water_plant("lettuce")
		water_plant("Carrots")
	except PlantError as error:
		print(f"Caught PlantError: {error}")
		print("... ending test and returning to main")
	finally:
		print("Closing watering system")

def water_plant(plant_name):
	if plant_name[0].isupper():
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def main():
	print("=== Garden Watering System ===")
	print("")
	print("Testing valid plants...")	
	test_watering_system1()
	print("")
	print("Test invalid plants...")
	test_watering_system2()
	print("")
	print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    main()