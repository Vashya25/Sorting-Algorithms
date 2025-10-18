# Insertion Sort

def insertion_sort(arr):
    # Traverse through the array starting from the second element.
    for i in range(1, len(arr)):
        # Select the key element to be inserted.
        key = arr[i]
        # Insert the key element into the sorted portion of the array (arr[0..i-1]).
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)