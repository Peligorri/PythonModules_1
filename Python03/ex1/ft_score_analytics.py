import sys

class NoArguments(Exception):
	pass

class NoNumericValues(Exception):
	pass

def main():
	print("=== Player Score Analytics ===")
	try:
		if (len(sys.argv) == 1):
			raise NoArguments("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
		x = 1
		invalid_parameters = []
		while x < len(sys.argv):
			try:
				int(sys.argv[x])
			except ValueError:
				invalid_parameters.append(sys.argv[x])
			x = x + 1
			pass

		if invalid_parameters:
		    for parameter in invalid_parameters:
		        print(f"Invalid parameter: '{parameter}'")
		    raise NoNumericValues("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2>")
		print(f"Scores processes: {sys.argv[1:]}")
		print(f"Total players: {len(sys.argv) - 1}")

		score = 0
		x = 1
		while x < len(sys.argv):
			score = score + int(sys.argv[x])
			x = x + 1
			pass
		print(f"Total score: {score}")

		score = score / int(len(sys.argv) - 1)
		print(f"Average score: {score}")

		x = 1
		high_score = 0
		while x < len(sys.argv):
			if high_score < int(sys.argv[x]):
				high_score = int(sys.argv[x])
			x = x + 1
			pass
		print(f"High score: {high_score}")

		x = 1
		low_score = high_score
		while x < len(sys.argv):
			if low_score > int(sys.argv[x]):
				low_score = int(sys.argv[x])
			x = x + 1
			pass
		print(f"Low score: {low_score}")

		score = high_score - low_score
		print(f"Score range: {score}")


	except NoArguments as error:
		print(error)
	except NoNumericValues as error:
		print(error)

if __name__ == "__main__":
    main()