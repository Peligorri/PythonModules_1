class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_plant(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    plant1 = Plant("Rose", 25.0, 30)

    plant1.show()
    initial_height = plant1.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.grow()
        plant1.age_plant()
        plant1.show()

    final_height = round(plant1.height - initial_height, 1)
    print(f"Growth this week: {final_height}cm")


if __name__ == "__main__":
    main()
