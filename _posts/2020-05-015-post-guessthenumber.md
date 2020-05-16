---
title: "Guess the Number"
tags:
  - Python
  - Game
---

## Guess the Number

 


{% highlight python linenos %}
import random

def guessthenum(start, stop):
    num = random.randint(start, stop)
    moves = 0
    while True:
        move = input("What do you think the number is?")
        if num > int(move):
            print("Higher\n")
            while True:
                giveup = input("Would you like to give up? (Y or N)")
                if giveup.lower() == "y":
                    return "You have given up"
                elif giveup.lower() == "n":
                    break
                else:
                    print("Hmm... I couldn't understand your answer. \n")
        elif num < int(move):
            print("Lower\n")
            while True:
                giveup = input("Would you like to give up? (Y or N)")
                if giveup.lower() == "y":
                    return "You have given up"
                elif giveup.lower() == "n":
                    break
                else:
                    print("Hmm... I couldn't understand your answer. \n")
        else:
            print("Congrats! You guessed the number in " + str(moves) + " turns. \n")
            break
        moves += 1
guessthenum(input("Start: "), input("Stop: "))


{% endhighlight %}

