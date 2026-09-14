hash_map={}
arr=[]
n=int(input("Enter the array filled number:"))
for i in range(n):
    arr.append(i)
print(arr)
# precompute
# hash[13]={0}
for item in arr:
    if item in hash_map:
        hash_map[item]+=1
    else:
        hash_map[item]=1

q=int(input("Enter number of queries:"))
while(q>0):
    query_val=int(input("Enter element you lookup"))
    print(f"frequency of {query_val}: {hash_map.get(query_val,0)}")
    q -=1

