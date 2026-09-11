def input_temperature(tem_str: str) -> int:
    return int(tem_str)


def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            input_temperature("abc")
        elif operation_number == 1:
            7 / 0
        elif operation_number == 2:
            open("/non/existent/file", "r")
        elif operation_number == 3:
            "3" + 2
        elif operation_number == 4:
            print("Operation completed successfully")
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations(0)
    garden_operations(1)
    garden_operations(2)
    garden_operations(3)
    garden_operations(4)
    print("")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    main()
