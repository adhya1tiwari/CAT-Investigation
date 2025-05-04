import turtle
import re
import tkinter as tk
from tkinter import ttk

# GUI window
root = tk.Tk()
root.title("Geometric Patterns with Straight Lines")
root.configure(bg="#f0f0f0") 

#Where the turtle screen is
canvas = turtle.ScrolledCanvas(master=root)
canvas.pack(fill="both", expand=True, side=tk.LEFT)

#Where the elements of the window are nested
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Set up the screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("White")

# Set up the pen
pen = turtle.RawTurtle(screen)
pen.color("Blue")
pen.speed(2)
pen.hideturtle()

def refresh():
    """
    Clears the turtle screen and puts the pen back to the origin.
    The entry field and feedback label is cleared as well.
    """
    screen.clear()
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    feedback_label.config(text="")
    entry.delete(0,tk.END)

def predict_loop(loop_list):
    """
    Predicts whether if the loop will be closed or not or the shape will be quadrilateral.
        1. It does this by checking whether if the length of the loop is divisible by 4.
        2. If that is the case then it would see whether if the 1st and 3rd as well as 2nd and 4th length is the same.
          If points 1 and 2 are correct then the shape will be closed and quadrilateral.
    If point 1 is only true then the loop will go on forever.
    If point one is not true then go onto the next analysis.

        1. Is the length of the loop_list 2 or 1
        2. Are all of the values in the loop are the same

    If point 1 or 2 are correct then the loop will be closed and quadrilateral
    Else the loop will be closed.
    """
    if len(loop_list) %4 == 0:
        is_xyxy = False
        for i in range(0, len(loop_list) - 3, 4):
            if not (loop_list[i] == loop_list[i + 2] and loop_list[i + 1] == loop_list[i + 3]):
                break
            else:
                is_xyxy = True
        if is_xyxy == True:
            feedback_label.config(text="Loop will be closed (quadrilateral)", foreground="green")
        else:
            feedback_label.config(text="Loop will go on forever", foreground="red")
    else:
        if len(loop_list) ==2 or len(loop_list) == 1:
            feedback_label.config(text="Loop will be closed (quadrilateral)", foreground="green")
        elif len(set(loop_list)) <= 1:
            feedback_label.config(text="Loop will be closed (quadrilateral)", foreground="green")
        else:
            feedback_label.config(text="Loop will be closed", foreground="green")

def step_any_loop(list_move):
    """
    This function loops over the lengths of list_move infinitely, 
    unless if it touches the edge of the screen or if the pen goes back to the initial position.
    """
    initial_position = pen.position()
    initial_heading = pen.heading()
    while True:
        for i in list_move:
            pen.forward(i*10)
            pen.right(90)
        current_position = pen.position()
        current_heading = pen.heading()
        max_x = screen.window_width() / 2 - 10
        max_y = screen.window_height() / 2 - 10
        if (abs(current_position[0]) >= max_x or 
            abs(current_position[1]) >= max_y):
            break
        if (abs(current_position[0]-initial_position[0]) < 0.01 
            and abs(current_position[1]-initial_position[1]) < 0.01 
            and abs(current_heading-initial_heading) < 0.01):
            break
    feedback_label.config(text="Done", foreground="blue")
def is_valid_pattern(s):
    """
    I have optimised the python code by making a new function that returns a Boolean. 
    The function is_valid_pattern uses the module re or the regular expression module to validate the pattern 
    inputted by the user. The function match helps to match the raw string, which has the rules 
    of what should the string be like. It then returns a Boolean (True or False) and then returns to the function. 
    """
    pattern = r'^\(\s*\d+\s*(\s*,\s*\d+\s*)*\)$'
    return bool(re.match(pattern,s))

#Holds all pattern controls
control_frame = ttk.Frame(main_frame, padding="10", relief="groove", borderwidth=2)
control_frame.pack(side=tk.RIGHT, fill="y", padx=5, pady=5)

#Title
title_label = ttk.Label(control_frame, text="Pattern Controls",font="-weight bold")
title_label.pack(pady=5)

#User intructions
instruction_label = ttk.Label(control_frame, text="Enter pattern (e.g., (1,2,3)):")
instruction_label.pack(pady=5)

#Where to enter pattern
entry = ttk.Entry(control_frame, width=20)
entry.pack(pady=5)

#configures when certain conditions occur
feedback_label = ttk.Label(control_frame, text="", foreground="blue")
feedback_label.pack(pady=5)

def input_pattern():
        """
        It takes the value from the entry and then validated if it is a valid loop by using the is_valid_pattern function.
        Then turns the pattern into a list and calls the predict_loop and step_any_loop function with the list made
        as the argument. If the pattern is not valid then the feedback label will tell the user that their input was invalid.
        """
        loop = entry.get().strip()
        if is_valid_pattern(loop) == True:
            values = loop[1:-1].split(',')
            loop_list = [int(v.strip()) for v in values if v.strip()]
            predict_loop(loop_list)
            step_any_loop(loop_list)
        else:
            feedback_label.config(text="Invalid input! Use format: (1,2,3)", foreground="red")

#Calls refresh function
clear_button = ttk.Button(control_frame, text="Clear", command=refresh)
clear_button.pack(pady=5)

#Calls input_pattern function
submit_button = ttk.Button(control_frame, text="Draw Pattern", command=input_pattern)
submit_button.pack(pady=5)

#Exits the program
exit_button = ttk.Button(control_frame, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()