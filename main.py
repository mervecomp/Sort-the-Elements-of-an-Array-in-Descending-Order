def sort_array_desc(arr):
    # Sorting the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr

# Example array
arr = [5, 3, 8, 6, 7, 2]

# Function call to sort the array
sorted_arr = sort_array_desc(arr)

# Printing the sorted array
print("Sorted array in descending order:", sorted_arr)
