import turtle
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
        
def user_interface():
    while True:
        loop = screen.textinput("Geometric Patterns with Straight Lines","Type pattern")
        loop_value = eval(loop)
        while type(loop_value) != tuple:
            loop = screen.textinput("Geometric Patterns with Straight Lines","Type pattern")
            loop_value = eval(loop)
        loop_list = list(loop_value)
        step_any_loop(loop_list)
        restart = screen.textinput("Done","Do you want to type another pattern?").lower()
        while True:
            if restart == "yes":
                refresh()
                break
            elif restart == "no":
                return
            else:
                restart = screen.textinput("Invalid input","Do you want to type another pattern?").lower()
# Call the function
user_interface()


# Hide the turtle and keep the window open
turtle.done()
