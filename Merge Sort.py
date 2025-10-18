# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array.
        mid = len(arr) // 2
        # Split the array into two halves.
        l = arr[:mid]
        r = arr[mid:]
        # Recursively sort both halves.
        merge_sort(l)
        merge_sort(r)
        
        # Merge the sorted halves.
        i, j, k = 0, 0, 0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
            
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
            
    return arr
    
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)