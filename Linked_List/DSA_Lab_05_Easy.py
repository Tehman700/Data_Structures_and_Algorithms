# Task 01 Implementinga a Basic Class for DLL that supports Append, Display, Delete from start

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Custom_Doubly:
    def __init__(self):
        self.head = None

    def appending(self,data):

        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return

        current = self.head
        while(current.next !=None):
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head

        while(current != None):
            print(current.data)
            current = current.next



    def delete_from_start(self):

        # 10, 20, 30
        current = self.head
        self.head = current.next


    def length_of_list(self):

        current = self.head
        count = 1
        while(current != None):
            count +=1
            current = current.next


        return count


dll =Custom_Doubly()
dll.appending(10)
dll.appending(20)
dll.appending(56)
dll.appending(78)
dll.display()
dll.delete_from_start()
print("\n\n")
dll.display()
#
print(dll.length_of_list())



















# Task 02 CLL Traversal Implementing a  Circular Linked List and Traverse it in a loop

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None  # Doubly linked feature
#
# class CircularDoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#
#         if self.head is None:  # If the list is empty
#             self.head = new_node
#             self.head.next = self.head  # Circular link
#             self.head.prev = self.head  # Circular link for doubly linked list
#             return
#
#         # Traverse to the last node
#         last = self.head.prev  # Using previous pointer
#
#         last.next = new_node
#         new_node.prev = last  # Link new node back to last node
#
#         new_node.next = self.head  # Circular link to head
#         self.head.prev = new_node  # Circular link from head back to new node
#
#     def display(self):
#         if self.head is None:
#             print("The list is empty!")
#             return
#
#         temp = self.head
#         while True:
#             print(temp.data, end=" ⇄ ")  # Print data
#             temp = temp.next
#             if temp == self.head:  # Stop when we reach back to the head
#                 break
#         print("(Back to Head)")
#
# # Create Circular Doubly Linked List
# cdll = CircularDoublyLinkedList()
# cdll.append(10)
# cdll.append(20)
# cdll.append(30)
# cdll.append(67)
#
# print("Circular Doubly Linked List Traversal:")
# cdll.display()

























# Task 03 DLL Reverse Traversal: Implement a method to print DLL in reverse Order

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
#
# class Doubly:
#     def __init__(self):
#         self.head = None
#
#     def insert_end(self, data):
#
#         new_node = Node(data)
#         if (self.head == None):
#             self.head = new_node
#             return
#
#         temp = self.head
#         while (temp.next != None):
#             temp = temp.next
#
#         temp.next = new_node
#         new_node.prev = temp
#
#
#     def display_backward(self):
#         current = self.head
#
#         while(current.next):
#             current = current.next
#         while(current):
#             print(current.data)
#             current = current.prev
#
#
#
# dll = Doubly()
# dll.insert_end(30)
# dll.insert_end(40)
# dll.insert_end(78)
# dll.display_backward()

















# Task 04

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class CircularLinkedList:
#     def __init__(self):
#         self.head = None
#
#     # Append a node to the circular linked list
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.head.next = self.head  # Circular link
#             return
#
#         temp = self.head
#         while temp.next != self.head:  # Traverse to the last node
#             temp = temp.next
#
#         temp.next = new_node
#         new_node.next = self.head  # Circular link back to head
#
#     # Delete a node by value
#     def delete(self, key):
#         if not self.head:
#             print("List is empty!")
#             return
#
#         temp = self.head
#         prev = None
#
#         # Case 1: Deleting the Head Node
#         if temp.data == key:
#             if temp.next == self.head:  # If only one node exists
#                 self.head = None
#                 return
#
#             # Find the last node to update its next pointer
#             last = self.head
#             while last.next != self.head:
#                 last = last.next
#
#             self.head = temp.next  # Move head to next node
#             last.next = self.head  # Update last node to new head
#             return
#
#         # Case 2 & 3: Deleting a Middle or Last Node
#         prev = self.head
#         temp = self.head.next
#         while temp != self.head:
#             if temp.data == key:
#                 prev.next = temp.next
#                 return
#             prev = temp
#             temp = temp.next
#
#         print("Node not found in the list!")
#
#     # Traverse and print the Circular Linked List
#     def display(self):
#         if not self.head:
#             print("Circular Linked List is empty!")
#             return
#
#         temp = self.head
#         while True:
#             print(temp.data, end=" → ")
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print("(Back to Head)")
#
#
# # Example Usage:
# cll = CircularLinkedList()
# cll.append(10)
# cll.append(20)
# cll.append(30)
# cll.append(40)
#
# print("Circular Linked List Before Deletion:")
# cll.display()
#
# cll.delete(10)  # Delete Head
# print("\nAfter Deleting 10 (Head):")
# cll.display()
#
# cll.delete(30)  # Delete Middle Node
# print("\nAfter Deleting 30:")
# cll.display()
#
# cll.delete(40)  # Delete Last Node
# print("\nAfter Deleting 40:")
# cll.display()

