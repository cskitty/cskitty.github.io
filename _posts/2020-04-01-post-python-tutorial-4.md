---
title: "Python for Beginner Lesson 4: Turtle"
categories:
  - Projects
  - Tutorials
tags:
  - Python
---

## Python for Beginner Lesson 4: Turtle

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

```python
# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. call it alice
alice = turtle.Turtle()

# Step 3: Move in the direction Alice's facing for 50 pixels
alice.forward(100)
# Step 4: We're done!
turtle.done()
```

### Draw a square

We can use Lines are boring. We can rotate the turtle in order to draw more interesting figures.

```python
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
```


### Draw a star


```python
import turtle

star = turtle.Turtle()

for i in range(5):
    star.forward(50)
    star.right(144)

turtle.done()
```

### Draw a hexagon

```python
import turtle

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
```

### Changing line color


```python
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
```

### Spiraling star


```python
import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()
```

### Drawing circles

The code below will draw a circle of radius 50units.

```python
import turtle
t = turtle.Turtle()

t.circle(50)
```

More than one circle having one point of intersection is called tangent circles.
The code below draws tangent Circles in Python turtle.

```python
#Program to draw tangent circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(10):
  t.circle(10*i)
```

Circles with varying radius are called spiral.
The code below draws spiral circles in Python turtle.


```python
#Program to draw spiral circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(30):
  t.circle(10+i, 45)
```

Circles with different radii having a common center are called concurrent circles.


```python
#Program to draw concentric circles in Python Turtle
import turtle

t = turtle.Turtle()
for i in range(10):
  t.circle(10*i)
  t.up()
  t.sety((10*i)*(-1))
  t.down()
```

### Turtle Olympics


```python
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
```


### Turtle's House


```python
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

```
