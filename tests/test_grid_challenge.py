import pytest
from src.grid_challenge import gridChallenge

def test_grid_challenge_yes():
    grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
    assert gridChallenge(grid) == "YES"

def test_grid_challenge_no():
    grid = ["mpxz", "abcd", "wlmm"]
    assert gridChallenge(grid) == "NO"

def test_grid_challenge_single():
    grid = ["a"]
    assert gridChallenge(grid) == "YES"

def test_grid_challenge_empty():
    assert gridChallenge([]) == "YES"

def test_grid_challenge_one_row():
    grid = ["acb"]
    assert gridChallenge(grid) == "YES"
