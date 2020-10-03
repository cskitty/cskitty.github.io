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


## Problem 3. Milk Measurement      

[Milk Measurement](http://usaco.org/index.php?page=viewproblem2&cpid=761)      

Farmer John purchases three cows: Bessie, Elsie, and Mildred, each of whom initially produces 7 gallons of milk per day. Since the milk output of a cow is known to potentially change over time, Farmer John takes periodic measurements over the next 100 days and scribbles them down in a log book. Entries in his log look like this:  
35 Bessie -2  
14 Mildred +3  
The first entry indicates that on day 35, Bessie's milk output was 2 gallons lower than it was when last measured. The next entry indicates that on day 14, Mildred's milk output increased by 3 gallons from when it was last measured. Farmer John has only enough time to make at most one measurement on any given day. Unfortunately, he is a bit disorganized, and doesn't necessarily write down his measurements in chronological order.  

To keep his cows motivated, Farmer John proudly displays on the wall of his barn the picture of whichever cow currently has the highest milk output (if several cows tie for the highest milk output, he displays all of their pictures). Please determine the number of days on which Farmer John would have needed to change this display.  

INPUT FORMAT (file measurement.in):  
The first line of input contains N, the number of measurements Farmer John makes. Each of the next N lines contains one measurement, in the format above, specifying a day (an integer in the range 1..100), the name of a cow, and the change in her milk output since it was last measured (a nonzero integer). Each cow's milk output will always be in the range 0..1000.  
OUTPUT FORMAT (file measurement.out):  
Please output the number of days (an integer in the range 0..100) on which Farmer John needs to adjust his motivational display.  
SAMPLE INPUT:  
```
4  
7 Mildred +3  
4 Elsie -1
9 Mildred -1
1 Bessie +2
```
SAMPLE OUTPUT:
```
3
```
Initially, all cows have milk output 7. On day 1, Bessie's milk output increases to 9, making her the unique cow with highest milk output and causing Farmer John to change his display. On day 4, Elsie's milk output decreases to 6, but this does not change the fact that Bessie is the sole cow in the lead. On day 7, Mildred jumps into the lead, changing the display, and on day 9, Mildred drops in production to be tied with Bessie, again changing the display.

Problem credits: Brian Dean    

{% highlight python linenos %}
fIn, fOut = open("measurement.in"), open("measurement.out", "w")
n = int(fIn.readline())
days = []
for _ in range(n):
    d, c, i = fIn.readline().split()
    days.append((int(d), c, int(i)))

days.sort(key=lambda x: x[0])
newDays = [(7, 7, 7)]

for day in days:
    prev = newDays[-1]
    if day[1] == 'Bessie':
        newDays.append((prev[0] + day[2], prev[1], prev[2]))

    elif day[1] == 'Elsie':
        newDays.append((prev[0], prev[1]+ day[2], prev[2]))

    elif day[1] == 'Mildred':
        newDays.append((prev[0], prev[1], prev[2] + day[2]))

maxList = []
for day in newDays:
    m = max(day)
    maxList.append([i for i, j in enumerate(day) if j == m])

count = 0
prev = maxList[0]
for x in maxList:
    if x != prev:
        count += 1

    prev = x

fOut.write(str(count))
{% endhighlight %}
