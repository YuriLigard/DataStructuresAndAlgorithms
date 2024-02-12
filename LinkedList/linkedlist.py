class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None 

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @next.setter
    def next(self, new_next):
        self._next = new_next 

    def __str__(self):
        return f"Node(data={self._data})"


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    
    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail 

    @head.setter
    def head(self, new_head):
        self._head = new_head
    
    @tail.setter
    def tail(self, new_tail):
        self._tail = new_tail
    


class Insert:

    def __init__(self, node, linked):
        self.node = node
        self.linked = linked
    

    def beginning(self):

        if self.linked.head:
            self.node.next = self.linked.head
            self.linked.head = self.node
        else:
            self.linked.head = self.node 
            self.linked.tail = self.node

    def end(self):

        if self.linked.head:
            self.linked.tail.next = self.node 
            self.linked.tail = self.node
        else:
            self.linked.head = self.node 
            self.linked.tail = self.node



if __name__ == "__main__":

# Create Node 

    terceiro_no = Node("TestN2")
    segundo_no  = Node("TestN")
    primeiro_no = Node("Cy")

# Linkar 

    linkedlist_01 = LinkedList()

# Add  Linkedlist 

    conn_01 = Insert(node=terceiro_no, linked=linkedlist_01)
    conn_01.beginning()

    conn_02 = Insert(node=segundo_no, linked=linkedlist_01)
    conn_02.beginning()

    conn_03 = Insert(node=primeiro_no, linked=linkedlist_01)
    conn_03.beginning()

    conn_03.end()

    print(linkedlist_01.head.next.next.next)