# Brute Force Approach

# arr=[10,22,12,3,0,6]
# ans=[]
# n=len(arr)
# for i in range(n):
#     leader=True
#     for j in range(1,n):
#         if(arr[j]>arr[i]):
#             leader=False
#             break
#     if(leader==True):
#         ans.append(arr[i])
# print(ans)

# Optimal Solution
# Without Function
# arr=[10,22,12,3,0,6]
# ans=[]
# n=len(arr)
# maxi=float('-inf')
# for i in range(n-1,-1,-1):
#     if(arr[i]>maxi):
#         ans.append(arr[i])
#     # keep tracking of right max
#     maxi=max(maxi,arr[i])
# # ans.sort()
# print(ans)

# With Function
# def leaders_array(arr,n):
#     ans=[]
#     maxi=float('-inf')
#     for i in range(n-1,-1,-1):
#         if(arr[i]>maxi):
#             ans.append(arr[i])
#         maxi=max(maxi,arr[i])
#     return ans
# arr=[10,22,12,3,0,6]
# n=len(arr)
# print(leaders_array(arr,n))