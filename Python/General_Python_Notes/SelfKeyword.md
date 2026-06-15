# When to Use `self`

### Use `self` when:
- The variable needs to be shared across multiple methods.
- The variable represents the object's state.
- You want the value to persist after a method call.

```python
self.count = 0
self.result = []
```

### Don't use `self` when:
- The variable is only needed inside one method.
- A nested function can access it through closure.

```python
def solve(self):
    result = []

    def dfs(node):
        result.append(node.val)
```

### Use `nonlocal` when:
A nested function needs to modify a variable from the outer function.

```python
count = 0

def dfs():
    nonlocal count
    count += 1
```

### LeetCode Rule of Thumb

- Nested helper function → use local variables (`lst`, `count`) and `nonlocal` if needed.
- Separate class method → use `self.variable`.