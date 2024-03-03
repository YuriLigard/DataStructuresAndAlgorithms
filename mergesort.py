def merge_sorted_lists(self, data):
    #Merges two already sorted lists in ascending order.

    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        # Recursively sort sub-lists
        self.merge_sorted_lists(left_half)
        self.merge_sorted_lists(right_half)

        # Initialize indices for tracking positions in sub-lists and merged data
        i, j, k = 0, 0, 0

        # Merge elements from left and right halves until one is exhausted
        while i < len(left_half) and j < len(right_half):
            # Compare elements at current positions in sub-lists
            if left_half[i] < right_half[j]:
                # Copy smaller element from left half to merged data
                data[k] = left_half[i]
                i += 1  # Move to next element in left half
            else:
                # Copy smaller element from right half to merged data
                data[k] = right_half[j]
                j += 1  # Move to next element in right half
            k += 1  # Move to next position in merged data

        # Copy remaining elements from left half (if any)
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements from right half (if any)
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data
    