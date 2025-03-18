def count_leading_chars(s, char):
    count = 0
    
    for c in s:
        if c == char:
            count += 1
        else:
            break
    
    print(count)

def main():
    s, char = input().strip().split(',')
    count_leading_chars(s, char)

main()
