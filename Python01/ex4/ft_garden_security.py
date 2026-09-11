class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._age = 0
        self._height = 0
        self._name = name
        self.set_height(height)
        self.set_age(age)
        self.show()

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

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8)

    def show(self) -> None:
        print(f"Created: {self._name}:"
              " {round(self.get_height(), 1)}cm, {self.get_age()} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    rose.set_height(-2)
    rose.show()
    rose.grow()
    rose.grow()
    rose.show()
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)


if __name__ == "__main__":
    main()
