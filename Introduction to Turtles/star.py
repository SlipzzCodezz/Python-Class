import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.title("Project turtle")
screen.bgcolor("grey")

board = turtle.Turtle()
for i in range(5):
    board.forward(250) 
    board.right(144)


turtle.done()