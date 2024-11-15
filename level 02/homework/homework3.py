# # 3) პითონში turtle ის გამოყენებით ააგეთ სასახლე რაც შეიძლება დახვეწილი და ლამაზი ვნახოთ როგორი გამოგივათ

from turtle import *
speed(50)
width(7)

penup()
goto(-250, -90) 
setup(width=700, height=900)  


color("purple")
begin_fill()
forward(500)
left(90)
forward(220)
left(90)
forward(500)
left(90)
forward(220)
end_fill()


penup()
goto( -70, 15) 
pendown()


color("darkcyan")  # Door color
begin_fill()
forward(100)  
left(90)
forward(150)  
left(90)
forward(100)
left(90)
forward(150)
end_fill()


penup()
goto(-160, 35)
pendown()


color("orangered")
begin_fill()
forward(65)
left(-90)
forward(65)
left(-90)
forward(65)
left(-90)
forward(65)
end_fill()

penup()
goto(220, 100)
pendown()

# Draw windows
color("orangered")
begin_fill()
forward(65)
left(-90)
forward(65)
left(-90)
forward(65)
left(-90)
forward(65)
end_fill()

penup()
goto(-250, 135)
pendown()
color("red")
begin_fill()
right(-90)
forward(100)
right(45)
forward(100)
right(90)
forward(100)
right(45)
forward(100)
left(-90)
forward(140)
end_fill()

penup()
goto(-210, 180)
pendown()

color("green")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(-179, 310)
pendown()

color("blue")
begin_fill()
right(90)
forward(35)
right(110)
forward(40)
right(150)
forward(35)
end_fill()

penup()
goto(247, 135)
pendown()

color("red")
begin_fill()
right(10)
forward(120)
right(90)
forward(100)
right(45)
forward(100)
right(100)
forward(90)
right(35)
forward(98)
end_fill()

exitonclick()








