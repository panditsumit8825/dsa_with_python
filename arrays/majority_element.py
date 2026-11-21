arr=[2,2,3,3,1,2,2]
n=len(arr)
count=0
for i in range(n):
    for j in range(n):
        if(arr[i]==arr[j]):
            count=count+1
if(count>n/2):
    print(arr[i])