def partition(data, first_index, last_index):
    # Choose the pivot as the first element of the list
    pivot = data[first_index]
    
    # Initialize pointers to traverse the list
    left_pointer = first_index + 1
    right_pointer = last_index 

    # Loop to find elements out of position and swap them
    while True:
        while data[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while data[right_pointer] > pivot and right_pointer >= left_pointer:
            right_pointer -= 1
            
        # If the pointers cross each other or are in the same position, break the loop
        if left_pointer >= right_pointer:
            break
        
        # Swap elements out of position
        data[left_pointer], data[right_pointer] = data[right_pointer], data[left_pointer]
    
    # Place the pivot in the correct position
    data[first_index], data[right_pointer] = data[right_pointer], data[first_index]
    
    # Return the final position of the pivot
    return right_pointer


def quicksort(data, first_index=None, last_index=None):
    # Set initial indices if not provided
    if last_index is None:
        last_index = len(data) - 1
        first_index = 0

    # Check if there are elements to sort
    if first_index < last_index:
        # Get the index where the pivot is in the correct position
        partition_index = partition(data, first_index, last_index)
        
        # Recursively call the quick function for the sublists to the left and right of the pivot
        quicksort(data, first_index, partition_index)
        quicksort(data, partition_index + 1, last_index)


    return data

if __name__ == "__main__":
    
    lista = [4, 19, 20, 5, 1, 0]

    print(quicksort(lista))

   