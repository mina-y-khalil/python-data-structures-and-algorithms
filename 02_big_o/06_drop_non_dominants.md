# Simplification Technique: Drop Non-Dominants

## Example

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)  # Nested loop runs in O(n²) time

    for k in range(n):
        print(k)  # Single loop runs in O(n) time

print_items(10)
```

### Explanation

- The **nested loop** runs in **O(n²)** → prints 100 items for n = 10.
- The **single loop** runs in **O(n)** → prints 10 items for n = 10.
- **Total time complexity:** O(n²) + O(n)
- **Drop Non-Dominants Rule:**
  - When combining complexities, **we only keep the dominant term** because it has the greatest effect as n grows.
  - Here, O(n²) dominates O(n), so the final **time complexity is O(n²)**.
