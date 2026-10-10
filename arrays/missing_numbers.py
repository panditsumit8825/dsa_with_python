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
def missing_num(sum,arr):
    sum1=0
    for i in arr:
        sum1 += i
    return(sum-sum1)

arr_list=[1,2,4,5]
l=len(arr_list)
n=l+1
sum=n*(n+1)//2
print(missing_num(sum,arr_list))