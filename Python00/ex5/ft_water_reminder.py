def ft_water_reminder() -> None:
    days = input("Days since last watering: ")
    if 2 < int(days):
        print("Water the plants!")
    else:
        print("Plants are fine")
