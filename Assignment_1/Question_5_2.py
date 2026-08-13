n = int(input("Enter n: "))

s = 0

for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        s = s + i

print("Sum is -->", s)