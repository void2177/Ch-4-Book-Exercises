import turtle

"""PUT YOUR FUNCTIONS HERE"""

def rhombus(length, angle):
    for i in range(2):
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(180-angle)



# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
rhombus(100, 45)

# Close the turtle graphics window when clicked
turtle.exitonclick()