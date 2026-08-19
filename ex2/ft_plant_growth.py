class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age_days: int,
            growth_rate: float,
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(
            self.name + ":",
            round(self.height, 1),
            "cm,",
            self.age_days,
            "days old")

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.age_days = self.age_days + 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age()

        print("=== Day", day, "===")
        rose.show()

    growth = rose.height - initial_height
    print("Growth this week:", round(growth, 1), "cm")
