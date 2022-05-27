"""Assurances for the numbers presented by user"""
from prep import number_systems


def ensure_no_base_10(number: str) -> bool:
    """Ensures the number presented is actually possible to be a decimal"""
    try:
        float(number)
        return True
    except ValueError:
        return False


def ensure_base_is_standard(base: int) -> bool:
    """
        Ensures the base entered is one of the 82 standard bases.
        Described 'prep/systems.csv' or https://en.wikipedia.org/wiki/List_of_numeral_systems
    """
    return base in number_systems[-1]
