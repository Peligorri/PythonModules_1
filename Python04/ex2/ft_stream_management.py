import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

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

            print("")
            print("Transform data:")
            file = open(sys.argv[1])
            print("===")
            print("")
            for i in lines:
                i = i.rstrip() + "#\n"
                print(i, end="")
            print("")
            print("===")
            file.close()
            print("Enter new file name (or empty): ", end="", flush=True)
            new_file_name: str
            new_file_name = sys.stdin.readline().strip()
            if not new_file_name:
                print("Not saving data.")
            else:
                try:
                    new_file = open(new_file_name, 'w')
                    file = open(sys.argv[1])
                    new_lines = file.readlines()
                    for i in new_lines:
                        i = i.rstrip() + "#\n"
                        new_file.write(i)

                    print(f"Saving data to '{new_file_name}'")
                    print(f"Data saved in file '{new_file_name}'")
                    print("")
                except Exception as e:
                    print(f"Saving data to '{new_file_name}'")
                    print(f"[STDERR] Error opening file '{new_file_name}'': {e}")
                    print("Data not saved.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    except Exception:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
