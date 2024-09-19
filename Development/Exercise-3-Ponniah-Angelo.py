import turtle

# let's define a pen
t = turtle.Turtle()

# Set the side length
side_length = 10

# Initialize a counter for the number of sides
count = 0

# Use a while loop to draw the square
while count < 4:
    t.forward(side_length)  # Move the turtle forward by the side length
    t.right(90)  # Turn the turtle right by 90 degrees
    count += 1  # Increment the counter


# let's not close the window
turtle.done()
