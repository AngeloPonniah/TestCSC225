import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the line length and horizontal spacing
line_length = 150
horizontal_spacing = 10

# Set the length of solid and gap segments
solid_segment = 10
gap_segment = 5

# Move the turtle to the starting position
t.penup()  # Lift the pen to avoid drawing while moving
t.goto(0, line_length / 2)  # Move the turtle to the top margin
t.pendown()  # Start drawing

# Use a for loop to draw 10 dashed vertical lines
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
    t.backward(line_length)  # Move back to the top margin
    t.right(90)  # Turn the turtle to the right
