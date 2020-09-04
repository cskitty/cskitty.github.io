---
title: "USACO 2017 Jan Bronze"
categories:
  - USACO
tags:
  - Algorithms
  - USACO
  - Python
---

# USACO 2017 Jan Bronze

## Problem 1: Don't Be Last!  

Farmer John owns 7 dairy cows: Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, and Henrietta. He milks them every day and keeps detailed records on the amount of milk provided by each cow during each milking session. Not surprisingly, Farmer John highly prizes cows that provide large amounts of milk.  
Cows, being lazy creatures, don't necessarily want to be responsible for producing too much milk. If it were up to them, they would each be perfectly content to be the lowest-producing cow in the entire herd. However, they keep hearing Farmer John mentioning the phrase "farm to table" with his human friends, and while they don't quite understand what this means, they have a suspicion that it actually may not be the best idea to be the cow producing the least amount of milk. Instead, they figure it's safer to be in the position of producing the second-smallest amount of milk in the herd. Please help the cows figure out which of them currently occupies this desirable position.  

INPUT FORMAT (file notlast.in):  
The input file for this task starts with a line containing the integer N (1≤N≤100), giving the number of entries in Farmer John's milking log.  
Each of the N following lines contains the name of a cow (one of the seven above) followed by a positive integer (at most 100), indicating the amount of milk produced by the cow during one of its milking sessions.  

Any cow that does not appear in the log at all is assumed to have produced no milk.  

OUTPUT FORMAT (file notlast.out):  
On a single line of output, please print the name of the cow that produces the second-smallest amount of milk. More precisely, if M is the minimum total amount of milk produced by any cow, please output the name of the cow whose total production is minimal among all cows that produce more than M units of milk. If several cows tie for this designation, or if no cow has this designation (i.e., if all cows have production equal to M), please output the word "Tie". Don't forget to add a newline character at the end of your line of output. Note that M=0 if one of the seven cows is completely absent from the milking log, since this cow would have produced no milk.  
SAMPLE INPUT:
```
10
Bessie 1
Maggie 13
Elsie 3
Elsie 4
Henrietta 4
Gertie 12
Daisy 7
Annabelle 10
Bessie 6
Henrietta 5
```
SAMPLE OUTPUT:
```
Henrietta
```
In this example, Bessie, Elsie, and Daisy all tie for the minimum by each producing 7 units of milk. The next-largest production, 9 units, is due to Henrietta.  

Problem credits: Brian Dean  


## Problem 2: Hoof, Paper, Scissors

You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".
The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.

Farmer John watches in fascination as two of his cows play a series of N games of "Hoof, Paper, Scissors" (1≤N≤100). Unfortunately, while he can see that the cows are making three distinct types of gestures, he can't tell which one represents "hoof", which one represents "paper" and which one represents "scissors" (to Farmer John's untrained eye, they all seem to be variations on "hoof"...)

Not knowing the meaning of the three gestures, Farmer John assigns them numbers 1, 2, and 3. Perhaps gesture 1 stands for "hoof", or maybe it stands for "paper"; the meaning is not clear to him. Given the gestures made by both cows over all N games, please help Farmer John determine the maximum possible number of games the first cow could have possibly won, given an appropriate mapping between numbers and their respective gestures.

INPUT FORMAT (file hps.in):
The first line of the input file contains N.
Each of the remaining N lines contain two integers (each 1, 2, or 3), describing a game from Farmer John's perspective.

OUTPUT FORMAT (file hps.out):
Print the maximum number of games the first of the two cows could possibly have won.
SAMPLE INPUT:
5
1 2
2 2
1 3
1 1
3 2
SAMPLE OUTPUT:
2
One solution (of several) for this sample case is to have 1 represent "scissors", 2 represent "hoof", and 3 represent "paper". This assignment gives 2 victories to the first cow ("1 3" and "3 2"). No other assignment leads to more victories.

Problem credits: Brian Dean

{% highlight python linenos %}
fIn, fOut = open('cowtip.in'), open('cowtip.out', 'w')

n = int(fIn.readline())
matrix = []

for x in range(n):
    matrix.append(list(map(int, list(fIn.readline().strip()))))

count = 0
for x in range(n - 1, -1, -1):
    for y in range(n-1,-1,-1):
        if matrix[x][y] == 1:
            count += 1
            for i in range(0, x + 1):
                for j in range(0, y + 1):

                    matrix[i][j] = 1 - matrix[i][j]

fOut.write(str(count))
{% endhighlight %}

## Problem 3. Cow Tipping  


[Cow Tipping](http://www.usaco.org/index.php?page=viewproblem2&cpid=689)      

Farmer John occasionally has trouble with bored teenagers who visit his farm at night and tip over his cows. One morning, he wakes up to find it has happened again -- his N2 cows began the night grazing in a perfect N×N square grid arrangement (1≤N≤10), but he finds that some of them are now tipped over.  
Fortunately, Farmer John has used parts from his tractor and forklift to build a glorious machine, the Cow-Untipperator 3000, that can flip over large groups of cows all at once, helping him put all his cows back on their feet as quickly as possible. He can apply the machine to any "upper-left rectangle" in his grid of cows -- a rectangular sub-grid that contains the upper-left cow. When he does so, the machine flips over every cow in this rectangle, placing tipped cows back on their feet, but unfortunately also tipping over cows that were already on their feet! In other words, the machine "toggles" the state of each cow in the rectangle.

Farmer John figures that by applying his machine sufficiently many times to the appropriate collection of rectangles, he can eventually restore all the cows to their rightful, un-tipped states. Please help him determine the minimum number of applications of his machine needed to do this.  

Note that applying the machine to the same rectangle twice would be pointless, since this would have no net impact on the cows in the rectangle. Therefore, you should only consider applying the machine to each upper-left rectangle possibly only once.  

INPUT FORMAT (file cowtip.in):  
The first line of the input is the integer N.
Each of the N subsequent lines contains a string of N characters, each either 0 (representing an up-tipped cow) or 1 (representing a tipped cow).  

OUTPUT FORMAT (file cowtip.out):  
Please output the minimum number of times Farmer John needs to apply the Cow-Untipperator 3000 to restore all his cows to their feet.  
SAMPLE INPUT:  
```
3
001
111
111
```
SAMPLE OUTPUT:
```
2
```
In this example, if FJ applies his machine to the entire herd of cows (which is a valid upper-left rectangle), he will toggle their state to the following:  

110  
000  
000  
All that remains is to apply the machine to the upper-left rectangle containing the two 1s, and he is finished. In total, this is just 2 applications.  

**Problem credits:** Nathan Pinsker  


{% highlight python linenos %}
fIn, fOut = open('cowtip.in'), open('cowtip.out', 'w')

n = int(fIn.readline())
matrix = []

for x in range(n):
    matrix.append(list(map(int, list(fIn.readline().strip()))))

count = 0
for x in range(n - 1, -1, -1):
    for y in range(n-1,-1,-1):
        if matrix[x][y] == 1:
            count += 1
            for i in range(0, x + 1):
                for j in range(0, y + 1):

                    matrix[i][j] = 1 - matrix[i][j]

fOut.write(str(count))
{% endhighlight %}
