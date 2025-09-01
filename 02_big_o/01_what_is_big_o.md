# Big O (Time and Space Complexity) Notes

## 1. Overview

- **Big O** is a fundamental concept in **Data Structures and Algorithms**.
- It is used to **compare the efficiency of two pieces of code** that perform the same function.

## 2. Time Complexity

- **Time complexity** measures **how long the code takes to execute**.
- Helps identify which implementation runs faster as input size grows.
- Example:
  ```text
  Code A: O(n)
  Code B: O(n^2)
  ```
  Even if both produce the same result, Code A is faster for large inputs.

## 3. Space Complexity

- **Space complexity** measures **how much memory the code uses** while running.
- Efficient code should **minimize both time and memory usage**.
- Example: Using a linked list instead of creating a new array can save memory.

## 4. Key Points

- Big O is about **scaling**: how the code behaves as input size increases.
- Always consider **both time and space** to write efficient and optimized code.
