plant1 = {
    "Name": "Rose",
    "Height": 25,
    "Age": 30
}
plant2 = {
    "Name": "Sunflower",
    "Height": 80,
    "Age": 45
}
plant3 = {
    "Name": "Cactus",
    "Height": 15,
    "Age": 120
}


def show(plant):
    print(f"{plant['Name']}: {plant['Height']}cm, {plant['Age']} days old")


def main():
    print("=== Garden Plant Registry ===")
    show(plant1)
    show(plant2)
    show(plant3)


if __name__ == "__main__":
    main()
