import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the line length and vertical spacing
line_length = 150
vertical_spacing = 10

# Set the length of solid and gap segments
solid_segment = 10
gap_segment = 5

# Move the turtle to the starting position
t.penup()  # Lift the pen to avoid drawing while moving
t.goto(-line_length / 2, 0)  # Move the turtle to the left vertical margin
t.pendown()  # Start drawing

# Use a for loop to draw 10 dashed horizontal lines
for _ in range(10):
    # Draw one dashed line
    dash_count = line_length // (solid_segment + gap_segment)  # Number of dashes
    for _ in range(dash_count):
        t.forward(solid_segment)  # Draw the solid segment
        t.penup()  # Lift the pen to create a gap
        t.forward(gap_segment)  # Move forward without drawing
        t.pendown()  # Put the pen down to draw the next solid segment

    # Move to the starting position of the next line
    t.penup()  # Lift the pen to move without drawing
    t.backward(line_length)  # Move back to the left margin
    t.right(90)  # Turn the turtle downwards
    t.forward(vertical_spacing)  # Move down to the next line
    t.left(90)  # Turn the turtle to the right to start drawing the next line
    t.pendown()  # Place the pen down to draw the next dashed line

# Close the Turtle graphics window when clicked
turtle.done()
