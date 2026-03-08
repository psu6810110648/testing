def alternatingCharacters(s: str) -> int:
    """
    Find minimum number of deletions such that there are no matching adjacent characters.
    """
    if not s:
        return 0
        
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions
