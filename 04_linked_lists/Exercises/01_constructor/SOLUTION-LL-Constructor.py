class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

"""
explaination and walkthrough:
first we will create the node class and create the constructor that will take in the value and set the value to be the value that we passed in and set the next to be None because when we create a new node it doesn't point to anything yet
then we will create the linked list class to make the linked list using the node class that we created and initialize the head and tail to be the new node that we created and set the length to be 1
                                                                                                                    
"""