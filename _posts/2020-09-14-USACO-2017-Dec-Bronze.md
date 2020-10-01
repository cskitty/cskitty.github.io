---
title: "USACO 2017 Dec Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - Python
  - USACO
---

# USACO 2017 Dec Bronze     

## Problem 1. The Blocked Billboard      

[The Blocked Billboard](http://usaco.org/index.php?page=viewproblem2&cpid=760)        

During long milking sessions, Bessie the cow likes to stare out the window of her barn at two huge rectangular billboards across the street advertising "Farmer Alex's Amazingly Appetizing Alfalfa" and "Farmer Greg's Great Grain". Pictures of these two cow feed products on the billboards look much tastier to Bessie than the grass from her farm.  
One day, as Bessie is staring out the window, she is alarmed to see a huge rectangular truck parking across the street. The side of the truck has an advertisement for "Farmer Smith's Superb Steaks", which Bessie doesn't quite understand, but she is mostly concerned about the truck potentially blocking the view of her two favorite billboards.  

Given the locations of the two billboards and the location of the truck, please calculate the total combined area of both billboards that is still visible. It is possible that the truck obscures neither, both, or only one of the billboards.  

INPUT FORMAT (file billboard.in):  
The first line of input contains four space-separated integers: x1 y1 x2 y2, where (x1,y1) and (x2,y2) are the coordinates of the lower-left and upper-right corners of the first billboard in Bessie's 2D field of view. The next line contains four more integers, similarly specifying the lower-left and upper-right corners of the second billboard. The third and final line of input contains four integers specifying the lower-left and upper-right corners of the truck. All coordinates are in the range -1000 to +1000. The two billboards are guaranteed not to have any positive area of overlap between themselves.  
OUTPUT FORMAT (file billboard.out):  
Please output the total combined area of both billboards that remains visible.  
SAMPLE INPUT:
```
1 2 3 5
6 0 10 4
2 1 8 3
```
SAMPLE OUTPUT:  
```
17
```
Here, 5 units of area from the first billboard and 12 units of area from the second billboard remain visible.  

Problem credits: Brian Dean  

{% highlight python linenos %}
fIn, fOut = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = tuple(map(int, fIn.readline().split()))
x3, y3, x4, y4 = tuple(map(int, fIn.readline().split()))
tx1, ty1, tx2, ty2 = tuple(map(int, fIn.readline().split()))

myMin = min(x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1)
myMax = max(x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1)

matrix = [[0 for x in range(myMin, myMax + 1)] for y in range(myMin, myMax + 1)]

coors = [x1, y1, x2, y2, x3, y3, x4, y4, tx1, ty2, tx2, ty1]
for i in range(12):
    coors[i] -= myMin

print(coors)

for x in range(x1, x2):
    for y in range(y1, y2):
        matrix[x][y] = 1

for x in range(x3, x4):
    for y in range(y3, y4):
        matrix[x][y] = 1

for x in range(tx1, tx2):
    for y in range(ty1, ty2):
        matrix[x][y] = 0

count = 0
for x in matrix:
    for y in x:
        if y == 1:
            count += 1

fOut.write(str(count))
{% endhighlight %}

## Problem 2. The Bovine Shuffle        

[The Bovine Shuffle](http://usaco.org/index.php?page=viewproblem2&cpid=760)      

Convinced that happy cows generate more milk, Farmer John has installed a giant disco ball in his barn and plans to teach his cows to dance!
Looking up popular cow dances, Farmer John decides to teach his cows the "Bovine Shuffle". The Bovine Shuffle consists of his N cows (1≤N≤100) lining up in a row in some order, then performing three "shuffles" in a row, after which they will be lined up in some possibly different order. To make it easier for his cows to locate themselves, Farmer John marks the locations for his line of cows with positions 1…N, so the first cow in the lineup will be in position 1, the next in position 2, and so on, up to position N.  

A shuffle is described with N numbers, a1…aN, where the cow in position i moves to position ai during the shuffle (and so, each ai is in the range 1…N). Every cow moves to its new location during the shuffle. Fortunately, all the ai's are distinct, so no two cows try to move to the same position during a shuffle.  

Farmer John's cows are each assigned distinct 7-digit integer ID numbers. If you are given the ordering of the cows after three shuffles, please determine their initial order.  

INPUT FORMAT (file shuffle.in):  
The first line of input contains N, the number of cows. The next line contains the N integers a1…aN. The final line contains the order of the N cows after three shuffles, with each cow specified by its ID number.  
OUTPUT FORMAT (file shuffle.out):  
You should write N lines of output, with a single cow ID per line, specifying the order of the cows before the three shuffles.   
SAMPLE INPUT:   
```
5
1 3 4 5 2
1234567 2222222 3333333 4444444 5555555
```
SAMPLE OUTPUT:  

```
1234567
5555555
2222222
3333333
4444444
```
Problem credits: Brian Dean  

{% highlight python linenos %}
fin, fout = open('shuffle.in'), open('shuffle.out', 'w')

n = int(fin.readline())
o = list(map(int , fin.readline().split()))
order = {}

for x in range(len(o)):
    order[x] = o[x]


cows = fin.readline().split()

for cowindex in range(n):
    curcowindex = cowindex + 1

    for x in range(3):
        curcowindex = order[curscowindex - 1]

    fout.write(cows[curcowindex - 1] + '\n')
{% endhighlight %}
