def reverse_aplha(s: str) -> str:

    s_new = s[::-1]

    s_new = [char for char in s_new if char.isalpha()]

    [s_new.insert(i, s[i]) for i in range(len(s)) if not s[i].isalpha()]

    return "".join(s_new)