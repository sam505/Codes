def palindromeIndex(s):
    # Write your code here
    low = 0
    high = len(s)-1
    
    while low < high:
        print(low, high)
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            # check if low index if removed, word is a palindrome
            low_string = s[low+1:high+1]
            high_string = s[low:high]

            print(high_string, low_string)
            
            if low_string == low_string[::-1]:
                return low
            elif high_string == high_string[::-1]:
                return high
            else:
                return -1
    return -1
        

if __name__ == '__main__':
    print(palindromeIndex("aaab"))
