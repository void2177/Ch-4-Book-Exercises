import turtle

"""PUT YOUR FUNCTIONS HERE"""

def polygon(t, sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)


def triangle(t, length):
    polygon(t=t, sides=3, length=length)

def pie(n, length):
    for i in range(n):
        triangle(t=t, length=length)
        t.right(360/n)

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(1)  # 1 is slow, 10 is fast, 0 is instant
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
pie(5, 25)

# Close the turtle graphics window when clicked
turtle.exitonclick()



