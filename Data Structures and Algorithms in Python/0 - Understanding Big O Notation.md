- Measures the **worst-case complexity** od an algorithm 
	- **Time complexity:** time taken to run completey
	- **Space compelxity:** extra memory space


- **Mathematical expressions:** O(1), O(n), O(n²)...

![Screenshot from 2024-01-27 23-21-49.png](../../_resources/Screenshot%20from%202024-01-27%2023-21-49.png)



![Screenshot from 2024-01-27 23-32-32.png](../../_resources/Screenshot%20from%202024-01-27%2023-32-32.png)



![Screenshot from 2024-01-27 23-33-02.png](../../_resources/Screenshot%20from%202024-01-27%2023-33-02.png)



![Screenshot from 2024-01-27 23-35-50.png](../../_resources/Screenshot%20from%202024-01-27%2023-35-50.png)


## Simplifying Big O Notation 

- 1. Remove constants 
	-  O(4 + 2n + 2m) -> O(n + m)
- 2. Different variables fpr different inputs
	- O(n + m)
- 3. Remove smaller terms 
	- O(n + n²) -> O(n²)