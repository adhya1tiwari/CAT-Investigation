import turtle
import re
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Geometric Patterns with Straight Lines")
root.configure(bg="#f0f0f0") 

canvas = turtle.ScrolledCanvas(master=root)
canvas.pack(fill="both", expand=True, side=tk.LEFT)

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
    screen.clear()
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    feedback_label.config(text="")
    entry.delete(0,tk.END)

def predict_loop(loop_list):
    if len(loop_list) %4 == 0:
        is_xyxy = False
        for i in range(0, len(loop_list) - 3, 4):
            if not (loop_list[i] == loop_list[i + 2] and loop_list[i + 1] == loop_list[i + 3]):
                break
            else:
                is_xyxy = True
        if is_xyxy == True:
            feedback_label.config(text="Loop will be closed", foreground="green")
        else:
            feedback_label.config(text="Loop will go on forever", foreground="red")
    else:
        feedback_label.config(text="Loop will be closed", foreground="green")


def step_any_loop(list_move):
    initial_position = pen.position()
    initial_heading = pen.heading()
    iteration = 0
    while True:
        for i in list_move:
            pen.forward(i*10)
            pen.right(90)
        iteration += 1
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

def is_valid_pattern(s):
    pattern = r'^\(\s*\d+\s*(\s*,\s*\d+\s*)*\)$'
    return bool(re.match(pattern,s))

control_frame = ttk.Frame(main_frame, padding="10", relief="groove", borderwidth=2)
control_frame.pack(side=tk.RIGHT, fill="y", padx=5, pady=5)

title_label = ttk.Label(control_frame, text="Pattern Controls",font="-weight bold")
title_label.pack(pady=5)

instruction_label = ttk.Label(control_frame, text="Enter pattern (e.g., (1,2,3)):")
instruction_label.pack(pady=5)

entry = ttk.Entry(control_frame, width=20)
entry.pack(pady=5)

feedback_label = ttk.Label(control_frame, text="", foreground="blue")
feedback_label.pack(pady=5)

def input_pattern():
        loop = entry.get().strip()
        if is_valid_pattern(loop) == True:
            values = loop[1:-1].split(',')
            loop_list = [int(v.strip()) for v in values if v.strip()]
            predict_loop(loop_list)
            step_any_loop(loop_list)
        else:
            feedback_label.config(text="Invalid input! Use format: (1,2,3)", foreground="red")

clear_button = ttk.Button(control_frame, text="Clear", command=refresh)
clear_button.pack(pady=5)

submit_button = ttk.Button(control_frame, text="Draw Pattern", command=input_pattern)
submit_button.pack(pady=5)

exit_button = ttk.Button(control_frame, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()