# Big O Example: O(log n) – Logarithmic Time

## Example: Binary Search

- Suppose we have a **sorted list** from 1 to 8: `[1, 2, 3, 4, 5, 6, 7, 8]`
- To find a number efficiently:
  1. **Cut the list into 2 halves**.
  2. Search the **first half**; if not found, search the **second half**.
  3. Repeat the process, halving the remaining list each time until the number is found.
- For 8 elements:
  - Step 1: 8 → 4 elements
  - Step 2: 4 → 2 elements
  - Step 3: 2 → 1 element → found
- This took **3 steps**, which is `log₂ 8 = 3`
  - **Explanation:** 2³ = 8 → we divide by 2 each step until 1 element remains.

### Time Complexity

- **Binary Search:** O(log n) – very **flat growth**, highly efficient for large datasets.

---

# Big O Example: O(n log n) – Efficient Sorting

- Many efficient sorting algorithms (like **Merge Sort**, **Quick Sort**) use a **divide-and-conquer approach**.
- Time Complexity: O(n log n)
  - `log n` → number of times the list is divided
  - `n` → number of operations to combine/merge elements
- **Note:** Different from binary search, but still very efficient for sorting large lists.
