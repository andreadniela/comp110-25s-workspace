"""File to define River class"""

__author__ = "730483450"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish older than 3 and Bears older than 5"""
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def bears_eating(self):
        """Each bear eats 3 fish if there are at least 5 fish in the river"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove Bears from the river if their hunger_score is less than 0"""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def repopulate_fish(self):
        """For every pair of fish, add four new fish to the river"""
        number_of_new_fish = (len(self.fish) // 2) * 4
        numbers = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
        ]
        counter = 0
        for num in numbers:
            if counter < number_of_new_fish:
                self.fish.append(Fish())
                counter += 1

    def repopulate_bears(self):
        """For every two bears, add one new bear to the river"""
        number_of_new_bears = len(self.bears) // 2
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        counter = 0
        for num in numbers:
            if counter < number_of_new_bears:
                self.bears.append(Bear())
                counter += 1

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


def one_river_week(self):
    """Simulate seven days in the river"""
    for i in range(7):
        self.one_river_day()


def remove_fish(self, amount: int):
    """Remove the frontmost Fish from the river"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for num in numbers:
        if count < amount and len(self.fish) > 0:
            self.fish.pop(0)
            count += 1
