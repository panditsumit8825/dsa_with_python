# hash_map={}
# arr=[]
# n=int(input("Enter the array filled number:"))
# for i in range(n):
#     arr.append(i)
# print(arr)
# # precompute
# # hash[13]={0}
# for item in arr:
#     if item in hash_map:
#         hash_map[item]+=1
#     else:
#         hash_map[item]=1

# q=int(input("Enter number of queries:"))
# while(q>0):
#     query_val=int(input("Enter element you lookup"))
#     print(f"frequency of {query_val}: {hash_map.get(query_val,0)}")
#     q -=1

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,6,7]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
        if(num<1 or num>10):
            print(0,end=" ")
        else:
            print(hash_list[num],end=" ")
