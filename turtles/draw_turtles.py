import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.color("green")
    brad.shape("turtle")

    loop_start = 0
    loop_end = 4

    while (loop_start < loop_end):
        brad.forward(100)
        brad.right(90)
        loop_start = loop_start + 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    josh = turtle.Turtle()
    josh.shape("turtle")
    josh.color("purple")
    josh.forward(100)
    josh.right(90)
    josh.forward(100)
    josh.right(135)
    josh.forward(140)


    window.exitonclick()
  
draw_square()
