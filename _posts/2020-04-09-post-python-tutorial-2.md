---
title: "Python Tutorial - Lesson 2 : Lists and Loops"
categories:
  - Projects
  - Tutorials
tags:
  - Python
  - Beginner
  - Turtle
---

## Python Tutorial - Lesson 2 : Lists and Loops

### Python Basics: List

### Python Basics: Loop

<div>
    <p>For loops tell the computer to do something <em>for</em> a bunch of values. They're particularly useful when we want the same "thing" done several times in succession.</p>
    <p>Let's say, for example, we wanted to print out the numbers 0-5 in sequence. We could write print statements:</p>
    <iframe class="embedded-trinket embedded-content" src="//trinket.io/embed/python?start=result#code=print%200%0Aprint%201%0Aprint%202%0Aprint%203%0Aprint%204%0Aprint%205" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen="allowfullscreen"></iframe>
    <p>But that seems tedious!</p>
    <h2 id="for-loop-and-a-list" class="class-anchor">For loop and a list</h2>
    <p>We could also put the numbers we want in a list and then print each thing in the list:</p>
    <iframe class="embedded-trinket embedded-content" src="//trinket.io/embed/python?start=result#code=numbers%20%3D%20%5B0%2C1%2C2%2C3%2C4%2C5%5D%0Afor%20n%20in%20numbers%3A%0A%20%20%20%20print%20n" width="100%" height="150" frameborder="0" marginwidth="0"
        marginheight="0" allowfullscreen="allowfullscreen"></iframe>
    <p>That seems a little better.</p>
    <p>On the first line, we make a list, called <code>numbers</code>, and fill it with the numbers we wish to print: <code>[0, 1, 2, 3, 4, 5]</code>.</p>
    <p>On the second line, we write <code>for n in numbers:</code> This is the for loop part, and converted into English, it says "Look at the list called <code>numbers</code>. For each element in it, grab the element and temporarily
        call it <code>n</code>. Then .. "</p>
    <p>On the third line, we write <code>print</code> just once, and ask Python to <code>print n</code>. That's the same as asking Python to print out the value in the variable container <code>n</code> &ndash; which we know is one of
        the elements in the list from the second line!</p>
    <h2 id="for-loop-and-range-function" class="class-anchor">For loop and <code>range( .. )</code> function</h2>
    <p>There's a special <code>range( .. )</code> function built into Python that gives back a range of numbers. Try running the code below:</p>
    <iframe class="embedded-trinket embedded-content" src="//trinket.io/embed/python?start=result#code=for%20n%20in%20range(0%2C%206)%3A%0A%20%20%20%20print%20n" width="100%" height="150" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen="allowfullscreen"></iframe>
    <p>Here we get the same result, though we didn't have to make a list ourselves. The <code>range(0, 6)</code> function gave us one that went from 0 (inclusive) to 6 (exclusive.)</p>
    <h2 id="general-form-of-a-for-loop" class="class-anchor">General form of a for loop</h2>
    <p>The general form of a for loop looks like this:</p>
    <pre><code>for temp_variable in some_sort_of_list:
do_something
</code></pre>
    <h2 id="doing-things-with-for-loops" class="class-anchor">Doing things with for loops</h2>
    <p>For loops end up being pretty useful. Take a look at the code below; when you think you know what it does, click 'Run', and take a look:</p>
    <iframe class="embedded-trinket embedded-content" src="//trinket.io/embed/python?start=result#code=sum%20%3D%200%0Afor%20x%20in%20range(0%2C%20101)%3A%0A%20%20%20%20sum%20%3D%20sum%20%2B%20x%0A%0Aprint%20sum" width="100%" height="200" frameborder="0"
        marginwidth="0" marginheight="0" allowfullscreen="allowfullscreen"></iframe>
    <p>That for loop sums the numbers between 0 and 100.</p>
</div>
