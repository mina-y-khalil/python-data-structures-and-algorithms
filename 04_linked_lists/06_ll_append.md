# Linked List - Append Method Notes

## Concept

- **Appending** adds an item to the **end of the linked list**.
- If the linked list **already has items**, the `tail.next` will point to the new node, and the `tail` will be updated to the new node.
- If the linked list is **empty**, both `head` and `tail` will point to the new node.

---

## Implementation

```python
# Node class to represent each element
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# LinkedList class to manage nodes
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Append a new node at the end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            # If list is empty, head and tail both point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the last node to the new node
            self.tail.next = new_node
            # Update the tail to the new node
            self.tail = new_node
        self.length += 1
        return True


# Example usage
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

# Function to print the list values
def print_list(linked_list):
    temp = linked_list.head
    while temp:
        print(temp.value)
        temp = temp.next

print_list(my_linked_list)
```

**Key Points**

1. `Node` stores `value` and `next` pointer.
2. `LinkedList` keeps track of `head`, `tail`, and `length`.
3. Appending updates the `tail` pointer correctly.
4. Works for both **empty** and **non-empty** lists.
