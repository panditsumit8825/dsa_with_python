# def patterns3(n):
#     for i in range(1,n):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# patterns3(6)

# def patterns5(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()
# patterns5(6)

# def patterns6(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
# patterns6(6)

# def patterns7(n):
#     for i in range(n):
#         print(" ",(n-i-1))
#         for j in range(i):
#             print("*")
# patterns7(6)

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Example usage:
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)
# Output: Sorted array: [11, 12, 22, 25, 64]
