---
title: "Project 4: Rock Paper Scissors"
tags:
  - Python
  - Game
---

## Project 4: Rock Paper Scissors



This game has two modes - two player, and against the computer. Adjust the parameters (x for amount of rounds) and "on" or "off" for against the computer or against another player, respectively.

{% highlight python linenos %}
import random

def rock_paper_scissors(x, computer = "off"):
  print("Welcome to Rock, Paper, Scissors. \n")
  wins = 0
  totalwins = 0
  if computer.lower() == "on":
    for turn in range(1, x + 1):
      computer_guess = random.choice(["rock", "paper", "scissors"])

      while True:
        your_guess = input("What do you choose?")

        your_guess = your_guess.lower()
        if your_guess == "rock" or your_guess == "paper" or your_guess == "scissors":
          break

      print "The computer chose", computer_guess

      if computer_guess == "rock" and your_guess == "scissors" or computer_guess == "paper" and your_guess == "rock" or computer_guess == "scissors" and your_guess == "paper":
        print("You lost :(")

        totalwins += 1

        if turn == x + 1:
          print("Next round! \n")


      if your_guess == "rock" and computer_guess == "scissors" or \
      your_guess == "paper" and computer_guess == "rock" or \
      your_guess == "scissors" and computer_guess == "paper":
        print("You won!")
        wins += 1
        if turn == x+ 1:
          print("Next round! \n")


      if your_guess == computer_guess:
        print("It is a tie... ")
        if turn == x+ 1:  
          print("Next Round!")


    if totalwins > wins:
      print("You lost! :(")  
    elif totalwins < wins:
      print("You won! :)")
    else:
      print("It's a tie!")

    play_again = input("Would you like to play again? (Yes/No)")
    if play_again.lower() == "yes":
      rock_paper_scissors(x, computer)




  else:

    p1wins = 0
    p2wins = 0
    for turn in range(1, x + 1):    

      while True:
        your_guess = input("What does Player 1 choose?")

        your_guess = your_guess.lower()
        if your_guess == "rock" or your_guess == "paper" or your_guess == "scissors":
          break  
      while True:
        p2_guess = input("What does Player 1 choose?")

        p2_guess = p2_guess.lower()
        if p2_guess == "rock" or p2_guess == "paper" or p2_guess == "scissors":
          break  

      print "The computer choose", computer_guess

      if p2_guess == "rock" and your_guess == "scissors" or \
      p2_guess == "paper" and your_guess == "rock" or \
      p2_guess == "scissors" and your_guess == "paper":                                    
        print("Player 1 lost! Player 2 won!")
        totalwins += 1
        if turn == x + 1:
          print("Next round! \n")


      if your_guess == "rock" and p2_guess == "scissors" or \
      your_guess == "paper" and p2_guess == "rock" or \
      your_guess == "scissors" and computer_guess == "paper":
        print("Player 1 won! Player 2 lost!")
        wins += 1
        if turn == x+ 1:
          print("Next round! \n")


      if your_guess == computer_guess:
        print("It is a tie... ")
        if turn == x+ 1:  
          print("Next Round!")


    if totalwins < wins:
      print("Player 1 won!")    
    elif wins > totalwins:
      print("Player 2 won!")
    else:
      print("It's a tie!")

    play_again = input("Would you like to play again? (Yes/No)")
    if play_again.lower() == "yes":
      rock_paper_scissors(x, computer)



x = 2
rock_paper_scissors(x, "on")
{% endhighlight %}
