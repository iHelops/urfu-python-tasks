def print_domain_levels(domain):
    parts = domain.strip().split('.')
    for part in reversed(parts):
        print(part)

def main():
    domain = input().strip()
    print_domain_levels(domain)

main()
