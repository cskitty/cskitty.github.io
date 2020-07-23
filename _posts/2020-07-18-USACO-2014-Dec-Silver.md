---
title: "USACO 2014 Dec Silver"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - USACO
---

# USACO 2014 December Silver

## Problem 1: Piggyback

[Piggyback](http://usaco.org/index.php?page=viewproblem2&cpid=491)

Bessie and her sister Elsie graze in different fields during the day,
and in the evening they both want to walk back to the barn to rest.
Being clever bovines, they come up with a plan to minimize the total
amount of energy they both spend while walking.  

Bessie spends B units of energy when walking from a field to an
adjacent field, and Elsie spends E units of energy when she walks to
an adjacent field.  However, if Bessie and Elsie are together in the
same field, Bessie can carry Elsie on her shoulders and both can move
to an adjacent field while spending only P units of energy (where P
might be considerably less than B+E, the amount Bessie and Elsie would
have spent individually walking to the adjacent field).  If P is very
small, the most energy-efficient solution may involve Bessie and Elsie
traveling to a common meeting field, then traveling together piggyback
for the rest of the journey to the barn.  Of course, if P is large, it
may still make the most sense for Bessie and Elsie to travel
separately.  On a side note, Bessie and Elsie are both unhappy with
the term "piggyback", as they don't see why the pigs on the farm
should deserve all the credit for this remarkable form of
transportation.  

Given B, E, and P, as well as the layout of the farm, please compute
the minimum amount of energy required for Bessie and Elsie to reach
the barn.  

INPUT: (file piggyback.in)  

The first line of input contains the positive integers B, E, P, N, and
M.  All of these are at most 40,000.  B, E, and P are described above.
N is the number of fields in the farm (numbered 1..N, where N >= 3),
and M is the number of connections between fields.  Bessie and Elsie
start in fields 1 and 2, respectively.  The barn resides in field N.  

The next M lines in the input each describe a connection between a
pair of different fields, specified by the integer indices of the two
fields.  Connections are bi-directional.  It is always possible to
travel from field 1 to field N, and field 2 to field N, along a series
of such connections.   

SAMPLE INPUT:  

4 4 5 8 8  
1 4  
2 3  
3 4  
4 7  
2 5  
5 6  
6 8  
7 8  


OUTPUT: (file piggyback.out)  

A single integer specifying the minimum amount of energy Bessie and
Elsie collectively need to spend to reach the barn.  In the example
shown here, Bessie travels from 1 to 4 and Elsie travels from 2 to 3
to 4.  Then, they travel together from 4 to 7 to 8.  

SAMPLE OUTPUT:  

22  

{% highlight python linenos %}
import java.io.*;
import java.util.*;

public class Piggyback {


    class Node {
        int value;
        int distance;
        Node(int v, int d) {
            value = v;
            distance = d;
        }
    }

    LinkedList<Integer>[] m_graph;

    int m_size;

    Piggyback(int size) {
        m_size = size;
        m_graph = new LinkedList[size];

        for (int i = 0; i < m_size; i++) {
            m_graph[i] = new LinkedList<Integer>();
        }
    }

    void addEdge(int i, int j) {
        m_graph[i].add(j);
        m_graph[j].add(i);
    }

    int[] distance(int start) {
        int[] values = new int[m_size + 1];

        Queue<Node> myQueue = new LinkedList<Node>();
        myQueue.add(new Node(start, 0));
        Map<Integer, Boolean> visited = new HashMap<Integer, Boolean>();

        visited.put(start, true);

        while (myQueue.size() > 0) {
            Node current = myQueue.poll();
            //current.distance++;

            values[current.value] = current.distance;

            for (int i = 0; i < m_graph[current.value].size(); i++) {
                int child = m_graph[current.value].get(i);

                if (! visited.containsKey(child)) {
                    visited.put(child, true);
                    myQueue.add(new Node(child, current.distance+1));
                }
            }
        }

        return values;
    }

    int distance(int start, int end) {
        if (start == end) {
            return 0;
        }

        Queue<Node> myQueue = new LinkedList<Node>();
        myQueue.add(new Node(start, 0));
        Map<Integer, Boolean> visited = new HashMap<Integer, Boolean>();

        while (myQueue.size() > 0) {
            Node current = myQueue.poll();
            //current.distance++;

            for (int i = 0; i < m_graph[current.value].size(); i++) {
                int child = m_graph[current.value].get(i);

                if (child == end) {
                    current.distance++;
                    return current.distance;
                }

                if (! visited.containsKey(child)) {
                    visited.put(child, true);
                    myQueue.add(new Node(child, current.distance+1));
                }
            }
        }
        return -1;
    }

    int minEnergy(int B, int E, int P, int N) {
        int[] BDistance = distance(1);
        int[] EDistance = distance(2);
        int[] PDistance = distance(N);

        //int[] BCompare = new int[N + 1];
        //for (int i = 0; i < N + 1; i++) {
        //    BCompare[i] = distance(1, i);
        //}

        // find solutions
        int smallestSize = Integer.MAX_VALUE;

        for (int i = 1; i < N + 1; i++) {
            int currentSize = (B*BDistance[i]) + (E*EDistance[i]) + (P*PDistance[i]);
            if (currentSize < smallestSize) {
                smallestSize = currentSize;
            }
        }

        return smallestSize;
    }


    public static void main (String args[]) throws IOException {

        try {
            // input
            BufferedReader br = new BufferedReader(new FileReader("piggyback.in"));
            Scanner scanner = new Scanner(br);

            String line = "";
            String[] firstLine = br.readLine().trim().split("\\s+");

            int B = Integer.parseInt(firstLine[0]);
            int E = Integer.parseInt(firstLine[1]);
            int P = Integer.parseInt(firstLine[2]);
            int N = Integer.parseInt(firstLine[3]);
            int M = Integer.parseInt(firstLine[4]);


            Piggyback mySolution = new Piggyback(N + 1);

            //while(scanner.hasNext()){
            for (int i = 0; i < M; i++) {
                line = scanner.nextLine();
                String[] arrItems = line.split(" ");

                mySolution.addEdge(Integer.parseInt(arrItems[0]), Integer.parseInt(arrItems[1]));
            }

            br.close();

            int returnInteger = mySolution.minEnergy(B, E, P, N);

            // output
            // int --> string = String.valueOf()

            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("piggyback.out"));
            bufferedWriter.write(String.valueOf(returnInteger));
            bufferedWriter.close();
            ///
        }


        catch (FileNotFoundException e) {
            System.out.println("File not exists or insufficient rights");
            e.printStackTrace();
        }
        catch (IOException e) {
            System.out.println("An exception occured while reading the file");
            e.printStackTrace();
        }


    }
}
{% endhighlight %}


