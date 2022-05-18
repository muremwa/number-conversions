"""
Convert to and from a representation
"""

from typing import List

from prep import number_codes


def convert_to_representation(numbers: List[int]) -> str:
    return ''.join([chr(number_codes[num]) for num in numbers])


def convert_from_representation(representation: str) -> List[int]:
    return [number_codes.index(ord(c)) for c in representation]
