# Simplifying Big O Notes

## 1. Drop Constants

- When calculating **Big O**, **constants are ignored** because they don’t change the growth rate as input size increases.

### Example:

```python
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)
```

- Analysis:
  - First loop: n operations
  - Second loop: n operations
  - Total: n + n = 2n
- Simplified Big O: **O(n)** (drop the constant `2`)
- Reason: Big O focuses on **growth rate**, not exact counts.
