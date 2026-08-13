roll_no = "1024170346"

digits = [int(digit) for digit in roll_no[:8]]

print("First 8 digits:", digits)

A = {digit * 7 for digit in digits}

B = {digit * 9 for digit in digits}

print("\nSet A:")
print(A)

print("\nSet B:")
print(B)

union = A.union(B)

print("\nUnion of A and B:")
print(union)

intersection = A.intersection(B)

print("\nIntersection of A and B:")
print(intersection)

A_minus_B = A.difference(B)

B_minus_A = B.difference(A)

print("\nA - B:")
print(A_minus_B)

print("\nB - A:")
print(B_minus_A)

symmetric_difference = A.symmetric_difference(B)

print("\nSymmetric difference:")
print(symmetric_difference)

print("\nIs A a subset of B?")
print(A.issubset(B))

print("\nIs B a superset of A?")
print(B.issuperset(A))

X = int(input("\nEnter a value X to remove from A: "))

A.discard(X)

print("Set A after discard(X):")
print(A)
# discard() is safer than remove() because it does not produce
# an error when X is not present in the set