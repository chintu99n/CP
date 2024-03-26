class QueueUsingStack:
    def __init__(self):
        self.stack1 = []  # Used for enqueue operation
        self.stack2 = []  # Used for dequeue operation

    # Enqueue operation
    def enqueue(self, item):
        self.stack1.append(item)

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return -1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return -1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # Check if queue is empty
    def is_empty(self):
        return not self.stack1 and not self.stack2


if __name__ == "__main__":
    queue = QueueUsingStack()

    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if queue is empty")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter element to enqueue: "))
            queue.enqueue(element)
        elif choice == 2:
            dequeued_item = queue.dequeue()
            if dequeued_item != -1:
                print("Dequeued element:", dequeued_item)
        elif choice == 3:
            front_item = queue.peek()
            if front_item != -1:
                print("Front element:", front_item)
        elif choice == 4:
            print("Is queue empty?", queue.is_empty())
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
