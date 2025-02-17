class MessageNode:
    def __init__(self, message):
        self.message = message
        self.prev = None
        self.next = None

class ChatHistory:
    def __init__(self):
        self.head = None
        self.current = None  # Pointer to navigate through messages

    def add_message(self, message):
        new_message = MessageNode(message)
        if self.head is None:
            self.head = new_message
            self.current = new_message
        else:
            temp = self.head
            while temp.next:  # Move to the last message
                temp = temp.next
            temp.next = new_message
            new_message.prev = temp

    def navigate_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print("Previous Message:", self.current.message)
        else:
            print("No previous messages!")

    def navigate_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("Next Message:", self.current.message)
        else:
            print("No more messages!")

    def display_chat(self):
        temp = self.head
        print("\n Chat History:")
        while temp:
            print("", temp.message)
            temp = temp.next
        print("")

# Example Usage
chat = ChatHistory()
chat.add_message("Hey! How are you?")
chat.add_message("I'm good! What about you?")
chat.add_message("Just chilling. What's up?")
chat.add_message("Nothing much, just coding.")

chat.display_chat()

chat.navigate_back()  # Move to previous message
chat.navigate_back()  # Move to another previous message
chat.navigate_forward()  # Move forward



























# Advanced Task 02 DSA Lab


class ActionNode:
    def __init__(self, action):
        self.action = action
        self.prev = None
        self.next = None

class UndoRedoSystem:
    def __init__(self):
        self.head = None
        self.current = None  # Keeps track of the current action

    def perform_action(self, action):
        new_action = ActionNode(action)

        if self.head is None:
            self.head = new_action
            self.current = new_action
        else:
            self.current.next = new_action
            new_action.prev = self.current
            self.current = new_action

        print(f"Performed action: {action}")

    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f" Undo: Back to '{self.current.action}'")
        else:
            print("Nothing to undo!")

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f" Redo: Moved to '{self.current.action}'")
        else:
            print(" Nothing to redo!")

    def display_history(self):
        temp = self.head
        print("\n Action History:")
        while temp:
            print(f" {temp.action}")
            temp = temp.next
        print("")

# Example Usage
editor = UndoRedoSystem()
editor.perform_action("Typed: Hello World")
editor.perform_action("Bolded: Hello World")
editor.perform_action("Deleted: World")

editor.display_history()

editor.undo()  # Undo last action (deleting "World")
editor.undo()  # Undo bolding
editor.redo()  # Redo bolding













# Advanced Problem 03 DSA Lab 05

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doubly:
    def __init__(self):
        self.head = None

    def adding_history_navigation(self,data):
        latest_node = Node(data)

        if(self.head == None):
            self.head = latest_node
            return

        temp = self.head
        while(temp.next != None):
            temp = temp.next

        temp.next = latest_node
        latest_node.prev = temp


    def forward_navigation(self):
        current = self.head

        while(current != None):
            print(current.data)
            current = current.next


    def backward_navigation(self):
        current = self.head

        while(current.next):
            current = current.next
        while(current):
            print(current.data)
            current = current.prev


obj = Doubly()
obj.adding_history_navigation("Medium Articles")
obj.adding_history_navigation("Youtube")
obj.adding_history_navigation("Searched on ChatGPT")
obj.adding_history_navigation("Navigated to the Darkweb")

obj.forward_navigation()
print("\n\n\n")
obj.backward_navigation()