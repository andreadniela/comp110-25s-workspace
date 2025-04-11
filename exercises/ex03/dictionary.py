"""This module has functions that work with dictionaries"""

__author__ = "730483450"


def invert(d: dict[str, str]) -> dict[str, str]:
    """inverts the keys and values of a dictionary"""
    inverted_dict = {}
    for key in d:
        value = d[key]
        if value in inverted_dict:
            raise KeyError(f"Duplicate key detected: {value}")
        inverted_dict[value] = key
    return inverted_dict


def count(items: list[str]) -> dict[str, int]:
    """ "Counts the frequency of each item in a list"""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """returns the most common favorite color from a dictionary"""
    color_counts = {}
    for name in colors:
        color = colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_frequent_color = ""
    highest_count = 0
    for color in color_counts:
        if color_counts[color] > highest_count:
            most_frequent_color = color
            highest_count = color_counts[color]
    return most_frequent_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """categorizes strings by their length and returns a dictionary of lists"""
    bins = {}
    for string in strings:
        length = len(string)
        if length not in bins:
            bins[length] = set()
        bins[length].add(string)
    return bins
