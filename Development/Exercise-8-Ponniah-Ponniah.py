import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the line length and vertical spacing
line_length = 150
vertical_spacing = 10

# Set the length of solid and gap segments for dashed lines
solid_segment = 10
gap_segment = 5

# Move the turtle to the starting position
t.penup()
t.goto(-line_length / 2, 0)  # Move to the left margin
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

# Use a for loop to draw 20 lines
for i in range(20):
    if i % 2 == 0:  # Odd lines (0-indexed i is even)
        draw_solid_line()
    else:  # Even lines
        draw_dashed_line()
    
    # Move to the starting position of the next line
    t.penup()  # Lift the pen to move without drawing
    t.backward(line_length)  # Move back to the left margin
    t.right(90)  # Turn the turtle downwards
    t.forward(vertical_spacing)  # Move down to the next line
    t.left(90)  # Turn the turtle right to face the right again
    t.pendown()  # Place the pen down to draw the next line

# Close the Turtle graphics window when clicked
turtle.done()
