import sys
sys.path.append('StructuresAndAlgotithms/LinkedList/')

from linkedlist import Node


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
            return (self.head.data, self.tail.data)
        else:
            return None
        
        
if __name__ == "__main__":
    
    queue = Queue()
    
    queue.enqueue("Cy")
    queue.enqueue("Gita")
    queue.enqueue("Drum")
    queue.enqueue("Tec")


    print(queue.read())

    
    #print(f'removido: {queue.dequeeu()}')
    #print(f'removido: {queue.dequeeu()}')
    #print(f'removido: {queue.dequeeu()}')
    


    
    