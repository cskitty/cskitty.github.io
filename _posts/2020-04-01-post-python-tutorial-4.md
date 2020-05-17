---
title: "Introduction to Python Lesson 4: Turtle Graphics"
categories:
  - Tutorials
tags:
  - Python
---

## Introduction to Python Lesson 4: Turtle Graphics

 In this tutorial we will learn how to draw a graph using Python Turtle library.

 “Turtle” is a python feature like a drawing board, which lets you command a turtle to draw all over it!
You can use functions like turtle.forward(...) and turtle.left(...) which can move the turtle around.

### Simple movement with turtle, draw a line
As a starting point, you can draw a line using python turtle functions: there are four steps involved:

1. Import the turtle module
2. Create a turtle to control and assign a name to it
3. Draw things.   
   1. Draw more things with forward(...) or backward(...)
   2. Draw more things.   
4. Run turtle.done() after finishing.

Copy the code below, open the [Python Playground](http://starcoder.org/playground/), paste the code and run it.

{% highlight python linenos %}
# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. call it alice
alice = turtle.Turtle()

# Step 3: Move in the direction Alice's facing for 50 pixels
alice.forward(100)
# Step 4: We're done!
turtle.done()
{% endhighlight %}

### Draw a square

We can use Lines are boring. We can rotate the turtle in order to draw more interesting figures.

{% highlight python linenos %}
import turtle
alice = turtle.Turtle()

alice.forward(100)   # Move forward 50 pixels
alice.right(90)     # Rotate clockwise by 90 degrees

alice.forward(100)
alice.right(90)

alice.forward(100)
alice.right(90)

alice.forward(100)
alice.right(90)

turtle.done()
{% endhighlight %}


### Draw a star


{% highlight python linenos %}
import turtle

star = turtle.Turtle()

for i in range(5):
    star.forward(50)
    star.right(144)

turtle.done()
{% endhighlight %}

### Draw a hexagon

{% highlight python linenos %}
import turtle

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
{% endhighlight %}

### Changing line color


{% highlight python linenos %}
import turtle

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time

painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()
{% endhighlight %}

### Spiraling star


{% highlight python linenos %}
import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()
{% endhighlight %}

### Drawing circles

The code below will draw a circle of radius 50units.

{% highlight python linenos %}
import turtle
t = turtle.Turtle()

t.circle(50)
{% endhighlight %}

More than one circle having one point of intersection is called tangent circles.
The code below draws tangent Circles in Python turtle.

{% highlight python linenos %}
#Program to draw tangent circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(10):
  t.circle(10*i)
{% endhighlight %}

Circles with varying radius are called spiral.
The code below draws spiral circles in Python turtle.


{% highlight python linenos %}
#Program to draw spiral circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(30):
  t.circle(10+i, 45)
{% endhighlight %}

Circles with different radii having a common center are called concurrent circles.


{% highlight python linenos %}
#Program to draw concentric circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(10):
  t.circle(10*i)
  t.up()
  t.sety((10*i)*(-1))
  t.down()
{% endhighlight %}

### Turtle Olympics


{% highlight python linenos %}
import turtle
myTurtle = turtle.Turtle()

myTurtle.circle(50)
myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)
myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
turtle.getscreen()._root.mainloop()

turtle.done()
{% endhighlight %}


### Turtle's House


{% highlight python linenos %}
# Create a scene with a house, a tree, and a sun
# Based on the picture at http://dragonometry.net/blog/?p=566
# copied from https://trinket.io/python/8bfa7a2f2a

import turtle
import math

# Set the background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create our turtle
george = turtle.Turtle()
george.color("black")
george.shape("turtle")
george.speed(10)

# Define a funtion to draw and fill a rectangle with the given
# dimensions and color
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()

# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color.  This
# is used to create a roof shape.
def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()

# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()

# Define a function to draw four sun rays of the given length,
# for the sun of the given radius.  The turtle starts in the
# center of the circle.
def drawFourRays(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)

# Draw and fill the front of the house
george.penup()
george.goto(-150, -120)
george.pendown()
drawRectangle(george, 100, 110, "blue")

# Draw and fill the front door
george.penup()
george.goto(-120, -120)
george.pendown()
drawRectangle(george, 40, 60, "lightgreen")

# Front roof
george.penup()
george.goto(-150, -10)
george.pendown()
drawTriangle(george, 100, "magenta")

