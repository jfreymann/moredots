from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed("fastest")
t.pensize(1)


rgb_tuple = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

def draw_dots(num_of_rows):
    for i in range(num_of_rows):
        for i in range(10):
            print(t.pos())
            t.dot(20, random.choice(rgb_tuple))
            t.penup()
            t.fd(50)
        print(t.pos())
        print(t.ycor())
        t.goto(0, t.ycor() + 50)
    t.hideturtle()

draw_dots(10)
screen.exitonclick()
