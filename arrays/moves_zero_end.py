# # Brute Force Approach

# arr=[1,0,2,3,2,0,0,4,5,1]
# n=len(arr)
# temp=[]
# # find nonzero and append temp array
# for i in range(n):
#     if(arr[i]!=0):
#         temp.append(arr[i])
# # append nonzero temp element in infront of array
# for i in range(len(temp)):
#     arr[i]=temp[i]
# # nonzero=nz
# # append zero in the last of array
# nz=len(temp)
# for i in range(nz,n):
#     arr[i]=0
# print(arr)


# Optimal Approach
# enter array bu user
# k=int(input("Enter a array Size :"))
# arr=[]
# for i in range(k):
#     nums=int(input(f"Enter number {i+1}:"))
#     arr.append(nums)
# print(arr)

# By using two pinter concept
arr=[1,0,2,3,2,0,0,4,5,1]
n=len(arr)
j=-1
for i in range(n):
    if(arr[i]==0):
        j=i
        break
for i in range(j+1,n):
    if(arr[i]!=0):
        arr[j],arr[i]=arr[i],arr[j]
        j +=1
print(arr)