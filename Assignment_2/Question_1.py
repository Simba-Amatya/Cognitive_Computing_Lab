import random

roll_no = "1024170346"

digits = [int(digit) for digit in roll_no]
L = [digit * 10 for digit in digits]

print("Initial L:", L)

L.append(500)
print("After append(500):", L)
# append() adds 500 at the end of the list
L.insert(2, 250)
print("After insert(2, 250):", L)
# insert() adds 250 at index 2 and shifts later elements right
L.remove(500)
print("After remove(500):", L)

removed = L.pop(2)
print("Afterpop(2):", L)
print("Element removed using pop():", removed)

L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)

print("First three elements:", L[:3])
print("Last three elements:", L[-3:])

average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Average:", average)
print("Elements graeter than average:", greater_than_average)