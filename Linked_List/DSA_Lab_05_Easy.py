# Task 01 Implementinga a Basic Class for DLL that supports Append, Display, Delete from start

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


# class Custom_Doubly:
#     def __init__(self):
#         self.head = None
#
#     def appending(self,data):
#
#         new_node = Node(data)
#         if(self.head == None):
#             self.head = new_node
#             return
#
#         current = self.head
#         while(current.next !=None):
#             current = current.next
#
#         current.next = new_node
#         new_node.prev = current
#
#     def display(self):
#         current = self.head
#
#         while(current != None):
#             print(current.data)
#             current = current.next
#
#
#
#     def delete_from_start(self):
#
#         # 10, 20, 30
#         current = self.head
#         self.head = current.next
#
#
# dll =Custom_Doubly()
# dll.appending(10)
# dll.appending(20)
# dll.appending(30)
# dll.display()
# dll.delete_from_start()
# print("\n\n")
# dll.display()
#



