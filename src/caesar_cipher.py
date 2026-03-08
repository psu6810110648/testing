def caesarCipher(s: str, k: int) -> str:
    """
    Encrypt string using Caesar cipher with rotation factor k.
    """
    res = []
    k = k % 26
    for char in s:
        if 'a' <= char <= 'z':
            res.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            res.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            res.append(char)
    return "".join(res)
