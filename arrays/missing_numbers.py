# Brute Force Approach To Find Missing Number

# def missing_num(arr,n):
#     for i in range(1,n+1):
#         flag=0
#         for j in arr:
#             if(j==i):
#                 flag=1
#                 break
#         if(flag==0):
#             return i
    
# arr_list = [1,2,3,4,5,7]
# n=len(arr_list)
# print(missing_num(arr_list,n))


# Better Solution By Using Hashing
# def missing_num(nums,n):
#     my_hash=set(nums)
#     for i in range(1,n+1):
#         if i not in my_hash:
#                     return i

# nums_list=[1,2,3,5]
# n=len(nums_list)
# print(missing_num(nums_list,n))

# Optimal solution
# def missing_num(sum,arr):
#     sum1=0
#     for i in arr:
#         sum1 += i
#     return(sum-sum1)

# arr_list=[1,2,4,5]
# l=len(arr_list)
# n=l+1
# sum=n*(n+1)//2
# print(missing_num(sum,arr_list))

# Most Optimal Solution By Using XOR operation

# def missing_num(arr,n):
#     xor1=0
#     xor2=0
#     for i in range(1,n+1):
#         xor1=xor1^i
#         if(i-1)<len(arr):
#             xor2=xor2^arr[i-1]
#     return xor1^xor2

# arr_list=[1,2,3,5]
# n=len(arr_list) + 1
# # n=m+1
# print(missing_num(arr_list,n))


# Linear Search practice
# def lin_ser(nums,k):
#     n=len(nums)
#     i=0
#     while(i<=n):
#         if(nums[i]==k):
#             i +=1
#             return nums[i]
#         else:
#             return False

# nums=[1,2,4,5,6,7,3]
# # n=len(nums)
# k=6
# print(lin_ser(nums,k))


# nums=[1,2,4,7,3,9]
# n=len(nums)
# k=9
# for i in range(n):
#     if(nums[i]==k):
#         print(f"element exist on index : {i}")
#         break
#     else:
#         print(False)
    # print(False)

# pattern practice
#   *  
#  *** 
# *****
# *****
#  ***
#   * 
# n=3
# for i in range(n):
#     print(" "*(n-(i+1)) + "*"*(2*i+1))
# for j in range(n,0,-1):
#     print(" "*(n-j) + "*"*((2*j-1)))


# Binary search practice
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,46]
x = 46
print(binarySearch(mylist,x))