import turtle
from multiprocessing.util import sub_debug

"""PUT YOUR FUNCTIONS HERE"""

def parallelogram(sidea, sideb, angle):
    for i in range(2):
        t.forward(sidea)
        t.left(angle)
        t.forward(sideb)
        t.left(180-angle)

def rhombus(length, angle):
    parallelogram(sidea=length, sideb=length, angle)



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
##parallelogram(80, 40, 45)
rhombus(50, 45)

# Close the turtle graphics window when clicked
turtle.exitonclick()