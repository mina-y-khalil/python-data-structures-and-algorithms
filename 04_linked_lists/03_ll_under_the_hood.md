# Linked List Nodes (Under the Hood)

### What is a Node?

- A **node** is not just a value, it also contains a **pointer** to the next node.
- Conceptually, a node can be represented as a **dictionary**:

```python
{
  "value": 4,
  "next": None
}
```

---

### Adding a Node to the End

- To add a node at the end, we update the **last node's `next` pointer** to point to the new node:

```python
# Last node
{
  "value": 7,
  "next": {
    "value": 4,
    "next": None
  }
}
```

- A linked list also keeps track of:
  - **Head** → points to the first node
  - **Tail** → points to the last node

---

### Accessing Values in a Linked List

- Accessing nodes is done by following the `next` pointers:

```python
# Nested dictionary example
print(head['next']['next']['value'])
```

- In a linked list class, this would be:

```python
print(my_linked_list.head.next.next.value)
```

- Essentially, a linked list is a **list of nested dictionaries** (or objects in Python classes) connected via pointers.
