def last_letters_word(words):
    result = "".join(word[-1] for word in words.split())
    print(result)

def main():
    words = input().strip()
    last_letters_word(words)

main()