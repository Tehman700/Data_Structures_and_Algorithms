# Implementing a Doubly Linked List in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doubly:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):

        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            return

        temp = self.head
        while (temp.next != None):
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_specific(self, prev_node, data):
        pass

# class Singly:
#     def __init__(self):
#         self.head = None

#     def adding(self, data):
#         first_node = Node(data)

#         if(self.head == None):
#             self.head = first_node
#             return

#         temp = self.head

#         while(temp.next != None):
#             temp = temp.next

#         temp.next = first_node