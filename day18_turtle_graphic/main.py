import turtle as t
import random

""" pen = Turtle()
pen.shape("arrow")
pen.color("#778899")

screen = Screen()
screen.bgcolor("#7FFFD4")
screen.exitonclick() """

t.colormode(255)
pen = t.Turtle()
pen.shape("arrow")
pen.color("black")
pen.width(0)
pen.speed(0)

screen = t.Screen()
screen.bgcolor("#7FFFD4")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Challenge-1: Draw a Square.
""" for _ in range(4):
    pen.forward(100)
    pen.right(90)
    
screen.exitonclick()
"""

# Challenge-2: Draw a dashed line.
""" pen.up()
pen.setx(-700)

for _ in range(50):
    pen.down()
    pen.forward(10)
    pen.up()
    pen.forward(10) 
    
    
screen.exitonclick()"""

# Challenge-3: Drawing different shapes.
""" colors = ["CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",]
for sides in range(3, 11):
    angle = 360 / sides
    pen.color(random.choice(colors))
    for t in range(sides):
        pen.forward(100)
        pen.right(angle)

screen.exitonclick() """

# Challenge-4: Generate a Random Walk.
""" colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
list_of_angles = [0, 90, 180, 270]
while True:
    pen.forward(30)
    pen.color(random.choice(colors))
    pen.setheading(random.choice(list_of_angles))
screen.exitonclick() """

# or - Completely Random color

""" list_of_angles = [0, 90, 180, 270]
while True:
    pen.forward(30)
    pen.color(random_color())
    pen.setheading(random.choice(list_of_angles))
screen.exitonclick() """

# Challenge-5: Generate random RGB colors.
""" for n in range(72):
    pen.color(random_color())
    pen.circle(100)
    pen.left(5)
screen.exitonclick() """

# or
def draw_spirograph(size_of_gap):
    for n in range(int(360 / size_of_gap)):
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + size_of_gap)


draw_spirograph(5)
screen.exitonclick()
