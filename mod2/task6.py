def check_equal_zeros_ones(binary_str):
    if binary_str.count('0') == binary_str.count('1'):
        print('yes')
    else:
        print('no')

def main():
    binary_str = input().strip()
    check_equal_zeros_ones(binary_str)

main()