from random import randint

def main():

	print("=== Game Data Alchemist ===")
	print("")
	initial_list = ["Charlie", "Dylan", "Alice", "Bob", "emma", "gregory", "john", "kevin", "Liam"]
	print(f"Initial list of players: {initial_list}")
	capitalize_list = []
	for i in initial_list:
		capitalize_list.append(i.capitalize())
	print(f"New list with all names capitalized: {capitalize_list}")
	only_capitalize_list = []
	for i in initial_list:
		if i[0].isupper():
			only_capitalize_list.append(i)
	print(f"New list of capitalized names only: {only_capitalize_list}")
	print("")
	dictionary = {}
	for i in capitalize_list:
		dictionary[i] = randint(0, 1000) 
	print(f"Score dict: {dictionary}")
	j = 0
	score_average = 0
	for name, score in dictionary.items():
		score_average = score + score_average
		j += 1
	score_average = score_average / j
	print(f"Score average is {score_average:.2f}")
	second_dictionary = {}
	for name, score in dictionary.items():
		if(score > score_average):
			second_dictionary[name] = score
	print(f"High scores: {second_dictionary}")

if __name__ == "__main__":
	main()