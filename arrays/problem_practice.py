# Check array is sorted or not
# def sorted_array(nums,n):
#     # n=len(nums)
#     for i in range (1,n):
#        if(nums[i]<nums[i-1]):
#            return "array is not sorted"
#     return "array is sorted"

# nums=[12,35,56,63,78,89,15]
# n=len(nums)
# print(sorted_array(nums,n))

# Pattern Practice
n=3
# for i in range(n):
#     for j in range(n):
for i in range(n):
    print(" "*(n-(i+1))+"*"*(2*i+1))
for i in range(n):
    print(" "*(i)+"*"*(2*n-(2*i+1)))