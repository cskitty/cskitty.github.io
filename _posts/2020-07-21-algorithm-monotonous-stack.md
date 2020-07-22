---
title: "Monotonous Stack"
categories:
  - Programming
tags:
  - Algorithms
  - Java
  - Monotonous Stack
---


## Monotonous Stack

A monotonic Stack is a data structure the elements from the front to the end is strictly either increasing or decreasing. For example, there is an line at the hair salon, and you would naturally start from the end of the line. However, if you are allowed to kick out any person that you can win at a fight, if every one follows the rule, then the line would start with the most powerful man and end up with the weakest one. This is an example of monotonic decreasing queue. We have either increasing or decreasing stack.

Monotonic increasing stack: to push an element e, starts from the stack top element, we pop out element s>e;  
Monotonic decreasing stack: we pop out element s<e.  


### Stock Spanner

[Leetcode  Online Stock Span](https://leetcode.com/problems/online-stock-span/)  

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.  

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.  

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].  



Example 1:  

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]  
Output: [null,1,1,1,2,1,4,6]  
Explanation:   
First, S = StockSpanner() is initialized.  Then:  
S.next(100) is called and returns 1,  
S.next(80) is called and returns 1,  
S.next(60) is called and returns 1,  
S.next(70) is called and returns 2,  
S.next(60) is called and returns 1,  
S.next(75) is called and returns 4,  
S.next(85) is called and returns 6.  

Note that (for example) S.next(75) returned 4, because the last 4 prices  
(including today's price of 75) were less than or equal to today's price.  

{% highlight java linenos %}
class StockSpanner {

    Stack<Pair<Integer, Integer>> m_stack;

    StockSpanner() {

        m_stack = new Stack<Pair<Integer, Integer>>();
    }


    public int next(int price) {

        if (m_stack.isEmpty()) {
            m_stack.push(new Pair<Integer, Integer>(price, 1));
            return 1;
        }
        else {
            int count = 1;
            while (! m_stack.isEmpty()) {
                Pair<Integer, Integer> past = m_stack.peek();

                if (past.getKey() <= price) {            
                    count += past.getValue();    
                    m_stack.pop();
                }
                else {
                    break;
                }

            }
            m_stack.push(new Pair<Integer, Integer>(price, count));
            return count;
        }

    }
}
{% endhighlight %}
