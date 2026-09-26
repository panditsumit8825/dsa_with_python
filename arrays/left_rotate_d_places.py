arr=[9,8,1,4,5,6,7]
n=len(arr)
d=3
temp=[]
# step:1- Store a d places in temp
for i in arr:
    temp.append(i)
# step 2:- Shifting the array
for i in range(d,n):
    arr[i-d]=arr[i]
# step 3:- store temp to array
for i in range(n-d,n):
    arr[i]=temp[i-(n-d)]
print(arr)


