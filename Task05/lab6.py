'''==> is python support multiple inheritance or not ?
Yes, Python does support multiple inheritance. 
It allows a class to inherit attributes and methods from multiple parent classes.
However, it can sometimes lead to complexity and 
issues like the "diamond problem" where conflicts arise if both parent classes define methods with the same name.
'''
import json


class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.insert(0, value)
        print(self.items)

    def pop(self):
        if self.is_empty():
            print("Warning: Queue is empty")
            return None
        return self.items.pop(len(self.items)-1)

    def is_empty(self):
        return len(self.items) == 0


class QueueOutOfRangeException(Exception):
    pass

class NamedQueue(Queue):
    queues = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.queues[name] = self

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException(f"Queue size exceeded")
        super().insert(value)

    @classmethod
    def get_queue(cls, name):
        return cls.queues.get(name, None)
    

    @classmethod
    def save(cls, file_path):
        queue_data = {name: queue.items for name, queue in cls.queues.items()}
        with open(file_path, 'w') as file:
            json.dump(queue_data, file)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'r') as file:
            queue_data = json.load(file)
        cls.queues = {name: NamedQueue(name, len(items)) for name, items in queue_data.items()}
        for name, items in queue_data.items():
            cls.queues[name].items = items


def main():
    queue1 = Queue()
    print("Queue is empty:", queue1.is_empty())
    queue1.insert(10)
    queue1.insert(20)
    queue1.insert(30)
    queue1.insert(50)
    print("Queue is empty:", queue1.is_empty())

    print("Popped value:", queue1.pop(),queue1.items) 
    print("Popped value:", queue1.pop(),queue1.items)
    print("Popped value:", queue1.pop(),queue1.items)
    print("Popped value:", queue1.pop(),queue1.items)  

    print(queue1.pop()) 


    try:
        queue2 = NamedQueue("queue1",3)
        queue2.insert(5)
        queue2.insert(10)
        queue2.insert(15) 
        queue2.insert(20)
    except QueueOutOfRangeException as e:
        print(e)
    try:
        queue3=NamedQueue("queue2",4)
        queue3.insert("python")
        queue3.insert("SQL")
        queue3.insert("java")
        queue3.insert("R")
    except QueueOutOfRangeException as e:
        print(e)    

    NamedQueue.save("queues.json")
    NamedQueue.load("queues.json")



    
  

if __name__ == "__main__":
    main()