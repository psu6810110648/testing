import pytest
from src.alternating_characters import alternatingCharacters

def test_alternating_characters_aabaab():
    assert alternatingCharacters("AABAAB") == 2

def test_alternating_characters_aaaa():
    assert alternatingCharacters("AAAA") == 3

def test_alternating_characters_bbbbb():
    assert alternatingCharacters("BBBBB") == 4

def test_alternating_characters_abababab():
    assert alternatingCharacters("ABABABAB") == 0

def test_alternating_characters_bababa():
    assert alternatingCharacters("BABABA") == 0

def test_alternating_characters_aaabbb():
    assert alternatingCharacters("AAABBB") == 4

def test_alternating_characters_empty():
    assert alternatingCharacters("") == 0
