# Assessment 3.2: Queue Implementation for ARENDAIN
# Structure: FIFO (First-In, First-Out)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        print(f"Enqueued '{element}' -> Current Queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed = self.queue.pop(0)
        print(f"Dequeued '{removed}' -> Remaining Queue: {self.queue}")
        return removed

    def is_empty(self):
        return len(self.queue) == 0


def main():
    last_name = "ARENDAIN"
    queue_ds = Queue()

    print("========================================")
    print(f" QUEUE ALGORITHM FOR LAST NAME: {last_name}")
    print("========================================\n")

    print("1. ADDING EACH LETTER (ENQUEUE):")
    for letter in last_name:
        queue_ds.enqueue(letter)

    print("\n2. REMOVING EACH LETTER UNTIL EMPTY (DEQUEUE):")
    while not queue_ds.is_empty():
        queue_ds.dequeue()

    print("\nProcess finished: Queue is completely empty.")


if __name__ == "__main__":
    main()