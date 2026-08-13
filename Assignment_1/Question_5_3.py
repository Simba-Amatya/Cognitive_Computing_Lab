n = int(input("Enter n: "))
s = 0
for i in range(2, n + 1):
    f = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        s = s + i
print("Sum of prime numbers -->", s)