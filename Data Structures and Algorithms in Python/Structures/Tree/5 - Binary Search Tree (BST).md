# Definition 
- **Left subtree** of a node:
	- Values **less** tha the node itself
- **Right subtree** of a node>
	- value **grrater** than the node itself
- Left and right subtreees must be binary search trees


![Screenshot from 2024-02-08 16-38-46.png](../../../../_resources/Screenshot%20from%202024-02-08%2016-38-46.png)

## Deleting 
- **No children**
	- delete it
- **One child**
	- delete it
	- connect the child with node's parent 
- **Two children**
	- replace it with its successor 
		-  the node with the smallest value granter than the value of the node 
	- **Find the successor:**
		- visit the **right child**
		- keep visiting the **left** nodes until the end
		- **if the sucessor has a right child:**
			- child becomes the left child of successor's parent.

# Uses 
- Order lists efficiently
- Much faster at searching than arrays and linked lists
- Much faster at inserting and deleting than arrays
- Used to **implement more advanced data structures:**
	- dynamic sets 
	- lookup tables
	- priority queues 
