# Assessment 3.2: Singly Linked List Implementation for ARENDAIN

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted '{data}' -> Current List: {self.display()}")

    def delete_front(self):
        if not self.head:
            print("Linked List is empty!")
            return None
        removed_data = self.head.data
        self.head = self.head.next
        print(f"Deleted '{removed_data}' -> Remaining List: {self.display()}")
        return removed_data

    def is_empty(self):
        return self.head is None

    def display(self):
        if not self.head:
            return "[]"
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(elements)


def main():
    last_name = "ARENDAIN"
    ll_ds = LinkedList()

    print("==================================================")
    print(f" LINKED LIST ALGORITHM FOR LAST NAME: {last_name}")
    print("==================================================\n")

    print("1. ADDING EACH LETTER (INSERT AT END):")
    for letter in last_name:
        ll_ds.insert(letter)

    print("\n2. REMOVING EACH LETTER UNTIL EMPTY (DELETE FROM FRONT):")
    while not ll_ds.is_empty():
        ll_ds.delete_front()

    print("\nProcess finished: Linked List is completely empty.")


if __name__ == "__main__":
    main()