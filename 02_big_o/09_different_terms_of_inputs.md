# Big O with Multiple Inputs

## Example

```python
def print_items(a, b):
    for i in range(a):
        print(i)  # Runs in O(a) time

    for j in range(b):
        print(j)  # Runs in O(b) time

print_items(1, 10)
```

### Explanation

- When inputs are **different variables** (`a` and `b`), time complexity is **O(a + b)**.
- If there were **nested loops** over `a` and `b`, the complexity would be **O(a \* b)**.
- **Dropping constants** only applies when you have multiples of the same input (like O(2n) → O(n)).
- This technique helps accurately measure how algorithms scale with **multiple independent inputs**.
