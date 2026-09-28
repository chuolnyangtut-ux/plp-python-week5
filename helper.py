import math


def tables_needed(people, seats):
    """Calculates the number of tables needed, rounding UP using math.ceil().

    Parameters:
        people (int): Total count of people.
        seats (int): Number of seats available per table.

    Returns:
        int: Number of tables required.
    """
    return math.ceil(people / seats)


def welcome(name):
    """Returns a welcome message string customized with the provided name.

    Parameters:
        name (str): Name of the person.

    Returns:
        str: Formatted welcome string.
    """
    return f"Welcome to PLP, {name}!"


if __name__ == "__main__":
    print(tables_needed(10, 4))