import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the line length and the horizontal spacing between lines
line_length = 50
horizontal_spacing = 10

# Move the turtle to the starting position
t.penup()  # Lift the pen so it doesn't draw while moving to the starting position
t.goto(0, line_length / 2)  # Move the turtle to the top margin
t.pendown()  # Place the pen down to start drawing

# Use a for loop to draw 10 vertical lines
for _ in range(10):
    t.right(90)  # Face the turtle downwards
    t.forward(line_length)  # Draw the vertical line
    t.penup()  # Lift the pen to move to the next line without drawing
    t.backward(line_length)  # Move back to the top margin
    t.left(90)  # Face the turtle to the right
    t.forward(horizontal_spacing)  # Move right by the horizontal spacing
    t.pendown()  # Place the pen down to draw the next line

# Close the Turtle graphics window when clicked
turtle.done()
