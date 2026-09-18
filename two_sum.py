list=[3,2,3]
n=len(list)
target=6
for i in range(n-1):
    for j in range(i+1,n):
        if(list[i]+list[j]==target):
            print([i,j])