# Side of the house
george.penup()
george.goto(-50, -120)
george.pendown()
drawParallelogram(george, 60, 110, "yellow")

# Window
george.penup()
george.goto(-30, -60)
george.pendown()
drawParallelogram(george, 20, 30, "brown")

# Side roof
george.penup()
george.goto(-50, -10)
george.pendown()
george.fillcolor("orange")
george.begin_fill()
george.left(30)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(75)
george.forward(60)
george.left(105)
george.forward(100 / math.sqrt(2))
george.left(45)
george.end_fill()

# Tree base
george.penup()
george.goto(100, -130)
george.pendown()
drawRectangle(george, 20, 40, "brown")

# Tree top
george.penup()
george.goto(65, -90)
george.pendown()
drawTriangle(george, 90, "lightgreen")
george.penup()
george.goto(70, -45)
george.pendown()
drawTriangle(george, 80, "lightgreen")
george.penup()
george.goto(75, -5)
george.pendown()
drawTriangle(george, 70, "lightgreen")

# Sun
george.penup()
george.goto(55, 110)
george.fillcolor("yellow")
george.pendown()
george.begin_fill()
george.circle(24)
george.end_fill()

# Sun rays
george.penup()
george.goto(55, 134)
george.pendown()
drawFourRays(george, 25, 24)
george.right(45)
drawFourRays(george, 15, 24)
george.left(45)

# Put down some labels
george.color("black")
george.penup()
george.goto(-150, 70)
george.pendown()
george.write("House", None, None, "14pt bold")
george.penup()
george.goto(150, -150)
george.pendown()
george.write("Tree", None, None, "14pt bold")
george.penup()
george.goto(130, 150)
george.pendown()
george.write("Sun", None, None, "14pt bold")

# Bring the turtle down to the front door, and we're done!
george.penup()
george.goto(-100, -150)
george.left(90)

{% endhighlight %}



### Guess What will You See After Running the Program ?

