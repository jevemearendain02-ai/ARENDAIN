# Assessment 3.2: Stack Implementation for ARENDAIN
# Structure: LIFO (Last-In, First-Out)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(f"Pushed '{element}' -> Current Stack: {self.stack}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        removed = self.stack.pop()
        print(f"Popped '{removed}' -> Remaining Stack: {self.stack}")
        return removed

    def is_empty(self):
        return len(self.stack) == 0


def main():
    last_name = "ARENDAIN"
    stack_ds = Stack()

    print("========================================")
    print(f" STACK ALGORITHM FOR LAST NAME: {last_name}")
    print("========================================\n")

    print("1. ADDING EACH LETTER (PUSH):")
    for letter in last_name:
        stack_ds.push(letter)

    print("\n2. REMOVING EACH LETTER UNTIL EMPTY (POP):")
    while not stack_ds.is_empty():
        stack_ds.pop()

    print("\nProcess finished: Stack is completely empty.")


if __name__ == "__main__":
    main()