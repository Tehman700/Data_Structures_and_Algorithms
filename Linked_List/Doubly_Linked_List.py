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

        # 10 20 __30___ 40
        if (prev_node == None):
            print("Previous cannot be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if(new_node.next):
            new_node.next.prev = new_node


    def display_forward(self):
        current = self.head

        while(current != None):
            print(current.data)
            current = current.next


    def display_backward(self):
        current = self.head

        while(current.next):
            current = current.next
        while(current):
            print(current.data)
            current = current.prev




dll = Doubly()
dll.insert_end(10)
dll.insert_end(30)
dll.insert_end(40)
dll.display_forward()
print("/n/n/n")

dll.insert_beg(12)
dll.insert_end(455)
dll.display_backward()


