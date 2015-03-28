import turtle
myturtle = turtle.Turtle()
mywin = turtle.Screen()

def drawSpiral(turtle, linelen) :
    if linelen > 0 :
        turtle.forward(linelen)
        turtle.right(90)
        drawSpiral(turtle, linelen - 5)

drawSpiral(myturtle, 100)
mywin.exitonclick()
