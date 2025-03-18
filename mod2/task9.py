import re

def clean_phone_number(phone):
    cleaned = re.sub(r'[^0-9+]', '', phone)
    print(cleaned)

def main():
    phone = input().strip()
    clean_phone_number(phone)

main()
