import pytest

from max_consecutive import max_consecutive_items


def test_empty():
    assert max_consecutive_items([]) == 0

def test_all_equal():
    assert max_consecutive_items([7, 7, 7]) == 3

def test_mixed_but_bug_not_exposed():
    assert max_consecutive_items([1, 1, 2, 2]) == 2