import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the step length and rise length
step_length = 15
rise_length = 10

# Move the turtle to the starting position
t.penup()
t.goto(-step_length / 2, 0)  # Start drawing at the bottom of the ladder
t.pendown()

# Use a loop to draw the ladder
for _ in range(10):
    # Draw the horizontal step
    t.forward(step_length)
    
    # Draw the vertical rise
    t.left(90)
    t.forward(rise_length)
    
    # Turn right to get ready for the next step
    t.right(90)

# Close the Turtle graphics window when clicked
turtle.done()
