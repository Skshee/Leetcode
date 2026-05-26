`Use BFS When`:
1. You want the shortest path (in unweighted graphs).

- BFS explores neighbors level-by-level, so the first time you reach the destination, it's guaranteed to be the shortest.

- Example: Finding the minimum number of moves in a maze or grid.

2. You need to explore all nodes within k steps.

- BFS is great for problems like "all nodes at distance k" or "minimum steps to reach a target."

- The problem has multiple solutions and you want the optimal one.

- Example: Word ladder (transform one word to another using a dictionary of words).

3. You're working with a tree or graph that is wide rather than deep.


`Use DFS When`:
1. You want to explore all possible paths (exhaustive search).

- Useful in puzzles, games, and simulations.

- Example: Backtracking problems like Sudoku, N-Queens.

2. You need to traverse all nodes and do something at each (like topological sort, cycle detection).

- DFS is ideal for graph algorithms such as:

- Detecting cycles in directed graphs.

- Finding connected components.

3. You're looking for a specific structure like a path or component without regard to length.

- Example: Checking if a path exists between two nodes.

- Memory is a concern.

- DFS uses less memory (just a stack), while BFS can consume a lot for wide graphs.

`RULE OF THUMB:`

| Problem Type                          | Preferred Algorithm |
| ------------------------------------- | ------------------- |
| Shortest Path in Unweighted Graph     | BFS                 |
| Path Existence Check                  | DFS or BFS          |
| All Possible Solutions (Backtracking) | DFS                 |
| Level Order Traversal (like trees)    | BFS                 |
| Topological Sort / Strong Components  | DFS                 |

- In an interview, you may be asked some trivia regarding BFS vs DFS, such as their drawbacks. The main disadvantage of DFS is that you could end up wasting a lot of time looking for a value. Let's say that you had a huge tree, and you were looking for a value that is stored in the root's right child. If you do DFS prioritizing left before right, then you will search the entire left subtree, which could be hundreds of thousands if not millions of operations. Meanwhile, the node is literally one operation away from the root. The main disadvantage of BFS is that if the node you're searching for is near the bottom, then you will waste a lot of time searching through all the levels to reach the bottom.
