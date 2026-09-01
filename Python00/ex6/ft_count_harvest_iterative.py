def ft_count_harvest_iterative() -> None:
    count = 1
    days = input("Days until harvest: ")
    while int(count) <= int(days):
        print(f"Day {count}")
        count += 1
    print("Harvest time!")
