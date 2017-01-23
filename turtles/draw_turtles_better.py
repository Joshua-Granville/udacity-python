import turtle

def draw_square(turtleName):
    for i in range(1,5):
        turtleName.forward(100)
        turtleName.right(90)

def draw_circle_of_squares(turletodraw):
    for i in range(1,36):
        draw_square(turletodraw)
        turletodraw.right(10)
    
def draw_art():
    #make the window
    window = turtle.Screen()
    window.bgcolor("red")

    #create brad the square circle guy
    brad = turtle.Turtle()
    brad.speed(10)
    brad.color("green")
    brad.shape("turtle")

    draw_circle_of_squares(brad)

    #create angie the circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #create Josh the triangle
    josh = turtle.Turtle()
    josh.shape("turtle")
    josh.color("purple")
    josh.forward(100)
    josh.right(90)
    josh.forward(100)
    josh.right(135)
    josh.forward(140)


    window.exitonclick()
  
draw_art()
