class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(data):
    global head
    new_node = Node(data)
    if head is None:
        head = new_node
        return
    current = head
    while current.next:
        current = current.next
    current.next = new_node

def display():
    global head
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def delete_duplicates():
    global head
    if head is None or head.next is None:
        return
    seen = set()
    current = head
    previous = None
    while current:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next

if __name__ == "__main__":
    head = None

    # Input the elements of the linked list
    n = int(input("Enter the number of elements in the linked list: "))
    print("Enter the elements:")
    for _ in range(n):
        data = int(input())
        insert(data)

    # Display the original linked list
    print("Original linked list:")
    display()

    # Delete duplicates from the linked list
    delete_duplicates()

    # Display the linked list after deleting duplicates
    print("Linked list after deleting duplicates:")
    display()
