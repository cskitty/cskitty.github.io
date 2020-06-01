---
title: "Recursion vs. Dynamic Programming Using a Question from AMC8"
categories:
  - Programming
tags:
  - Python
  - Algorithms
---

## Recursion vs. Dynamic Programming Using a Question from AMC8



Here is an example from 2010 AMC8 Question $$25$$ (American Mathmatical Competition):  

Everyday at school, Jo climbs a flight of $$6$$ stairs. Jo can take the stairs $$1$$, $$2$$, or $$3$$ at a time. For example, Jo could climb $$3$$, then $$1$$, then $$2$$. In how many ways can Jo climb the stairs?  
  
$$\textbf{(A)}\ 13 \qquad\textbf{(B)}\ 18\qquad\textbf{(C)}\ 20\qquad\textbf{(D)}\ 22\qquad\textbf{(E)}\ 24$$ 

### Recursion  

This mathmatical question can be easily solved using the following python recursion code:
{% highlight python linenos %}
def stairs(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return stairs(x - 1) + stairs(x - 2) + stairs(x - 3)
print(stairs(6))
{% endhighlight %}

But, what if there is a quicker way? Let's try using dynamic progamming.

### Dynamic Programming

We can start with $$\text{step}_1$$ as the last step, $$\text{step}_2$$ as the second to last step, and $$\text{step}_3$$ as the third to last step. According to the recursion code, if $$x$$ is the current step, we have $$\text{step}_x = \text{step}_{x-1} + \text{step}_{x- 2} + \text{step}_{x - 3}.$$

Writing it in the dynamic programming way, we get

{% highlight python linenos %}
def stairs(x):
    step1 = 1 # stair 1
    step2 = 2 # stair 2
    step3 = 4 # stair 3

    run = 0
    # This is x - 3, and not x because using this method,
    # it starts from the stair 4
    while run < x - 3:
      temp = step1
      step1 = step2
      step2 = step3
      step3 = temp + step1 + step2
      run += 1
    return step3
print(stairs(6))
{% endhighlight %}

which runs much faster than recusion.