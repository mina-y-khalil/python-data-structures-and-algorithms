# Python Pointers and Mutability Notes

Pointers in Python behave differently depending on the data type.

---

## 1. Example with Integers (Immutable)

```python
num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))  # memory address of num1
print("num2 points to:", id(num2))    # same as num1

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))    # now points to a different memory address
```

**Explanation:**

- Integers are **immutable**, meaning their value cannot be changed in memory.
- When `num2` is updated, Python creates a **new integer object** in memory and points `num2` to it.
- `num1` remains unchanged.

---

## 2. Example with Dictionaries (Mutable)

```python
dict1 = {'value': 11}
dict2 = dict1

print("\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))  # same memory address

dict2['value'] = 22  # mutates the object, does not create a new one

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))  # memory address unchanged
```

**Explanation:**

- Dictionaries are **mutable**, so updating a value through `dict2` changes the same object `dict1` points to.
- Both `dict1` and `dict2` still point to the **same dictionary in memory**.

---

## 3. General Notes on Mutability and References

- Nodes in **data structures** and **algorithms** (like linked lists) behave similarly to dictionaries.
- If two variables point to the same node, updating the node from any variable affects the object itself.
- You **can also reassign** a variable to point to another object:

```python
dict2 = dict3  # dict2 now points to dict3 instead of dict1
```

- After this reassignment, if no variable points to `dict1`, Python will eventually remove it via **garbage collection**.

---

### Key Takeaways

1. **Immutable types** (int, float, tuple, string) cannot be changed in memory; updates create new objects.
2. **Mutable types** (dict, list, set, custom objects) can be changed in place; updates affect all references.
3. **Garbage collection** automatically cleans up objects that are no longer referenced.
