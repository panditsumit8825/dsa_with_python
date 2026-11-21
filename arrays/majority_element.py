# BRUTE FORCE APPROACH
# arr=[2,2,3,3,1,2,2]
# n=len(arr)
# count=0
# for i in range(n):
#     for j in range(n):
#         if(arr[i]==arr[j]):
#             count=count+1
# if(count>n//2):
#     print(arr[i])

# BETTER SOLUTION
def majority_element(arr):
    mpp={}
    for num in arr:
        mpp[num]=mpp.get(num,0)+1
    for key,count in mpp.items():
        if(count>len(arr)//2):
            return key
    return -1
arr=[2,2,3,3,1,2,2]
print(majority_element(arr))