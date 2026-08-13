def AddOdd(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s = s + i
    return s
n = int(input("Enter n: "))
print("Sum of odd numbers -->", AddOdd(n))