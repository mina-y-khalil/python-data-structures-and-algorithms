# Linked List - Pop Method Notes

## Concept

- **Pop** removes the **last node (tail)** from a linked list.
- Pop is more **complex than append** because you need to update the `tail` pointer and handle special cases (edge cases).

---

## Edge Cases

1. **Empty list** → Nothing to remove.
2. **Single-node list** → Removing it sets both `head` and `tail` to `None`.

---

## Logic / Step by Step

1. Use two pointers:

   - `temp` → to traverse nodes.
   - `pre` → keeps track of the node before `temp`.

2. Start both at `head`.
3. Move `temp` forward until it reaches the last node. Keep `pre` one node behind.
4. When `temp.next is None` (temp is the last node):
   - Set `pre.next = None` → removes the last node.
   - Update `tail = pre` → assign new tail.
5. Decrease `length` by 1.
6. Return the removed node if you need its value.

> **Tip:** Always handle empty and single-node lists first to avoid errors.

---

## Implementation

```python
# Node class represents each element
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# LinkedList class manages nodes
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

        if self.length == 1:           # single-node list
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        # Traverse the list to find the last node
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

1. **Pop requires traversing the list** to find the second-to-last node.
2. Always check for **empty** and **single-node lists** first.
3. After popping, **update `tail`** and **decrease `length`**.
4. Returns the popped node so you can use its value if needed.
5. Works for both **small and large lists**.
6. Use pop carefully in **performance-critical** applications since it traverses the list, making it **O(n)** time complexity.
