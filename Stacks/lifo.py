import sys
sys.path.append('StructuresAndAlgotithms/LinkedList/')

from linkedlist import Node


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data):

        new_node = Node(data)
        if self.top:
            new_node.next = self.top

        self.top =  new_node

        self.size+=1

    
    def pop(self):

        if self.top:
            popping = self.top.data
            self.top = self.top.next
            self.size-=1

            return popping
        else:
            return None
        
    def read(self):

        if self.top:
            return self.top.data
        else:
            return None 



if __name__ == "__main__":
    stack = Stack()

    stack.push('Bass')
    stack.push('Drum')
    
    print(f'Rm: {stack.pop()}')

    print(stack.read())

    