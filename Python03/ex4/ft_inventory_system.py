import sys

class ParameterError(Exception):
	def __init__(self, message="Error - "):
		super().__init__(message)
	pass

def main():
	print("=== Inventory System Analysis ===")

	inventory = {}
	item_quantity = 0
	total_items = 0

	for item in sys.argv[1:]:
		try:
			if ":" in item:
				item_name, quantity = item.split(":")
				if item_name in inventory:
					print(f"Redundant item '{item_name}' - discarding")
				else:
					inventory[item_name] = int(quantity)
					item_quantity = item_quantity + 1
					total_items = total_items + int(quantity)
			else:
				raise ParameterError(f"invalid parameter '{item}'")
		except ParameterError as error:
			print(f"Error - {error}")
		except Exception as error:
			print(f"Quantity error for '{item_name}': {error}")        

	print(f"Got inventory: {inventory}")
	print(f"Item list: {list(inventory.keys())}")
	print(f"Total quantity of the {item_quantity} items: {total_items}")
	for item, quantity in inventory.items():
		percentage = quantity / total_items * 100
		print(f"Item {item} represents {percentage:.1f}%")
	print(f"Item most abundant: {max(inventory, key=inventory.get)} with quantity {inventory[max(inventory, key=inventory.get)]}")
	print(f"Item least abundant: {min(inventory, key=inventory.get)} with quantity {inventory[min(inventory, key=inventory.get)]}")
	inventory["magic_item"] = 1
	print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()