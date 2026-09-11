class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._age = 0
        self._height = 0
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = int(height)
        else:
            print()
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            print()

    def set_age(self, age: int) -> None:
        if (age >= 0):
            self._age = age
        else:
            print()
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            print()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, days: int) -> None:
        self.set_height(self.get_height() + (0.8 * days))

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        print(f"Created: {self._name}:"
              " {round(self.get_height(), 1)}cm,"
              " {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def get_bloom(self) -> None:
        if not self._bloom:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        if not self._bloom:
            self._bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        self.get_bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces "
              "a shade of {self._height}cm long"
              " and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Nutritional value: "
              f"{self._nutritional_value}, harvest "
              f"season: {self._harvest_season}")

    def grow(self, days: int) -> None:
        super().grow(days)
        super().age(days)
        self._nutritional_value = int(self._nutritional_value + (1.5 * days))


def main() -> None:
    print("=== Garden Plant Types")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    tomato.grow(20)
    tomato.show()


if __name__ == "__main__":
    main()
