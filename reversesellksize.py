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

def reverse_k_block(head, k):
    current = head
    prev = None
    next_node = None
    count = 0

    # Reverse the first K nodes of the linked list
    while count < k and current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    # Recursive call for the remaining nodes
    if next_node is not None:
        head.next = reverse_k_block(next_node, k)

    return prev  # New head of the reversed sublist

if __name__ == "__main__":
    head = None

    # Input the elements of the linked list
    n = int(input("Enter the number of elements in the linked list: "))
    print("Enter the elements:")
    for _ in range(n):
        data = int(input())
        insert(data)

    # Input the block size K
    k = int(input("Enter the block size (K): "))

    # Display the original linked list
    print("Original linked list:")
    display()

    # Reverse the linked list in blocks of size K
    head = reverse_k_block(head, k)

    # Display the reversed linked list
    print("Linked list after reversing in blocks of size", k, ":")
    display()
