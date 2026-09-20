list=[2,2,9,7,4,3,4,2,2]
n=len(list)
count=0
for i in range(n):
    for j in range(1,n):
        if(list[i]==list[j]):
            count+=1
            # if(count>=n//2):
                
print(count)