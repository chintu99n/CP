class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def update(self, position, new_data):
        current = self.head
        count = 0
        while current:
            if count == position:
                current.data = new_data
                return
            current = current.next
            count += 1
        print("Position out of range. Cannot update.")

    def split(self):
        if self.head is None or self.head.next is None:
            print("Cannot split. List has less than two elements.")
            return
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        second_half = slow_pointer.next
        slow_pointer.next = None
        print("First half:")
        self.display()
        print("Second half:")
        current = second_half
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    @staticmethod
    def merge(list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.data < list2.data:
            list1.next = LinkedList.merge(list1.next, list2)
            return list1
        else:
            list2.next = LinkedList.merge(list1, list2.next)
            return list2

    def link(self, list2_head):
        if self.head is None:
            self.head = list2_head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = list2_head

if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\nChoose an operation:")
        print("1. Insert")
        print("2. Display")
        print("3. Reverse")
        print("4. Sort")
        print("5. Update")
        print("6. Split")
        print("7. Merge")
        print("8. Link")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert: "))
            linked_list.insert(data)
        elif choice == 2:
            print("Linked List:")
            linked_list.display()
        elif choice == 3:
            linked_list.reverse()
            print("Linked List after reversing:")
            linked_list.display()
        elif choice == 4:
            linked_list.sort()
            print("Linked List after sorting:")
            linked_list.display()
        elif choice == 5:
            position = int(input("Enter position to update: "))
            new_data = int(input("Enter new data: "))
            linked_list.update(position, new_data)
            print("Linked List after updating:")
            linked_list.display()
        elif choice == 6:
            linked_list.split()
        elif choice == 7:
            list1 = linked_list.head
            list2 = linked_list.head.next if linked_list.head else None
            linked_list.sort()
            print("First linked list:")
            linked_list.display()
            print("Second linked list:")
            while list2:
                print(list2.data, end=" ")
                list2 = list2.next
            print()
            print("Merged linked list:")
            merged_list = LinkedList.merge(list1, list2)
            current = merged_list
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
        elif choice == 8:
            print("Create another linked list to link with the current one.")
            list2 = LinkedList()
            num_elements = int(input("Enter the number of elements in the second linked list: "))
            print("Enter the elements:")
            for _ in range(num_elements):
                element = int(input())
                list2.insert(element)
            print("Linked list before linking:")
            linked_list.display()
            print("Linked list to be linked:")
            list2.display()
            linked_list.link(list2.head)
            print("Linked list after linking:")
            linked_list.display()
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
