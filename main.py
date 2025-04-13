import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("White")

# Set up the pen
pen = turtle.Turtle()
pen.color("Blue")
pen.speed(2)

# Define the step_3_loop function
# def step_3_loop(first, second, third, sequence):
#     list_move = [first, second, third]
#     for i in range(sequence):
#         for m in list_move:
#             pen.forward(m * 10)
#             pen.right(90)
# pen.forward(20)
# pen.right(90)
# pen.forward(30)
# pen.right(90)
# pen.forward(20)
# pen.right(90)
# pen.forward(30)

def step_any_loop(*args):
    initial_position = pen.position()
    initial_heading = pen.heading()
    iteration = 0
    maximum_iterations = 1000
    while True:
        for i in args:
            pen.forward(i*10)
            pen.right(90)
        iteration += 1
        current_position = pen.position()
        current_heading = pen.heading()
        if (abs(current_position[0]-initial_position[0]) < 0.01 
            and abs(current_position[1]-initial_position[1]) < 0.01 
            and abs(current_heading-initial_heading) < 0.01):
            break
        if iteration == maximum_iterations:
            break
# Call the function
step_any_loop(1,2,3,2,1)
# step_3_loop(2, 4, 1, 6)

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.done()