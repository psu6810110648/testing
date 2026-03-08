def funnyString(s: str) -> str:
    """
    Determine whether a string is Funny or Not Funny.
    """
    r = s[::-1]
    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i-1]))
        diff2 = abs(ord(r[i]) - ord(r[i-1]))
        if diff1 != diff2:
            return "Not Funny"
    return "Funny"
