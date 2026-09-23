def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high):
            i +=1
        while(arr[j]>pivot and j>=low):
            j -=1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low=0,high=None):
    if high is None:
        high=len(arr)-1
    if(low<high):
        pivot_index=partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

arr=[4,6,2,5,7,9,1,3]
quick_sort(arr)
print("Sorted array :", arr)