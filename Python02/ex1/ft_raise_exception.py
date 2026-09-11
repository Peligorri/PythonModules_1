
def input_temperature(tem_str: str) -> int:
    return int(tem_str)


def test_temperature(data: str) -> None:
    try:
        print(f"Input data is '{data}'")
        temperature = input_temperature(data)
        if temperature > 40:
            print(f"Caught input_temperature error: {temperature}ºC "
                  "is too hot for plants (max 40ºC)")
        elif temperature < 0:
            print(f"Caught input_temperature error: {temperature}ºC "
                  "is too cold for plants (min 0ºC)")
        else:
            print(f"Temperature is now {temperature}ºC")
        print("")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print("")


def main() -> None:
    print("=== Garden Temperature ===")
    print("")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    main()
