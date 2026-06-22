import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.title("Project turtle")
screen.bgcolor("grey")

board = turtle.Turtle()
for i in range(1,4):
    board.forward(200)
    board.left(120)


turtle.done()