def fetch_string_from_api(url: str) -> str:
    """
    Simulates an external API call that shouldn't be executed during tests.
    """
    raise NotImplementedError("This function is part of an external API call and MUST be stubbed in tests.")

def process_api_string_for_funny(url: str) -> str:
    """
    Fetches a string from an API and determines if it's funny.
    """
    from src.funny_string import funnyString
    
    # Needs STUB during test to avoid NotImplementedError
    s = fetch_string_from_api(url)
    
    return funnyString(s)
