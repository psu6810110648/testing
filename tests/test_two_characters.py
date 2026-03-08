import pytest
from src.two_characters import alternate

def test_alternate_beabeefeab():
    assert alternate("beabeefeab") == 5

def test_alternate_asdcbsdcagfsdbgdfanfghbsfdab():
    assert alternate("asdcbsdcagfsdbgdfanfghbsfdab") == 8

def test_alternate_asvkkuvkskksksvkskvsksvkksvkvsckn():
    assert alternate("asvkkuvkskksksvkskvsksvkksvkvsckn") == 2

def test_alternate_short():
    assert alternate("a") == 0

def test_alternate_two_chars():
    assert alternate("ab") == 2

def test_alternate_repeated():
    assert alternate("aba") == 3

def test_alternate_invalid_two():
    assert alternate("aa") == 0
