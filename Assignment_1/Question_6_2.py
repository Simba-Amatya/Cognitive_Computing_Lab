def IsPrime(n):
    if n < 2:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1
def AddPrime(n):
    s = 0
    for i in range(2, n + 1):
        if IsPrime(i):
            s = s + i
    return s
n = int(input("Enter n: "))
print("Sum of prime numbers -->", AddPrime(n))