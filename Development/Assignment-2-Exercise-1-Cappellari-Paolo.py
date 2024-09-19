# Define a vector of integers with 10 elements
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# From 1st to last element, using a for loop
print("From 1st to last element, using a for loop:")
for i in range(len(vector)):
    print(vector[i], end=' ')
print()

# From last to 1st element, using a for loop
print("From last to 1st element, using a for loop:")
for i in range(len(vector)-1, -1, -1):
    print(vector[i], end=' ')
print()

# From 1st to last element, using a while-do loop
print("From 1st to last element, using a while-do loop:")
i = 0
while i < len(vector):
    print(vector[i], end=' ')
    i += 1
print()

# From last to 1st element, using a while-do loop
print("From last to 1st element, using a while-do loop:")
i = len(vector) - 1
while i >= 0:
    print(vector[i], end=' ')
    i -= 1
print()