#Write a function that prints all elements 
# whose index is an odd number Use a for-loop

def odd_index_only(vector):
    for i in range(1, len(vector), 2):
        print(vector[i])

# Example usage:
# odd_index_only([10, 20, 30, 40, 50, 60])
# This will print:
# 20
# 40
# 60