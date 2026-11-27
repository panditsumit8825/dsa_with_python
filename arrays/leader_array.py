arr=[10,22,12,3,0,6]
ans=[]
n=len(arr)
for i in range(n):
    leader=True
    for j in range(1,n):
        if(arr[j]>arr[i]):
            leader=False
            break
    if(leader==True):
        ans.append(arr[i])
print(ans)