def secure_archive(file: str,
                   action: str, text: str | None = None) -> tuple[bool, str]:
    if action == 'read':
        try:
            read_file = open(file, 'r')
            return (True, repr(read_file.read()))
        except Exception as e:
            error = f"{e}"
            return (False, error)
    elif action == 'write':
        if text is None:
            return (False, "Error: No text detected")
        write_file = open("console_data.txt", 'w')
        write_file.write(text)
        write_file.close()
        return (True, "Content successfully written to file.")
    return (False, "Invalid action.")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("")
    print("Using 'secure_archive' to read from a noexistent file:")
    tuple_ko1 = secure_archive('noexistent.txt', 'read')
    print(f"{tuple_ko1}")
    print("")
    print("Using 'secure_archive' to read from a inaccessible file:")
    tuple_ko2 = secure_archive('/etc/shadow', 'read')
    print(f"{tuple_ko2}")
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    tuple_ok = secure_archive('ancient_fragment.txt', 'read')
    print(f"{tuple_ok}")
    print("")
    print("Using 'secure_archive' to write previous content ti a new file:")
    all_str = (
        "=== Cyber Archives Security ===\n\n"
        "Using 'secure_archive' to read from a noexistent file:\n"
        f"{tuple_ko1}\n\n"
        "Using 'secure_archive' to read from a inaccessible file:\n"
        f"{tuple_ko2}\n\n"
        "Using 'secure_archive' to read from a regular file:\n"
        f"{tuple_ok}\n\n"
        "Using 'secure_archive' to write previous content ti a new file:"
    )
    tuple_write = secure_archive('regularfile.txt', 'write', str(all_str))
    print(f"{tuple_write}")


if __name__ == "__main__":
    main()
