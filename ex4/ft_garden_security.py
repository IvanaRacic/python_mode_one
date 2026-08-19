class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self._name + ": Error, height cannot be negative.")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(self._name + ": Error, age cannot be negative.")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            self._name + ":",
            round(self._height, 1),
            "cm, ",
            self._age,
            "days old",
        )


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()

    rose.set_height(25)
    print("Height updated:", rose.get_height(), "cm")

    rose.set_age(30)
    print("Age updated:", rose.get_age(), "days")
    print()

    rose.set_height(-5)
    print("Height update rejected")
    print()

    rose.set_age(-10)
    print("Age update rejected")
    print()

    print("Current state:", end=" ")
    rose.show()
