---
title: "Function Argument Passing in Python"
categories:
  - Programming
tags:
  - Python
  - Algorithms
---


## Function Argument Passing in Python

In C language, the function assigns the parameter value to a local variable and performs actions on it.  There are two ways of passing parameter to a function: pass by value or pass by reference:


### Pass by value
Pass by value means that a copy of the actual parameter’s value is made in memory, i.e. the caller and callee have two independent variables with the same value. If the callee modifies the parameter value, the effect is not visible to the caller.

### Pass by reference

Pass by reference means to pass the reference of an argument in the calling function to the corresponding formal parameter of the called function so that a copy of the address of the actual parameter is made in memory, i.e. the caller and the callee use the same variable for the parameter. If the callee modifies the parameter variable, the effect is visible to the caller’s variable.


Functions in Python also assigns parameter value to a local variable, but the assignment looks much different. Instead of storing a copy of the parameter value in the local variable, Python simply has the local variable refer to the value. This means the local variable now points to the object — the same object that is the parameter value — which is also pointed to by the parameter variable. In other words, the parameter value object can now be referred to by both the local and the parameter variables. This is similar to passing a pointer in C, as the function has direct access to the original object (not just a local copy of its value) and is able to manipulate it in place.


Things become complicated in Python when we passing mutable or immutable objects to function:
Here's the table of data types in Python and are immutable or not.

| Class        | Immutable?           |
| -------------   | ---------------------|  
| bool             | Yes |
| int             | Yes |
| float             | Yes |
| string             | Yes |
| tuple             | Yes |
| list             | No |
| set             | No |
| dict             | No |

If a function in Python is passing an immutable as argument, then the immutable variable won't be changed oustide of the function. It is effectively same as "pass by value".

In the example below, the variable a will print out still as 111 after calling increment(a).

{% highlight python linenos %}
def increment(n):
  n += 1

a = 111
increment(a)
print(a)
{% endhighlight %}


If a function in Python is passing a mutable as argument, then the mutable variable will be changed oustide of the function. It is effectively same as "pass by reference".

In the example below, the variable aList will print out still as [1,2,3] after calling increment(aList).

{% highlight python linenos %}
def increment(n):
  n.append(3)

a = [1,2]
increment(a)
print(a)
{% endhighlight %}
