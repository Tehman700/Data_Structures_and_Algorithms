# class TaskNode:
#     def __init__(self, task_name):
#         self.task_name = task_name
#         self.next = None
#
#
# class CircularScheduler:
#     def __init__(self):
#         self.head = None
#
#     def add_task(self, task_name):
#         new_task = TaskNode(task_name)
#         if not self.head:
#             self.head = new_task
#             self.head.next = self.head  # Circular link
#             return
#
#         temp = self.head
#         while temp.next != self.head:
#             temp = temp.next
#         temp.next = new_task
#         new_task.next = self.head  # Circular link
#
#     def run_tasks(self, cycles):
#         if not self.head:
#             print("No tasks to execute.")
#             return
#
#         temp = self.head
#         for _ in range(cycles):
#             print(f"Executing Task: {temp.task_name}")
#             temp = temp.next  # Move to the next task
#
#
# # Example Usage:
# scheduler = CircularScheduler()
# scheduler.add_task("Task A")
# scheduler.add_task("Task B")
# scheduler.add_task("Task C")
#
# print("Task Execution Order:")
# scheduler.run_tasks(6)  # Runs tasks cyclically
























# MEDIUM QUESTION NUMBER 02

# class Node:
#     def __init__(self,data):
#         self.next = None
#         self.prev = None
#         self.data = data
#
#
# class Doubly_Linked_List:
#     def __init__(self):
#         self.head = None
#
#     def adding_at_end(self,data):
#         latest_node = Node(data)
#
#         if(self.head == None):
#             self.head = latest_node
#             return
#
#         temp = self.head
#         while(temp.next != None):
#             temp = temp.next
#
#         temp.next = latest_node
#         latest_node.prev = temp
#
#
#     def display(self):
#         temp = self.head
#
#         while(temp != None):
#             print(temp.data)
#             temp = temp.next
#
#
#
#     def sorting_the_nodes_highest_score(self):
#
#         if self.head is None:
#             print("List is empty, nothing to sort.")
#             return
#
#         swapped = True
#         while swapped:
#             swapped = False
#             temp = self.head
#             while temp.next:
#                 if temp.data < temp.next.data:  # Sorting in descending order
#                     temp.data, temp.next.data = temp.next.data, temp.data  # Swap values
#                     swapped = True
#                 temp = temp.next
#
#
#
#
# dll = Doubly_Linked_List()
# dll.adding_at_end(10)
# dll.adding_at_end(30)
# dll.adding_at_end(80)
# dll.display()
# print("\n\n\n")
# dll.sorting_the_nodes_highest_score()
# dll.display()































# MEDIUM QUESTION NUMBER 03

class Node:
    def __int__(self,data):
        self.data = data
        self.next =None
        self.prev =None



class Round_Robin:
    def __init__(self):
        self.head =None

    def adding_processes(self,data):
        latest_node = Node(data)

        if(self.head == None):
            self.head = latest_node
            return

        temp = self.head
        while(temp.next != None):
            temp = temp.next

        temp.next = latest_node
        latest_node.prev = temp



    def display(self):

        curr = self.head

        while(curr != None):
            print(curr.data)
            curr = curr.next


ty = Round_Robin()
ty.adding_processes(56)
ty.adding_processes(45)
ty.display()


