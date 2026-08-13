import random

random.seed(1024170346)

numbers = [random.randint(100, 900) for _ in range(100)]

print("100 Random Numbers:")
print(numbers)

odd_numbers = [number for number in numbers if number % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)

print("Number of odd numbers:", len(odd_numbers))

even_numbers = [number for number in numbers if number % 2 == 0]

print("\nEven numbers:")
print(even_numbers)

print("Number of even numbers:", len(even_numbers))

def is_prime(number):

    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True

prime_numbers = [number for number in numbers if is_prime(number)]

print("\nPrime numbers:")
print(prime_numbers)

print("Number of prime numbers:", len(prime_numbers))

frequency = {}

for number in numbers:

    frequency[number] = frequency.get(number, 0) + 1

most_frequent = max(frequency, key=frequency.get)

most_frequent_count = frequency[most_frequent]

print("\nMost frequently occuring number:", most_frequent)

print("Number of times it occurs:", most_frequent_count)