---
title: "USACO 2019 January Bronze"
categories:
  - USACO
tags:
  - USACO
  - Bronze
---                          
# USACO 2019 January Bronze     

## Problem 2. Sleepy Cow Sorting

Farmer John is attempting to sort his N cows (1≤N≤100), conveniently numbered 1…N, before they head out to the pastures for breakfast.  

Currently, the cows are standing in a line in the order $$p_1,p_2,p_3,…,p_N$$, and Farmer John is standing in front of cow p1. He wants to reorder the cows so that they are in the order $$1,2,3,…,N,$$ with cow 1 next to Farmer John.  

The cows are a bit sleepy today, so at any point in time the only cow who is paying attention to Farmer John's instructions is the cow directly facing Farmer John. In one time step, he can instruct this cow to move k paces down the line, for any k in the range 1…N−1. The k cows whom she passes will amble forward, making room for her to insert herself in the line after them.  

For example, suppose that N=4 and the cows start off in the following order:  

  FJ: 4, 3, 2, 1  

The only cow paying attention to FJ is cow 4. If he instructs her to move 2 paces down the line, the order will subsequently look like this:  

 FJ: 3, 2, 4, 1  

Now the only cow paying attention to FJ is cow 3, so in the second time step he may give cow 3 an instruction, and so forth until the cows are sorted.   

Farmer John is eager to complete the sorting, so he can go back to the farmhouse for his own breakfast. Help him find the minimum number of time steps required to sort the cows.  


INPUT FORMAT (file sleepy.in):  
The first line of input contains N.  
The second line contains N space-separated integers, $$p_1,p_2,p_3,…,p_N$$, indicating the starting order of the cows.  

OUTPUT FORMAT (file sleepy.out):  

A single integer: the number of time steps before the N cows are in sorted order, if Farmer John acts optimally.  

SAMPLE INPUT:  
4  
1 2 4 3  
SAMPLE OUTPUT:  
3  
Problem credits: Dhruv Rohatgi  

{% include video id="-iObZJW8f5A" provider="youtube" %}


## Problem 3. Guess the Animal

When bored of playing their usual shell game, Bessie the cow and her friend Elsie like to play another common game called "guess the animal".  

Initially, Bessie thinks of some animal (most of the time, this animal is a cow, making the game rather boring, but occasionally Bessie is creative and thinks of something else). Then Elsie proceeds to ask a series of questions to figure out what animal Bessie has selected. Each question asks whether the animal has some specific characteristic, and Bessie answers each question with "yes" or "no". For example:  

Elsie: "Does the animal fly?"  
Bessie: "No"  
Elsie: "Does the animal eat grass?"  
Bessie: "Yes"  
Elsie: "Does the animal make milk?"  
Bessie: "Yes"  
Elsie: "Does the animal go moo?"  
Bessie: "Yes"  
Elsie: "In that case I think the animal is a cow."  
Bessie: "Correct!"  

If we call the "feasible set" the set of all animals with characteristics consistent with Elsie's questions so far, then Elsie keeps asking questions until the feasible set contains only one animal, after which she announces this animal as her answer. In each question, Elsie picks a characteristic of some animal in the feasible set to ask about (even if this characteristic might not help her narrow down the feasible set any further). She never asks about the same characteristic twice.  

Given all of the animals that Bessie and Elsie know as well as their characteristics, please determine the maximum number of "yes" answers Elsie could possibly receive before she knows the right animal.  


INPUT FORMAT (file guess.in):  

The first line of input contains the number of animals, N (2≤N≤100). Each of the next N lines describes an animal. The line starts with the animal name, then an integer K (1≤K≤100), then K characteristics of that animal. Animal names and characteristics are strings of up to 20 lowercase characters (a..z). No two animals have exactly the same characteristics.  

OUTPUT FORMAT (file guess.out):  

Please output the maximum number of "yes" answers Elsie could receive before the game ends.  

SAMPLE INPUT:  

4  
bird 2 flies eatsworms  
cow 4 eatsgrass isawesome makesmilk goesmoo  
sheep 1 eatsgrass  
goat 2 makesmilk eatsgrass  

SAMPLE OUTPUT:  

3  
  
In this example, it is possible for Elsie to generate a transcript with 3 "yes" answers (the one above), and it is not possible to generate a transcript with more than 3 "yes" answers.  

Problem credits: Brian Dean  

{% include video id="McxxgmkXyu8" provider="youtube" %}
