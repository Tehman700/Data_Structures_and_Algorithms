class TaskNode:
    def __init__(self, task_name):
        self.task_name = task_name
        self.next = None


class CircularScheduler:
    def __init__(self):
        self.head = None

    def add_task(self, task_name):
        new_task = TaskNode(task_name)
        if not self.head:
            self.head = new_task
            self.head.next = self.head  # Circular link
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_task
        new_task.next = self.head  # Circular link

    def run_tasks(self, cycles):
        if not self.head:
            print("No tasks to execute.")
            return

        temp = self.head
        for _ in range(cycles):
            print(f"Executing Task: {temp.task_name}")
            temp = temp.next  # Move to the next task


# Example Usage:
scheduler = CircularScheduler()
scheduler.add_task("Task A")
scheduler.add_task("Task B")
scheduler.add_task("Task C")

print("Task Execution Order:")
scheduler.run_tasks(6)  # Runs tasks cyclically
