import turtle
#create turtle screen and set background colour
screen=turtle.Screen()
screen.bgcolor("White")
# create a turtle object to draw with
pen=turtle.Turtle()
# set colour of the turtle
pen.color("Blue")
# set speed of the turtle
pen.speed(2)
def step_3_loop(first,second,third):
    list_move = [second,third]
    while pen.position() != (0,0):
        for item in list_move:
            pen.forward(item*10)
            pen.right(90)
step_3_loop(2,4,1)
# # draw line
# pen.forward(20)
# pen.right(90)
# pen.forward(30)
# pen.right(90)
# pen.forward(20)
# pen.right(90)
# pen.forward(30)
# #hide turtle
pen.hideturtle()
#keep turtle window open when done
turtle.done()