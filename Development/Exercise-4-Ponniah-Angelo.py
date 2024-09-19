import turtle

# let's define a pen
t = turtle.Turtle()

# Set the line length and the vertical spacing between lines
line_length = 50
vertical_spacing = 10

# Move the turtle to the starting position
t.penup()  # Lift the pen so it doesn't draw while moving to the starting position
t.goto(-line_length / 2, 0)  # Move the turtle to the left margin
t.pendown()  # Place the pen down to start drawing

# Use a for loop to draw 10 lines
for _ in range(10):
    t.forward(line_length)  # Draw the line
    t.penup()  # Lift the pen to move to the next line without drawing
    t.backward(line_length)  # Move back to the starting point (left margin)
    t.right(90)  # Turn the turtle to face downward
    t.forward(vertical_spacing)  # Move down by the vertical spacing
    t.left(90)  # Turn the turtle back to face the right
    t.pendown()  # Place the pen down to draw the next line

# Close the Turtle graphics window when clicked
turtle.done()