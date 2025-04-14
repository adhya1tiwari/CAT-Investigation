import turtle
screen=turtle.Screen()
screen.bgcolor("White")
# create a turtle object to draw with
pen=turtle.Turtle()

# set colour of the turtle
pen.speed()
pen.color("Blue")

#draw line
pen.forward(20)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(30)

#hide turtle
pen.hideturtle()
turtle.done()