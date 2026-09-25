arr=[-2,-3,1,1,2,2,2,3,3,4,4,4,]
n=len(arr)
i=0
for j in range(1,n):
    if(arr[j]!=arr[i]):
        arr[i+1]=arr[j]
        i +=1
print(i+1)