# Node class
class Node:
    def __init__(self, data):
        self.data = data      # Assign data
        self.next = None      # Initialize next as None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize head

    # Function to print linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__ == "__main__":
    # Start with empty list
    list = LinkedList()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link nodes
    list.head.next = second
    second.next = third

    # Print linked list
    list.printList()
