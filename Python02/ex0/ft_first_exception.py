
def input_temperature(tem_str):
	return int(tem_str)

def main():
	print("=== Garden Temperature ===")
	print("")
	try:
		data = "25"
		print(f"Input data is '{data}'")
		temperature = input_temperature(data)
		print(f"Temperature is now {temperature}ºC")
		print("")
		data = "abc"
		print(f"Input data is '{data}'")
		temperature = input_temperature(data)
		print(f"Temperature is now {temperature}ºC")
	except ValueError as error:
		print(f"Caught input_temperature error: {error}")
	print("")
	print(f"All test completed - program didn't crash!")



if __name__ == "__main__":
    main()

