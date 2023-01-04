from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def move_counter_clock_dir():
    pen.left(10)


def move_clock_dir():
    pen.right(10)


def clear_screen():
    pen.clear()
    pen.reset()


screen.listen()
screen.onkey(
    fun=move_forwards, key="w"
)  # passing a function move_forwards() inside another function screen.onkey() - this is called Higher order functions
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_clock_dir, key="a")
screen.onkey(fun=move_clock_dir, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()
