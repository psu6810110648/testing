def alternate(s: str) -> int:
    """
    Find the longest string you can construct by removing all but two characters, 
    such that the remaining two characters alternate.
    """
    max_len = 0
    unique_chars = list(set(s))
    
    if len(unique_chars) < 2:
        return 0
        
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            # Filter the string to only include char1 and char2
            filtered = [c for c in s if c == char1 or c == char2]
            
            # Check if they alternate
            is_alternating = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k-1]:
                    is_alternating = False
                    break
            
            if is_alternating:
                max_len = max(max_len, len(filtered))
                
    return max_len
