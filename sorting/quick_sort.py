def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=arr[pivot] and i<=high):
            i +=1
        while(arr[j]>=arr[pivot] and j>=low):
            j -=1
        if(i<j):
            arr[i]=arr[j]
            




arr=[4,6,2,5,7,9,1,3]
quick_sort(arr,0,len(arr)-1)
print("Sorted array :", arr)