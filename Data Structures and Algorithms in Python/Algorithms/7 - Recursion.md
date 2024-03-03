# Identifying the base case
- Add a condition 
	- ensures thar our algorithm doesn't execute forever 
- **Factorial base case** -> n = 1

```
def factorial_recursion(n):
    if n == 1:
	      return 1 
		else:
		  retrun n * factorial_recursion(n-1)
``` 

# How recursion works 
- Computer uses a **stack** to keep track of the functions 
	- **Call stack**

```python
def fib(n):
  #base case
  if n <= 1:
     return n
  else:
    print(f'recursion: {n}')
    return fib(n-1) + fib(n-2)

print(fib(5))
``` 

- n=5


![Screenshot from 2024-02-08 01-30-01.png](../../../_resources/Screenshot%20from%202024-02-08%2001-30-01.png)



![Screenshot from 2024-02-08 01-31-04.png](../../../_resources/Screenshot%20from%202024-02-08%2001-31-04.png)


# Dynamic programming
- Optimization technique 
- Mainly applied to recursion 
- Can reduce the complexty of recursive algorithms 
- Used for: 
	- Any prolem that can be divided into smaller subproblems 
	- Subproblems overlap 
- Solutions of subproblems are saved, avoiding the need to recalculate 
- Memoization
```python 
cache = [None]*(100)

def fib(n):
  #base case
  if n <= 1:
    return n
  elif not cache[n]:
    print(f'recursion: {n}')
    cache[n] = fib(n-1) + fib(n-2)
    
  return cache[n]
  


print(fib(5))

```

![Screenshot from 2024-02-08 01-21-37.png](../../../_resources/Screenshot%20from%202024-02-08%2001-21-37.png)

![Screenshot from 2024-02-08 01-28-44.png](../../../_resources/Screenshot%20from%202024-02-08%2001-28-44.png)



