---
title: "Conway's Game of Life"
tags:
  - Python
  - Game
---

## Conway's Game of Life
![](/assets/images/gamesheadercat.png)

 Conway's Game of Life can be found in the wiki article [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).



{% highlight python linenos %}
import turtle
import random
import copy

#size is 30 * 30 matrix
screenSize = 600 #pixels
gridSize = 30 #lines
halfGridSize = gridSize // 2
lineDistance = screenSize // gridSize #distance in pixels

#a python dictionary with (x,y) coordinates as key, True or False as value
lifeDict = {}

def draw_line(turtle, x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)


def draw_square(lifeturtle, x,y,size,color):
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

def draw_grid(turtle):
    turtle.color("grey")

    for x in range(-400, 400 + lineDistance, lineDistance):
        draw_line(turtle, x,-400,x,400)
    for y in range(-400, 400 + lineDistance + 1, lineDistance):
        draw_line(turtle, -400,y,400,y)

#assuming x >=0 , x < 50
#y >= 0, y < 25
def draw_life(turtle, x,y,color):
    x -= halfGridSize
    y -= halfGridSize
    draw_square(turtle, x * lineDistance, y * lineDistance, lineDistance, color)


def draw_all_lives(lifeTurtle, lifeDict):
    turtle.clear()

    for i in range(50):
        x = random.randint(0, gridSize)   
        y = random.randint(0, gridSize)   
        lifeDict[(x, y)] = True

    for g in lifeDict:
        x,y = g
        draw_life(lifeTurtle, x, y, "black")

def check_neighbors(x, y, lifed):
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


def update_board(lifeTurtle, lifeDict):
    newLifeD = copy.deepcopy(lifeDict)
    for x in range(gridSize):
        for y in range(gridSize):
            neighbour, self = check_neighbors(x,y, lifeDict)
            if neighbour != 3 and neighbour != 2 and self == True:
                del newLifeD[(x, y)]
            elif neighbour == 3 and self == False:
                newLifeD[x, y] = True
    lifed = copy.deepcopy(newLifeD)
    draw_all_lives(lifeTurtle, lifeDict)

#wn = turtle.screen()

lifeTurtle = turtle.Turtle()
lifeTurtle.speed(0)
lifeTurtle.tracer(0,0)
draw_grid(lifeTurtle)
#draw_all_lives(lifeTurtle, lifeDict)
#update_board(lifeTurtle, lifeDict)

for i in range(100):
  draw_all_lives(lifeTurtle, lifeDict)
  update_board(lifeTurtle, lifeDict)
  #time.sleep(0.5)
  #wn.mainloop()
{% endhighlight %}
