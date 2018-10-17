import turtle


def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(80)


def draw_triangle():
    marko = turtle.Turtle()
    marko.shape("triangle")
    marko.color("green")
    for i in range(3):
        marko.forward(100)
        marko.left(120)


def start_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(8)

    for i in range(36):
        draw_square(brad)
        brad.right(10)
    #draw_circle()
    #draw_triangle()

    window.exitonclick()

start_art()
