# Classes in Data Structures and Algorithms

## Importance of Classes

- Almost **everything in data structures and algorithms uses classes**.
- Classes can be thought of as **templates or blueprints** (like a cookie cutter).
- They allow you to **create multiple objects** with shared attributes and behaviors (methods).
- Using classes helps organize code, **encapsulate data**, and make structures reusable.

## Example: Cookie Class

```python
class Cookie:
    def __init__(self, color):
        # Constructor method to initialize the object's color
        self.color = color

    def get_color(self):
        # Method to get the current color of the cookie
        return self.color

    def set_color(self, color):
        # Method to update the color of the cookie
        self.color = color

# Creating two cookie objects
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

# Accessing the colors using the getter method
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# Changing the color of cookie_one
cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
```

### Explanation

1. **`class Cookie`**

   - Defines a **new type of object** called `Cookie`.
   - Acts like a **cookie cutter**: every object created will have the same structure.

2. **`__init__` method**

   - Special method called **constructor**.
   - Initializes the object when it is created.
   - Example: `cookie_one = Cookie('green')` → `color` is set to `'green'`.

3. **Attributes (`self.color`)**

   - Each object has its own **copy of the attribute**.
   - Changing one object’s attribute does not affect another object.

4. **Methods (`get_color`, `set_color`)**

   - **Getter** method returns the current value of an attribute.
   - **Setter** method updates the attribute.
   - Encapsulates behavior so you don’t directly modify attributes outside the class.

5. **Creating Objects**

   - `cookie_one` and `cookie_two` are **two separate instances** of the `Cookie` class.
   - They **share the class structure** but maintain independent states.

6. **Key Takeaways**
   - Classes allow **modularity and code reuse**.
   - **Every data structure (linked lists, stacks, queues, etc.) is often implemented as a class**.
   - Methods inside classes **define operations** for the objects (like adding, deleting, or updating data in structures).
   - Using classes prepares you for **complex structures** in algorithms while keeping your code clean and organized.
