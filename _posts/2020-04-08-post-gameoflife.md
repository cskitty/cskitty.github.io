---
title: "Conway's Game of Life"
tags:
  - Python
  - Game
---

## Conway's Game of Life
![](/assets/images/gameoflife.gif)

 Conway's Game of Life can be found in the wiki article [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).



{% highlight python linenos %}
import turtle
import random
import copy
import time


#size is 50 * 50 matrix
screenSize = 800 #pixels
gridSize = 50 #lines
lineDistance = screenSize // gridSize #distance in pixels

lifed = {}

def draw_square(x,y,size,color):
    global lifeturtle
    lifeturtle.penup()
    lifeturtle.goto(x,y)
    lifeturtle.pendown()
    lifeturtle.seth(0)
    lifeturtle.color(color)
    lifeturtle.begin_fill()
    for o in range(4):
        lifeturtle.left(90)
        lifeturtle.fd(size)
    lifeturtle.end_fill()
    lifeturtle.hideturtle()


def draw_line(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)


#assuming x >=0 , x < 50
#y >= 0, y < 25
def draw_life(x,y,color):
    x -= 25
    y -= 25
    draw_square(x * lineDistance, y * lineDistance, lineDistance, color)

def draw_border(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    for o in range(4):
        turtle.left(90)
        turtle.fd(lineDistance)

def draw_grid():
    turtle.color("grey")

    for x in range(-400, 400 + lineDistance, lineDistance):
        draw_line(x,-400,x,400)
    for y in range(-400, 400 + lineDistance + 1, lineDistance):
        draw_line(-400,y,400,y)


def check_neighbors(x, y):
    neighbors = 0
    self = False
    if (x + 1,y) in lifed:
        neighbors += 1
    if (x, y + 1) in lifed:
        neighbors  += 1
    if (x - 1, y) in lifed:
        neighbors += 1
    if (x, y - 1) in lifed:
        neighbors += 1
    if (x + 1,y + 1) in lifed:
        neighbors += 1
    if (x - 1, y - 1) in lifed:
        neighbors  += 1
    if (x - 1, y + 1) in lifed:
        neighbors += 1
    if (x + 1, y - 1) in lifed:
        neighbors += 1
    if (x, y) in lifed:
        self = True

    return (neighbors, self)


def uptate_board():
    global lifed
    newLifeD = copy.deepcopy(lifed)
    for x in range(50):
        for y in range(50):
            neighbour, self = check_neighbors(x,y)
            if neighbour != 3 and neighbour != 2 and self == True:
                del newLifeD[(x, y)]
            elif neighbour == 3 and self == False:
                newLifeD[x, y] = True
    lifed = copy.deepcopy(newLifeD)
    draw_all_lives()

def draw_all_lives():
    global lifeturtle
    global lifed
    lifeturtle.clear()
    for g in lifed:
        x,y = g
        draw_life(x, y, "black")

def print_score(score,color):
    global scoreTurtle

    scoreTurtle.clear()
    scoreTurtle.goto(-400, 400)
    scoreTurtle.color(color)
    scoreTurtle.write("Generation: {} ".format(score))

def bmain():
    global lifeturtle

    screen = turtle.Screen()
    turtle.setup(1000, 1000)
    turtle.title("Conway's Game of Life - from CSBunny")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(2)
    draw_grid()

    lifeturtle.up()
    lifeturtle.hideturtle()
    lifeturtle.speed(10)
    lifeturtle.color('black')


    for i in range(500):
        x = random.randint(0, 50)  # -25, 25
        y = random.randint(0, 49)  # -25, 25
        lifed[(x, y)] = True

    i = 0
    while True:
        i += 1
        draw_all_lives()
        uptate_board()
        print_score(i, "black")
        time.sleep(0.5)
    screen.mainloop()

if __name__ == "__main__":
    lifeturtle  = turtle.Turtle()  # turtle for drawing life
    scoreTurtle = turtle.Turtle()  # turtle for drawing score
    turtle.tracer(0,0)
    bmain()
{% endhighlight %}
