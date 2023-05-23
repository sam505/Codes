def caesarCipher(s, k):
    # Write your code here
    rotation = k % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotated_alpha = alphabet[rotation:] + alphabet[:rotation]
    new_s = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_s += rotated_alpha[alphabet.index(char.lower())].upper()
            else:
                new_s += rotated_alpha[alphabet.index(char)]
        else:
            new_s += char        
    return new_s




def main():
    s = "naMe"
    k = 100
    print(caesarCipher(s, k))



if __name__ == "__main__":
    main()