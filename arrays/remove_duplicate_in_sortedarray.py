arr=[1,1,2,2,2,3,3,4,4,4,5,5,5,6]
n=len(arr)
i=0
for j in range(1,n):
    if(arr[j]!=arr[i]):
        arr[i+1]=arr[j]
        i +=1
print(arr[i])