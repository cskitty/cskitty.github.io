---
title: "Backtracking: Knights Tour Algorithm"
categories:
  - Programming
tags:
  - Java
  - Algorithms
  - Backtracking
---

## Knights Tour Algorithm

![](/assets/images/aknightstour.gif)

Explanation

The Knights Tour Algorithm implements backtracking. Given a square "chessboard" (side length denoted by "size"), the algorithm finds a possible solution where a knight can travel to all parts of the board. Each step is printed from 1 to size squared.


{% highlight java linenos %}
import javax.swing.text.Position;
import java.nio.file.attribute.PosixFileAttributes;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class position {
    int x;
    int y;
    position(int xval, int yval) {
        x = xval;
        y = yval;
    }
}

public class KnightTour {

    int size = 8;

    void print_board(List<List<Integer>> board) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board.get(i).size(); j++) {
                System.out.printf("%d ", board.get(i).get(j));
            }
            System.out.println();
        }
        System.out.println();
    }

    boolean knight(position currentPosition, List<List<Integer>> board, Integer turn) {
        if (turn == (size*size) + 1) {
            return true;
        }
        else {
            List<String> movelst = new ArrayList<String>
                    (Arrays.asList("-2, 1", "-1, 2", "1, 2", "2, 1", "2, -1", "1, -2", "-1, -2", "-2, -1"));

            for (int i = 0; i < movelst.size(); i++) {

                String[] line = movelst.get(i).split(", ");
                int addX = Integer.parseInt(line[0]);
                int addY = Integer.parseInt(line[1]);

                position newpos = new position(currentPosition.x + addX, currentPosition.y + addY);
                if (newpos.x < size && newpos.x >= 0 && newpos.y < size && newpos.y >= 0
                        && board.get(newpos.x).get(newpos.y) == 0) {
                    // currently valid possibility
                    // push
                    board.get(newpos.x).set(newpos.y, turn);

                    // recurse
                    if (knight(newpos, board, turn + 1)) {
                        return true;
                    }

                    // pop
                    // System.out.print(board);
                    board.get(newpos.x).set(newpos.y, 0);
                }

            }
        }
        return false;
    }

    public static void main (String args[]) {
        KnightTour knightTour = new KnightTour();

        List<List<Integer>> board = new ArrayList<List<Integer>>(knightTour.size);
        for (int i = 0; i < knightTour.size; i++) {
            List<Integer> lst = new ArrayList<Integer>(knightTour.size);
            for (int j = 0; j < knightTour.size; j++) {
                lst.add(0);
            }
            board.add(lst);
        }

        position current = new position(0, 0);
        List<position> path = new ArrayList<position>();

        board.get(0).set(0, 1);

        boolean possible = knightTour.knight(current, board, 2);

        if (possible) {
            knightTour.print_board(board);
        }
        else {
            System.out.println("No Solution");
        }
    }
}


{% endhighlight %}
