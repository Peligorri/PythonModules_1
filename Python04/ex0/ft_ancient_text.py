import sys


def main() -> None:
    print("=== Cyber Archives Recovery ===")

    try:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            lines = file.readlines()
            print("===")
            print("")
            for i in lines:
                print(i, end="")
            print("")
            print("===")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    except Exception:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
