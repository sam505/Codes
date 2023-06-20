def pangrams(s: str) -> str:
    # Write your code here
    s = s.lower()
    alphabet = [chr(i) for i in range(97, 123)]

    for char in alphabet:
        if char not in s:
            return "not pangram"
    
    return "pangram"
    