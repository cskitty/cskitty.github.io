---
title: "Project 3: Guess The Number"
tags:
  - Python
  - Game
---

## Project 3: Guess The Number

This game is played by giving a range of a smallest possible number and a largest possible number. The player guesses a randomly generated number between the two.


{% highlight python linenos %}
import random

def guess_the_number(start, stop):
  num = random.randint(int(start), int(stop))
  moves = 0
  while True:
    moves += 1
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
      print("Congrats! You guessed the number in " + str(moves) + " turns\n")
      break

guess_the_number(input("Start: "), input("Stop: "))
{% endhighlight %}
