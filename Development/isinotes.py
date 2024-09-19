def calculate_revenue(my_values):
    total = 0
    for value in my_values:
        total = total + value
    
    return total

# my program starts here
print("START OF PROGRAM")
# we must invoke the function
sales_week_01 = [14, 21, 13, 554, 35]
sales_week_02 = [234, 45, 23, 12, 34]
sales_week_03 = [23, 45, 12, 34, 56]

revenue_week_01 = calculate_revenue(sales_week_01)
revenue_week_02 = calculate_revenue(sales_week_02)
revenue_week_03 = calculate_revenue(sales_week_03)

print("Total revenue is: ", revenue_week_01)
print("END OF PROGRAM")