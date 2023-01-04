from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(10)


screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()
