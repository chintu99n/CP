class StackUsingQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        # Get the current size of the queue
        n = len(self.queue)
        # Add the new item to the end of the queue
        self.queue.append(item)
        # Rotate the queue to bring the new item to the front
        for _ in range(n):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for item in self.queue:
                print(item)


# Create a stack object
stack = StackUsingQueue()
print("stack implementation using queue")
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item to push onto the stack: ")
        stack.push(item)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped item:", popped_item)
    elif choice == '3':
        peek_item = stack.peek()
        if peek_item is not None:
            print("Top element:", peek_item)
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
