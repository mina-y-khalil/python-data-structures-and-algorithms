# Linked Lists Notes

- A **linked list** does **not have indexing** like arrays or Python lists.
- Unlike arrays, which occupy **contiguous memory**, nodes in a linked list can be stored **anywhere in memory**.  
  Each node contains a **pointer/reference** to the next node, so the order is maintained even if the nodes are scattered.
- A linked list typically has:
  - **Head:** a variable pointing to the **first node** in the list.
  - **Tail:** a variable pointing to the **last node** in the list.
- Each node contains:
  - The **value/data** it holds.
  - A **pointer/reference** to the **next node** (or `None` if it's the last node).

**Visual Representation:**

```
Head -> [Node1 | next] -> [Node2 | next] -> [Node3 | next] -> Tail(None)
```
