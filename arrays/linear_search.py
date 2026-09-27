def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1

arr=[6,7,8,4,1]
target=4
print(linear_search(arr,target))
