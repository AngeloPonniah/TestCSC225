#Write a function that prints all elements of a 
# vector from the first element up to the first occurrence of the 
# element having value equal to a provide number


def print_up_to_value(a_vector, a_value):
    index = 0
    result = []
    while index < len(a_vector):
        result.append(a_vector[index])
        if a_vector[index] == a_value:
            break
        index += 1
    print(result)

# Example usage
my_vector = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9]
print_up_to_value(my_vector, 7)