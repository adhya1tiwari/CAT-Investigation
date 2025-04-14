import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("White")

# Set up the pen
pen = turtle.Turtle()
pen.color("Blue")
pen.speed(2)

# Define the step_3_loop function
def step_3_loop(first, second, third, sequence):
    list_move = [first, second, third]
    for i in range(sequence):
        for m in list_move:
            pen.forward(m * 10)
            pen.right(90)
# Call the function
step_3_loop(2, 4, 1, 6)

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()