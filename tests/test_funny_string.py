import pytest
from src.funny_string import funnyString

def test_funny_string_acxz():
    assert funnyString("acxz") == "Funny"

def test_funny_string_bcxz():
    assert funnyString("bcxz") == "Not Funny"

def test_funny_string_single_char():
    assert funnyString("a") == "Funny"

def test_funny_string_empty():
    assert funnyString("") == "Funny"

def test_funny_string_all_same():
    assert funnyString("zzzz") == "Funny"
