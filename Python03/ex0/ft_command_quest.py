import sys

def main():
	print("=== Comand Quest ===")
	print(f"Program name: {sys.argv[0]}")
	x = 1
	if (len(sys.argv) == 1):
		print("No arguments provided!")
	else:
		print(f"Arguments recived: {len(sys.argv) - 1}")
		while x < len(sys.argv):
			print(f"Argument {x}: {sys.argv[x]}")
			x = x + 1
			pass
	print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
    main()