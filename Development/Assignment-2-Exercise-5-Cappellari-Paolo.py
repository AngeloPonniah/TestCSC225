def swap(vector, index1, index2):
    # Swap the elements at index1 and index2
    vector[index1], vector[index2] = vector[index2], vector[index1]
    return vector

# Example usage
my_vector = [40, 51, 62, 73, 84, 95]
print("Original vector:", my_vector)

# Invoke the swap function
swapped_vector = swap(my_vector, 2, 4)
print("Swapped vector:", swapped_vector)