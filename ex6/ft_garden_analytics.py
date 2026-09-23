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
        self._stats = Plant.Stats()

    @staticmethod
    def is_older(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def new_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.record_show()
        print(
            self._name + ":",
            round(self._height, 1),
            "cm,",
            self._age_days,
            "days old",
        )

    def grow(self, amount: float = 2.1) -> None:
        self._height = self._height + amount
        self._stats.record_grow()

    def age(self, days: int = 1) -> None:
        self._age_days = self._age_days + days
        self._stats.record_age()

    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def record_grow(self) -> None:
            self._grow = self._grow + 1

        def record_age(self) -> None:
            self._age = self._age + 1

        def record_show(self) -> None:
            self._show = self._show + 1

        def record_shade(self) -> None:
            self._shade = self._shade + 1

        def display(self, with_shade: bool = False) -> None:
            print(
                "Stats:",
                self._grow,
                "grow,",
                self._age,
                "age,",
                self._show,
                "show",
            )
            if with_shade:
                print(self._shade, "shade")


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

    def bloom(self) -> None:
        self._bloomed = True

    def bloom_status(self) -> None:
        if self._bloomed:
            print(self._name, "is blooming beautifully!")
        else:
            print(self._name, "has not bloomed yet")

    def show(self) -> None:
        super().show()
        print("Color:", self._color)
        self.bloom_status()


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            "Tree",
            self._name,
            "now produces a shade of",
            round(self._height, 1),
            "cm long and",
            round(self._trunk_diameter, 1),
            "cm wide.",
        )

    def show(self) -> None:
        super().show()
        print(
            "Trunk diameter:",
            round(self._trunk_diameter, 1),
            "cm",
        )


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seeds = 0

    def bloom(self, seeds: int = 0) -> None:
        super().bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print("Seeds:", self._seeds)


def display_statistics(plant: Plant) -> None:
    plant._stats.display(with_shade=isinstance(plant, Tree))


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? ->",
        Plant.is_older(30),
    )
    print(
        "Is 400 days more than a year? ->",
        Plant.is_older(400),
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.new_plant()
    anonymous.show()
    display_statistics(anonymous)
