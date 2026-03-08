import pytest
from src.caesar_cipher import caesarCipher

def test_caesar_cipher_basic():
    assert caesarCipher("middle-Outz", 2) == "okffng-Qwvb"

def test_caesar_cipher_large_k():
    assert caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5) == "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

def test_caesar_cipher_all_types():
    assert caesarCipher("159357lcfd", 98) == "159357fwzx"

def test_caesar_cipher_no_rotation():
    assert caesarCipher("Hello World!", 0) == "Hello World!"

def test_caesar_cipher_punctuation():
    assert caesarCipher("!@#$%^&*()", 13) == "!@#$%^&*()"
