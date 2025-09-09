# Linked List - Pop Method Notes

## Concept

- **Pop** removes the **last node (tail)** from a linked list.
- Pop is more **complicated than append** because we need to update the `tail` pointer and handle edge cases.

### Edge Cases

1. If the list is **empty**, there is nothing to remove.
2. If the list has **only one node**, removing it will set both `head` and `tail` to `None`.

### Logic

- To remove the tail, we need to find the **second-to-last node**.
- Use two variables:

  - `temp` → starts at `head`
  - `pre` → starts at `head`

- Move `temp` to the next node, and keep `pre` one node behind `temp`.
- When `temp` reaches the last node (`temp.next is None`):
  - Set `pre.next = None` → removes the last node
  - Update `tail = pre` → set new tail
- Decrease `length` by 1

---

## Implementation

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    # Append a new node at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Pop removes the last node
    def pop(self):
        if self.length == 0:           # empty list
            return None

        temp = self.head
        pre = self.head

        # If only one node exists
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        # Move through the list until temp reaches the last node
        while temp.next:
            pre = temp
            temp = temp.next

        pre.next = None                 # remove last node
        self.tail = pre                 # update tail
        self.length -= 1
        return temp                     # return popped node


# Example usage
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

popped_node = my_linked_list.pop()
print("Popped value:", popped_node.value if popped_node else None)
```

---

## Key Points

1. Pop requires **traversing the list** to find the second-to-last node.
2. Always handle **empty list** and **single-node list** as edge cases.
3. After popping, **update `tail`** and **decrease `length`**.
4. Returns the popped node so you can access its value if needed.
5. Works for both small and large linked lists.
