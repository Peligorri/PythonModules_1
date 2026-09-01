def ft_recursive(count: int, days: str) -> None:
    print(f"Day {count}")
    count += 1
    if (count <= int(days)):
        ft_recursive(count, days)


def ft_count_harvest_recursive() -> None:
    count = 1
    days = input("Days until harvest: ")
    ft_recursive(count, days)
    print("Harvest time!")
