def to_base(n, base):
    digits = "0123456789ABCDEF"
    result = ""

    while n > 0:
        result = digits[n % base] + result
        n //= base
    
    return result

def main():
    try:
        n = int(input().strip())

        if n <= 0:
            raise ValueError
        
        print(f"{to_base(n, 2)}, {to_base(n, 8)}, {to_base(n, 16)}")
    except ValueError:
        print("Неверный ввод")

main()
