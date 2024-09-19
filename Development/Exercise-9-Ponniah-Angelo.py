import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the line length and horizontal spacing
line_length = 150
horizontal_spacing = 10

# Set the length of solid and gap segments for dashed lines
solid_segment = 10
gap_segment = 5

# Move the turtle to the starting position
t.penup()
t.goto(0, line_length / 2)  # Move to the top margin
t.pendown()

# Function to draw a solid line
def draw_solid_line():
    t.forward(line_length)

# Function to draw a dashed line
def draw_dashed_line():
    dash_count = line_length // (solid_segment + gap_segment)
    for _ in range(dash_count):
        t.forward(solid_segment)  # Draw the solid segment
        t.penup()  # Lift the pen to create a gap
        t.forward(gap_segment)  # Move forward without drawing
        t.pendown()  # Put the pen down to draw the next solid segment

# Use a for loop to draw 20 vertical lines
for i in range(20):
    t.right(90)  # Rotate the turtle to face downward
    if i % 2 == 0:  # Odd lines (0-indexed i is even)
        draw_solid_line()
    else:  # Even lines
        draw_dashed_line()

    # Move to the starting position of the next line
    t.penup()  # Lift the pen to move without drawing
    t.backward(line_length)  # Move back to the top margin
    t.left(90)  # Rotate to face right (horizontal direction)
    t.forward(horizontal_spacing)  # Move right by the horizontal spacing
    t.pendown()  # Place the pen down to draw the next line

# Close the Turtle graphics window when clicked
turtle.done()
