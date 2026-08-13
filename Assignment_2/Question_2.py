L = [10, 0, 20, 40, 10, 70, 0, 30, 40, 60]

scores = tuple(L[:8])

print("Scores tiple:")
print(scores)

highest = max(scores)

highest_index = scores.index(highest)

lowest = min(scores)

lowest_count = scores.count(lowest)

print("\nHighest score:", highest)
print("Index of highest score:", highest_index)

print("Lowest score:", lowest)
print("Number of times lowest appears:", lowest_count)

reversed_scores = list(reversed(scores))

print("\nReversed tuple as a list:")
print(reversed_scores)

user_score = int(input("\nEnter a score to search: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score is not present in the tuple.")

print("\nTrying to change scores[0] to 100")

try:
    scores[0] = 100

except TypeError as error:
    print("Python error:")
    print(error)

first_score, second_score, *remaining_scores = scores

print("\nFirst score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)