import sys


class ParameterError(Exception):
    def __init__(self, message: str = "Error - "):
        super().__init__(message)
    pass


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    item_quantity = 0
    total_items = 0

    for item in sys.argv[1:]:
        try:
            if ":" in item:
                item_name, quantity_str = item.split(":")
                quantity = int(quantity_str)
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
        percentage = int(quantity) / int(total_items) * 100
        print(f"Item {item} represents {percentage:.1f}%")
    print("Item most abundant: "
          f"{max(inventory, key=lambda item: inventory[item])} "
          f"with quantity {inventory[max(inventory,
                           key=lambda item: inventory[item])]}")
    print("Item least abundant: "
          f"{min(inventory, key=lambda item: inventory[item])} "
          f"with quantity {inventory[min(inventory,
                           key=lambda item: inventory[item])]}")
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
