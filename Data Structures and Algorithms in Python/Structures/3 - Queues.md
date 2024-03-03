# **FIFO:** First-In First-Out

- Can only **insert** at the **end** (**Enqueue**)

- Can only **remove** from the head (**Dequeue**)

- Other kinds of queues:

	- Doubly ended queues

	- Circular queues

	- Priority queues

```Python
class Queue:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
        
    def enqueue(self, data):
        
        new_node = Node(data)

        if self.head:
            self.tail.next = new_node   
            self.tail = new_node        
        else:
            self.tail = new_node
            self.head = new_node
            
    def dequeeu(self):
        
        if self.head:
            deq = self.head
            self.head = deq.next
            return deq.data 
        else:
            return None
        
    def read(self):
        
        if self.head:
            return self.head
        else:
            return None
```