---
title: "Dynmamic Programming: Passing Notes"
categories:
  - Algorithm
tags:
  - Algorithms
  - C++
  - Dynamic Programming
---

## Passing Notes (Chinese NOIP2008 Intermediate Q3)

Bessie and Elsie are good friends and classmates, they always talk about endless topics together.

In a class activity, all the students arranged to sit together in m Row and each row has n Columns, and Bessie and Elsie are arranged at the opposite ends of the diagonal of the matrix, so they can’t talk directly.

Fortunately, they can communicate by passing notes.

The note must be passed to each other through many classmates. Bessie sits in the upper left corner of the matrix with coordinates (1,1), and Elsie sits in the lower right corner of the matrix with coordinates (m,n).

The note passed from Bessie to Elsie can only be passed down or to the right, and the note passed from Elsie to Bessie can only be passed up or to the left. 

During the class, Bessie hoped to pass a note to Elsie, and also hoped that Elsie would reply to him.

Every classmate in the class can help them, but only once. That is to say, if the student helped when Bessie handed the note to Elsie, then he would not help when Elsie handed it to Bessie and vice versa. 

There is one more thing to pay attention to. Every student in the class is willing to help with a degree of goodwill (note: the degree of kindness of Bessie and Elsie is not defined, use 0 when entering), you can use a natural number from 0 to 100 To indicate that the larger the number, the better-hearted.

Bessie and Elsie hope to find as many kind students as possible to help pass the note, that is, to find two back and forth transmission paths, so that the sum of the kindness of the students on the two paths is maximized.

Now, please help Bessie and Elsie find these two paths.

Input format
The first line has 2 integers separated by spaces m and n, Which means that the student matrix has m Row n Column.

Next m Line is a m x n Matrix, the first in the matrix i Row j The integers in the column represent the i Row j The kindness of the students in the column, for each row n Use a space to separate the integers.

Output format
Output an integer, which represents the maximum value of the sum of the kindness of the students who participated in passing the note on the two roads back and forth.

data range
1 ≤ n , m ≤ 50

```
3 3
0 3 9
2 8 5
5 7 0
```

```
34
```

## Solution 1: Using 4D array as state,

Since there are two routes, we can think that the DP state is represented by sum of two routes from (1, 1) to (x1, y1) and (x2, y2).
And because n is only 50, we can directly mark state as dp[x1][y1][x2][y2], which represents the maximum value of the first route to (x1, y1) and the second route to (x2, y2).
For each student, the note is transferred from the two directions (top or left), so there are total four state transfer situations.  

Please note that the two routes ((1, 1) to (x1, y1) and (x2, y2)) can not share any common node.  To avoid that, we set dp[x][y][x][y]=-1.

The actual code can be written as =0, because the value is all >0.

{% highlight C++ linenos %}
#include<bits/stdc++.h>
using namespace std;
const int	N=55;
int n,m,a[N][N];
int f[N][N][N][N];
void MAX(int &a,int b){a=max(a,b);}
int main()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++) scanf("%d",&a[i][j]);
	for (int x1=1;x1<=n;x1++)
		for (int y1=1;y1<=m;y1++)
			for (int x2=1;x2<=n;x2++)
				for (int y2=1;y2<=m;y2++){
					if ((x1!=1 || y1!=1) && (x1!=n || y1!=m) && x1==x2 && y1==y2){
						f[x1][y1][x2][y2]=0;
						continue;
					}
					int t=f[x1][y1][x2][y2];
					MAX(t,f[x1][y1-1][x2][y2-1]);
					MAX(t,f[x1][y1-1][x2-1][y2]);
					MAX(t,f[x1-1][y1][x2-1][y2]);
					MAX(t,f[x1-1][y1][x2][y2-1]);
					f[x1][y1][x2][y2]=t+a[x1][y1]+a[x2][y2];
				}
	printf("%d\n",f[n][m][n][m]);
	return 0;
}
{% endhighlight %}
