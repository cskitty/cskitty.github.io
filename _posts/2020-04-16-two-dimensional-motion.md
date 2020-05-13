---
title: "Two Dimensional Motion"
date: 2020-04-13T15:34:30-04:00
tags:
  - Python
  - Physics
---

## Two Dimensional Motion

Below is the two dimensional kinematic equation that we learn in physics class.

Given the initial position (x1, y1), initial speed v1, angle theta and vertical
acceleration a, calculate the (x2, y2) position at time t.

![](/assets/images/2dphysics.png)

Now we can use Python to calculate and visually see the result.
These are the starting values:

* t  = 100 seconds
* x1 = 0 meters
* y1 = 1000 meters
* v1 = 500 m/s
* a  = -10 m/s^2
* $$\theta$$ = 60 degree

Using the following two dimensional formula:

$$ v_{1x} = v_{1} \cdot \cos {\theta} $$

$$ v_{1y} = v_{1} \cdot \sin {\theta} $$

$$ x_{2} = x_{1} + v_{1x} \cdot \Delta {t} $$

$$ y_{2} = y_{1} + v_{1y} \cdot \Delta {t} + \frac{1}{2} \cdot a \cdot (\Delta t)^2 $$  

Copy and paste the code below to Playground (trinket) and run it :)

{% highlight python linenos %}
#runnable under trinket.io
import matplotlib.pyplot as plt
import math

#comment out this line in trinket
fig = plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')

#parameters
x1 = 0
y1 = 1000
v1 = 500
a  = -10
theta = 60

#initial speed of v in x and y directions
vx = v1 * math.cos(math.radians(theta))
vy = v1 * math.sin(math.radians(theta))

#generate a list of time points, deltaT = 5
dt = 3
tLst = [x for x in range(0, 100, dt)]

#generate two lists for x and y positions and push the initial position (x1,y1)
xLst = []
yLst = []

#calculate new (x, y) position at time t
for t in tLst:
  x2 = x1 + vx*t
  y2 = y1 + vy*t + .5*a*t**2
  xLst.append(x2)
  yLst.append(y2)

plt.title('Two dimensional position (x, y) for throwing a ball at angle theta')
plt.xlabel('x (t)')
plt.ylabel('y (t)')
plt.plot(xLst, yLst, 'ro')
plt.show()
{% endhighlight %}


![png](/assets/images/2dphysics-1.png)


You can get awesome 3D plot by running the code under jupyter notebook.

{% highlight python linenos %}
#runnable under jupyter notebook
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
ax  = plt.axes(projection='3d')

# convert list of (x, y, t) to np.array
xline = np.array(xLst, dtype=np.float32)
yline = np.array(yLst, dtype=np.float32)
zline = np.array(tlist, dtype=np.float32)

ax.set_xlabel('X(t)')
ax.set_ylabel('time')
ax.set_zlabel('Y(t)')
ax.plot3D(xline, yline, zs = zline, zdir='y', c='red')
{% endhighlight %}


![png](/assets/images/output_1_1.png)
