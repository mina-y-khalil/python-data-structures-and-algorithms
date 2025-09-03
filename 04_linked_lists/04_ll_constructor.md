# Linked List Constructor Notes

### Node Class

```python
class Node:
    def __init__(self, value):
        self.value = value  # store the value
        self.next = None    # pointer to the next node
```

### LinkedList Class Constructor

```python
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # create the first node
        self.head = new_node    # head points to the first node
        self.tail = new_node    # tail also points to the first node
        self.length = 1         # initial length of the list
```

**Usage Example:**

```python
my_linked_list = LinkedList(4)
# Now the linked list has one node with value 4
# head and tail both point to this node
# length = 1
```

---

### Common Methods Sharing the Constructor Logic

All of these methods **create a new node** using the value passed to them:

1. **Append** - Add a node to the **end** of the list:

```python
def append(self, value):
    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
```

2. **Prepend** - Add a node to the **beginning** of the list:

```python
def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
    self.length += 1
```

3. **Insert** - Add a node at a **specific index**:

```python
def insert(self, index, value):
    if index == 0:
        return self.prepend(value)
    if index >= self.length:
        return self.append(value)

    new_node = Node(value)
    temp = self.head
    for _ in range(index - 1):
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
```

**Key Takeaways:**

- All these methods **start by creating a new node**.
- The constructor is essentially a **special case** of prepend/append for the first node.
- After creating the first node, `head` and `tail` both point to it.
- The `length` keeps track of the number of nodes in the linked list.
