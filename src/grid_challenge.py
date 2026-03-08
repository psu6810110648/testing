def gridChallenge(grid: list[str]) -> str:
    """
    Given a grid of characters, sort each row alphabetically and check if columns are sorted.
    """
    if not grid:
        return "YES"
        
    # Sort each row
    sorted_grid = [sorted(list(row)) for row in grid]
    
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    # Check each column
    for j in range(cols):
        for i in range(1, rows):
            if sorted_grid[i][j] < sorted_grid[i-1][j]:
                return "NO"
                
    return "YES"
