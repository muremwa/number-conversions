"""
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

"""
from csv import DictReader
import os


with open(os.path.join(os.path.dirname(__file__), 'systems.csv'), 'r') as sys_file:
    n_sys = DictReader(sys_file)
    number_systems = [dict(n_s) for n_s in n_sys]


__all__ = ['number_systems']
