
    class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print("Enqueued:", item)
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print("Dequeued:", item)
        self.display()
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are:", end=" ")
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.capacity
        print(self.queue[self.rear])

# Create a Queue object with user-defined capacity
capacity = int(input("Enter the capacity of the queue: "))
queue = Queue(capacity)
print("1.enqueue")
print("2.dequeue")
print("3.peek")
print("4.display")
print("5.exit")
# Continue to take user input until 'exit' is entered
while True:
    operation = int(input("Enter operation: "))
    
    if operation == 1:
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif operation == 2:
        queue.dequeue()
    elif operation == 3:
        print("Peek:", queue.peek())
    elif operation == 4:
        queue.display()
    elif operation == 5:
        print("Exiting...")
        break
    else:
        print("Invalid operation. Please enter enqueue, dequeue, peek, display, or exit.")
