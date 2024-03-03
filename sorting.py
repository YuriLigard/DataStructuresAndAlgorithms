from LinkedList.linkedlist import Node, LinkedList, Insert


class Sorting:


    def bubble(self, node, end=None):
        # The bubble method performs one iteration of the Bubble Sort algorithm on a linked list.

        current_node = node
        swap = None  # Variable to indicate whether there was any swap during the iteration.

        while current_node and current_node.next:
            #print(current_node, current_node.next)
            lastProcessedNode = current_node  # Stores the last processed node.
            # Compares the data of the current node with the next node in the list.
            if current_node.data > current_node.next.data:
                # If the current node is greater than the next, swaps the data.
                swap = current_node.next.data
                current_node.next.data = current_node.data
                current_node.data = swap

            # Moves to the next node in the list, unless it has reached the specified end.
            current_node = current_node.next if current_node.next is not end else None
         
        # If there was any swap during the iteration and the last processed node is not the initial node,
        # recursively call the bubble method.
        if swap is not None and lastProcessedNode is not node:
            #print('--------',lastProcessedNode)
            self.bubble(node, end=lastProcessedNode)
        return
    

    def selection(self, node):
        # Initialize current_node and lowest_node with the provided node
        current_node = node
        lowest_node = node 

        # Determine the lowest value in the linked list
        while current_node and current_node.next:
            # Compare the data of the current lowest node with the next node
            if lowest_node.data > current_node.next.data:
                # If the next node has a lower value, update lowest_node
                lowest_node = current_node.next

            current_node = current_node.next  # Move to the next node in the linked list

        # Swap the lowest value with the first unordered element in the linked list
        if node is not lowest_node:
            swap = node.data 
            node.data = lowest_node.data
            lowest_node.data = swap

        # Recursively call the selection function on the next node if it exists
        if node.next:
            self.selection(node.next)
        return
    

   


if __name__ == "__main__":

# Create Node 

    a_no = Node(1)
    b_no  = Node(5)
    c_no = Node(20)
    d_no = Node(0) #0
    e_no  = Node(19)
    f_no = Node(4)


# Linkar 

    linkedlist_01 = LinkedList()

# Add  Linkedlist 

    conn_01 = Insert(node=a_no, linked=linkedlist_01)
    conn_01.beginning()

    conn_02 = Insert(node=b_no, linked=linkedlist_01)
    conn_02.beginning()

    conn_03 = Insert(node=c_no, linked=linkedlist_01)
    conn_03.beginning()

    conn_04 = Insert(node=d_no, linked=linkedlist_01)
    conn_04.end()

    conn_05 = Insert(node=e_no, linked=linkedlist_01)
    conn_05.beginning()

    conn_06 = Insert(node=f_no, linked=linkedlist_01)
    conn_06.beginning()




    #current_node = linkedlist_01.head
    #print('##before sorting##')
    #while current_node:
        #print(current_node)
        #current_node = current_node.next
    #print('-------\n\n')


    # bubble 
    #sorting = Sorting()
    #sorting.bubble(linkedlist_01.head)


    # Selection 

    #sorting = Sorting()
    #sorting.selection(linkedlist_01.head)


    #print('##after sorting##')
    #current_node = linkedlist_01.head
    #while current_node:
        #print(current_node)
        #current_node = current_node.next

   