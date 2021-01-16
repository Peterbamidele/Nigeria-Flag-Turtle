import turtle
from turtle import*
 
#screen for output
screen = turtle.Screen()
 
# A turtle Instance
t = turtle.Turtle()
speed(0)
 
# initially penup()
t.penup()
t.goto(-400, 250)
t.pendown()
 
# green Rectangle 
#white rectangle
t.color("green")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)
 
# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()
 
 
# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()
      
turtle.done()