import pytest

from advent_of_code_2024.day1 import get_distance_between_numbers


def test_how_far_apart_are_2_numbers():
    actual = get_distance_between_numbers(['3', '4', '2', '1', '3', '3'], ['4', '3', '5', '3', '9', '3'])
    assert sum(actual) == 11
