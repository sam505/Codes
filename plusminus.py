def plusMinus(arr):
    neg = 0
    pos = 0
    zero = 0
    # Write your code here
    for num in arr:
        if num < 0:
            neg += 1
        elif num > 0:
            pos += 1
        else:
            zero += 1
            
    return round(float(pos/len(arr)),6), round(float(neg/len(arr)),6 ), round(float(zero/len(arr)), 6)

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    print(plusMinus(arr))
