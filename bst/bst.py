# Implementation Binary Search Tree (BST)


from os import curdir


class TreeNode:
    
    def __init__(self, data, left=None, right=None) -> None:
        self.__data = data 
        self.__left_child = left
        self.__right_child = right

    @property
    def data(self):
        return self.__data

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

    def delet(self, data):
        prior_node, current_node = __class__.search(self, data)

        #print(current_node.left_child)

        #print(prior_node)

        if current_node:
            # No children # 
            if current_node.right_child == None and current_node.left_child == None:
                if prior_node.right_child is not None and prior_node.right_child.data == data:
                    prior_node.right_child = None
                else:
                    prior_node.left_child = None

           
            # Two children #
            elif current_node.right_child is not None and current_node.left_child is not None:
                pass
                


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




if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(45)
    bst.insert(30)
    bst.insert(15)
    bst.insert(12)

    bst.delet(30)
    bst.delet(15)
    bst.delet(12)

    a, b = bst.search(20)
    print(a)
    print(b)
    



                    




