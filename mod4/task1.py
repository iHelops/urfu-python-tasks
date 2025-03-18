def check_numbers(numbers):
    if len(set(numbers)) == 1:
        print("Все числа равны")
    elif len(set(numbers)) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

input_numbers = list(map(int, input().split()))
check_numbers(input_numbers)
