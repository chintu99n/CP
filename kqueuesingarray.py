class KQueueUsingArray:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.queues = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [i + 1 for i in range(n)]
        self.next[-1] = -1
        self.free = 0

    def enqueue(self, queue_number, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        i = self.free
        self.free = self.next[i]
        if self.is_empty(queue_number):
            self.front[queue_number] = self.rear[queue_number] = i
        else:
            self.next[self.rear[queue_number]] = i
            self.rear[queue_number] = i
        self.queues[i] = item
        self.next[i] = -1

    def dequeue(self, queue_number):
        if self.is_empty(queue_number):
            print(f"Queue {queue_number} is empty. Cannot dequeue.")
            return -1
        i = self.front[queue_number]
        self.front[queue_number] = self.next[i]
        self.next[i] = self.free
        self.free = i
        return self.queues[i]

    def peek(self, queue_number):
        if self.is_empty(queue_number):
            print(f"Queue {queue_number} is empty. Cannot peek.")
            return -1
        return self.queues[self.front[queue_number]]

    def is_empty(self, queue_number):
        return self.front[queue_number] == -1

    def is_full(self):
        return self.free == -1


if __name__ == "__main__":
    k = int(input("Enter the number of queues (K): "))
    n = int(input("Enter the size of each queue (N): "))

    k_queues = KQueueUsingArray(k, n)

    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            queue_number = int(input("Enter queue number: "))
            if queue_number < 0 or queue_number >= k:
                print("Invalid queue number.")
                continue
            element = int(input("Enter element to enqueue: "))
            k_queues.enqueue(queue_number, element)
        elif choice == 2:
            queue_number = int(input("Enter queue number: "))
            if queue_number < 0 or queue_number >= k:
                print("Invalid queue number.")
                continue
            dequeued_item = k_queues.dequeue(queue_number)
            if dequeued_item != -1:
                print("Dequeued element:", dequeued_item)
        elif choice == 3:
            queue_number = int(input("Enter queue number: "))
            if queue_number < 0 or queue_number >= k:
                print("Invalid queue number.")
                continue
            front_item = k_queues.peek(queue_number)
            if front_item != -1:
                print(f"Front element of queue {queue_number}:", front_item)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
5
