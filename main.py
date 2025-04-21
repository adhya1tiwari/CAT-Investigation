import turtle
import re
# Set up the screen
screen = turtle.Screen()
screen.bgcolor("White")

# Set up the pen
pen = turtle.Turtle()
pen.color("Blue")
pen.speed(2)
pen.hideturtle()

def refresh():
    screen.clear()
    pen.penup()
    pen.goto(0,0)
    pen.pendown()

def step_any_loop(list_move):
    initial_position = pen.position()
    initial_heading = pen.heading()
    iteration = 0
    maximum_iterations = 1000
    while True:
        for i in list_move:
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
def is_valid_pattern(s):
    pattern = r'^\(\s*\d+\s*(\s*,\s*\d+\s*)*\)$'
    return bool(re.match(pattern,s))

def user_interface():
    while True:
        loop = screen.textinput("Geometric Patterns with Straight Lines","Type pattern in this format (1,2,3)")
        while True:
            if is_valid_pattern(loop) == True:
                values = loop[1:-1].split(',')
                loop_list = [int(v.strip()) for v in values if v.strip()]
                break
            else:
                loop = screen.textinput("Invalid Input","Type pattern in this format (1,2,3)")
        step_any_loop(loop_list)
        restart = screen.textinput("Done","Do you want to type another pattern?").lower()
        while True:
            if restart == "yes":
                refresh()
                break
            elif restart == "no":
                return
            else:
                restart = screen.textinput("Invalid input: type yes or no","Do you want to type another pattern?").lower()
# Call the function
user_interface()
# Hide the turtle and keep the window open
turtle.done()