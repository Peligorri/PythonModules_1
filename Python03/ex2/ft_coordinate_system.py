import math

def check_coordinates():
	coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")

	i = 0
	x = []
	y = []
	z = []
	rest = []
	while i < len(coordinates) and coordinates[i].isdigit() == False:
		i = i + 1;
	if i == len(coordinates):
		print(f"Invalid syntax")
		return check_coordinates()
	else:
		i = 0
	while i < len(coordinates):
		
		if(coordinates[i] == ' ' or coordinates[i] == ','):
			i = i + 1
		elif len(x) == 0:
			while i < len(coordinates) and coordinates[i] != ' ' and coordinates[i] != ',':
				x.append(coordinates[i])
				i = i + 1
		elif len(y) == 0:
			while i < len(coordinates) and coordinates[i] != ' ' and coordinates[i] != ',':
				y.append(coordinates[i])
				i = i + 1
		elif len(z) == 0:
			while i < len(coordinates) and coordinates[i] != ' ' and coordinates[i] != ',':
				z.append(coordinates[i])
				i = i + 1
		else:
			while i < len(coordinates):
				rest.append(coordinates[i])
				i = i + 1
		pass
	if len(rest) != 0:
		print("Too many arguments")
	else:
		try:
			final_coordinates = []
			str = ''.join(x)
			x = float(str)
			final_coordinates.append(x)
			str = ''.join(y)
			y = float(str)
			final_coordinates.append(y)
			str = ''.join(z)
			z = float(str)
			final_coordinates.append(z)
			return final_coordinates
		except ValueError as error :
			print(f"Error on parameter '{str}'': {error}")
			return check_coordinates()

def calculate_distance(first_tuple, second_tuple):
	distance = math.sqrt((second_tuple[0] - first_tuple[0])**2 + (second_tuple[1] - first_tuple[1])**2 + (second_tuple[2] - first_tuple[2])**2)
	return distance

def main():
	print("=== Game Coordinate System ===")
	print("")
	print("Get a first set of coordinates")
	first_tuple = []
	first_tuple = check_coordinates()
	print(f"Got a first tuple: ({first_tuple[0]}, {first_tuple[1]}, {first_tuple[2]})")
	print(f"It includes: X={first_tuple[0]}, Y={first_tuple[1]}, Z={first_tuple[2]}")
	distance = []
	distance = calculate_distance(first_tuple, [0, 0, 0])
	print(f"Distance to center: {distance:.4f}")
	print("")
	print("Get a second set of coordinates")
	second_tuple = []
	second_tuple = check_coordinates()
	distance = calculate_distance(first_tuple, second_tuple)
	print(f"Distance between the 2 sets of coordinates: {distance:.4f}")

if __name__ == "__main__":
    main()