# Big O for List Operations

## Example List

```python
my_list = [11, 3, 23, 7]
```

### Operations with O(1) – Constant Time

```python
my_list.append(17)  # Adds element at the end
my_list.pop()       # Removes element from the end
```

- **Reason:** No reindexing required; the operation takes **constant time**.

### Operations with O(n) – Linear Time

```python
my_list.pop(0)        # Removes element from the start
my_list.insert(0, 11) # Inserts element at the start
```

- **Reason:** All elements **must be reindexed**, so the operation scales with the list size `n`.
- **Important Note:** Big O always measures the **worst-case scenario**, not the average.
- Even if it looks like "1/2 n" on average, the **constant factor is dropped**, so complexity remains **O(n)**.

### Searching in Lists

- **Looping through a list** to find an element → **O(n)**.
- **Accessing an element by index** directly → **O(1)**.

### Reference

- More details on Big O for Python data structures: [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
