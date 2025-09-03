# Linked List Big O Notes

### Operations and Complexity

1. **Adding a node at the end (append)**

   - **O(1)** if we maintain a tail pointer.
   - This is one operation regardless of the number of nodes.

2. **Removing a node at the end (pop)**

   - **O(n)** because we must iterate from the head to find the node **before the tail** to update the tail pointer.

3. **Adding a node at the beginning (prepend)**

   - **O(1)** because we make the new node point to the current head, then update the head to the new node.

4. **Removing the first node (pop first)**

   - **O(1)** because we update the head to point to the second node.

5. **Adding a node in the middle**

   - **O(n)** because we start from the head and iterate to the desired position.
   - Once there, we adjust the `next` pointers of the surrounding nodes.

6. **Removing a node from the middle**

   - **O(n)** because we must iterate to the node just before the one to remove, then adjust pointers.

7. **Lookup by index**

   - **O(n)** because we must iterate through the list to reach the desired index.

8. **Lookup by value**
   - **O(n)** because we may need to check each node until the value is found.

---

### Big O Table for Linked Lists vs Arrays

| Operation           | Linked List | Array |
| ------------------- | ----------- | ----- |
| Append              | O(1)        | O(1)  |
| Pop (end)           | O(n)        | O(1)  |
| Prepend (add first) | O(1)        | O(n)  |
| Pop First           | O(1)        | O(n)  |
| Insert (middle)     | O(n)        | O(n)  |
| Remove (middle)     | O(n)        | O(n)  |
| Lookup by Index     | O(n)        | O(1)  |
| Lookup by Value     | O(n)        | O(n)  |
