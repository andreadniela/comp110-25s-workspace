"""This module tests the functions that work with dictionaries"""

__author__ = "730483450"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

import pytest


def test_invert_use_1() -> None:
    """Test use case #1 for invert"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    """Test use case #2 for invert"""
    assert invert({"apple": "cat", "banana": "dog"}) == {
        "cat": "apple",
        "dog": "banana",
    }


def test_invert__edge() -> None:
    """Test edge case for invert"""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use_1() -> None:
    """Test use case #1 for count"""
    assert count(["apple", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 1,
        "cherry": 1,
    }


def test_count_use_2() -> None:
    """Test use case #2 for count"""
    assert count(["apple", "banana", "apple", "cherry", "banana"]) == {
        "apple": 2,
        "banana": 2,
        "cherry": 1,
    }


def test_count_edge() -> None:
    """Test edge case for count"""
    assert count([]) == {}


def test_favorite_color_use_1() -> None:
    """Test use case #1 for favorite_color"""
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"
    )


def test_favorite_color_use_2() -> None:
    """Test use case #2 for favorite_color"""
    assert favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "red"}) == "blue"


def test_favorite_color_edge() -> None:
    """Test edge case for favorite_color"""
    assert favorite_color({}) == ""


def test_bin_len_use_1() -> None:
    """Test use case #1 for bin_len"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_2() -> None:
    """Test use case #2 for bin_len"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge() -> None:
    """Test edge case for bin_len"""
    assert bin_len([]) == {}
