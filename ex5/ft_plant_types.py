class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
    ) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days

    def show(self):
        print(
            self._name + ":",
            round(self._height, 1),
            "cm,",
            self._age_days,
            "days old",
        )

    def grow(self):
        self._height = self._height + 2.1

    def age(self):
        self._age_days = self._age_days + 1


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def bloom_status(self):
        if self._bloomed:
            print(self._name, "is blooming beautifully!")
        else:
            print(self._name, "has not bloomed yet")

    def show(self):
        super().show()
        print("Color:", self._color)
        self.bloom_status()


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diametar: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diametar = trunk_diametar

    def produce_shade(self):
        print(
            "Tree",
            self._name,
            "now produces a shade of",
            round(self._height, 1),
            "cm long and",
            round(self._trunk_diametar, 1),
            "cm wide.",
        )

    def show(self):
        super().show()
        print("Trunk diameter:", round(self._trunk_diametar, 1), "cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self):
        super().grow()

    def age(self):
        super().age()
        self._nutritional_value = self._nutritional_value + 1

    def show(self):
        super().show()
        print("Harvest season:", self._harvest_season)
        print("Nutritional value:", self._nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
