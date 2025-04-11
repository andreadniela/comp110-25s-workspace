""" This program calculates the required tea bags, treats, and estimated cost for a tea party based on the number of guests"""

__author__: str = "730483450"


def main_planner(guests: int) -> None:
    """Integrates all helper functions to calculate and print the quantities of tea bags, treats, and the total cost for a tea party"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Total Cost: $"
        + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests)))
    )


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed based on the number of teas each guest is expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats combined based on their quantities and costs"""
    return (0.50 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
