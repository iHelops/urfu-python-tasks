from collections import Counter

def palindrome(s):
    char_count = Counter(s)
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    if odd_count > 1:
        print("Палиндром составить нельзя")
        return
    
    half_palindrome = []
    middle_char = ''
    
    for char, count in char_count.items():
        if count % 2 != 0:
            middle_char = char
        half_palindrome.append(char * (count // 2))
    
    half_palindrome = ''.join(half_palindrome)
    palindrome = half_palindrome + middle_char + half_palindrome[::-1]
    
    print(palindrome)

s = input()
palindrome(s)
