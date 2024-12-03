# queue.py

class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def insert(self, element):
        # Insert an element at the end of the queue
        self.queue.append(element)

    def remove(self):
        # Remove an element from the front of the queue
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "The queue is empty"