Paste the code below to playground and run it :)   Original author [Jack Dong](https://github.com/PerpetualSmile/Python-Painting-Doraemon/blob/master/Pikachu.py)

{% highlight python linenos %}
import turtle

t = turtle.Turtle()

def noTrace_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def leftEye( x, y):
    noTrace_goto(x, y)
    t.seth(0)
    t.fillcolor('#333333')
    t.begin_fill()
    t.circle(22)
    t.end_fill()

    noTrace_goto(x, y + 10)
    t.fillcolor('#000000')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    noTrace_goto(x + 6, y + 22)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def rightEye( x, y):
    noTrace_goto(x, y)
    t.seth(0)
    t.fillcolor('#333333')
    t.begin_fill()
    t.circle(22)
    t.end_fill()

    noTrace_goto(x, y + 10)
    t.fillcolor('#000000')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    noTrace_goto(x - 6, y + 22)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def mouth( x, y):
    noTrace_goto(x, y)

    t.fillcolor('#88141D')
    t.begin_fill()

    l1 = []
    l2 = []
    t.seth(190)
    a = 0.7
    for i in range(28):
        a += 0.1
        t.right(3)
        t.fd(a)
        l1.append(t.position())

    noTrace_goto(x, y)

    t.seth(10)
    a = 0.7
    for i in range(28):
        a += 0.1
        t.left(3)
        t.fd(a)
        l2.append(t.position())

    t.seth(10)
    t.circle(50, 15)
    t.left(180)
    t.circle(-50, 15)

    t.circle(-50, 40)
    t.seth(233)
    t.circle(-50, 55)
    t.left(180)
    t.circle(50, 12.1)
    t.end_fill()

    noTrace_goto(17, 54)
    t.fillcolor('#DD716F')
    t.begin_fill()
    t.seth(145)
    t.circle(40, 86)
    t.penup()
    for pos in reversed(l1[:20]):
        t.goto(pos[0], pos[1] + 1.5)
    for pos in l2[:20]:
        t.goto(pos[0], pos[1] + 1.5)
    t.pendown()
    t.end_fill()

    noTrace_goto(-17, 94)
    t.seth(8)
    t.fd(4)
    t.back(8)

def leftCheek( x, y):
    turtle.tracer(False)
    noTrace_goto(x, y)
    t.seth(300)
    t.fillcolor('#DD4D28')
    t.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.lt(3)
            t.fd(a)
        else:
            a += 0.05
            t.lt(3)
            t.fd(a)
    t.end_fill()
    turtle.tracer(True)

def rightCheek( x, y):
    turtle.tracer(False)
    noTrace_goto(x, y)
    t.seth(60)
    t.fillcolor('#DD4D28')
    t.begin_fill()
    a = 2.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.lt(3)
            t.fd(a)
        else:
            a += 0.05
            t.lt(3)
            t.fd(a)
    t.end_fill()
    turtle.tracer(True)

def colorLeftEar( x, y):
    noTrace_goto(x, y)
    t.fillcolor('#000000')
    t.begin_fill()
    t.seth(330)
    t.circle(100, 35)
    t.seth(219)
    t.circle(-300, 19)
    t.seth(110)
    t.circle(-30, 50)
    t.circle(-300, 10)
    t.end_fill()

def colorRightEar( x, y):
    noTrace_goto(x, y)
    t.fillcolor('#000000')
    t.begin_fill()
    t.seth(300)
    t.circle(-100, 30)
    t.seth(35)
    t.circle(300, 15)
    t.circle(30, 50)
    t.seth(190)
    t.circle(300, 17)
    t.end_fill()

def body():
    t.fillcolor('#F6D02F')
    t.begin_fill()
    # right face
    t.penup()
    t.circle(130, 40)
    t.pendown()
    t.circle(100, 105)
    t.left(180)
    t.circle(-100, 5)

    # right ear
    t.seth(20)
    t.circle(300, 30)
    t.circle(30, 50)
    t.seth(190)
    t.circle(300, 36)

    # upper face
    t.seth(150)
    t.circle(150, 70)

    # left ear
    t.seth(200)
    t.circle(300, 40)
    t.circle(30, 50)
    t.seth(20)
    t.circle(300, 35)
    # print(t.pos())

    # left face
    t.seth(240)
    t.circle(105, 95)
    t.left(180)
    t.circle(-105, 5)

    # left hand
    t.seth(210)
    t.circle(500, 18)
    t.seth(200)
    t.fd(10)
    t.seth(280)
    t.fd(7)
    t.seth(210)
    t.fd(10)
    t.seth(300)
    t.circle(10, 80)
    t.seth(220)
    t.fd(10)
    t.seth(300)
    t.circle(10, 80)
    t.seth(240)
    t.fd(12)
    t.seth(0)
    t.fd(13)
    t.seth(240)
    t.circle(10, 70)
    t.seth(10)
    t.circle(10, 70)
    t.seth(10)
    t.circle(300, 18)

    t.seth(75)
    t.circle(500, 8)
    t.left(180)
    t.circle(-500, 15)
    t.seth(250)
    t.circle(100, 65)

    # left foot
    t.seth(320)
    t.circle(100, 5)
    t.left(180)
    t.circle(-100, 5)
    t.seth(220)
    t.circle(200, 20)
    t.circle(20, 70)

    t.seth(60)
    t.circle(-100, 20)
    t.left(180)
    t.circle(100, 20)
    t.seth(300)
    t.circle(10, 70)

    t.seth(60)
    t.circle(-100, 20)
    t.left(180)
    t.circle(100, 20)
    t.seth(10)
    t.circle(100, 60)

    # left
    t.seth(180)
    t.circle(-100, 10)
    t.left(180)
    t.circle(100, 10)
    t.seth(5)
    t.circle(100, 10)
    t.circle(-100, 40)
    t.circle(100, 35)
    t.left(180)
    t.circle(-100, 10)

    # right foot
    t.seth(290)
    t.circle(100, 55)
    t.circle(10, 50)

    t.seth(120)
    t.circle(100, 20)
    t.left(180)
    t.circle(-100, 20)

    t.seth(0)
    t.circle(10, 50)

    t.seth(110)
    t.circle(100, 20)
    t.left(180)
    t.circle(-100, 20)

    t.seth(30)
    t.circle(20, 50)

    t.seth(100)
    t.circle(100, 40)

    # right body
    t.seth(200)
    t.circle(-100, 5)
    t.left(180)
    t.circle(100, 5)
    t.left(30)
    t.circle(100, 75)
    t.right(15)
    t.circle(-300, 21)
    t.left(180)
    t.circle(300, 3)

    # right hand
    t.seth(43)
    t.circle(200, 60)

    t.right(10)
    t.fd(10)

    t.circle(5, 160)
    t.seth(90)
    t.circle(5, 160)
    t.seth(90)

    t.fd(10)
    t.seth(90)
    t.circle(5, 180)
    t.fd(10)

    t.left(180)
    t.left(20)
    t.fd(10)
    t.circle(5, 170)
    t.fd(10)
    t.seth(240)
    t.circle(50, 30)

    t.end_fill()
    noTrace_goto(130, 125)
    t.seth(-20)
    t.fd(5)
    t.circle(-5, 160)
    t.fd(5)

    # finger
    noTrace_goto(166, 130)
    t.seth(-90)
    t.fd(3)
    t.circle(-4, 180)
    t.fd(3)
    t.seth(-90)
    t.fd(3)
    t.circle(-4, 180)
    t.fd(3)

    # tail
    noTrace_goto(168, 134)
    t.fillcolor('#F6D02F')
    t.begin_fill()
    t.seth(40)
    t.fd(200)
    t.seth(-80)
    t.fd(150)
    t.seth(210)
    t.fd(150)
    t.left(90)
    t.fd(100)
    t.right(95)
    t.fd(100)
    t.left(110)
    t.fd(70)
    t.right(110)
    t.fd(80)
    t.left(110)
    t.fd(30)
    t.right(110)
    t.fd(32)

    t.right(106)
    t.circle(100, 25)
    t.right(15)
    t.circle(-300, 2)
    ##############
    # print(t.pos())
    t.seth(30)
    t.fd(40)
    t.left(100)
    t.fd(70)
    t.right(100)
    t.fd(80)
    t.left(100)
    t.fd(46)
    t.seth(66)
    t.circle(200, 38)
    t.right(10)
    t.fd(10)
    t.end_fill()

    # tail
    t.fillcolor('#923E24')
    noTrace_goto(126.82, -156.84)
    t.begin_fill()

    t.seth(30)
    t.fd(40)
    t.left(100)
    t.fd(40)
    t.pencolor('#923e24')
    t.seth(-30)
    t.fd(30)
    t.left(140)
    t.fd(20)
    t.right(150)
    t.fd(20)
    t.left(150)
    t.fd(20)
    t.right(150)
    t.fd(20)
    t.left(130)
    t.fd(18)
    t.pencolor('#000000')
    t.seth(-45)
    t.fd(67)
    t.right(110)
    t.fd(80)
    t.left(110)
    t.fd(30)
    t.right(110)
    t.fd(32)
    t.right(106)
    t.circle(100, 25)
    t.right(15)
    t.circle(-300, 2)
    t.end_fill()

    # cap、eye、mouse、chin
    cap(-134.07, 147.81)
    mouth(-5, 25)
    leftCheek(-126, 32)
    rightCheek(107, 63)
    colorLeftEar(-250, 100)
    colorRightEar(140, 270)
    leftEye(-85, 90)
    rightEye(50, 110)
    t.hideturtle()

def cap( x, y):
    noTrace_goto(x, y)
    t.fillcolor('#CD0000')
    t.begin_fill()
    t.seth(200)
    t.circle(400, 7)
    t.left(180)
    t.circle(-400, 30)
    t.circle(30, 60)
    t.fd(50)
    t.circle(30, 45)
    t.fd(60)
    t.left(5)
    t.circle(30, 70)
    t.right(20)
    t.circle(200, 70)
    t.circle(30, 60)
    t.fd(70)
    # print(t.pos())
    t.right(35)
    t.fd(50)
    t.circle(8, 100)
    t.end_fill()
    noTrace_goto(-168.47, 185.52)
    t.seth(36)
    t.circle(-270, 54)
    t.left(180)
    t.circle(270, 27)
    t.circle(-80, 98)

    t.fillcolor('#444444')
    t.begin_fill()
    t.left(180)
    t.circle(80, 197)
    t.left(58)
    t.circle(200, 45)
    t.end_fill()

    noTrace_goto(-58, 270)
    t.pencolor('#228B22')
    t.dot(35)

    noTrace_goto(-30, 280)
    t.fillcolor('#228B22')
    t.begin_fill()
    t.seth(100)
    t.circle(30, 180)
    t.seth(190)
    t.fd(15)
    t.seth(100)
    t.circle(-45, 180)
    t.right(90)
    t.fd(15)
    t.end_fill()
    t.pencolor('#000000')


t.speed(100)
body()
turtle.mainloop()
{% endhighlight %}
