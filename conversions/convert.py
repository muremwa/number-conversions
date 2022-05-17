from typing import List

from conversions.representations import convert_to_representation


def convert_from_base_10(decimal: int, new_base: int) -> List[str]:
    """
    Takes a decimal and converts it to the the designated number into the new base.
    """
    rems = []
    value = decimal

    while value >= new_base:
        rems.append(value % new_base)
        value //= new_base

    rems.append(value)

    return [convert_to_representation([rem for rem in reversed(rems)]), str(new_base)]


def convert_float_from_base_10(floating_decimal: float, new_base: int) -> List[str]:
    """
    Takes the decimal part and converts it to the new base
    """
    pass
