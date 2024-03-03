# LIFO: **Last-In First-Out**

- Can only **add** at the **top** (**Pushing**)

- Can only **take** from the **top** (**Popping**)

- Can only **read** the **last element** 

```Python
class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1
    
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
```