# Import the Node class you created in node.py
from node import Node

# Queue class for the Help Desk Ticketing System
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        if self.front is None:
            print("No customers in the queue.")
            return

        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next




def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            helped = queue.dequeue()
            if helped:
                print(f"Helped: {helped}")
            else:
                print("No customers in the queue.")

        elif choice == "3":
            next_customer = queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
