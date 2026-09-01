def ft_plant_age() -> None:
    days = input("Enter plant age in days: ")
    if 60 < int(days):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
