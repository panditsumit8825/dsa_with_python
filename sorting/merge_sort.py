# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid

#     # Create temp arrays
#     L = [0] * n1
#     R = [0] * n2

#     # Copy data to temp arrays L[] and R[]
#     for i in range(n1):
#         L[i] = arr[left + i]
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]
        
#     i = 0  
#     j = 0  
#     k = left  

#     # Merge the temp arrays back
#     # into arr[left..right]
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     # Copy the remaining elements of L[],
#     # if there are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     # Copy the remaining elements of R[], 
#     # if there are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def mergeSort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2

#         mergeSort(arr, left, mid)
#         mergeSort(arr, mid + 1, right)
#         merge(arr, left, mid, right)

# # Driver code
# if __name__ == "__main__":
#     arr = [3,1,2,4,1,5,2,6,4]
   
#     mergeSort(arr, 0, len(arr) - 1)
#     for i in arr:
#         print(i, end=" ")
#     print()

def merge(list,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(list[left]<=list[right]):
            temp.append(list[left])
            left +=1
        else:
            temp.append(list[right])
            right +=1
    while(left<=mid):
        temp.append(list[left])
        left +=1
    while(right<=high):
        temp.append(list[right])
        right +=1
    for i in range(low,high+1):
        list[i] = temp[i-low]
def merge_sort(list,low,high):
    if(low>=high):
        return
    mid = (low+high)//2
    merge_sort(list,low,mid)
    merge_sort(list,mid+1,high)
    merge(list,low,mid,high)
arr=[3,1,2,4,1,5,2,6,4]
merge_sort(arr,0,len(arr)-1)
print(arr)