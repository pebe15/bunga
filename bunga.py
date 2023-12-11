import turtle
import tkinter

turtle.bgcolor("black")
turtle.speed(50)
turtle.hideturtle()

colors = ["pink","#FFFDD0","#5F9EA0"]

for i in range(120):
    for bunga in colors:
        turtle.color(bunga)
        turtle.circle(200-i, 100)
        turtle.lt(90)
        turtle.circle(200-1, 100)
        turtle.end_fill()
turtle.mainloop()