## Problem 3: Cow Jog

[Cow Jog](http://usaco.org/index.php?page=viewproblem2&cpid=493)

The cows are out exercising their hooves again!  There are N cows
jogging on an infinitely-long single-lane track (1 <= N <= 100,000).
Each cow starts at a distinct position on the track, and some cows jog
at different speeds.  

With only one lane in the track, cows cannot pass each other.  When a
faster cow catches up to another cow, she has to slow down to avoid
running into the other cow, becoming part of the same running group.  

The cows will run for T minutes (1 <= T <= 1,000,000,000).  Please
help Farmer John determine how many groups will be left at this time.
Two cows should be considered part of the same group if they are at
the same position at the end of T minutes.  

INPUT: (file cowjog.in)  

The first line of input contains the two integers N and T.  

The following N lines each contain the initial position and speed of a
single cow.  Position is a nonnegative integer and speed is a positive
integer; both numbers are at most 1 billion.  All cows start at
distinct positions, and these will be given in increasing order in
the input.  

SAMPLE INPUT:  

5 3  
0 1  
1 2  
2 3  
3 2  
6 1  

OUTPUT: (file cowjog.out)  

A single integer indicating how many groups remain after T minutes.  

SAMPLE OUTPUT:  

3  


{% highlight python linenos %}
import javax.xml.soap.Node;
import java.io.*;
import java.util.*;

class Cow implements Comparable<Cow> {
    float position;
    float speed;
    int id;
    Cow(int p, int s, int i) {
        position = p;
        speed = s;
        id = i;
    }
    @Override
    public int compareTo(Cow o) {
        return (this.position < o.position ? -1 :
                (this.position == o.position ? 0 : 1));
    }
}

public class CowJog {

    List<Cow> m_cows;

    CowJog() {
        m_cows = new ArrayList<Cow>();
    }

    void sortCow() {
        Collections.sort(m_cows);
    }

    void printCows() {
        for (int i = 0; i < m_cows.size(); i++) {
            System.out.printf("(%d, %d), ",(int) m_cows.get(i).position, (int) m_cows.get(i).speed);
        }
        System.out.println();
    }


    List<Cow> deepCopy(List<Cow> origin) {
        List<Cow> rL = new ArrayList<Cow>();

        for (int i = 0; i < origin.size(); i++) {
            rL.add(origin.get(i));
        }
        return rL;
    }

    Integer cowJog() {

        float worldTime = 0;
        boolean flag = true;
        List<Integer> mL = new ArrayList<Integer>();
        int dCount = 0;

        while (flag) {
            flag = false;
            float nextMeetTime = Float.MAX_VALUE;
            for (int i = m_cows.size() - 1; i > 0; i--) {
                //System.out.printf("P: %d, S: %d\n", m_cows.get(i).position, m_cows.get(i).speed);

                Cow one = m_cows.get(i);
                Cow two = m_cows.get(i - 1);

                if (one.speed < two.speed) {
                    float meetTime = (one.position - two.position)/(two.speed - one.speed);
                    if (meetTime < nextMeetTime) {
                        nextMeetTime = meetTime;
                    }

                    flag = true;
                }

            }

            if (! flag) {
                break;
            }
            // smallest meet time found

            // printCows();
            worldTime += nextMeetTime;
            List<Cow> deletedCows = new ArrayList<Cow>();

            // System.out.printf("World Time: %f\n", worldTime);

            // one round

            float lastPosition = 0;
            for (int i = m_cows.size() - 1; i >= 0; i--) {
                Cow currentCow = m_cows.get(i);
                float newPos = currentCow.position + (currentCow.speed * nextMeetTime);

                if (i != 0 && m_cows.get(i).position <= m_cows.get(i - 1).position) {
                    deletedCows.add(m_cows.get(i - 1));
                }

                m_cows.get(i).position = newPos;

            }

            for (int i = 0; i < deletedCows.size(); i++) {
                m_cows.remove(deletedCows.get(i));
            }

        }


        return m_cows.size();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("cowjog.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cowjog.out")));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        CowJog cowJog = new CowJog();

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            Cow currentCow = new Cow(x, y, i);

            cowJog.m_cows.add(currentCow);
        }

        int ans = cowJog.cowJog();

        pw.println(ans);
        pw.close();
    }
}
{% endhighlight %}
