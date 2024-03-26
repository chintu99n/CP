class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Stack is full. Cannot push.")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# Get stack capacity from user input
capacity = int(input("Enter the capacity of the stack: "))
stack = ArrayStack(capacity)

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = int(input("Enter element to push: "))
        stack.push(item)
    elif choice == '2':
        popped_element = stack.pop()
        if popped_element is not None:
            print("Popped element:", popped_element)
    elif choice == '3':
        top_element = stack.peek()
        if top_element is not None:
            print("Top element:", top_element)
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
