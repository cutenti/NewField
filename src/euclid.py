def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a, b = int(input()), int(input())
print(gcd(a, b))