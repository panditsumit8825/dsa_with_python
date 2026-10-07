list=[1,2,4,5]
n=5
# flag=0
for i in range(1,n):
    for j in range(n-1):
        if list[j]==i:
            flag=1
            break
if(flag==0):
    print(i)