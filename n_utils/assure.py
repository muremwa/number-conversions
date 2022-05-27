"""Assurances for the numbers presented by user"""
from prep import number_systems, number_codes


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


def ensure_number_is_representable(number: str) -> bool:
    """Ensure that the characters in a number are among the chosen 360"""
    # . is removed since it's not part of the representation
    return all([ord(c) in number_codes for c in number.replace('.', '')])


def ensure_number_representation_is_within_base_limits(number: str, base: int) -> bool:
    """
        Ensure the representations of a number are within the base character representations
        E.g., G4 cannot be base 16 as G is well beyond base 16
        Can be used to the same effect as ensure_number_is_representable
    """
    # . is removed since it's not part of the representation
    # uses the number codes up to a certain place to ensure only character usable for that base are checked
    return all([ord(c) in number_codes[:base] for c in number.replace('.', '')])
