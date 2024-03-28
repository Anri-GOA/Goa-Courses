from turtle import *
import turtle
# We want to paint a house

bgcolor("white")

speed(50)

title("Goa day 7 homework castle and 2 sticmans")

pensize(5)
pencolor("gold")
#Drawing a suare
goto(0,0)
shape("turtle")

for i in range(4):
    fd(200)  
    lt(90)  


#drawing a door using Loop
forward(70)
color("yellow")
pencolor("orange")
begin_fill()
left(90)
for i in range(1):
    fd(120)
    rt(90)
forward(60)
for i in range(1):
    rt(90)
    fd(120)
end_fill()

   
#Drawing 1 WInodw
color("orange")
pencolor("black")
penup()
goto(30,160)
begin_fill()
for i in range(4):
    lt(90)
    fd(30)
end_fill()

#Drawing 2 Window
color("orange")
pencolor("black")
penup()
goto(140,160)
begin_fill()
for i in range(1):
    lt(180)
    fd(30)
for i in range(4):
    rt(90)
    fd(30)

end_fill()

#Drawing Roof

color=("red")
pencolor("gold")
penup()
goto(200,200)
begin_fill()
lt(400)
fd(150)
lt(100)
fd(150)

t = turtle.Turtle

#ადამიანი 1


#თავი


penup()
goto(-20,-60)
pendown()


fillcolor = "pink"
forward(2.5)
right(90)
forward(2.5)
left(90)
forward(2.5)
forward(2.5)
right(90)
forward(2.5)
left(90)
forward(2.5)
forward(2.5)
right(90)
forward(2.5)
left(90)
forward(2.5)
forward(2.5)
right(90)
forward(2)
left(90)


forward(7.5)


left(90)
forward(2.5)
right(90)
forward(2.5)
forward(2.5)
left(90)
forward(2.5)
right(90)
forward(5)
left(90)
forward(2.5)
right(90)
forward(2.5)
forward(2.5)
left(90)
forward(2.5)
right(90)
forward(2.5)
left(90)


forward(25)


left(90)
forward(2.5)
right(90)
forward(2.5)
left(90)
forward(2.5)
forward(2.5)
right(90)
forward(2.5)
left(90)
forward(5)
right(90)
forward(2.5)
left(90)
forward(5)
right(90)
forward(2.5)
left(90)

forward(7.5)


left(90)
forward(2.5)
right(90)
forward(2.5)
forward(2.5)
left(90)
forward(2.5)
right(90)
forward(5)
left(90)
forward(2.5)
right(90)
forward(5)
left(90)
forward(2.5)
right(90)
forward(2.5)
left(90)


forward(25)
left(90)

#ტანი
fillcolor = "black"
right(135)
forward(8)
left(45)
forward(6)
right(45)

forward(2.5)
left(90)
forward(2.5)
right(90)
forward(2.5)
forward(2.5)
left(90)
forward(2.5)
right(90)
forward(2.5)

right(45)

forward(60)


fillcolor = "pink"

forward(3)

right(90)
forward(2)
left(90)
forward(7)
right(90)
forward(2)
left(90)
forward(7)
right(90)
forward(2)
right(90)

forward(5)
left(90)
forward(2)
right(90)
forward(3)
left(90)
forward(2.5)
right(90)
forward(6)



color("black")
forward(50)


left(90)
forward(2)
right(90)
forward(1)
left(90)
forward(2)
right(90)
forward(1)


left(180)
forward(45)


right(90)
forward(40)


right(90)
forward(45)


left(90)
forward(7)
right(90)
forward(3)
left(90)
forward(3)
right(90)
forward(2)
left(90)
forward(4)
right(90)
forward(2)
left(90)
forward(2)
right(90)
forward(6)
left(90)
forward(2)
right(90)
forward(16)
right(90)
forward(2)
left(90)
forward(14)

color("pink")
forward(6)
right(90)
forward(1.5)
left(90)
forward(3.5)
right(90)
forward(1.5)
right(90)
forward(1.5)
right(90)
forward(1.5)
left(90)
forward(2)
left(90)
forward(2.5)
right(90)
forward(13)
color("black")
forward(15)
left(90)
forward(7)
right(90)
forward(6)
left(90)
forward(10)
left(90)
forward(2)
right(90)
forward(2)
left(90)
forward(2)
right(90)
forward(2)




#შარვალი


color("brown")
penup()
goto(-53,-120)
pendown()
right(90)

forward(55)
left(90)
forward(15)
left(90)
forward(45)
right(90)
forward(10)
right(90)
forward(45)
left(90)
forward(15)
left(90)
forward(55)






#ყვავილები

penup()
goto(-40,-280)
pendown()

color("green")

forward(15)
left(90)


begin_fill()
color("red")

forward(7.5)
right(90)
forward(5)
left(90)
forward(5)
right(90)
forward(10)
right(90)
forward(5)
left(90)
forward(5)
right(90)
forward(15)
right(90)
forward(5)
left(90)
forward(5)
right(90)
forward(10)
right(90)
forward(5)
left(90)
forward(5)
right(90)
forward(7.5)
right(90)

end_fill()
exitonclick()