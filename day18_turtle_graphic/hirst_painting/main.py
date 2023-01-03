""" # Following code block is used to generate color list of RGB tuple values.

import colorgram


rgb_colors = []
colors = colorgram.extract(".\day18_turtle_graphic\hirst_painting\image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors) """
# [x]TODO-1: Painting should be in frame of 10x10 rows of spots
# [x]TODO-2: each dots should be 20 in size & space apart by 50 in size

import turtle
import random

# list extracted from the image.
color_list = [
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209),
]


def draw(pen):
    """Draws dots & leaves 50 spaces for next dot

    Args:
        pen (turtle): turtle object
    """
    pen.dot(20, random.choice(color_list))
    pen.up()
    pen.fd(50)
    pen.down()


def set_position(pen, y):
    """moves turtle to specific location without drawing any lines(X Co-ordinate is fixed.(-200))

    Args:
        pen (_type_): turtle object
        y (int): y co-ordinate value
    """
    pen.up()
    pen.setposition(-200, y)
    pen.down()


def main():
    y = -200  # y default co-ordinate
    turtle.colormode(255)  # to use custom RGB colors

    # Turtle definition & specs
    pen = turtle.Turtle()
    pen.shape("arrow")
    pen.speed(0)
    pen.hideturtle()
    set_position(pen, y)  # default position

    # Screen introduction & specs
    screen = turtle.Screen()
    screen.bgcolor("#DDF2FD")

    # outer loop for rows
    for j in range(10):
        # inner loop for columns or dots in a row
        for i in range(10):
            draw(pen)
        # distance between rows is also 50
        y += 50
        set_position(pen, y)

    screen.exitonclick()


if __name__ == "__main__":
    main()
