from random import randint

def gen_event():
	events = ["move", "run", "grab", "use", "climb", "swim", "release", "eat", "sleep"]
	player_name = ["Charlie", "Dylan", "Alice", "Bob"]
	name = player_name[randint(0, 3)]
	action = events[randint(0, 8)]
	
	yield (name, action)

def consume_event(second_list, i):
	eliminated = second_list.pop(randint(0, i))

	yield eliminated

def main():
	
	i = 0
	second_list = []
	
	print("=== Game Data Stream Processor ===")
	while i < 1000:
		name, action = next(gen_event())
		print(f"Event {i}: Player {name} did action {action}")
		i += 1
	print("")
	i = 0
	while i < 10:
		second_list.append(next(gen_event()))
		i += 1
	print(f"Build list of 10 events: {second_list}")
	print("")
	while i > 0:
		eliminated = next(consume_event(second_list, i - 1))
		print(f"Got event from list: {eliminated}")
		print(f"Remains in list: {second_list}")
		i -= 1


if __name__ == "__main__":
	main()