"""
Stores the number systems and number codes

Return all 82 standard number systems defined by Wikipedia  \n
URL: https://en.wikipedia.org/wiki/List_of_numeral_systems \n
DATE: 2022-05-02.  \n

[
    {
        'base': str,
        'system': str,
        'system_name': str
    },
    ...
]

usage:
from prep import number_systems

Return the character representations for the first 360 number, which is enough for the 82 number systems that max out
at base 360. Return a tuple of codes that are in order of the digits, index 0 for the 1st digit and index 359 for the
360th digit.

usage:
from prep import number_codes

"""
from csv import DictReader
from functools import lru_cache
from typing import Tuple
import os


"""
Retrieve the number systems from file
"""


@lru_cache(maxsize=1024)
def __load_number_systems() -> Tuple[Tuple[dict,...], Tuple[int]]:
    with open(os.path.join(os.path.dirname(__file__), 'systems.csv'), 'r') as sys_file:
        n_sys = DictReader(sys_file)
        number_systems_p = tuple(dict(n_s) for n_s in n_sys)

    return number_systems_p, tuple(int(sys_['base']) for sys_ in number_systems_p)


number_systems = __load_number_systems()


"""
We need 360 unique characters from UNICODE / ASCII

ascii_codes below represents 360 values in order, that I have chosen (Someone has to).
(peep prep/numbers_map.csv to see their equivalent)

to convert just use chr, a built-in function
"""
number_codes = (
    48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
    84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
    115, 116, 117, 118, 119, 120, 121, 122, 45, 95, 43, 47, 35, 36, 37, 38, 42, 64, 126, 175, 161, 163, 181, 191, 192,
    200, 204, 504, 210, 217, 224, 232, 236, 505, 242, 249, 193, 201, 500, 205, 313, 323, 211, 340, 346, 218, 221, 377,
    510, 225, 233, 501, 237, 314, 324, 243, 341, 347, 250, 253, 378, 511, 194, 202, 284, 292, 206, 308, 212, 348, 219,
    372, 374, 226, 234, 285, 293, 238, 309, 244, 349, 251, 373, 375, 195, 516, 296, 209, 213, 360, 227, 517, 245, 297,
    241, 337, 361, 196, 203, 207, 214, 220, 376, 228, 235, 239, 246, 252, 255, 197, 366, 229, 367, 199, 552, 310, 315,
    325, 342, 536, 354, 231, 311, 316, 326, 537, 355, 216, 248, 478, 482, 298, 332, 492, 362, 562, 479, 483, 333, 493,
    363, 563, 550, 379, 551, 329, 357, 380, 461, 494, 486, 542, 463, 496, 488, 327, 465, 356, 381, 462, 495, 487, 543,
    464, 489, 328, 466, 382, 208, 514, 518, 522, 526, 530, 534, 515, 519, 523, 527, 531, 535, 286, 334, 364, 287, 335,
    365, 358, 370, 385, 387, 391, 394, 396, 398, 401, 403, 406, 408, 411, 413, 416, 418, 428, 886, 435, 437, 440, 484,
    386, 952, 994, 490, 548, 330, 570, 571, 331, 359, 371, 383, 384, 388, 389, 390, 392, 393, 395, 397, 399, 400, 402,
    404, 405, 407, 960, 409, 410, 412, 414, 415, 417, 419, 995, 420, 421, 422, 423, 425, 928, 426, 427, 429, 433, 430,
    434, 436, 438, 439, 441, 477, 485, 491, 502, 503, 544, 545, 549, 565, 572, 573, 574, 576, 577, 614, 615, 625, 580,
    598, 608, 611, 624, 887, 626, 627, 581, 650, 651, 652, 653, 654, 656, 1021, 1022, 915, 916, 658, 648, 661, 662, 663,
    669, 670, 940, 672, 664
)

__all__ = ['number_systems', 'number_codes']
