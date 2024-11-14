from turtle import *
speed(50)
width(5)

color("purple")
begin_fill()
forward(200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward (200)
left(90)
forward (70)
end_fill()


color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15, 130)
pendown()

color("blue")
begin_fill()
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()
goto(180, 130)
pendown()

color("blue")
begin_fill()
setheading(90) 
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


exitonclick()



