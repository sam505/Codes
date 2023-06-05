def solution(N):
    # Implement your solution here
    gap = 0

    num = str(bin(N))
    if "0" not in num:
        return 0
    else:
        values = num.split("1")
        if num[0] != 1:
            values.pop(0)
        if num[-1] != 1:
            values.pop()

        for value in values:
            length = len(value)
            if length > gap:
                gap = length
    
    return gap



if __name__ == "__main__":
    print(solution(32))