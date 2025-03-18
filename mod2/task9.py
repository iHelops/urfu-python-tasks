def clean_phone_number(phone):
    cleaned = ''.join(c for c in phone if c.isdigit() or c == '+')
    print(cleaned)

phone = input().strip()
clean_phone_number(phone)
