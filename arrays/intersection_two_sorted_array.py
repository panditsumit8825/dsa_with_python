# Brute Force Approach
# T.C=(n1xn2)
# S.C=(n2)

# arr1=[1,2,2,3,3,4,5,6]
# arr2=[2,3,3,5,6,6,7]
# n1=len(arr1)
# n2=len(arr2)
# visit=[0]*n2
# ans=[]
# for i in range(n1):
#     for j in range(n2):
#         if(arr1[i]==arr2[j] and visit[j]==0):
#             ans.append(arr1[i])
#             visit[j]=1
#             break 
#         if(arr2[j]>arr1[i]):
#             break   
# print(ans)

# Optimal Solution bu Using Two Pointer Concept
# T.C=(n1+n2)
# S.C=(1)
# def intersection(arr1,arr2,n1,n2):
#     ans=[]
#     i=0
#     j=0
#     while(i<n1 and j<n2):
#         if(arr1[i]<arr2[j]):
#             i=i+1
#         elif(arr2[j]<arr1[i]):
#             j=j+1
#         elif(arr1[i]==arr2[j]):
#             ans.append(arr1[i])
#             i=i+1
#             j=j+1
#     return ans

# arr1=[1,2,2,3,3,4,5,6]
# arr2=[2,3,3,5,6,6,7]
# n1=len(arr1)
# n2=len(arr2)
# print(intersection(arr1,arr2,n1,n2))

# Without Using Function
arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]
n1=len(arr1)
n2=len(arr2)
ans=[]
i=0
j=0
while(i<n1 and j<n2):
    if(arr1[i]<arr2[j]):
        i=i+1
    elif(arr2[j]<arr1[i]):
        j=j+1
    elif(arr1[i]==arr2[j]):
        ans.append(arr1[i])
        i=i+1
        j=j+1
print(f"Optimal Solution Is: {ans}")