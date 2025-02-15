# this is the singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly:
    def __init__(self):
        self.head = None

    def adding(self, data):
        first_node = Node(data)

        if (self.head == None):
            self.head = first_node
            return

        temp = self.head

        while (temp.next != None):
            temp = temp.next

        temp.next = first_node

    def displaying(self):
        teh = self.head

        while (teh != None):
            print(teh.data)
            teh = teh.next


dll = Singly()
dll.adding(10)
dll.adding(30)

dll.displaying()

