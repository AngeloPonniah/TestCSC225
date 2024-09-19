# Define a vector of integers with 5 elements
vector = [1, 2, 3, 4, 5]

def vector_sum(v):
    """Given a vector, returns the sum of all its elements"""
    return sum(v)

def vector_prod(v):
    """Given a vector, returns the product of all its elements"""
    product = 1
    for num in v:
        product *= num
    return product

def vector_max(v):
    """Given a vector, returns the max value among all its elements"""
    return max(v)

def vector_min(v):
    """Given a vector, returns the min value among all its elements"""
    return min(v)

# Example usage
print("Vector:", vector)
print("Sum:", vector_sum(vector))
print("Product:", vector_prod(vector))
print("Max:", vector_max(vector))
print("Min:", vector_min(vector))