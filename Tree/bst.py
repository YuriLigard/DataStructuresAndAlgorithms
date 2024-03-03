# Implementation Binary Search Tree (BST)
from math import log2, ceil
from os import curdir

import sys
sys.path.append('StructuresAndAlgotithms/Queues/')

from fifo import Queue


class TreeNode:
    
    def __init__(self, data, left=None, right=None) -> None:
        self.__data = data 
        self.__left_child = left
        self.__right_child = right

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left_child(self):
        return self.__left_child
    
    @property
    def right_child(self):
        return self.__right_child
    
    @left_child.setter
    def left_child(self, new_node: object):
        self.__left_child = new_node
    
    @right_child.setter
    def right_child(self, new_node: object):
        self.__right_child = new_node
    
    def __str__(self):
        return f"(data={self.__data}, right={self.right_child}, left={self.__left_child})"
    

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None 

    def insert(self, data):

        new_node = TreeNode(data)

        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root

            while True:
                if new_node.data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                else:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

    def delete(self, data):
        prior_node, current_node = __class__.search(self, data)

        if current_node:
            # No children # 
            if current_node.right_child == None and current_node.left_child == None:
                if prior_node.right_child is not None and prior_node.right_child.data == data:
                    prior_node.right_child = None
                else:
                    prior_node.left_child = None

           
            # Two children #
            elif current_node.right_child is not None and current_node.left_child is not None:
                top_node = current_node
                current_node = current_node.right_child
                while True:
                    if current_node.left_child is not None:
                        prior_node = current_node
                        current_node = current_node.left_child
                    else:
                        if current_node.right_child is not None:
                            prior_node.left_child = current_node.right_child
                        else:
                            prior_node.left_child = None
                
                        top_node.data = current_node.data
                        return True

            # One child # 
            else:
                
                if prior_node.right_child is not None and prior_node.right_child.data == data:
                    if current_node.right_child is not None:
                        current_node = current_node.right_child
                        prior_node.right_child = current_node
                    else:
                        current_node = current_node.left_child
                        prior_node.right_child = current_node
                else:
                    if current_node.right_child is not None:
                        current_node = current_node.right_child
                        prior_node.left_child = current_node
                    else:
                        current_node = current_node.left_child
                        prior_node.left_child = current_node


            

    def search(self, data) -> object|bool:
        
        prior_node = None
        current_node = self.root

        while True:

            if current_node:
                if data == current_node.data:
                    return prior_node, current_node
                elif data < current_node.data:
                    prior_node = current_node
                    current_node = current_node.left_child
                else:
                    prior_node = current_node
                    current_node = current_node.right_child
            else:
                return prior_node, None
            

    # Depth First Search (DFS)
    
    def in_order(self, current_node):
    # Order: Left -> Current -> Right
        
        if current_node:
            self.in_order(current_node.left_child)
            print(f'{current_node.data}, ', end='')
            self.in_order(current_node.right_child)
    
    def pre_order(self, current_node):
    # Order: Current -> Left -> Right
        
        if current_node:
            print(f'{current_node.data}, ', end='')
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)
                
    def post_order(self, current_node):
    # Order: Left -> Right -> Current 
        
        if current_node:
            self.post_order(current_node.left_child)
            self.post_order(current_node.right_child)
            print(f'{current_node.data}, ', end='')

    
    # Breadth First Search (BFS)    
    def bfs(self, current_node):
        
        if current_node:
            visited_node = []
            queueS = Queue()
            queueS.enqueue(current_node)

            while queueS.read() is not None:
                current_node = queueS.dequeue()
                visited_node.append(current_node.data)
                if current_node.left_child:
                    queueS.enqueue(current_node.left_child)
                if current_node.right_child:
                    queueS.enqueue(current_node.right_child)
            return visited_node


    #Tree height#
    def _height(self, current_node):
        #
        # worst-case -> O(log(n)) = Tree height #balanced#
        # 
        hleft = 0
        hright = 0
        if current_node is None:
            return current_node
        else:
            if current_node.left_child:
                hleft = self._height(current_node.left_child)
            if current_node.right_child:
                hright = self._height(current_node.right_child)
            if hleft > hright:
                return hleft+1
            else:
                return hright+1
            
    
    def _countNodes(self, current_node):
    
        sumleft = 0
        sumright = 0
        
        if current_node:
            sumleft = self._countNodes(current_node.left_child)
            sumright = self._countNodes(current_node.right_child)
            
            return sumleft + sumright + 1
        
        return 0
    
    
    def balanced(self, current_node) -> bool:

        # if O(log(n)) = Tree height (_height) #balanced#
        # n -> number of nodes in the tree (_countNodes)

        return ceil(log2(self._countNodes(current_node))) == self._height(current_node)
        

        

if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(45)
    bst.insert(15)
    bst.insert(12)
    bst.insert(30) 
    bst.insert(50)
    bst.insert(40)
    bst.insert(49)
    #bst.insert(60)
    #bst.insert(47)
    #bst.insert(48)

    #bst.delete(45)
    a, b = bst.search(20)
    #print(a)
    #print(b)
    #print(b)
    #print(bst.balanced(b))
    #print(bst.height(b))
    
    print(bst.bfs(b))
    



                    




