## When should I consider using DP?

1. The problem will be asking for an optimal value (max or min) of something or the number of ways to do something.
    What is the minimum cost of doing ...
    What is the maximum profit of ...
    How many ways are there to ...
    What is the longest possible ...


2. At each step, you need to make a "decision", and decisions affect future decisions.
    A decision could be picking between two elements
    Decisions affecting future decisions could be something like "if you take an element x, then you can't take an element y in the future"

Note on the first characteristic: not all problems that are in these formats are meant to be solved with DP, and not all DP problems are in one of those formats. However, for a general guideline, these characteristics hold up very well.

The second characteristic is usually what differentiates greedy and DP. The idea behind greedy is that local decisions do not affect other decisions.

### State

State refers to a set of variables that can fully describe a scenario. When we looked at tree problems, every recursive call to dfs took node, and maybe some other variables as arguments. These arguments represent the state.

The following are common state variables that you should think about:

- An index along an input string, array, or number. This is the most common state variable and will be a state variable in almost all problems, and is frequently the only state variable. With Fibonacci, the "index" refers to the current Fibonacci number. If you are dealing with an array or string, then this variable will represent the array/string up to and including this index. For example, if you had nums = [0, 1, 2, 3, 4] and you had a state variable i = 2, then it would be like if nums = [0, 1, 2] was the input.
- A second index along an input string or array. Sometimes, you need another index variable to represent the right bound of the array. Again, if you had nums = [0, 1, 2, 3, 4] and two state variables along the input, let's say i = 1 and j = 3, then it would be like nums = [1, 2, 3] - we are only considering the input between and including i and j.
- Explicit numerical constraints given in the problem. This will usually be given in the input as k. For example, "you are allowed to remove k obstacles". This state variable would represent how many more obstacles we are allowed to remove.
- A boolean to describe a status. For example, "true if currently holding a package, false if not".

Important Framework for Solving Problems : https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/712/dynamic-programming/4540/