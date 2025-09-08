# Python Linked List Example

```python
# Node class to represent each element in the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print all values in the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append a new node at the end of the linked list
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


# Example usage
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()
```

**Explanation:**

- `Node` stores a value and a reference to the next node.
- `LinkedList` manages the `head`, `tail`, and length of the list.
- `append()` adds a new node to the end of the list.
- `print_list()` traverses the list and prints all node values.

---

If you want, I can also add **`prepend`, `insert`, and `remove` methods** to make this linked list fully functional like a data structure in textbooks.

Do you want me to do that?
