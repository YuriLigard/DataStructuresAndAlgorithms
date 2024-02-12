import queue
from re import T 

# Create the queue
my_orders_queue = queue.SimpleQueue()
# Add an element to the queue 
my_orders_queue.put("Tmj")
#Remove an element from the queue 
print(my_orders_queue.get())
